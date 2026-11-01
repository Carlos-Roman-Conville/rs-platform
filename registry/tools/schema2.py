# Registry schema 2 (agreed with the Kernel keeper, Toolchain/kernel/DESIGN.md §8, commit 8b41825).
# Run after build.py. Adds writes/reads/aggregates to every row, seeds quantities.json from the outputs of
# built mechanism rows, and creates an empty aliases.json. Seeds are status "seed" until the owner confirms.
import json, re, collections, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from curated import EXTRA_QUANTITIES, QUANTITY_KINDS, QUANTITY_UNIT_FIX, QUANTITY_WRITER_FIX, ALIASES, QUANTITY_OPS, QUANTITY_PATCH
R = "E:/AI Programs/Toolchain/registry"
doc = json.load(open(R + "/mechanisms.json", encoding="utf-8"))
rows = doc["mechanisms"]

SCOPE_BY_AREA = {
    "physiology": "body", "nutrition": "body", "nutri": "body", "circulation": "body", "anatomy": "body",
    "muscular": "body", "neurology": "body", "medicine": "body", "bio": "body",
    "gas": "air", "atmos": "air", "env": "place", "eco": "stock", "population": "population",
    "thermo": "component", "chem": "component", "equip": "component", "infra": "world", "materials": "component",
}
def scope_of(r):
    e, area = r["id"].split(".")[0], r["id"].split(".")[1]
    if e == "realism": return SCOPE_BY_AREA.get(area, "component")
    if e in ("settlement", "economy"): return e
    if e == "shared": return "contract"
    return "plugin"

def slug(s):
    s = re.sub(r"\(.*?\)", "", str(s)).strip().lower()
    s = re.sub(r"[^a-z0-9]+", "_", s).strip("_")
    return s[:48] or "value"

UNIT_HINT = {  # free text -> likely kernel symbol; confirmed only when units.json lands
    "kg": "kg", "g": "g", "mg": "mg", "l": "L", "ml": "mL", "w": "W", "j": "J", "kj": "kJ", "pa": "Pa", "mmhg": "mmHg",
    "s": "s", "min": "min", "h": "h", "day": "d", "days": "d", "k": "K", "c": "degC", "°c": "degC", "mol": "mol",
    "unitless": "1", "fraction": "1", "0..1": "1", "index": "1", "boolean": "1", "count": "count", "kcal": "kcal",
    "kcal/day": "kcal/d", "l/h": "L/h", "l/min": "L/min", "ml/min": "mL/min", "m": "m", "m2": "m2", "m/s": "m/s",
    "0-1": "1", "bool": "1", "x": "1", "persons": "count", "ppm": "ppm", "d": "d", "yr": "a", "kg/s": "kg/s",
    "kg/m3": "kg/m3", "ml/kg": "mL/kg", "met-h": "MET.h",
}
def unit_hint(u):
    k = str(u).strip().lower()
    return UNIT_HINT.get(k)

# Mapping to the kernel parser's vocabulary (Toolchain/kernel/src/units.ts parse; data/units.json, unit 2592).
# The parser has no SI prefixes, mmHg, ppm, year or MET yet: those are "needs symbol" (asked of the kernel keeper).
NON_NUMERIC = {"list", "object", "struct", "state", "event", "label", "text", "string", "ids", "registry", "by id",
               "object[]", "table unit", "tone", "mixed", "via nutrition", "per day|hour|event", "mg|mcg|g"}
TEXT_MAP = {
    "0-1": "1", "0..1": "1", "0-2": "1", "0-3": "1", "0-100": "1", "0.55-1": "1", "0.78-1.0": "1", "0.3-1": "1",
    "x0-1": "1", "0/1": "1", "0/1/null": "1", "0-2 or 0-1": "1", "0-10 midpoint": "1", "int": "count", "number": "1",
    "dimensionless": "1", "unitless": "1", "fraction": "1", "fractions": "1", "bool": "1", "boolean": "1", "x": "1",
    "index": "1", "% mass": "percent", "kcal (cum)": "kcal", "min span": "min", "currency/unit": "money/count",
    "currency/day": "money/d", "units/day": "count/d", "units/(fixture*day)": "count/(count*d)", "persons/day": "person/d",
    "persons": "person", "count": "count",
}
NEEDS_SYMBOL = {"ml": "mL", "ml/min": "mL/min", "ml/kg": "mL/kg", "mmhg": "mmHg", "ppm": "ppm", "ppm min": "ppm*min",
                "met-h": "MET*h", "yr": "a", "g/dl": "g/dL", "g/dl (alcohol) | mg/l": "g/dL", "mg": "mg", "kj": "kJ",
                "mcg": "ug"}
TEXT_MAP.update({"kcal/day": "kcal/d", "l/h": "L/h", "l/min": "L/min"})
def map_unit(text, hint):
    t = str(text).strip(); k = t.lower()
    if k in ("unknown", "", "none", "host units", "host units/day", "host/yr"):
        return None, "unknown: the owner must state it"
    if k in NON_NUMERIC or "|" in t:
        return None, "non-numeric (a structured, categorical or text value; kernel convention requested)"
    if k in TEXT_MAP: return TEXT_MAP[k], "mapped"
    if k in NEEDS_SYMBOL: return NEEDS_SYMBOL[k], "needs symbol (not yet in the kernel units table)"
    return (hint or t), "as given"

quantities, writers = {}, collections.defaultdict(list)
_EXTRA_IDS = {_q["id"] for _q in EXTRA_QUANTITIES}   # outputs already named by a registered quantity id are used as is (REG-28, 2026-10-31)
for r in rows:
    r["writes"], r["reads"], r["aggregates"] = [], [], None
    if r["kind"] != "mechanism" or r["status"] != "built": continue
    sc = scope_of(r)
    for o in r["outputs"] or []:
        name = o.get("name") if isinstance(o, dict) else str(o)
        unit = o.get("unit") if isinstance(o, dict) else "unknown"
        if name in _EXTRA_IDS:
            writers[name].append(r["id"])
            if name not in r["writes"]: r["writes"].append(name)
            continue
        qid = f"{sc}.{slug(name)}"
        writers[qid].append(r["id"])
        if qid not in r["writes"]: r["writes"].append(qid)
        mu, ust = map_unit(unit, unit_hint(unit))
        q = quantities.setdefault(qid, {"id": qid, "unit": mu, "unit_text": unit, "unit_status": ust, "scope": sc,
                                        "writer": r["id"], "description": name, "status": "seed"})
for qid, ws in writers.items():
    ws = sorted(set(ws))
    if qid in _EXTRA_IDS:
        assert len(ws) == 1, (qid, ws)   # a registered quantity keeps one built writer
        continue
    if len(ws) > 1:
        quantities[qid]["writer"] = None
        quantities[qid]["candidate_writers"] = ws
        quantities[qid]["status"] = "seed: several writers (an overlap or a naming clash to resolve)"

# Unit symbols confirmed with the Kernel keeper ahead of units.json (2026-10-30): base symbol `person` (count);
# labour in person-hours is `person*h`. Today's values keep today's units; CONTRACTS s16 (when agreed) moves
# the worker-day quantities to person*h.
UNIT_OVERRIDES = {
    "population.labour": ("person", "kernel keeper 2026-10-30"),
    "contract.workers_drawn": ("person", "kernel keeper 2026-10-30"),
    "economy.labourperunit": ("person*d", "kernel keeper 2026-10-30; replaced by economy.labourhoursperunit (CONTRACTS s16 field labourHoursPerUnit, person*h) in economy unit 2627; retired after unit 2630 removes labourPerUnit (economy keeper 2026-10-30)"),
}
for qid, (u, why) in UNIT_OVERRIDES.items():
    quantities[qid]["unit"] = u; quantities[qid]["unit_source"] = why
for _q in EXTRA_QUANTITIES:
    quantities[_q["id"]] = dict(_q)
for _id, (_k, _d) in QUANTITY_KINDS.items():
    assert _id in quantities, _id
    quantities[_id].update({"kind": _k, "unit": None, "unit_status": "n/a (" + _k + ")", "kind_note": _d})
for _id, (_u, _d) in QUANTITY_UNIT_FIX.items():
    quantities[_id].update({"unit": _u, "unit_status": "mapped", "kind_note": _d})
for _q in quantities.values():
    _q.setdefault("kind", "quantity")
for _id, (_w, _k, _d) in QUANTITY_WRITER_FIX.items():
    _q = quantities[_id]
    _q.update({"writer": _w, "kind": _k, "unit": None, "unit_status": "n/a (" + _k + ")", "kind_note": _d, "status": "confirmed by owner"})
    _q.pop("candidate_writers", None)
    for _r in rows:
        if _r["id"] != _w and _id in _r["writes"]: _r["writes"].remove(_id)
def _drop_writes(qid, keep=None):
    for _r in rows:
        if _r["id"] != keep and qid in _r["writes"]: _r["writes"].remove(qid)
def _retire(qid, alias, why, date="2026-10-30"):
    _q = quantities[qid]; _q.update({"status": "retired", "writer": None, "retired_reason": why, "replaced_by": alias})
    _q.pop("candidate_writers", None); _drop_writes(qid)
    ALIASES_OUT.append({"old": qid, "new": alias, "date": date, "kind": "quantity", "reason": why})
ALIASES_OUT = [dict(a) for a in ALIASES]
for op in QUANTITY_OPS:
    if op[0] == "retire": _retire(op[1], op[2], op[3], *op[4:5])   # optional 5th element: the retirement date (2026-11-01)
    elif op[0] == "writer":
        _q = quantities[op[1]]; _q.update({"writer": op[2], "status": "confirmed by owner", "writer_note": op[3]}); _q.pop("candidate_writers", None); _drop_writes(op[1], keep=op[2])
    elif op[0] == "split":
        for nid, unit, w, desc in op[2]:
            quantities[nid] = {"id": nid, "unit": unit, "unit_text": unit, "unit_status": "mapped", "kind": "quantity", "scope": "settlement",
                               "writer": w, "description": desc, "status": "confirmed by owner"}
            wr = next(r for r in rows if r["id"] == w); wr["writes"].append(nid)
        _retire(op[1], [n[0] for n in op[2]], op[3])
    elif op[0] == "rename":   # ("rename", old, [(new, unit, kind, desc)], why): same writer, scope from the new id (2026-10-31)
        _w = quantities[op[1]].get("writer")
        for nid, unit, kind, desc in op[2]:
            quantities[nid] = {"id": nid, "unit": unit, "unit_text": unit, "unit_status": ("mapped" if unit else "n/a (" + kind + ")"),
                               "kind": kind, "scope": nid.split(".")[0], "writer": _w, "description": desc, "status": "confirmed by owner"}
            if _w:
                wr = next(r for r in rows if r["id"] == _w)
                if nid not in wr["writes"]: wr["writes"].append(nid)
        _retire(op[1], [n[0] for n in op[2]] if len(op[2]) > 1 else op[2][0][0], op[3], date="2026-10-31")
    elif op[0] == "merge":
        nid, kind, desc = op[2]
        ws = sorted({q["writer"] for q in (quantities[o] for o in op[1]) if q.get("writer")})
        quantities[nid] = {"id": nid, "unit": None, "kind": kind, "unit_status": "n/a (" + kind + ")", "scope": "settlement", "writer": None,
                           "candidate_writers": ws, "description": desc, "status": "known duplicate authority: " + op[3]}
        for o in op[1]: _retire(o, nid, "merged into " + nid + ": the same field")
        for r in rows:
            if r["id"] in ws: r["writes"].append(nid)
for qid, patch in QUANTITY_PATCH.items(): quantities[qid].update(patch)
json.dump({"meta": {"schema_version": 1, "rule": "one entry per rename, split or merge: old id -> new id (or list); a retired id is never reused", "applies_to": "mechanism ids and quantity ids"},
           "aliases": ALIASES_OUT}, open(R + "/aliases.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
qs = sorted(quantities.values(), key=lambda q: q["id"])
doc["meta"]["schema_version"] = 2
doc["meta"]["schema_2"] = ("rows carry writes/reads (quantity ids, mirrored from each engine's kernel.json processes) "
                           "and aggregates {of, by, interface, test} (refinement B); agreed with the Kernel keeper, "
                           "Toolchain/kernel/DESIGN.md §8")
json.dump(doc, open(R + "/mechanisms.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
qs = sorted(quantities.values(), key=lambda q: q["id"])
json.dump({"meta": {"schema_version": 1, "generated": "2026-10-30", "keeper": "registry keeper",
                    "status": "seed: ids derived from the audit's output names; each owner confirms or renames (renames go to aliases.json)",
                    "unit": "a symbol of Toolchain/kernel/data/units.json once it exists; null = not yet mapped (unit_text keeps the audit's text)",
                    "rule": "exactly one writer per quantity; an aggregate writes its own scoped quantity and links via aggregates"},
           "quantities": qs}, open(R + "/quantities.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
if not os.path.exists(R + "/aliases.json"):
    json.dump({"meta": {"schema_version": 1, "rule": "one entry per rename: old id -> new id; a retired id is never reused",
                        "applies_to": "mechanism ids and quantity ids"}, "aliases": []},
              open(R + "/aliases.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
multi = [q for q in quantities.values() if q.get("candidate_writers")]
print(len(qs), "quantities;", sum(1 for q in qs if q["unit"]), "unit-mapped;", len(multi), "multi-writer")
for q in multi: print(" ", q["id"], q["candidate_writers"])
print(collections.Counter(q["scope"] for q in qs))
print(collections.Counter(str(q.get("unit_text")) for q in qs if not q["unit"]).most_common(25))
