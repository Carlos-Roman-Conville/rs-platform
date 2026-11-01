import json, re, sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from curated import RENAME_PREFIX, RENAME_EXACT, RESTATES, GROUPS, UNITS, AUTH, BATCH, EXTRA_ROWS, INTERFACES, DECISIONS, ROW_PATCHES

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = "E:/AI Programs/Toolchain/registry"
SRC = ["realism-phys", "realism-bio", "setl-econ", "pirate-body", "pirate-world"]

rows = []
for f in SRC:
    for l in open(os.path.join(HERE, f + ".jsonl"), encoding="utf-8"):
        if l.strip():
            r = json.loads(l); r["audit_batch"] = f; rows.append(r)
rows += [dict(r) for r in EXTRA_ROWS]

def rename(i):
    if i in RENAME_EXACT: return RENAME_EXACT[i]
    for p, q in RENAME_PREFIX.items():
        if i.startswith(p): return q + i[len(p):]
    return i

DOM = {"A": "A", "B": "B", "C": "C", "D": "D", "E": "E", "F": "F", "G": "G", "i": "infra"}
def norm_status(s):
    s0 = s.lower()
    if s0.startswith("built"): base = "built"
    elif s0.startswith("document"): base = "documented-only"
    elif s0.startswith("planned"): base = "planned"
    else: base = "documented-only"
    return base, (s if s != base else "")

def norm_scope(s):
    for b in ("universal", "pirate-specific", "mixed"):
        if s.startswith(b): return b, (s[len(b):].strip(" ()") or "")
    return "mixed", s

def norm_ev(e):
    m = re.match(r"\s*([1-6])", str(e))
    return (int(m.group(1)) if m else None), ("" if (m and str(e).strip() == m.group(1)) else str(e))

ENGINE_NAME = {"pirate-ship (docs)": "pirate-ship", "pirate-ship (code)": "pirate-ship"}

out = []
for r in rows:
    rid = rename(r["id"])
    st, stn = norm_status(r["status"])
    sc, scn = norm_scope(r["scope"])
    ev, evn = norm_ev(r["evidence"])
    eng = ENGINE_NAME.get(r["engine"], r["engine"])
    home_kind = "code" if r["engine"] in ("realism", "settlement", "economy", "shared", "pirate-ship (code)") else "docs"
    rec = {
        "id": rid,
        "name": r["name"],
        "owning_engine": eng,
        "home": r["home"],
        "home_kind": home_kind,
        "status": st,
        "status_note": stn,
        "kind": "restatement" if rid in RESTATES else "mechanism",
        "restates": RESTATES.get(rid),
        "domain": DOM.get(str(r["domain"])[:1], "infra"),
        "scope": sc,
        "scope_note": scn,
        "inputs": r["inputs"], "outputs": r["outputs"], "state": r["state"],
        "formulation": r["formulation"], "dependencies": r["dependencies"],
        "timescale": r["timescale"], "invariants": r["invariants"], "sources": r["sources"],
        "evidence": ev, "evidence_note": evn, "approximations": r["approximations"],
        "tests": r["tests"], "consumers": r["consumers"], "notes": r["notes"],
        "overlap_groups": [], "unit_issues": [],
        "audit_batch": r["audit_batch"], "audit_id": r["id"] if rid != r["id"] else None,
    }
    if rec["kind"] == "restatement" and rec["status"] == "built":
        rec["status"] = "documented-only"
        rec["status_note"] = ("restates built code; " + rec["status_note"]).strip("; ")
    out.append(rec)

ids = {r["id"]: r for r in out}
assert len(ids) == len(out), "duplicate ids after rename"
bad = [k for k, v in RESTATES.items() if k not in ids or v not in ids]
for g in GROUPS:
    for m in g[3]:
        if m not in ids: bad.append(g[0] + ":" + m)
if bad: print("MISSING", bad); sys.exit(1)
for g in GROUPS:
    closed = DECISIONS.get(g[0], {}).get("state") == "closed"
    for m in g[3]: ids[m].setdefault("closed_overlap_groups", []).append(g[0]) if closed else ids[m]["overlap_groups"].append(g[0])
for k, patch in ROW_PATCHES.items():
    assert k in ids, k
    ids[k].update(patch)
# Rex 2026-10-31 (ENGINES.md "Reality and Life are separate engines"): realism rows re-owned by domain tag; ids and homes unchanged
from curated import ENGINE_SPLIT_OVERRIDES
for r in out:
    if r["owning_engine"] != "realism": continue
    new_eng = ENGINE_SPLIT_OVERRIDES.get(r["id"]) or {"A": "reality", "B": "life"}.get(r["domain"])
    if new_eng:
        r["owning_engine"] = new_eng
        _tag = "package split pending, SPLIT.md; owner " + new_eng + " since 2026-10-31"
        if isinstance(r.get("notes"), list): r["notes"] = r["notes"] + [_tag]
        else: r["notes"] = ((r.get("notes") or "") + " [" + _tag + "]").strip()
for u in UNITS:
    for m in re.findall(r"[a-z_]+\.[a-z_]+\.[A-Za-z0-9_]+", u[1]):
        if m in ids: ids[m]["unit_issues"].append(u[0])

# dependency resolution
by_last = collections.defaultdict(list)
for r in out:
    by_last[r["id"].split(".")[-1].lower()].append(r["id"])
    by_last[r["name"].lower()].append(r["id"])
def resolve(d, src):
    d0 = d.strip()
    if d0 in ids: return d0
    if rename(d0) in ids: return rename(d0)
    key = re.split(r"[ (:/]", d0)[0].lower()
    for k in (d0.lower(), key, key.split(".")[-1]):
        c = [x for x in by_last.get(k, []) if x != src]
        if len(c) == 1: return c[0]
        same = [x for x in c if x.split(".")[0] == src.split(".")[0]]
        if len(same) == 1: return same[0]
    return None

edges, unresolved = [], collections.Counter()
for r in out:
    for d in r["dependencies"]:
        t = resolve(str(d), r["id"])
        if t and t != r["id"]: edges.append({"from": r["id"], "to": t, "type": "depends_on"})
        else: unresolved[str(d)] += 1
    if r["restates"]: edges.append({"from": r["id"], "to": r["restates"], "type": "restates"})
for g in GROUPS:
    m = g[3]
    for a in m[1:]: edges.append({"from": a, "to": m[0], "type": "overlap", "group": g[0]})
for i in INTERFACES:
    assert i[1] in ids and i[2] in ids, i
    edges.append({"from": i[2], "to": i[1], "type": "interface", "interface": i[0]})
    ids[i[1]].setdefault("interfaces", []).append(i[0]); ids[i[2]].setdefault("interfaces", []).append(i[0])

# cycles on depends_on
adj = collections.defaultdict(set)
for e in edges:
    if e["type"] == "depends_on": adj[e["from"]].add(e["to"])
idx, low, stack, on, sccs, n = {}, {}, [], set(), [], [0]
sys.setrecursionlimit(10000)
def sc(v):
    idx[v] = low[v] = n[0]; n[0] += 1; stack.append(v); on.add(v)
    for w in adj[v]:
        if w not in idx: sc(w); low[v] = min(low[v], low[w])
        elif w in on: low[v] = min(low[v], idx[w])
    if low[v] == idx[v]:
        comp = []
        while True:
            w = stack.pop(); on.discard(w); comp.append(w)
            if w == v: break
        if len(comp) > 1: sccs.append(sorted(comp))
for v in list(ids):
    if v not in idx: sc(v)

os.makedirs(OUT, exist_ok=True)
meta = {
    "title": "Mechanism registry of the reality simulation platform",
    "generated": "2026-10-30", "keeper": "registry keeper (HQ/handoffs/registry)",
    "status": "approved with refinements by Rex 2026-10-30 (organisation and order); owners per overlap group remain proposals until each batch is approved",
    "contract_fields": "PLATFORM.md §7", "evidence_scale": "PLATFORM.md §4 (1 law ... 6 fiction)",
    "counts": dict(collections.Counter(r["status"] for r in out)),
    "kinds": dict(collections.Counter(r["kind"] for r in out)),
}
json.dump({"meta": meta, "mechanisms": sorted(out, key=lambda r: r["id"])},
          open(OUT + "/mechanisms.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
groups = [{"id": g[0], "kind": g[1], "authority": AUTH[g[0]][0], "authority_note": AUTH[g[0]][1], "batch": BATCH[g[0]], "summary": g[2], "members": g[3], "proposed_owner": g[4], "approved_owner": (DECISIONS[g[0]].get("approved_owner", g[4]) if g[0] in DECISIONS else None), "state": DECISIONS.get(g[0], {}).get("state", "proposed"), "decision": DECISIONS.get(g[0], {}).get("decision"), "progress": DECISIONS.get(g[0], {}).get("progress", [])} for g in GROUPS]
units = [{"id": u[0], "where": u[1], "problem": u[2], "proposal": u[3]} for u in UNITS]
json.dump({"meta": {"generated": "2026-10-30", "status": "approved with refinements (Rex 2026-10-30); group owners proposed per batch", "authority_classes": {"duplicate-authority": "two homes own or compute the same state or value; one must become a read", "aggregation": "detailed and aggregate computations coexist legitimately: one owner holds the state and the aggregation interface is documented (refinement B)", "mixed": "part legitimate aggregation, part duplicate authority", "ownership-gap": "no owner, or the owner sits in the wrong engine", "shared-part": "distinct mechanisms that should share a helper or a boundary contract"},
                    "edge_types": {"depends_on": "from reads an output of to (resolved from the dependency field)",
                                   "restates": "from is a doc/adapter restating the authoritative mechanism to",
                                   "overlap": "from and to are in the same overlap group (to = first member)",
                                   "interface": "a documented hand-off between engines that looks like an overlap and is not one: from reads to"}},
           "interfaces": [{"id": i[0], "provider": i[1], "consumer": i[2], "summary": i[3], "related_groups": i[4]} for i in INTERFACES],
           "nodes": [{"id": r["id"], "engine": r["owning_engine"], "status": r["status"], "kind": r["kind"],
                      "domain": r["domain"], "scope": r["scope"]} for r in sorted(out, key=lambda r: r["id"])],
           "edges": edges, "overlap_groups": groups, "unit_issues": units,
           "cycles": sccs, "unresolved_dependencies": dict(unresolved.most_common())},
          open(OUT + "/graph.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)

print(meta)
print("edges", collections.Counter(e["type"] for e in edges), "unresolved", sum(unresolved.values()), len(unresolved))
print("cycles", sccs)
print(collections.Counter((r["owning_engine"], r["status"], r["kind"]) for r in out))
print(collections.Counter((r["owning_engine"], r["scope"]) for r in out))
print(collections.Counter((r["domain"]) for r in out if r["kind"]=="mechanism"))
print(collections.Counter((r["domain"], r["status"]) for r in out if r["kind"]=="mechanism"))
