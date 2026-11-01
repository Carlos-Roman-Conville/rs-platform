# Registry schema 3: verification and validation (PLATFORM.md §11a, Rex 2026-10-30). Run after schema2.py.
# Three states per mechanism, never conflated: implemented (code + unit tests pass), integrated (wired through
# registry ports to what it reads and feeds), validated (behaviour matches independent evidence within declared
# tolerances). Seeded from what exists; nothing here is "validated: yes" until a re-audit with independent data.
import json, os, sys, collections, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from curated import CHAINS, VALIDATION_CANDIDATES, VV_OVERRIDES, VV_PLANNED_SPECS
R = "E:/AI Programs/Toolchain/registry"
doc = json.load(open(R + "/mechanisms.json", encoding="utf-8"))
rows = {r["id"]: r for r in doc["mechanisms"]}
for ch in CHAINS:
    missing = [m for m in ch["members"] if m not in rows]
    assert not missing, (ch["id"], missing)

in_chain = collections.defaultdict(list)
for ch in CHAINS:
    for m in ch["members"]: in_chain[m].append(ch)

def has_tests(r):
    t = str(r.get("tests") or "").strip().lower()
    return bool(t) and not t.startswith("none")

for r in rows.values():
    mech = r["kind"] == "mechanism"
    built = r["status"] == "built"
    chs = in_chain.get(r["id"], [])
    partners = sorted({m for ch in chs for m in ch["members"] if m != r["id"]})
    if not mech:
        integ = "n/a (restatement)"
    elif not built:
        integ = "no (not built)"
    elif r["id"].startswith("pirate."):
        integ = "plugin (outside the registry ports)"
    elif chs:
        integ = "yes (combined test: " + ", ".join(ch["id"] for ch in chs) + ")"
    else:
        integ = "no (no combined test; wiring by prop names, process order or CONTRACTS.md providers only)"
    cand = VALIDATION_CANDIDATES.get(r["id"])
    r["vv"] = {
        "implemented": bool(mech and built and has_tests(r)),
        "integrated": integ,
        "validated": ("candidate (registry re-audit pending)" if cand else "no") if (mech and built) else "n/a",
        "record": {
            "sources_and_model": {"sources": r.get("sources"), "model": r.get("formulation"), "evidence_level": r.get("evidence")},
            "applicability": r.get("approximations"),
            "verification_tests": r.get("tests"),
            "validation_evidence": [cand] if cand else [],
            "tolerance": None,
            "stability_conservation_boundary": [f"{ch['id']}: {ch['conservation']}" for ch in chs],
            "numerical": {"stability": None, "coupled_update_consistency": None, "sensitivity": None},
            "integration_tested_with": partners,
            "integration_tests": [ch["test"] + ("" if ch["complete"] else " [partial]") for ch in chs],
            "report": r.get("notes") or "",
        },
    }
for k, ov in VV_OVERRIDES.items():
    rows[k]["vv"]["validated"] = ov["validated"]
    if "integrated" in ov: rows[k]["vv"]["integrated"] = ov["integrated"]
    rows[k]["vv"]["record"]["validation_evidence"].append(ov["evidence"])
for k, spec in VV_PLANNED_SPECS.items():
    rows[k]["vv"]["record"]["validation_plan"] = spec
doc["meta"]["schema_version"] = 3
# Schema 4 (Rex 2026-10-31, field survey): every contract answers what enters (inputs), what leaves (outputs), what
# accumulates (state), what limits the rate (rate_limiter) and what makes it fail (failure_mode). Empty until owners fill them
# (ROW_PATCHES / VV_NUMERICAL); the kernel check warns, never fails, when they are empty on a built row.
from curated import VV_NUMERICAL
for r in rows.values():
    r.setdefault("rate_limiter", None)
    r.setdefault("failure_mode", None)
for k, num in VV_NUMERICAL.items():
    rows[k]["vv"]["record"]["numerical"].update(num)
doc["meta"]["schema_version"] = 4
doc["meta"]["schema_4"] = ("adds rate_limiter and failure_mode to the §7 contract fields (with inputs = what enters, outputs = what leaves, "
                           "state = what accumulates), null until owners fill them; widens vv.record item 5 with numerical {stability, "
                           "coupled_update_consistency, sensitivity} (PLATFORM §11a item 5, Rex 2026-10-31); check-registry warns, never fails, on empty fields of built rows")
doc["meta"]["schema_3"] = ("each row carries vv {implemented, integrated, validated, record{sources_and_model, applicability, "
                           "verification_tests, validation_evidence, tolerance, stability_conservation_boundary, "
                           "integration_tested_with, integration_tests, report}} (PLATFORM.md §11a); seeded 2026-10-30 from the "
                           "audit and the combined tests; owners complete it, the registry keeper re-audits")
doc["meta"]["vv_counts"] = {
    "implemented": sum(1 for r in rows.values() if r["vv"]["implemented"]),
    "built_mechanisms": sum(1 for r in rows.values() if r["kind"] == "mechanism" and r["status"] == "built"),
    "with_integration_test": sum(1 for r in rows.values() if r["vv"]["record"]["integration_tested_with"]),
    "integrated_yes": sum(1 for r in rows.values() if str(r["vv"]["integrated"]).startswith("yes")),
    "validated_yes": sum(1 for r in rows.values() if str(r["vv"]["validated"]).startswith("yes")),
    "validated_candidate": sum(1 for r in rows.values() if r["vv"]["validated"].startswith("candidate")),
    "validation_failed": sum(1 for r in rows.values() if r["vv"]["validated"].startswith("failed")),
}
json.dump(doc, open(R + "/mechanisms.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)

# Connected pairs (a depends_on edge between two built mechanisms) with no combined test covering both.
g = json.load(open(R + "/graph.json", encoding="utf-8"))
tested = {frozenset(p) for ch in CHAINS for p in itertools.combinations(ch["members"], 2)}
gaps, covered = [], 0
seen = set()
for e in g["edges"]:
    if e["type"] != "depends_on": continue
    a, b = rows.get(e["from"]), rows.get(e["to"])
    if not a or not b: continue
    if not (a["kind"] == b["kind"] == "mechanism" and a["status"] == b["status"] == "built"): continue
    key = frozenset((a["id"], b["id"]))
    if key in seen: continue
    seen.add(key)
    if key in tested: covered += 1
    else: gaps.append({"reader": a["id"], "read": b["id"], "engines": sorted({a["owning_engine"], b["owning_engine"]})})
g["integration_gaps"] = {"meta": {"rule": "a depends_on edge between two built mechanisms with no combined test that runs both (PLATFORM.md §11a item 6)",
                                  "covered_pairs": covered, "gap_pairs": len(gaps)},
                         "gaps": sorted(gaps, key=lambda x: (x["engines"], x["reader"])),
                         "chains": [{"id": c["id"], "test": c["test"], "complete": c["complete"], "members": len(c["members"])} for c in CHAINS]}
from curated import INTERFACE_GAPS
g["integration_gaps"]["interface_gaps"] = INTERFACE_GAPS   # planned interfaces with no built edge yet (2026-10-31)
g["integration_gaps"]["meta"]["interface_gap_count"] = len(INTERFACE_GAPS)
json.dump(g, open(R + "/graph.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print(doc["meta"]["vv_counts"], "pairs covered", covered, "gaps", len(gaps))
for x in gaps[:60]: print(" ", x["reader"], "->", x["read"])
