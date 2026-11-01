# Handoffs digest (audit input), read 2026-10-30

Sources: `Toolchain/PLATFORM.md`, `ENGINES.md`; `HQ/handoffs/{README, art, balance, bestiary, combat, controller, economy, reality, settlement, story, town}`; six side-session notes. NOTE: `HQ/handoffs/registry/` does not exist yet (README lists it; the registry keeper has not written). Pirate repo = `E:/AI Programs/Games/RPG's/pirate-ship` (files under `files/pirate-ship/`). Nothing is pushed anywhere. Test-count discrepancies: ENGINES.md says Settlement "23 tests", PLATFORM/HANDOFF say 26; pirate web is 387 (economy, settlement) vs 384 (reality) at different commits.

## 1. Per keeper

**Art** (paused). Records art direction, judges art Rex shares; never makes art or code. Built: ART_DIRECTION.md, CHARACTER_SHEETS.md, TOWN_SHEETS.md, REVIEWS.md in `art/`; commits 82daa66, aa5d6ad, f808486, 1ba0342, a1c56e2. Tests: none (docs). In flight: nothing; TOWN_SHEETS lags UPGRADES (ART-3, held). Next: update TOWN_SHEETS to ~19 `port.*` slots, farm first.

**Balance** (paused on C5 28). Guards that every ending stays possible; owns `balance/` (BALANCE.md, ALIGNMENT.md), alignment engine `web/src/alignment/*.ts`, data `data/pirate-ship/alignment/{thresholds,charts,starts,institutions,events,gates,conditions}.json`, PLAN Phase 2/3. Built: reducer `reduce(state, command, config)` (belt tasks 2474-2478), simulator `sim/` (9b5fdbb), gates (259f4a1, 0059012, 221ed95, 38b36b9, 5443841), develop conditions (3d33ff8, 567c2f7, 5320602, a09e2a7), scope run-downs (b664ef2 ... 70aa049), economy pointers (a257ef5, f54e1fd, 58c6387, c789d8a), death decisions (81e7886, 6c02836). Latest 6c02836. Tests: 8 files, 178 pass; all four perfect towns reachable (OG 61 steps, CG 68, OE 49, CE 57). In flight: nothing; Phase 2 gate = Rex tunes `thresholds.json`. Next: after C5 28, rewrite BALANCE C1 / ALIGNMENT §5/§7, respec PLAN unit 21 (`die`/`transform`/`resurrect`), rerun sims.

**Bestiary** (maintain, idle). Creature definitions, species-specific profiles (content only; never physiology), provenance labels, journal entries, encounter data; `bestiary/`. Built: BESTIARY.md, ENTRIES.md (133 candidate rows), `build-bestiary.py`, `bestiary.json` (aef4e71). Tests: build script's duplicate-id/label check. In flight: none. Next: when Rex picks creatures, stamp, rebuild, write profile rows in the shape Reality specifies (BST-9 waits on that shape).

**Combat** (idle until Rex resumes walkthrough). `combat/COMBAT.md` only (docs); not physics. Commits (2026-10-29): 906b733, 10b8dd1, a8a7c13, cd21103, 8f7b547, e91d147, 027d602, 563cb3e, fdcd450, 1f12497, 822dd4b, d01b78a. No code, no tests. Next: COMBAT.md §9 "Interfaces consumed" (CMB-11), then Open 1-3.

**Controller**. Coordinates; does not build; owns PLATFORM.md, ENGINES.md. Built: ENGINES.md, PLATFORM.md, belt lanes `settlement`/`economy` in `Card Games/_agent/lanes.py`, `STARTING_TOWN.md` (pirate repo, uncommitted), handoff folders. In flight: registry keeper audit (REGISTRY.md, registry/, GRAPH.md, ROADMAP.md), STARTING_TOWN pass, Reality phases. Next: read registry deliverables, present to Rex, then tell keepers their reassignment, queue belt units, update dashboard (CTRL-9, CTRL-10).

**Economy**. `Toolchain/economy/` (own repo, universal) + pirate adapter `web/src/economy/`. Commits: contract 6eb241b (byte-identical `CONTRACTS.md` in economy and settlement); engine 754de91 (records, reducer, MaterialProvider), b54a984 (spoilage, consumption, shortage, prices, abstract production), ffee3eb (orgs, sell/buy, shipments, freight, accounting), 1760571 (labour quotes, `examples/three-ports.ts`); pirate 962702a (adapter + thirty-day benchmark), c2d2122 (docs), 45c7bab, db65de2 (research rows); economy fbcc56f (`RESEARCH.md`), 374f740 (burial/waste scope, E15/E16 planned). Tests: engine 25/25 (E1-E14), pirate web 387/387 incl. I1, I2. Idle. Next: `king-davenant` price rule on Rex's approval; PLAN step 11 (consumption from a realism population/nutrition provider) needs Reality to offer one.

**Reality & Species**. `Toolchain/realism/` (`@rex/realism`), pirate `body/`, `world/`, `science/`, STATS.md editing coordinator (design is Rex's). Engine HEAD 7190219 (plan commit), last code 5491dac; registry, connection graph, conservation/process engine, scheduler, trace (phases 1-3); ten modules in `src/` (physiology, nutrition, atmosphere, environment, neurology, circulation, anatomy, muscular, medicine, ecology/population; belt 2520-2532); `crisis.ts` (2561); chemistry pass 2571-2583 (930197d, 1dd835c); fixes a3bc20e, c503778, 1b1e14f, 87c0031, eefb0ab. Checkpoints (CHECKPOINTS.md): `human-week.ts`, `human-wound.ts`, `horse-stable.ts`. Game adapters `web/src/world/adapters/` (characters, food, places, stats, work, medicine), `settlement.run.ts` (2539/2563/2570). Tests: engine 239 passed, 1 todo; game 384. In flight: `PHASES-6-PLUS.md` (7190219) awaits Rex's build-order pick. Next: `src/mechanics.ts` (de Leva 1996 / Winter 2009 segment masses, gravity, Coulomb friction, momentum/energy checks; human standing one minute, then horse).

**Settlement**. `Toolchain/settlement/` (`@rex/settlement`, universal) + pirate adapter `web/src/settlement/`, `data/pirate-ship/settlement/start.json`. Commits: 8e3e282 (design), ae07c4c (step 1), 1592a6f, 8ca880e + 2c4223c (contract; U13/U14), 7cdc178, bca54db (cemeteries/sanitation/land-use scope, Q16-Q18); pirate dfed944, 2fad6d4, 2830cce, 0d6777c, b4e72c6. Tests: 26/26 package (U1-U14); pirate T0, T1, A1, A2. MIGRATION: 12 steps, 1-2 done. Idle. Next: none ready; step 3 `derive_map.py` on Q1, `inventoryOf` hook if economy asks.

**Story**. `story/` (STORY.md, QUESTLINES.md, `characters/` 19 files). Docs only. Commits: 5676d43, 55b7907, 377d779, e81a30a, 50af6e2, 91d844b, e4de1a4, 4a87aae, f91bdcb, 71fe052, 232b70a, 06db31e, 062e70e, a056e5c, a244d58, 09065c0, 74dbb4e. Held scope sits in the pending-scope note. Idle. Next: none.

**Town**. `town/` (TOWNS.md, UPGRADES.md, ENDINGS.md, FACILITIES.md, CULTURE.md, JUDGING.md), owns STARTING_TOWN.md from Rex's answer. Commits: 48c5bba ... ee41de1 (slot model, ghost rule), 5ab5fa3, 31fbc99, 5bb7b22, 9e63174, 31866cf, f42fd2d, d2e8b7c, 6b52a95, 394a995 (+ docks fix, TOWN-22). Docs only. In flight: balance run-downs pending (not folded in); STARTING_TOWN awaiting Rex. Next: carry Rex's answers into FACILITIES/`town/`, hand rows to Settlement for `start.json`; CULTURE.md per town is a standing duty.

**Registry** (not yet in handoffs): lane named `registry-keeper`, session local_b3c59b5a-...; deliverables REGISTRY.md, registry/, GRAPH.md, ROADMAP.md, universal-vs-pirate split, reorganisation proposal. Folder absent.

## 2. Open questions blocked on Rex

Rex answers most town/economy/settlement ones in one place: `STARTING_TOWN.md` (30 rows; Q15 there carries a proposed, undecided answer).

| Id | Owner | What it blocks |
|---|---|---|
| A1 portrait size, A2 outline at bust, A3 palette ramps, A4/ART-5 three-quarter camera numbers, A5 side facing, A6 expression list, A7 heart-event overpaint, A8 source-file location | art | bust renders, palette snap, every world sprite/tile, walk sheets, expression sheets, heart events, Files columns |
| ART-1 (fangs/tattoo literal?), ART-2 (own mesh or chest slot), ART-4 told Rex | art | intj-f design, story doc, world sprite |
| Scope change ALIGNMENT §10 (108 chars, ghost state, locales) | art/town/story | TOWN_SHEETS shape (ART-3), ghost column |
| C5 28 (BAL-28) ghost rule vs "only actual death transforms" | balance | PLAN units 20, 21, 29, every fate-dependent sim; pauses the balance lane |
| C5 31 (BAL-31) does "perfect" become completing influential characters' endings | balance | simulator search target |
| C5 2 (BAL-2) points carried home: adopt / deposit / daily | balance | engine §5, unit 22 |
| C5 1, 11, 12 (BAL-1/11/12) pairs vs twelve locales; do docks/tavern/fort develop | balance | units 20, 27 |
| C5 29, 30 (BAL-29/30) fate + form; resurrection cost | balance | unit 21 |
| C5 16, 18, 19 (BAL-16/18/19) faction moves the square; ending = faction; Act II antagonist set | balance | units 32, 34 |
| C5 5, 6, 9 neutrals, empty-town key, sequence rules | balance | unit 25 |
| C5 3, 8 (BAL-3/8) per-character influence; 16 novices in alignment data | balance | unit 26 |
| C5 4, 7, 13, 15, 20-23, 25-27, 32 (BAL-4,7,13,15,20,21,22,23,25,27, 32 partly) | balance | thresholds, regional rules, ending count, one clock across three engines, ocean waiting |
| C5 24 (BAL-24) import mechanism for Toolchain economy package | balance -> economy | adapter wiring |
| Phase 2 gate: tune `thresholds.json` | balance | Phase 2 sign-off |
| Open 1 kraken; Open 2 which of 133 legends; Open 3 lwa/orisha; Open 4 post-period folklore; Open 5 enemy classes; Open 6 factions field creatures?; Open 7 the game's year | bestiary | first boss class, row stamping, 13 section-D rows, journal stacking rule, class JSON / combat enemy count (COMBAT Open 8), faction rosters, "found here in <year>" |
| COMBAT Open 1 (levels/HP), 2-3 (turns, actions, prepared shot), 4 (called shots), 5 (wound ladder), 6 (Intuition, poise, pool recovery), 7 (light/elevation), 8 (grid, enemy count), 9 (balance owner), 10 (ammo), 12 (per-limb split, Te floor N), 13 (muscle vs per-limb Strength), 14 (what combat reads); CMB-1 = ghost rule | combat | engine task, walkthrough, STATS edits |
| Approve/change STARTING_TOWN pass (30 rows) | controller/town | thirty-day sim on approved data, Town/Settlement/Economy rows |
| Registry proposal + roadmap approval; CTRL-12 `git init` at Toolchain root | controller/registry | keeper reassignments, belt units, dashboard (CTRL-9, CTRL-10) |
| CONTRACTS §12.1/GOODS Open 1-8 goods types; §12.2/Q7 `port.cash` treasury; §12.3 who values property (ECON-7/SET-9); §12.4 named characters' spending (ECON-8); §12.5 price formula; §12.6/Q10 wage levels; §12.7/Q9 idle fixture | economy (shared settlement) | goods typing, adapter account binding, `valueOf`, household consumption, price rule, `setWage`, `hasFixture` |
| Q15 (ECON-4/SET-8) labour sharing across lines; GOODS "Not here yet" numbers (ECON-5) | economy/settlement | step 7, hours per process, game lines/markets |
| REAL-1, REAL-2, F-CH-9, F-SE-12, F-MD-8 (=REAL-11), P12/F-SE-11, STATS.md "Open for Rex" (10 items), 50 empty fixtures, REAL-12 (phase order; may `estimate` drive a process) | reality | stats adapter band, checkpoint finality, settlement run, mechanism edits under STATS §1-3, all new engine work |
| Q1 footprints, Q5 fixtures, Q6 titles/operating, Q10 posts/wages/rents, Q7, Q9; Q3, Q4, Q8, Q11-Q14 "not blocking yet"; SET-11/12/13/14 (inheritance law, hoursPerDay 10 vs 11, brewhouse, docks title); Q16-Q18 | settlement | steps 3-7, `start.json` real rows |
| STORY-1/ISTJ, ENTJ priest recruitable, ENFP/ISFP, INFP chart, death forms/merfolk, STORY-2, `develops_place` (14 of 16), Open threads 1-6, 8, 9, go on held scope | story | character files, ending structure |
| UPGRADES open (pair ghost vs death ghosts; develop condition per character), ENDINGS Open 1 (TOWN-14), pending scope (twelve locales, three neutrals, nine factions, Acts), TOWN-4, TOWN-6, TOWN-13, TOWN-19, TOWN-22/23 approval | town | ghost states per slot, endings table, folding scope into `town/` |

Approximate count: ~100 raw line items across 10 keepers (art 12, balance 29, bestiary 7, combat 14, economy 8, reality 9, settlement ~7 unique, story ~9, town ~5 unique, controller 3); about 85 distinct decisions after merging the ghost-rule duplicates (CMB-1 = BAL-28 = TOWN-12 = STORY-2 = CTRL-11) and the Q7/Q9/Q10/Q15 shared items.

## 3. Overlap, duplicate, contradiction, boundary issues

| Id | Two sides | State |
|---|---|---|
| CMB-1 / BAL-28 / TOWN-12 / STORY-2 / CTRL-11 | Pair-competition ghost rule (town UPGRADES, balance BALANCE C1, 2026-10-28) vs death-only ghosts/forms (COMBAT §4e, 2026-10-29) | open, Rex; pauses balance |
| CMB-2 / BAL-29 | Alignment fate set (alive/dead/ghost) vs new states (missing, mecha, zombie, angel, demon, fish-person) | open |
| CMB-3 / BAL-32 / BAL-13 / BAL-30 / BST-5 | Balance reachability vs every new death path (disease, siege, resurrection, boss guarding water) | partly decided (no biological immunity) |
| CMB-4 / BAL-31 | "Perfect" redefinition (ChatGPT) vs town ENDINGS "perfect = consistency" | open |
| TOWN-14 | `end.perfect/good/ruin` vs the nine region endings | open |
| CMB-5, CMB-6, CMB-7 | PSYCHOLOGY.md vs existing madness/hearts/sliders; POPULATION.md vs town/alignment fates; second ship-wear system vs DUTIES.md | fixed (scoped to inputs only / extend existing) |
| CMB-8 | Hidden penalties need a visible face | open |
| CMB-9 | Per-limb stored Strength vs computed from muscular system (Open 13) | open |
| CMB-10 / CTRL-2 | STATS.md edited by Combat, Reality, Story | decided by Rex: Reality coordinates; others propose |
| CMB-11 | COMBAT §3/§4 restate physics/wound effects that realism owns | open (§9 interfaces proposed) |
| ECON-1 / SET-5 | Recipe rates stored in Settlement lines and Economy recipes | fixed (2c4223c) |
| ECON-2 / SET-6, SET-7 | Closed `TransactionKind`; no `pay`/ledger day filter | fixed (2c4223c) |
| ECON-3 / SET-4 | `inv.port.<place>` placeholder refs vs economy-owned `inv.` prefix | open, alias workaround |
| ECON-4 / SET-8 / Q15 | In-order labour sharing starves second line; proposed: finite worker time, Settlement availability / Economy hours per process (unit mismatch: worker-days vs hours per unit) | open, Rex |
| ECON-5 / ECON-10 / REAL-9 | Recipe quantities/yields/labour per unit absent (inputs named, unitless); every work rate a fixture (F-WK) | open; economy owns rates |
| ECON-6 | `byproductOf` is `<skill>:<name>` not a recipe id | open workaround |
| ECON-7 / SET-9 | `PriceProvider.valueOf` for property has no owner | open, Rex (§12.3) |
| ECON-8 | Household consumption source: five numbers vs headcount x per-capita vs ledger | open (§12.4) |
| ECON-9 | No Caribbean wage source; Pennsylvania 1698 / Navy 1653 used | open |
| SET-12 | Engine `hoursPerDay` 10 (no source) vs 11 working hours found (Voth) | open |
| SET-11 / TOWN-23 | Rex's inheritance precedents vs period primogeniture | open/decided (precedent stands; a will explains) |
| SET-13, SET-14 / TOWN-22 | `start.json` brewhouse and town-held docks vs sources (docks fixed on town side) | open (Rex) / fixed |
| SET-3 | `Toolchain/SCOPE.md` has no row for `realism/` | open |
| SET-10 | `start.json` geometry placeholder | open, waits Q1 |
| TOWN-1, 2, 3, 5, 7, 9, 11, 18 | One-owner slot model vs titles/leases; slot id vs parcel id; one state per slot; mayor vs `sec.townhall` contest; recruit vs employ; one-screen port (PIRATE.md) vs 16 places; `developed` vs staffed | decided by Rex (FACILITIES §6a); TOWN-9 PIRATE.md not reconciled |
| TOWN-4 | Two rivals on one parcel (`port.church`, ISTJ+ENTJ) | open |
| TOWN-6 | Property market could bypass "can't max a town" and the ghost rule | open, guard noted |
| TOWN-8 | Facilities a settlement-level boolean in recipes.json vs per-parcel fixtures (Q5) | open |
| TOWN-10 | `ports.json` per-settlement production vs per-facility production | open (economy keeper) |
| TOWN-17 | GOODS.md L824 says ports aren't data; `ports.json` exists | open (economy file) |
| TOWN-15, TOWN-16 | Twelve locales (one place/sector) vs UPGRADES two; tavern and brothel separate | open, pending |
| TOWN-20 | CULTURE.md enslaved labour as fact vs GOODS Open 1 | open; Open 1 governs |
| BAL-16 / STORY-4 | Nine factions on the alignment square vs "factions apart from alignment" | partly decided; held |
| BAL-17 | Criminal vs demonic: one faction or two; which cult owns evil forms | decided (three evil factions); cult ownership open |
| BAL-24 / BAL-26 / BAL-14 | Where economy lives; economic viability owner; combat balance owner | decided / fixed / fixed (but COMBAT Open 9 still unowned) |
| BAL-25 | Three engines, three ticks, one clock | open |
| BAL-27 | Ocean waiting vs town neglect vs ghosting a slot | open |
| BAL-3 | Per-character influence has no STATS owner | open |
| BAL-23 | World module apart from town engine | open |
| BST-2 | Time Anomaly label (JOURNAL.md, Reality's rule) vs post-period folklore | open |
| BST-4 | Abyssal "ancient force" vs Olokun | open |
| BST-9 | Profile row shape not specified by Reality | open |
| BST-5 | Bosses guarding water vs ending reachability | open |
| REAL-8 | Weather repeats a daily mean; diurnal curve unused | open (game adapter) |
| REAL-10 | Trace grows 3 transfers/step; 30 days at 1 s = millions | open |
| REAL-12 | Old rule (null+flag) vs new value labels (`estimate` driving a process) | open, Rex |
| REAL-1 | Hydration "over 10%" band says death risk/hour; code reads work_capacity 0 | open |
| CTRL-5 | Population/demography under Reality, belongs to Society | open |
| CTRL-6 | Culture/organisations no owner; factions split Story (fiction) vs Balance (`factions.json`) | open |
| CTRL-7 | Alignment engine pirate-specific; eight-function model optional in Cognition | decided |
| CTRL-3 | Settlement built economy interfaces before an economy owner | fixed |
| CTRL-12 | Toolchain root not a git repo; PLATFORM, ENGINES, REGISTRY, ROADMAP unversioned | open |
| ART-5 | High Roller camera (2:1 dimetric 64x32) vs three-quarter view | open |

## 4. Calculations a keeper owns

| Mechanism | Owner | File | Code/doc | Scope |
|---|---|---|---|---|
| Alignment square, reducer, regions/endings (9 + perfect), town alignment as mean of developed institutions | balance (town doc ENDINGS/UPGRADES records the rule) | `web/src/alignment/*.ts`, `balance/ALIGNMENT.md`, `town/ENDINGS.md` | code + docs (two homes for the formula) | pirate |
| Ghost rule, develop conditions, joining gates, fates | balance/town | `gates.json`, `conditions.json`, `UPGRADES.md` | code+data / doc | pirate |
| Reachability simulator | balance | `alignment/sim/` | code | pirate |
| Combat resolution (hit odds, regional damage, flinch ladder, Endurance pool / Efficiency spend, Te floor, detection) | combat | `combat/COMBAT.md` | doc only | pirate (physics under it is realism's) |
| Functional capacity (`BODY.md` hub: states in, numbers out; per-limb stats) | reality | `body/BODY.md`, `STATS.md`; code `crisis.ts`, adapters `stats` | doc + code | universal core, pirate STATS layer |
| Physiology, nutrition, hydration, circulation, neurology, anatomy, muscular, medicine, atmosphere, environment, ecology/population, sweat | reality | `Toolchain/realism/src/*.ts`, `data/library/*.json` | code | universal |
| Conservation/process engine, connection graph, registry, scheduler, trace | reality | `Toolchain/realism/src/` | code | universal |
| Crisis (every death opens one) | reality | `src/crisis.ts` | code | universal |
| Mechanics, fluids, optics, materials, metabolism flux, waste/decomposition, genes/ageing | reality | `realism/PHASES-6-PLUS.md` | doc (plan) | universal, unbuilt |
| Psychology inputs to stress/madness/hearts | reality (inputs only) | `body/PSYCHOLOGY.md`; meters in PIRATE.md §7, STATS.md §3/§5 | doc | pirate meters |
| Population/demography pool | reality (to move to Society) | `world/POPULATION.md` | doc | universal |
| Weather/ocean currents, ecology/animal stocks | reality / economy (stocks) | `world/ENVIRONMENT.md`, `ECOLOGY.md` | doc | mixed |
| Ship wear | story/PIRATE.md | `DUTIES.md`, `PIRATE.md` §5a | doc | pirate |
| Production (recipes, rates, abstract markets), spoilage, consumption, shortage events | economy | `economy/src/tick/index.ts`, `queries.ts` | code | universal |
| Prices (`priceRule: base` default; `king-davenant` planned), wage quotes (`wageRule: posted-median`), trade, shipments, freight, accounting | economy | `src/queries.ts`, `commands.ts`, `labour.ts` | code | universal |
| Pirate economy data and adapter (`goods.json`, `recipes.json`, `ports.json`, `runDay`) | economy | `web/src/economy/`, `data/pirate-ship/economy/` | code+data | pirate |
| Daily capacity Q, labour availability, construction/renovation, businesses/posts/assignments, titles/leases, ledger/`pay`, Post.wage | settlement | `Toolchain/settlement/src/tick/`, `context.ts`, `commands.ts` | code | universal |
| Inheritance/succession | town (UPGRADES) / settlement titles | `UPGRADES.md`, `QUESTIONS.md` | doc | pirate |
| Bestiary classes (body plans, roles, hooks) | bestiary | `ENTRIES.md`, `bestiary.json` | data | pirate |
| Cemeteries, sanitation, burial services (scope) | settlement / economy | `PACKAGES.md` s8; `economy/PLAN.md` step 12 | doc | universal, unbuilt |

Not in any handoff but visible as latent overlaps (my inference): economy spoilage vs realism decomposition/nutrition; economy consumption vs realism nutrition/population; Post.wage (settlement) vs wage quotes (economy); settlement construction labour vs realism work capacity.

## 5. Registry, scheduler/time, catalogue, historical data

- **Registry:** realism's engine already has a "registry, connection graph" (PHASES 1-3; `realism/README`). PLATFORM §7 requires `REGISTRY.md` with a dependency graph; the registry keeper (absent folder) is producing it plus `GRAPH.md`, `ROADMAP.md`, audit, universal-vs-pirate split. PLATFORM §12 items 2-6, 8, 10 are that keeper's; Rex approves before any migration. Ids are stable per slot (`port.*`, `sec.*`, `end.*`, `event.*`); economy/settlement mint counters with the `inv.` prefix reserved for economy.
- **Scheduler/time:** ENGINES.md lists "universal time and events" as MISSING shared infrastructure (one scheduler, ms to years). Realism has a scheduler inside its engine (1 s steps; trace grows, REAL-10). Settlement ticks daily, then economy (contract §9); alignment has its own tick; BAL-25 and C5 25/27 want one clock across the three; PLATFORM §9 requires multiple resolutions (individual, village aggregate, civilisation long steps), finer refining the aggregate.
- **Catalogue:** PLATFORM §6 universal reference catalogue (ids, origin, spread, dates, provenance class, confidence) is unbuilt with no owner; nearest: bestiary `ENTRIES.md` (provenance labels = the eight in `science/JOURNAL.md`), `SOURCES.md` keys (TWN-, STL-, ECON-), GOODS.md. Rule: catalogue tags, never unlocks.
- **Historical data:** "historical first" with three labels researched / estimate / fiction (ENGINES). PLATFORM §4 six evidence levels and §5 reconstruction target (70% similarity, indicator list). Realism library rows need a `source`; unsourced stay `null` + flag (`FLAGS.md`, `flags/<module>.md`); REAL-12 asks whether `estimate` may drive a process. Historical rows: `economy/RESEARCH.md`, `STARTING_TOWN.md`, `town/CULTURE.md`; gaps ECON-9, ECON-10, TOWN-19. The three label systems (researched/estimate/fiction; PLATFORM's six evidence levels; library `[science]/[history]/[model]/[fiction]` marks) are not reconciled.
