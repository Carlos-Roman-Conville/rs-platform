import json, collections
g = json.load(open("E:/AI Programs/Toolchain/registry/graph.json", encoding="utf-8"))
nodes = {n["id"]: n for n in g["nodes"]}
E = collections.Counter(e["type"] for e in g["edges"])
deg = collections.Counter(e["to"] for e in g["edges"] if e["type"] == "depends_on")
cross = collections.Counter((nodes[e["from"]]["engine"], nodes[e["to"]]["engine"]) for e in g["edges"]
                            if e["type"] == "depends_on" and nodes[e["from"]]["engine"] != nodes[e["to"]]["engine"])
def c(s): return str(s).replace("|", "/")
L = []
L.append("""# The dependency graph (opened 2026-10-30, registry keeper)

**Status: approved with refinements (Rex, 2026-10-30).** Rex approved the engine organisation and the phase order
(`ENGINES.md` "The approved organisation"). The owner of each overlap group stays **proposed** until its batch is
approved (batch 1: `OVERLAPS-BATCH-1.md`); no migration starts before the affected keepers agree ownership and
acceptance tests. This is the readable view of `registry/graph.json`; ids are those of `registry/mechanisms.json`.

## 1. The graph in numbers
""")
L.append(f"- Nodes: {len(nodes)} rows ({sum(1 for n in nodes.values() if n['kind']=='mechanism')} mechanisms, "
         f"{sum(1 for n in nodes.values() if n['kind']=='restatement')} restatements).")
L.append(f"- Edges: {E['depends_on']} `depends_on` (resolved from each row's dependency list), {E['restates']} `restates`, "
         f"{E['overlap']} `overlap` (members of the {len(g['overlap_groups'])} groups below), {E['interface']} `interface` (hand-offs, §2).")
L.append(f"- Unresolved dependencies: {sum(g['unresolved_dependencies'].values())} mentions of "
         f"{len(g['unresolved_dependencies'])} names that match no row (data files, host inputs, props, other docs); listed in graph.json.")
L.append("- Cross-engine `depends_on` edges: " + ", ".join(f"{a} → {b}: {n}" for (a, b), n in cross.most_common()) + ".")
L.append("  The realism → pirate-ship edges are realism code citing a pirate doc as its formula's authority (ENGINE.md, "
         "GAS_DYNAMICS.md, ANATOMY.md §3a, BODY.md): universal formulas whose statement lives in the plugin. "
         "Proposed: move each statement into a realism gear file (PLATFORM.md §8) and leave the doc pointing at it.")
L.append("- Most-read mechanisms (in-degree): " + ", ".join(f"`{k}` {v}" for k, v in deg.most_common(8)) + ".")
L.append("""
The causal spine the code follows today (from `examples/human-wound.ts`, `three-ports.ts` and the pirate adapter's
`runDay`): environment → room air → physiology → breathing → nutrition → neurology → circulation → medicine →
anatomy (realism, one 1 s step, in declared process order); then, once a day and with no link to the above,
settlement tick → economy tick. Realism and the two economic engines do not exchange anything yet; the pirate
adapters read both.

## 2. Duplicates and overlaps (every one found)

Kinds: **duplicate** = the same quantity computed in two places; **conflict** = homes disagree in value or unit;
**double-penalty** = one cause applied as several effects (forbidden by PLATFORM.md §7); **ownership** = two
owners, or none; **overlap** = related mechanisms that must share a part.

**Authority (refinement B, Rex 2026-10-30):** closure removes duplicate *authority*, not every related
calculation. **duplicate-authority** = two homes own or compute the same state or value: one becomes a read.
**aggregation** = a detailed and an aggregate computation coexist legitimately, provided one owner holds the state
and the aggregation interface is documented. **mixed** = part of each (the note says which part). **ownership-gap**
= no owner, or the owner sits in the wrong engine. **shared-part** = distinct mechanisms that should share a helper
or a boundary contract. **Batch** = the presentation batch for Rex (batch 1 is `OVERLAPS-BATCH-1.md`; 2–5 proposed).

**State:** proposed → **closing** (Rex approved the owner; the keepers agree tests and queue units) → **closed**
(the keeper reported it done and the registry keeper re-audited it). Progress per group is in §2a.

**Closure criteria (PLATFORM.md §11a, Rex 2026-10-30).** A group closes only when, where each applies:
(1) **implemented**: the owner's code and the group's acceptance test pass; (2) **integrated**: the owner is wired
to every former home that now reads it (through registry ports once P0 lands, through the agreed contract until
then) and a combined test runs them together; (3) **validated**: where independent evidence exists for the owned
quantity, the behaviour matches it within a declared tolerance; where none exists, the row says so and names the
experiment that would test it. A re-audit by the registry keeper (not the author) checks all three; "validated"
never comes from the author's own tests alone.

| Id | Kind | Authority | Batch | State | What | Homes (ids) | Owner (approved, or proposed) |
|---|---|---|---|---|---|---|---|""")
for o in g["overlap_groups"]:
    au = o["authority"] + (f" ({c(o['authority_note'])})" if o["authority_note"] else "")
    L.append(f"| {o['id']} | {o['kind']} | {au} | {o['batch']} | {o['state']} | {c(o['summary'])} | " + "<br>".join(f"`{m}`" for m in o["members"]) + f" | {c(o['proposed_owner'])} |")
L.append("""
Counts: """ + ", ".join(f"{k} {v}" for k, v in collections.Counter(o["kind"].split("+")[0] for o in g["overlap_groups"]).items()) + """.
Counts by authority: """ + ", ".join(f"{k} {v}" for k, v in collections.Counter(o["authority"] for o in g["overlap_groups"]).items()) + """.
Batches: """ + "; ".join(f"{k}: " + " ".join(o["id"] for o in g["overlap_groups"] if o["batch"] == k) for k in sorted({o["batch"] for o in g["overlap_groups"]}, key=str)) + """.

### 2a. Closure tracking

| Id | State | Decision | Progress (agreed / units queued / closed with commit) |
|---|---|---|---|""")
for o in g["overlap_groups"]:
    if o["state"] == "proposed": continue
    pr = "; ".join(f"{p['date']} {p['step']}" + (f" ({p['commit']})" if p.get("commit") else "") + (f": {c(p['note'])}" if p.get("note") else "") for p in o["progress"]) or "awaiting the keepers' agreement"
    L.append(f"| {o['id']} | {o['state']} | {c(o['decision'])} | {pr} |")
L.append("""
### Interfaces, not overlaps

Hand-offs between engines that look like overlaps and are not. They are recorded so nobody tries to close them;
`graph.json` holds them under `interfaces`, as edges of type `interface`.

| Id | Provider → consumer | What | Related groups |
|---|---|---|---|""")
for i in g.get("interfaces", []):
    L.append(f"| {i['id']} | `{i['provider']}` → `{i['consumer']}` | {c(i['summary'])} | {', '.join(i['related_groups'])} |")
L.append("""
## 3. Incompatible units

| Id | Where | Problem | Proposal |
|---|---|---|---|""")
for u in g["unit_issues"]:
    L.append(f"| {u['id']} | `{c(u['where'])}` | {c(u['problem'])} | {c(u['proposal'])} |")
L.append("""
UNIT-1 was checked by the registry keeper against the code: `circulation.ts` L91/L105 write `blood_lost_ml`,
`nutrition.ts` L409/L438 read `blood_lost_l`, and only `nutrition.test.ts` L224 sets `blood_lost_l`.

## 3a. Integration: connected pairs with no combined test (PLATFORM.md §11a)

Each mechanism is **implemented** (code and unit tests pass), **integrated** (wired through registry ports to
what it reads and feeds), and **validated** (its behaviour matches independent evidence within declared
tolerances): three separate states, recorded per row in `mechanisms.json` (`vv`). Seeded 2026-10-30:
""")
m = json.load(open("E:/AI Programs/Toolchain/registry/mechanisms.json", encoding="utf-8"))["meta"].get("vv_counts", {})
ig = g.get("integration_gaps", {"meta": {"covered_pairs": 0, "gap_pairs": 0}, "gaps": [], "chains": []})
L.append(f"- built mechanisms {m.get('built_mechanisms')}; **implemented** {m.get('implemented')}; with a combined "
         f"(integration) test {m.get('with_integration_test')}; **integrated (yes)** {m.get('integrated_yes')}; "
         f"**validated (yes)** {m.get('validated_yes')}; {m.get('validated_candidate')} candidates; {m.get('validation_failed')} failed. "
         "'Integrated' means a named combined test runs the row with what it reads and feeds (REVIEWS.md, V&V states); "
         "wiring by prop names alone is 'no'. That most rows are implemented-not-validated is the honest starting point (Rex).")
L.append("\nThe combined tests counted as integration evidence:\n\n| Combined test | Mechanisms | Complete? |\n|---|---|---|")
for ch in ig["chains"]:
    L.append(f"| {c(ch['test'])} | {ch['members']} | {'yes' if ch['complete'] else 'partial (acceptance blocked)'} |")
L.append(f"\nOf the connected pairs (a `depends_on` edge between two built mechanisms), {ig['meta']['covered_pairs']} run "
         f"together in one of these tests and **{ig['meta']['gap_pairs']} do not**:\n\n| Reader | Reads | Engines |\n|---|---|---|")
for x in ig["gaps"]:
    L.append(f"| `{x['reader']}` | `{x['read']}` | {', '.join(x['engines'])} |")
L.append("""
Limits of this view: pairs inside one module may already be exercised together by that module's unit tests (the
owner confirms and adds the test to the row's `integration_tests`); the `depends_on` edges are resolved by name
(GRAPH.md §6), so a missing edge hides a pair. Thermoregulation and hydration, the pair Rex named, run together in
checkpoint 1 and hydration-week and are covered.

**Couplings that should exist and are not wired at all** (no edge, no test; from the overlap groups):

| Coupling | Today | Group |
|---|---|---|
| dehydration → plasma volume → oxygen delivery | documented in circulation's delivery failures, not implemented | DUP-22 |
| nutrition (per body) ↔ economy consumption (goods) ↔ population famine | three unconnected accounts | DUP-21 |
| population labour → settlement assignment → economy labour quote | no LabourSupply implementation until units 2617–2636 | DUP-26, DUP-29 |
| organ function ← hydration, anaemia, drug burden, nutrition | anatomy reads only perfusion and host signals | DUP-15 |
| realism (any) ↔ settlement/economy | no exchange; only the pirate adapters read both | P5, economy PLAN step 11 |

## 4. Circular dependencies

No import-level cycle exists in any engine (the readers checked imports). The resolved `depends_on` graph has
these two-node cycles:

| Cycle | Reading |
|---|---|""")
reading = {
 "realism.physiology.urine": "intended feedback: urine output depends on water balance and changes it; acceptable inside one step if the order is declared",
 "realism.anatomy.feed_gate": "intended feedback: the gut gate limits absorption and absorption feeds organ state; acceptable, order declared only in comments",
 "realism.muscular.banister": "an ownership loop, not causality: table in the physiology library, code in muscular (DUP-18)",
 "pirate.doc.anatomy.tissue_integrity": "doc-level loop: vitamin C pool and collagen state cite each other (DUP-16)",
 "pirate.doc.physiology.acclimatisation": "doc-level feedback: acclimatisation lowers heat strain which drives acclimatisation; the code orders it",
 "pirate.body.state_multiplier": "doc-level loop: STATS performance and BODY state multiplier define each other (DUP-38)",
 "pirate.env.period_hurricane_factor": "pirate code: the period factor is parsed into the weather chain that it describes (DUP-34)",
}
for cy in g["cycles"]:
    r = next((v for k, v in reading.items() if k in cy), "")
    L.append(f"| `{cy[0]}` ⇄ `{cy[1]}` | {r} |")
L.append("""
Run-order coupling (not cycles, but hidden dependencies): physiology reads `place.props.wbgt_c` written by
environment; breathing must follow room air and physiology; circulation after breathing; medicine after
circulation; anatomy after both. This order lives only in comments and examples. Settlement's tick calls economy's
`produce` and economy then reads settlement's output: works only by the agreed day order (CONTRACTS.md §9).
The anatomy cascade and circulation's regulation loops are intended feedback, half built.
The universal scheduler (ROADMAP phase 0) should declare these orders as data.

## 5. Ownership conflicts and contract-vs-code gaps

| Item | Two sides | State |
|---|---|---|
| Banister | physiology library table vs `muscular.ts` code vs physiology flags "not implemented" | DUP-18 |
| Hb saturation | CIRCULATION.md §1a vs `atmosphere.ts` | DUP-11 |
| Body mass, body water | nutrition, circulation, physiology all write | DUP-22 |
| Endurance pool | BODY §3, PHYSIOLOGY §6, COMBAT | DUP-47 |
| Inventory identity | `Project.account` as inventory id vs economy `inv.*` + holder | DUP-44 |
| Money supply | `credit`/`debit` outside conservation; no owner | DUP-43 |
| Property value | `PriceProvider.valueOf` declared, never implemented or called | DUP-43, CONTRACTS §12.3 |
| Taxation | settlement `publicWorks` stub vs future Government | DUP-42 |
| Population | Reality vs Society | DUP-41, CTRL-5 |
| Culture, organisations, factions | no owner; factions split Story vs Balance | CTRL-6 |
| Reference catalogue (§6) | no owner | AUDIT.md |
| Universal clock | no owner; six tick systems | DUP-33, BAL-25, REAL-10 |
| CONTRACTS.md §9 | promises market clearing, labour quotes and accounting snapshots inside `economy.tick`; the code has quotes and accounts as queries and no clearing | contract text ahead of code |
| CONTRACTS.md §8 | promises cost-of-goods and spoilage lines; `accounts()` has neither | contract text ahead of code |
| CONTRACTS.md §6, §4b | economy reads `reader.production` and `hasFixture`; economy `src/` calls only `reader.posts()` | equipment-presence check unbuilt |
| Question ids | CONTRACTS/README call idle fixtures "Q9"; in settlement QUESTIONS.md it is Q5 and Q9 is inheritance | id inconsistency |
| Load-bearing prose | realism regex-parses constants from library text cells (glycogenFactor, repair rates, places.ts hurricane weight): rewording a sentence changes the model | structural; ROADMAP phase 0 |

## 6. How to read graph.json

`nodes` (id, engine, status, kind, domain, scope); `edges` (`from`, `to`, `type`, and `group` on overlap edges);
`overlap_groups`; `unit_issues`; `cycles` (strongly connected components of `depends_on`); `unresolved_dependencies`
(name → mentions). The dependency resolution is by id, then by unique name or last id segment; a wrong match is
possible on generic names, so treat single edges as leads and the overlap groups (hand-checked) as findings.
""")
open("E:/AI Programs/Toolchain/GRAPH.md", "w", encoding="utf-8").write("\n".join(L) + "\n")
print(len("\n".join(L)), cross.most_common())
