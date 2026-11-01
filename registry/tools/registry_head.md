# The mechanism registry (opened 2026-10-30, registry keeper)

**Status: approved with refinements (Rex, 2026-10-30).** Rex approved the audit's engine organisation and phase
order (`ENGINES.md` "The approved organisation"; PLATFORM.md log). The registry records what exists; the owner of
each overlap group stays **proposed** until its batch is approved (`OVERLAPS-BATCH-1.md` first). Nothing has
moved, nothing was deleted or rewritten, and no code changed. Refinement B governs closure: a detailed and an
aggregate computation may coexist when one owner holds the state and the aggregation interface is documented; each
overlap group carries an `authority` class saying which it is (GRAPH.md §2).

**The rule it serves (Rex, PLATFORM.md §7):** every mechanism has one authoritative owner. Before any new
subsystem, formula, table or document, search this registry (`registry/mechanisms.json`, or the tables below) for
an equivalent. If one exists, consume its output through its interface; never add a second penalty for an effect
owned elsewhere.

## The files

| File | What |
|---|---|
| `REGISTRY.md` (this) | how to use the registry; the summary; one line per mechanism |
| `registry/mechanisms.json` | the full contract per row: every PLATFORM.md §7 field |
| `registry/graph.json` | nodes, edges (depends_on, restates, overlap), the __NGROUPS__ overlap groups (each with its `authority` class and presentation `batch`), the 15 unit issues, cycles, unresolved dependencies |
| `registry/quantities.json` | the quantity vocabulary (schema 2, agreed with the Kernel keeper, `kernel/DESIGN.md` §8): one row per quantity id `<scope>.<quantity>`, its unit symbol (from `kernel/data/units.json` once it exists), its one writer. 317 seeds from the audit's output names, awaiting each owner's confirmation; 17 have several candidate writers |
| `registry/aliases.json` | renames of mechanism and quantity ids (old → new, date, reason); a retired id is never reused |
| `OVERLAPS-BATCH-1.md` | the first batch of overlap groups for Rex: owner, reads and aggregates, acceptance test, keepers to agree, routing |
| `GRAPH.md` | the readable graph: every duplicate and overlap with its homes and proposed owner, unit problems, cycles, ownership conflicts |
| `AUDIT.md` | the seven domains against what exists; missing foundations; universal vs pirate-specific; the engine-organisation proposal |
| `ROADMAP.md` | phases in dependency order with acceptance tests, owners and belt routing; the historical-reconstruction benchmark |

## How each row reads (the §7 contract)

`mechanisms.json` rows carry: `id` (stable, dotted `<engine>.<area>.<mechanism>`), `name`, `owning_engine`,
`home` (file and function or section), `home_kind` (code / docs), `status` (**built** = code exists;
**documented-only** = a formula or rule written in a doc, no code; **planned** = named as future work), `kind`
(**mechanism** = an authoritative home; **restatement** = a doc or adapter restating a mechanism owned elsewhere,
with `restates` pointing at the owner), `domain` (A–G of PLATFORM.md §3, or infra), `scope` (universal /
pirate-specific / mixed), `inputs` and `outputs` with units, `state`, `formulation`, `dependencies`, `timescale`,
`invariants`, `sources`, `evidence` (1–6, PLATFORM.md §4: 1 physical law, 2 statistical, 3 historical observation,
4 simulation approximation, 5 hypothetical, 6 fiction), `approximations`, `tests`, `consumers`, `notes`,
`overlap_groups` (DUP- ids in GRAPH.md), `unit_issues` (UNIT- ids), and `audit_batch` (which reader extracted it).
Schema 2 (2026-10-30) adds `writes` and `reads` (quantity ids from `quantities.json`, mirrored from each engine's
`kernel.json` processes once declared; seeded today from outputs) and `aggregates` ({of, by, interface, test}:
the refinement-B link from an aggregate to the detailed quantity it summarises). The kernel's check
(`check-registry.ts <registry dir> <kernel.json…>`) reads only rows with kind "mechanism" and status "built" and
fails on a declared write with no row, or a quantity with two writers; there is no exception list.
Schema 4 (Rex, 2026-10-31) makes every contract answer five questions: what enters (`inputs`), what leaves
(`outputs`), what accumulates (`state`), **what limits the rate (`rate_limiter`)** and **what makes it fail
(`failure_mode`)**. The two new fields are null on every row until its owner fills them; the kernel's check warns,
never fails, when they are empty on a built row. The V&V record's item 5 also gains `numerical` {`stability`,
`coupled_update_consistency`, `sensitivity`} (PLATFORM.md §11a item 5, widened the same day).

Evidence grades are the auditors' judgement from the code and docs, to be confirmed by each owner. Fields the
source does not state are recorded as such ("none stated", "unknown"), never filled in.

## How the audit was done

Six readers (Sonnet), each over one batch with one extraction schema: realism physical side, realism life side,
settlement + economy, the pirate body docs and STATS.md, the pirate world/science/balance/goods/combat docs and
their game code, and the ten keepers' handoffs and issues. The registry keeper merged the rows, linked 91
restatements to their owners, wrote the first 47 overlap groups (DUP-1..47; __NGROUPS__ today) and 15 unit issues by hand, and computed the graph.
Files over 40 KB were searched, never read whole; per-food, per-disease and per-item table rows are data, not
mechanisms, and are not itemised. Coverage limits are listed in `HQ/handoffs/registry/HANDOFF.md`.

## Summary

| | built | documented-only | planned | total |
|---|---|---|---|---|
__SUMMARY__

**Restatements** are not errors: the pirate body docs are rendered from the same library JSON as the realism
code (`body/build-body-data.py`), so their tables cannot disagree with the code. Disagreements live only in their
prose formulas; those are in GRAPH.md (DUP-14, DUP-18, the sweat formula, the DO2 dissolved term).

**Most important findings** (detail in GRAPH.md and AUDIT.md):

1. **No platform mechanism registry existed.** `realism/src/registry.ts` is an entity store (substances,
   materials, components); `graph.ts` is a list of port edges. Both are reusable as shared vocabulary (their ids).
2. **47 overlap groups at the first audit** (__NGROUPS__ today), of which the gravest are the double penalties the §7 rule forbids: work capacity from
   four multipliers (DUP-15), vitamin C with four consequences (DUP-16), fatigue in five places (DUP-13), vision
   dips from several sources (DUP-37), and mortality from five sources with no cause-of-death ledger (DUP-19).
3. **One wiring bug:** circulation writes `blood_lost_ml`, nutrition reads `blood_lost_l`; haemorrhage never costs
   iron outside tests (UNIT-1). Several neurology inputs have no producer (UNIT-15).
4. **No shared clock:** six tick systems, nothing converts between them (DUP-33).
5. **Contract text and code differ** in three places (CONTRACTS.md §6, §8, §9; GRAPH.md §5).
6. **Domains C, E, F, G have almost nothing universal.** What exists there is pirate-specific (alignment,
   personality charts, STATS) or a placeholder (settlement offices, population.ts).
7. **Four PLATFORM.md §6 conflicts** (date- or level-gated unlocks) live in the pirate plugin; acceptable as plugin
   configuration, never as universal rules (AUDIT.md §4).
8. **Cellular biology (Rex, 2026-10-30):** 12 planned rows `realism.cellular.*` record the foundational
   Life & Species layer (`CELLULAR.md`, not yet written): cell populations with representative states, ATP flux,
   mitochondria, DNA damage and repair, telomeres, senescence, proteostasis, stem-cell pools, epigenetics,
   inflammation, death and replacement, and ageing as an emergent output. What moves under it is the registry's
   task R-CELL after P0 and P1 (ROADMAP.md). Beside them, 9 planned rows for the representational resolution of
   biology (Rex, 2026-10-30): three records per organism (`realism.records.genetic_profile`, `cellular_state`,
   `organism_state`), genetics (`realism.genetics.recombination`, `inheritance`, `mutation`, `expression_response`,
   `population_distribution`) and `realism.development.trait_change` (ΔM = f(G, T, N, H, R)).
9. **Interfaces, not overlaps:** IF-1 death to fate (Reality decides biological failure, with a crisis before every
   death; the pirate fate system decides what a dead character becomes); IF-2 the character sheet as a view of the
   three organism records, never a second source of numbers (GRAPH.md §2).

## Mechanisms (authoritative homes), by owning engine

Columns: id · status · domain · scope · evidence · V&V · overlap groups and unit issues · home.
Status: B built, D documented-only, P planned. Scope: U universal, P pirate-specific, M mixed.
V&V (schema 3, PLATFORM.md §11a): **I** implemented (code and unit tests), **T** integration-tested (a combined test
runs it with connected mechanisms; registry ports arrive with P0), **V** validated against independent evidence
(re-audited), **v** a validation candidate awaiting re-audit, **F** failed validation (the owner reported it; see the row's
record), **-** not yet. Model reviews of proposed changes are in `REVIEWS.md`. The full record per row is `vv` in
`mechanisms.json`: sources and model, applicability, verification tests, validation evidence and tolerance,
stability/conservation/boundary tests, `integration_tested_with`, integration tests, report.

