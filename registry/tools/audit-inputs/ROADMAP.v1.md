# The platform roadmap (registry keeper, 2026-10-30)

**Status: proposed.** For Rex's approval (PLATFORM.md §12 item 8). Phases are ordered by dependency: a phase
starts when the phases it reads from have passed their acceptance tests. Each phase names its owning engine
(per the organisation proposed in `AUDIT.md` §6), its acceptance test, and how the work is run (§11): **keeper**
= needs an Opus keeper's design judgement; **belt** = units on the conveyor belt (Codex for engine logic,
Composer for data, tests and UI, Sonnet for platform work, Haiku for checks). No phase starts before Rex approves
the roadmap; nothing existing is deleted; the pirate content is preserved and parked (PLATFORM.md §1, §10).

Two rules apply to every phase:

- **Registry first.** A phase's first unit writes its mechanisms' rows (`registry/mechanisms.json`, the §7 contract)
  and searches for equivalents; its last unit updates the rows to built, and the registry keeper re-audits.
- **Historical first, labelled.** Every value is researched / estimate / fiction; every mechanism carries an
  evidence level (AUDIT.md §5).

## The order at a glance

```
P0 Kernel ──► P1 Overlap closure ──┬─► P2 Physical foundations ─┐
                                   ├─► P3 Life completion ──────┼─► P5 Grounded economy ─┐
                                   └─► P4 Catalogue v1 ─────────┘                        │
                                    P2,P3 ─► P7 Cognition ───────────────────────────────┤
                                    P3,P5 ─► P6 Society ─────────────────────────────────┤
                                              P5,P6,P7 ─► P8 Government ─────────────────┤
                                                 P2–P7 ─► P9 Knowledge & Technology ─────┤
                                                         P5–P9 ─► P10 History ───────────┴─► P11 Reconstruction benchmark
Plugin track (after P1, in parallel): PL, the pirate plugin re-seated on the interfaces
```

## Phases

| Phase | Owner (engine) | Contents | Acceptance test | Run as |
|---|---|---|---|---|
| **P0 Kernel** | Kernel (new) | one clock and event scheduler across timescales with declared process order (DUP-33); shared ids, reducer/replay, seeded RNG streams per mechanism (DUP-32); a units table (UNIT-5, -9, -12); interfaces keyed by registry id (UNIT-15); trace compaction (REAL-10); a registry check script | (1) one run drives realism at 1 s and settlement + economy daily from one clock for 30 simulated days; (2) the same inputs and seed replay byte-identical, and a different seed differs only in stochastic mechanisms; (3) the check script fails when a mechanism writes an output with no registry row, or two rows own one output | keeper (design); belt: Codex (scheduler, kernel), Sonnet (check script), Haiku (checks) |
| **P1 Overlap closure** | each current owner; the registry keeper tracks | Rex approves an owner per DUP group (GRAPH.md §2); losing homes become reads or restatements; fix the wiring faults (UNIT-1 `blood_lost_ml`/`_l`, UNIT-15 neurology inputs, UNIT-2 RH); one combination rule for functional capacity (DUP-15); one cause-of-death ledger (DUP-19); move the universal formulas out of the pirate docs into realism gear files (§8) | (1) for each closed group, a test that the cause changes one state and every effect reads it (e.g. 6 % dehydration lowers work capacity once; vitamin C depletion reaches healing only through collagen); (2) every death in a 30-day run has one recorded cause; (3) GRAPH.md shows no open double-penalty group | keeper (Reality, Settlement, Economy, each for its groups); belt: Codex units per group, Haiku checks |
| **P2 Physical foundations** | Reality → `physical` package | mechanics, gravity, friction, collisions (Phase 6); fluids, buoyancy, drag (7); optics, visibility (8); materials: deformation, fracture, corrosion, decay (9); structural mechanics and construction techniques per wall and roof type; weather and climate generation (taking over the pirate Markov chain's role, DUP-34); solar geometry and seasons; oceans and currents; hydrology; soils; geography and routes; a world energy ledger; acoustics | (1) a human standing one minute and a falling body conserve energy within 0.1 %; (2) a timber beam's deflection matches Euler–Bernoulli within 5 % and a wall fails at its tabulated load; (3) a hull floats at its Archimedes draught; (4) the weather generator reproduces a station's monthly normals (mean, variance, rain days) within 10 % over 30 simulated years; (5) visibility falls with illuminance as the source curve | keeper (Reality; the split decision at the start); belt: Codex (mechanisms), Composer (material and station data, tests) |
| **P3 Life completion** | Reality → `life` package | metabolism as flux (10); excretion, sanitation exposure, decomposition (11); genes and ageing through organ capacity (12, DUP-17); reproduction, pregnancy, growth and development; homeostasis loops; fever; hunger and appetite; one sleep pressure (DUP-12); crops as plants (growth from soil, water, light); pathogen transmission between bodies | (1) food in = tissue + heat + CO₂ + water + faeces + urine, mass balanced within 1 % over a week; (2) 1,000 simulated lives from birth reproduce the shape of a source life table (survival at 1, 5, 20, 50, 70 within 15 %); (3) a crop's yield responds to rain and soil as in the source trials; (4) no ageing effect exists outside organ capacity | keeper (Reality); belt: Codex, Composer (data), Haiku |
| **P4 Catalogue v1** | Catalogue (new) | the §6 schema; first content: substances, materials, crops, livestock, foods, tools and technologies, institutions and practices for the four benchmark regions and the pirate window; provenance classes; the pirate TECHNOLOGY.md lists as tags | (1) "Caribbean, 1690–1720" and "England, 1270" each return a starting-conditions bundle with every value labelled and sourced; (2) a test proves no mechanism reads a catalogue date as a gate | keeper (schema); belt: Composer (rows), Haiku (source and label checks) |
| **P5 Grounded economy** | Economy, Settlement | recipes with quantities, yields, labour and energy, mass-balanced (ECON-5); agriculture fed by P3 crops; construction bills of materials from P2 structures; households (income, budget, consumption; CONTRACTS §12.4); price discovery and market clearing (CONTRACTS §9); money, credit and a money-supply owner (DUP-43); property valuation (§12.3); transport over P2 geography; one labour unit (UNIT-11) | (1) a 30-day settlement conserves mass by element, and money except declared mints; (2) a harvest failure raises the grain price and lowers consumption with no price script; (3) a house's materials and labour come from its walls and roof, not a list; (4) staple prices over a simulated decade fall within the documented range for the reference region | keeper (Economy; Settlement for its side); belt: Codex, Composer (recipes from GOODS.md), Haiku |
| **P6 Society** | Society (new) | demography from Reality (DUP-41; Reality keeps biological reproduction, ageing, mortality); households, marriage, kinship, inheritance customs; organisations as actors; religion and belief; norms and sanctions; cultural transmission; class; migration decisions; collective action | (1) a village of 500 run 100 years keeps its age structure within 15 % of the source population; (2) migration follows a wage or food differential with the documented sign; (3) collective action arises from individual states (hungry, angry, connected), never from a meter | keeper (a new Society keeper); belt: Codex, Composer |
| **P7 Cognition** | Cognition (new) | perception (P2 optics, acoustics), attention, memory, learning and skill (the universal form of STATS skill, rust and talent), needs, emotion, decisions, attribution, communication, relationships; the personality-model slot with the eight-function model as one configuration (CTRL-7) | (1) the bar simulator (ENGINES.md) runs headless and deterministically with a seed; (2) skill gain follows the power law of practice and decays without use as its source says; (3) swapping the personality model changes behaviour without touching any other engine | keeper (a new Cognition keeper; design-heavy); belt: Codex |
| **P8 Government** | Government (new) | authority and legitimacy; law as data; offices' powers (Settlement keeps the records); taxation and spending (the publicWorks stub, DUP-42); property-rights regimes; succession; courts and policing; military organisation; diplomacy | (1) a tax reaches households only through Economy's ledger; (2) a contested succession arises from the rules and the claimants, never a script; (3) the same society under two property regimes diverges as the sources describe (e.g. enclosure) | keeper (a new Government keeper); belt: Codex, Composer (institutional data) |
| **P9 Knowledge & Technology** | Knowledge & Technology (new) | possibility (P2/P3 feasibility), knowledge, invention, adoption and deployment as separate states; diffusion through trade, migration and writing; experimentation | (1) a society with no ore never deploys iron tools; one with ore, fuel, skill and contact adopts them, earlier than history if it can; (2) adoption follows an S-curve whose speed depends on contact and incentive | keeper (new); belt: Codex, Composer (catalogue links) |
| **P10 History** | History (new) | long-step aggregation of settlements and polities; territory; international relations and the causes of war; collapse and transition; the resolution hand-off at civilisation scale (§9) | (1) the same village run individually and aggregated agrees within 10 % on population, output and deaths over 50 years; (2) a polity forms, expands or fragments from its conditions in seeded runs, with outcomes differing across seeds | keeper (new); belt: Codex |
| **P11 Reconstruction benchmark** | History (the harness); every engine | the §5 benchmark below | below | keeper (History, with the registry keeper for investigations); belt: Composer (datasets), Sonnet (harness), Haiku |
| **PL Pirate plugin** | the pirate keepers | re-seat the plugin on the interfaces: the moves of AUDIT.md §3; STATS and combat read the capacity core; weather and climate from Reality; alignment untouched | the plugin's 387 web tests and 178 alignment tests still pass; the plugin defines no universal rule (a check over its imports) | belt mostly (Sonnet, Codex); keepers only for design questions |

A partial benchmark run (H1 England, demography and economy only) is worth doing after P6 to find missing
mechanisms early; it is diagnostic, never a pass.

## P11: the historical-reconstruction benchmark (PLATFORM.md §5)

### The four first targets (proposed)

Chosen so outcomes differ as much as possible (collapse, abandonment, long stability, shocks and regime change)
and environments differ (sub-Arctic pastoral, tropical forest maize, temperate mixed farming, island rice).
Two are **development** societies (used while building mechanisms) and two are **held-out validation**
societies (never used for tuning), per §5's rule. A fifth, Iceland, is a reserve control for Greenland.

| # | Society, window | Outcome to reproduce (never forced) | Role | Why it tests the platform |
|---|---|---|---|---|
| H1 | England, 1270–1700 | Malthusian ceiling, Black Death (−40–50 %), wage rise, enclosure, civil war 1642–51, a republic 1649–60, restoration | development | best-documented pre-industrial economy: annual series for population, wages, prices, output; tests demography, economy, government and conflict together |
| H2 | Tokugawa Japan, 1600–1868 | long internal peace, population plateau (~26–32 M) after 1720, closed trade, proto-industry, no war for 250 years | development | stability as an outcome (a sim that only makes wars fails it); household registers give demography; rice tax gives the fiscal state |
| H3 | Norse Greenland, 985–c.1450 | settlement, peak (~2,000–3,000 people), diet shift to marine food, abandonment | validation (held out) | small, closed, environment-driven; collapse without conquest; tests climate → ecology → nutrition → migration |
| H4 | Copán valley (Classic Maya), 400–1200 CE | dynastic growth to ~20–28 k, deforestation and soil loss, political collapse c. 820, slow depopulation | validation (held out) | tropical maize, no draft animals or metal tools; collapse of institutions before people; tests land use, soil, legitimacy |
| (H5) | Iceland, 874–1300 | settlement, deforestation and erosion, the Commonwealth (no executive), absorption by Norway 1262–64, survival | reserve control | same founders and technology as H3 with a different outcome |

### The data each needs (proposed; every value labelled researched / estimate / fiction)

| Target | Starting conditions (initialise) | Trajectory to compare against | Main sources to research |
|---|---|---|---|
| H1 England | 1270 population (~4.5–5 M), land use by type, crop yields, livestock, wages and prices, manorial and royal institutions, towns and their sizes, technology inventory (mills, ploughs, ships), climate | annual population, real wages, GDP per head, urban share, enclosure, tax revenue, plague mortality, wars and the civil war, regime changes | Broadberry, Campbell, Klein, Overton & van Leeuwen *British Economic Growth 1270–1870*; Clark's wage and price series; Wrigley & Schofield *Population History of England*; Campbell *The Great Transition*; tree-ring and documentary climate series |
| H2 Tokugawa | 1600 population (~12–18 M, contested), kokudaka by domain, irrigated area, rice yields, castle towns, the bakuhan institutions, the 1630s trade restrictions as a starting rule set | population by province (1721 onward shogunal surveys), arable area, urban sizes (Edo, Osaka, Kyoto), famines (Kyōhō, Tenmei, Tenpō), peasant uprisings (ikki counts), rice prices | Hayami Akira's register demography; Saito Osamu on wages and output; Totman on forestry; Aoki Kōji's ikki counts |
| H3 Greenland | founding c. 985 (~14 ships, ~400–500 people), farm sites and pasture, livestock, walrus-ivory trade link to Norway, church, climate | farm counts by phase, population estimates, δ13C/δ15N diet shift in burials, trade contacts, abandonment date | Lynnerup's demography; Arneborg et al. isotope studies; McGovern's zooarchaeology; GISP2/ice-core and lake-sediment temperature reconstructions; Dugmore et al. |
| H4 Copán | c. 400 CE founding of the dynasty, valley soils and slopes, maize yields, forest cover, settlement hierarchy | structure counts by phase (obsidian-hydration dated), population estimates, pollen-recorded forest loss, monument dates (political activity), skeletal health | Webster, Freter & Gonlin *Copán: The Rise and Fall of an Ancient Maya Kingdom*; Abrams on construction energetics; pollen cores (Rue); regional speleothem drought records |
| H5 Iceland | 874 settlement, birch cover, pasture, livestock, Althing institutions | farm counts, tephra-dated erosion, institutional change 1262 | Landnámabók (with care), tephrochronology studies, Grágás |

### The indicators (proposed definitions)

Each indicator is a time series sampled at fixed checkpoints (every 10 years for H1/H2, every 25 years for
H3/H4). Each gets a similarity score S in [0, 1]; the reality differential is 1 − S.

| # | Indicator | Measure | Score |
|---|---|---|---|
| I1 | Population | total people | S = max(0, 1 − mean over checkpoints of \|ln(sim/hist)\| / ln 2) (a factor of 2 off scores 0) |
| I2 | Settlement growth | number of settlements by size class; largest settlement size | as I1 on the largest settlement; class-count distribution by 1 − total-variation distance |
| I3 | Resource availability | arable/pasture/forest area; key stock (timber, fish, game) | as I1 per resource, averaged |
| I4 | Production | output per head of the staple (grain, rice, maize, dairy) in kg | as I1 |
| I5 | Technology | set of deployed technologies at each checkpoint (catalogue ids) | Jaccard similarity of the simulated and historical deployed sets; adoption-date error scored 1 − min(1, \|Δt\| / 50 y) |
| I6 | Institutional change | ordered list of regime/institution transitions (e.g. manorial → leasehold, monarchy → republic) | event matching within a window (±25 y): F1 score of matched events |
| I7 | Territory | area controlled / occupied | as I1 |
| I8 | Conflict | count and intensity of wars, revolts, uprisings per period | rate as I1; timing of major events by I6's F1 |
| I9 | Political stability | regime duration; successions that were violent | 1 − \|share violent sim − hist\|; mean regime duration as I1 |
| I10 | Migration | net migration and abandonment (settlements lost) | as I1 where series exist; abandonment timing as I6 |
| I11 | Cultural and religious change | share of population by religion or practice at checkpoints | 1 − total-variation distance |

Combined score: the weighted mean of the indicators the target has data for (equal weights by default; Rex sets
any other weighting). The 70 % target (§5) applies to the combined score **and** is reported per indicator.

Protocol: N ≥ 30 runs per target with recorded seeds; report the mean and spread of each S; an error that keeps
its sign across seeds is systematic (a missing mechanism or input, investigated and logged), one that does not is
stochastic. No parameter may be tuned on H3 or H4; a failed held-out target opens an investigation issue, never a
tuning pass.

Acceptance (proposed): the benchmark harness runs all four targets headless; H1 and H2 reach ≥ 70 % combined
before H3 and H4 are first run; H3 and H4 results are reported as-is.

## What Rex decides before P0

1. Approve, change or reject the engine organisation (AUDIT.md §6), in particular the Kernel and Catalogue as new
   engines and the later split of Reality.
2. Approve this phase order, or name another.
3. The four benchmark societies and their development/validation split (P11).
4. Owners for the 47 overlap groups (GRAPH.md §2); the registry keeper can present them in batches.
5. CTRL-12: whether `Toolchain/`'s root becomes a git repository, so PLATFORM, ENGINES, REGISTRY, GRAPH, AUDIT and
   ROADMAP are versioned.
