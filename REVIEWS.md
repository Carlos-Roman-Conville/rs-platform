# Independent model reviews (registry keeper)

PLATFORM.md §11a: a change to a scientific model or an architectural assumption is recorded and reviewed before it
becomes authoritative, and an author testing its own work is not independence. The registry keeper reviews such
changes against the registry (one owner per mechanism, no second penalty, refinement B, evidence levels) and the
evidence offered. A review **accepts**, **accepts with conditions**, or **names the change**. It never replaces
validation: an accepted model is still only implemented until independent evidence validates it.

## Testing cost rule used in every review and re-audit (PLATFORM.md §11b, Rex 2026-10-30)

Three levels: (1) **mechanism tests**, small and deterministic (equations, units, conservation, boundary conditions),
run with every unit; (2) **integration tests**, run only when a shared interface or contract changes; (3)
**scientific validation**, periodic comparisons against independent data, never on every change. A Gate runs the
filtered suite for what the unit touched plus the mandatory cheap checks; the full thirty-day harness or a full engine
suite is never rerun per change. **Mandatory regardless of cost:** conservation checks, destructive-operation
safeguards, and the tests of any modified shared contract. §11a's states (implemented, integrated, validated) are
unchanged. How the registry applies it:
- A re-audit reads the committed Gate and its log; it reruns a suite only when the unit changed a shared contract or
  the log does not show the touched tests passing.
- A review that finds a Gate running a full suite with no contract change notes it as a cost finding, not a defect.
- A Gate that drops a conservation check, a safeguard, or a modified contract's tests fails the review.
- "Validated" in the registry comes only from level 3 evidence, recorded with its date; a later change does not
  re-run it unless it touches the validated mechanism's equations or data.

## V&V states the registry uses (defined 2026-10-31, after the organisation review)

PLATFORM.md §11a defines three states; the registry writes each in one of these forms only:
- **implemented**: true when the row is built and its own tests pass; false otherwise.
- **integrated**: `yes (combined test: <ids>)` when a named combined test runs the row with what it reads and feeds;
  `yes with stubs (…)` when the combined test runs it only against host stubs or itself (named in the text);
  `no (no combined test; …)` when wiring is only by prop names, process order or contract text; `no (not built)`;
  `plugin (…)` for pirate rows outside the registry's ports; `n/a (restatement)`. "Integrated by convention" is
  **retired**: it was not a §11a state, and its 168 rows now read `no` or `yes (combined test …)` from the data.
- **validated**: `yes (…)` only with independent evidence within a declared tolerance; `candidate (…)` when a test
  compares with published values awaiting re-audit; `failed (…)`; `no (…)`. A fit of a model's output to its own
  functional form is **verification**, never validation (V1 forgetting, reclassified 2026-10-31).

## R-1 — Reality P1 batch 1, five model changes (2026-10-30)

Request: `HQ/handoffs/reality/P1-MODEL-REVIEW.md` (Reality keeper); units in
`Games/Card Games/_agent/queue/realism/`, gated on the marker `reality-p1-model-review`.

| Unit | Change | Registry group | Verdict | Conditions |
|---|---|---|---|---|
| 2623 | dehydration lowers plasma volume (raises haemoglobin concentration); body water one registry content | DUP-22 (approved owner: physiology water balance) | **accepted with conditions** | (a) the source's unit and sign (unit 2643) are confirmed before 2623's plasma term becomes authoritative; until then the term is labelled level 5 (hypothesis) and the unit's Gate records "unvalidated"; (b) this becomes **the one pathway** from dehydration to oxygen delivery: when batch 2 group 1 (DUP-15) lands, the hydration bands' work-capacity factors must not also count the delivery effect (recorded in DUP-15); (c) "red-cell mass unchanged over days" is recorded as an approximation, level 4 |
| 2626 | epidemic new cases = catch rate × remaining susceptibles | DUP-20 (aggregation of medicine's course) | **accepted with a condition** | the force of infection is a host input here, not linked to prevalence (one exposure a day at dose = catch rate); record it as an approximation (level 4) and as a declared gap until pathogen transmission between bodies (P3) supplies it; the batch-1 acceptance test (individual mean vs aggregate) still applies |
| 2633 | one death per body with exactly one cause, matching an open crisis; starvation opens a crisis; background death aggregate-only | DUP-19 (approved owner: crisis record; IF-1) | **accepted with conditions** | (a) the declared gap names its successor: individual background death comes from Rex's cellular layer (ageing emergent, P3, after R-CELL), not phase 12's timer; (b) organ floors citing only the game's ANATOMY.md are labelled level 5 (hypothesis), and their statement moves into a realism gear file (§8) with the doc pointing back |
| 2634 | local (3CC) and systemic (MET-hours) fatigue not derived from each other; one schedule row drives both | DUP-13 (mixed) | **accepted** | this satisfies refinement B as a common-driver relation rather than an aggregation: two distinct quantities, one source record, neither derived from the other. Batch-1 group 7's acceptance test is read accordingly: one work record drives both, and no other home keeps a fatigue counter. "Activation share = 3CC effort" recorded as an approximation, level 4 |
| 2635 | Banister's state scales maximal cardiac output through a clamp, the only pathway into `aerobic_today` | DUP-14 (approved owner: circulation `aerobic_today`) and DUP-18 | **accepted with conditions** | the architecture (one pathway) is accepted; the clamp (0.6–1.0) and its normalisation are **estimates** from the game's PHYSIOLOGY.md §2, uncalibrated: labelled `estimate`, evidence level 4–5, and moved into a realism gear file; one constant set (DUP-18), never both the prose and the table values; "validated" only after DO2max × a cited extraction falls within published VO2max norms |

The registry keeper does not write into another keeper's queue: the Reality keeper writes the marker, with the
conditions above carried into the units' Gates (2623 additionally waits on 2643 or carries the level-5 label).

## R-2 — Settlement building decay (SET-20), proposed material-class model (2026-10-30)

Request: settlement keeper; `Toolchain/settlement/VALIDATION.md` (commit 5a0603b), belt unit 2645 (VAL-D1).

- **Finding confirmed:** with today's bands (`src/config.ts`: 0.0005, 0.001, 0.002 per day) a new building falls
  from 1.0 to ruined in 400 + 300 + 150 = 850 days without repair, against sourced lifetimes of years (thatch) to
  decades (brick, stone). Registry rows `settlement.building.condition_decay` and `.condition_output_factor`:
  **implemented, failed validation**, evidence level 5.
- **Proposed change (decay per material class, rates from sources): accepted in structure, as interim**, with
  conditions:
  1. It is the interim aggregate of overlap group **DUP-9** (degradation in four homes; proposed owner the planned
     materials mechanism, Physical Reality Phase 9). The per-class rates are **data** (config, each value labelled
     researched or estimate with its source), not a second degradation model; when the materials mechanism lands,
     building condition reads physical decay and the class rates become its validation data.
  2. Exposure (salt wind, rain) enters only as a host-supplied exposure class, never a weather computation inside
     Settlement (weather belongs to Physical Reality, P2).
  3. The band shape (accelerating decay, output factors) stays level 5 and flagged until evidence exists.
  4. Rates come only from sources; where the evidence leaves a class unsourced, the class is null and flagged, or
     the question goes to Rex (no invented rules). Secondary or vendor sources are labelled as such.
- **Who reviews:** this review (the registry keeper) covers the structure and the overlap. No Cursor Opus design
  review is needed. Rex only if the sources conflict or leave a class empty.

### R-2 follow-up (2026-10-30): settlement VALIDATION.md §4b, commit e4de618; belt unit 2646 after kernel 2615

**Accepted:** all four conditions are met.
- The rates are config data, labelled per row, with DUP-9 named as the later owner.
- Exposure is a host-supplied class.
- The band shape stays at level 5.
- Unsourced classes are null and flagged. Masonry and wattle walls are null; years to ruin = the roof's service life is labelled level 5.

Two consequences, recorded so neither is a surprise:
1. **Documented behaviour change.** A building with no class does not decay, and the pirate data has no classes yet. So when 2646 lands, the pirate port's buildings stop decaying. They do not keep today's 850 days. Under Rex's "no silent change" rule (ENGINES.md, kernel adoption), the pirate adapter's thirty-day results and goldens change knowingly, with the correction documented. The plugin's keepers (town, balance) should hear of it before 2646 runs.
2. **A gap the pirate game will meet.** Its port is a salt-wind Caribbean coast, and `salt-wind` is null. Even classed buildings there will not decay until a source is found or Rex decides the factor. Flagged for Rex, to be decided when the game assigns classes, not before.

The rows are re-marked when 2646 passes. Until then they stay "implemented, failed validation" at level 5. Afterwards, rows for classes with sourced estimates become validation candidates, against VAL-D1.

## Log

| Date | Review | Verdict |
|---|---|---|
| 2026-10-30 | R-1 Reality P1 batch 1 (2623, 2626, 2633, 2634, 2635) | all five accepted; conditions on 2623, 2626, 2633, 2635 |
| 2026-10-30 | R-1 follow-up | Reality wrote the marker `realism/done/reality-p1-model-review.md` (verified). The conditions are carried in the Gates: 2623's level-5 "unvalidated: plasma" line names DUP-15, plus a level-4 red-cell line; 2626's level-4 force-of-infection gap; 2633's gap names the cellular layer, with organ floors at level 5 in `realism/gears/anatomy-crisis-floors.md`; 2635's `realism/gears/aerobic-training-clamp.md` is an estimate at levels 4–5 using only the Banister table's constants. Pirate unit 2637 points PHYSIOLOGY.md §2 and ANATOMY.md §3a at the gear files |
| 2026-10-30 | R-2 re-audit: settlement 2646 (79a848a) | the class model is implemented as §4b: `decayClasses` labelled and sourced, null classes flagged, `unvalidatedDecay` lists the unclassified. VAL-D1 passes, but it verifies the model against its own configured lifetimes, so it is verification, not independent validation. The row is now **implemented, interim class model; validation candidate** (secondary, partly modern sources), evidence level 5 for the band shape and the roof-life assumption. The output-factor row is unvalidated at level 5 |
| 2026-10-30 | R-2 follow-up: settlement §4b (e4de618) | conditions met; two consequences recorded (unclassified buildings stop decaying; `salt-wind` null) |
| 2026-10-30 | R-2 Settlement decay (SET-20) | finding confirmed; material-class model accepted in structure as DUP-9's interim aggregate, with conditions |
| 2026-10-30 | PLATFORM §11b testing cost rule | recorded above R-1; applied to every review and re-audit from now |
| 2026-10-31 | Organisation review (controller's sub-agent) | V&V states defined above; Cognition's 13 rows 'yes with stubs'; episodic V1 → verification (validated no); 'by convention' retired; shared re-owned to contracts only; DUP-58..60 opened (batch 2b) |
