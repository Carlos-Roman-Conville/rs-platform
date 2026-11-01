## Phase H: the historical-reconstruction benchmark (PLATFORM.md §5) (proposed)

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
