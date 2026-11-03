# The eleven engines: what each does and how they connect

**Status:** the stable reference (controller, 2026-10-31; last rewritten 2026-10-31 ~22:15 after every engine got a keeper, a repo and a lane). `ENGINES.md` is the dated decision log and stays the
authority on *why*; this file is the authority on *what each engine is for* and is rewritten, never appended, when a
decision changes it. Every row here traces to `PLATFORM.md`, `ENGINES.md`, `ROADMAP.md` or the registry. Nothing
below is a controller invention. Marks: **(Rex)** his decision; proposed; open.

The ordering principle (Rex, 2026-10-30): **physics decides what can happen, biology what an organism can do,
cognition what it attempts, society the institutions and incentives around the attempt. The game supplies the
objectives.** Every engine is independent of every game; games are plugins that pick a time window, a region and what
the Catalogue allows, and read the engines through adapters.

**Living resources have three owners in sequence (Rex, 2026-10-31):** Reality owns soil, minerals, water, terrain and
the material properties of wood; Life owns the living tree, its biomass production, growth and biological mortality;
Economy owns harvested timber inventories, processing and exchange. Felling is a conservation-preserving transfer of
mass from Life's stock to Economy's inventory, never a second count. The same sequence holds for crops, fish and game.

**Dependencies are pinned, never live (Rex, 2026-10-31, kernel DESIGN §16):** an engine consumes another only at an
immutable release tag installed from the local backup mirror (tarball as fallback), upgrades only in a paired belt unit,
and each run records its compatible versions; releases are cut for any change a consumer needs; release commits must
exist off-machine. Live `file:` links are being retired.

Three rules bind all eleven: one authoritative owner per mechanism (the registry tracks it); explain outcomes by
mechanisms, never by scripts, dates, levels or meters; nothing is a fixed property that a mechanism could produce.

## Six engines built before 2026-10-31

### 1. Kernel (`Toolchain/kernel`, `@rex/kernel`, repo `rs-kernel`) — P0, complete 2026-10-30

**Purpose.** The shared infrastructure every engine runs on, and nothing else: simulation time from milliseconds to
years with a declared process order; event ordering and causality; stable ids qualified by engine; units and
dimensional checks; seeded random streams per mechanism and per entity; snapshots and replay; cross-engine
transactions; the registry check script (duplicate writers, wired-but-unintegrated mechanisms, empty contract fields,
all as warnings or failures).
**Never owns (Rex):** any scientific, biological or economic formula, any engine's state, any contract.
**Reads from / writes to:** nothing of its own; every other engine imports it and declares its processes, reads and
writes in a `kernel.json` that the check script reads as data. Provider calls between engines are ports too
(decided 2026-10-31), so ports are the one integration mechanism.
**State:** 149 tests; adopted by every engine; the thirty-day three-engine harness lives here; v0.1.0 released 2026-11-01 and pinned by
six engines; v0.1.1 released (compiled JS in dist/, because Node refuses to type-strip .ts under node_modules; §16);
snapshot header v2 with numeric epoch and catalogue hash landed.

### 2. Reality (`Toolchain/realism` today → `Toolchain/reality`, `@rex/reality`, repo `rs-reality`) — P2 next

**Purpose.** The physical world and nothing alive: mechanics (phase 6, next), contact and impact, thermodynamics and
heat transfer, chemistry and reactions, gases and atmosphere (what the air is), fluids and buoyancy, optics and
acoustics (light and sound as physical quantities), materials (deformation, fracture, corrosion, wear), terrain and
geology (formations, deposits, soils as physical records, excavation and stability), hydrology, climate and
**weather generated from physics, never a table** (Rex), the once-run world-formation stage (geological history
establishing formations, deposits, terrain; crude oil at its long end) and the active world (erosion, sediment, water).
Holds the shared substrate (elements, registry, graph, world, trace, scheduler, snapshot) that Life imports one way.
**Never owns:** anything that lives, perceives or decides. **Reality never imports Life.**
**Reads from:** Kernel only. **Writes to:** place and air quantities (`place.*`, `air.*`), materials, terrain,
light and sound fields. **Read by:** Life (heat, air, light, sound, terrain, water), Settlement (terrain, materials for
construction), Economy (non-living resource stocks: mineral deposits, water, stone, clay, as physical quantities with conservation), game
adapters (tiles, blocks, weather display).
**State:** built inside `realism/` (thermodynamics, gases, chemistry, atmosphere, environment); the package split
(`realism/SPLIT.md`, landed) moves it out module by module; 82 registry rows, 44 built. Keeper: the Reality & Species
keeper, sole committer to `realism/` until the split; phase 6 mechanics is its next design.

### 3. Life (`Toolchain/realism` today → `Toolchain/life`, `@rex/life`, repo `rs-life`) — P1 landed, P3 later

**Purpose.** Every organism as a species configuration, humans first and richest: anatomy and organs, physiology
(circulation, respiration, thermoregulation, metabolism as flux), nutrition and hydration, neurology and endocrine
(every chemical with cited effects, Rex), muscular adaptation, fatigue and aerobic capacity, medicine (wounds, disease,
healing, crises, one death ledger), genetics and development, the cellular layer as representative populations
(ageing emerges from it, never a timer), phenotype, reproduction; later plants with the same three records, pollinators
as populations, herbivores and carnivores, decomposition and the food web, nutrient return to soil and water. Three
records per organism: genetic profile, cellular and developmental state, organism state; a character sheet is a view
of them, never a second source of numbers (Rex). **Life owns what a body can do.**
**Never owns:** what a mind attempts (no behaviour rules in species records), culture, population as a social fact.
**Reads from:** Kernel; Reality (heat, air, light, sound, terrain, water, food as matter). **Writes to:** `body.*`
quantities: hunger and satiety signals, capacity, pain, transmitter and hormone levels, detectability (what a body can
perceive), fatigue, crises and deaths. **Read by:** Cognition (every body signal and sense), Settlement and Economy
(labour supply in person-hours from population, mortality), game adapters (stats, medicine, food, weather on bodies).
**State:** the bulk of today's `realism/`: 132 registry rows, 83 built, 286+ tests; population and demography sit here
until Society exists. Keeper since 2026-10-31: the Life keeper (design approved: plants with the three records, four
Caribbean species first, pollinators as populations; twelve units queued in the realism lane); takes the `life` package
when SPLIT step 4 lands.

### 4. Settlement (`Toolchain/settlement`, `@rex/settlement`, repo `rs-settlement`) — built

**Purpose.** The physical and institutional layer a society stands on: land and parcels, buildings and layouts,
titles and leases, the ledger (money has one home here), construction projects, businesses, posts and workforce
assignments, offices as records of who holds them (never what an office may do), cemeteries and sanitation
infrastructure, land use. Daily tick with production `Q = floor(min(equipment, labour, materials, utilities))`.
**Never owns:** goods, recipes, prices and wages (Economy), persons and labour supply (Life, later Society), office
law (Government), culture, narrative.
**Reads from:** Kernel; Economy (production, prices, wage levels through the agreed contract); Life (labour supply in
person-hours); Reality (terrain, materials; planned). **Writes to:** parcels, buildings, titles, ledger balances,
posts, business status. **Read by:** Economy (premises, posts, inventories through the contract), Government (who holds
an office), game adapters (the town).
**State:** 67 tests; contract with Economy byte-identical in both repos through §18; 23 registry rows built.

### 5. Economy (`Toolchain/economy`, `@rex/economy`, repo `rs-economy`) — built

**Purpose.** Production, consumption, prices, trade and accounting: goods and recipes grounded in materials, tools,
knowledge, labour and energy; inventories; markets and price rules (Davenant proposed, `base` default until Rex
decides); spoilage, shortage, trade and shipments; labour quotes and the wage channel; extraction that moves
physical stocks (never creates them); burial services and waste flows; ownership, investment. Capitalism never assumed
(Rex).
**Never owns:** premises, posts and the ledger (Settlement); persons, nutrition, resource existence (Life, Reality);
laws and taxes (Government); any pirate fact.
**Reads from:** Kernel; Settlement (premises, posts, ledger through the contract); Life (labour supply, consumption
needs; the food group DUP-21 makes consumption move food from inventory into nutrition); Reality (resource stocks,
planned). **Writes to:** inventories, prices, trades, shipments, wage levels. **Read by:** Settlement (production,
prices, wages), Society and Government (planned: incomes, taxation), game adapters.
**Planned edge:** Cognition → Economy (IF-26, IF-27): an individual's wants and refusals become demand and labour
offers; today consumption is per-capita with no individual input.
**State:** 42 tests; 26 registry rows, 21 built; 19 provider calls declared as ports; pirate adapter and thirty-day benchmark. The food group (DUP-21) is approved,
not built.

### 6. Cognition (`Toolchain/cognition`, `@rex/cognition`, repo `rs-cognition`) — P7 baseline accepted 2026-10-30

**Purpose.** The reusable, species-configurable decision engine: perception and attention (the only code that sees a
stimulus), beliefs (a subjective world that can be wrong), memory (stored, retrievable, articulable; stages attention
→ encoding → consolidation → retrieval → communication, below personality), needs and goals (`M_i = w_i·D_i·S_i`),
action generation, evaluation and selection, learning and attribution, the personality slot (null model by default;
Rex's eight-function model as frozen versions, hooks on pertinence, interpretation, generation and learning only).
Planned inside it: belief-system formation and individual supernatural belief with conviction and doubt (through the built belief update, no second store); the experience pipeline (perception filter → encoding → chemical response → re-read of the body
state, which is the emotion), general preference learning and attraction, cultural salience, dynamic function
allocation, the communication subsystem (messages, media, persuasion as a change to a specific part of the listener's
evaluation, conversational plausibility, gaze, suppression with detection), and the four fallible routes to the past
(memory, written records, inference from evidence, oral transmission). **Cognition owns what the mind attempts and
outputs intentions only; actions are host data.** A mind is not a body.
**Never owns:** physiology, senses as capacities, phenotype (Life); norms and their transmission (Society); goods
(Economy); world state; the pirate alignment engine.
**Reads from:** Kernel; Life (every body signal and sense: hunger, pain, capacity, chemistry, detectability); messages
from other minds (communication, planned). **Writes to:** `mind.*` quantities: beliefs, intentions, appraisal,
recalled body state, conversation state. **Read by:** Life (appraisal feeds neurology; planned), Economy (demand and
labour offers; planned), Society (collective action aggregates individual states; planned), game adapters (NPC
behaviour).
**State:** 307 tests; 54 registry rows, 13 built; CB-1 to CB-7 pass; V1 is verification only (validated: no), V2 recorded as a failure, not tuned; 13 rows
built, integrated with stubs; personality v1 opt-in, 16 types collapse to 3 behaviours in the hungry pair (T-3).

## Five engines started 2026-10-31 (keeper, approved design, repo and lane each; first units running)

### 7. Catalogue (`Toolchain/catalogue`, `@rex/catalogue`, repo `rs-catalogue`) — P4, started 2026-10-31

**Purpose.** The universal reference catalogue: every entity, substance, organism, technology, institution, practice
and phenomenon with stable id, names, classification, geographic origin and spread, culture, earliest evidence, dates
of discovery, invention, identification and adoption, sources, confidence, provenance class (real, prehistoric,
mythological, fantasy, science fiction, original fiction). **Tags, never unlocks (Rex):** a date is reference
information; nothing exists in the world because its year arrived. Two uses: game configuration ("Caribbean,
1690–1720" gives historically grounded starting conditions) and unconstrained simulation. Also the reference truth
that beliefs and History are compared against.
**Reads from:** Kernel (ids). **Read by:** every engine for reference data and labels; game adapters for starting
conditions; History for validation baselines.
**State:** design approved (CAT-Q1–Q6); repo at c02b0d1; 7 planned rows; schema, dates, regions and window query,
tags-never-unlocks check, fixture manifest landed or running; the pirate town files are being ingested in place as the
first fixture (~520 records); England 1270 benchmark rows next. Owns calendars and date conversion (agreed with Kernel
and History).

### 8. Society (`Toolchain/society`, `@rex/society`, repo `rs-society`) — P6, started 2026-10-31

**Purpose.** Population and demography (moves here from Life), households and kinship, religion, norms and
traditions, organisations (families, churches, guilds, cults, political groups) as actors that are at once economic,
political and social, class, cultural transmission, social networks (the one transmission substrate, proposed),
collective action, cooperation, conflict, rebellion, migration. **Culture emerges from individuals, their
relationships, institutions and material conditions and feeds back into upbringing (Rex); no rebellion meter.** Also
the institutions that keep memory: priests, scribes, schools, oral tradition.
**Never owns:** the individual decision (Cognition), buildings and parcels (Settlement), law and authority
(Government).
**Reads from:** Cognition (individual states and intentions to aggregate), Life (demography), Economy (incomes,
goods), Settlement (where people are), Catalogue (culture profile as a seed). **Writes to:** organisations, norms,
cultural salience and social valuation (read by Cognition's attraction and preference learning), networks, collective
events. **Read by:** Cognition, Economy, Government, History.
**State:** design approved (SOC-Q1–Q8; charter forms are composable components, never an exhaustive menu, Rex);
repo at a6567b8; 17 planned rows; ten units queued (organisation actors, composable charters, the one network,
affordances port IF-46 with Cognition); demonstration: a late-fourteenth-century English parish with fraternities.
DUP-58/59/60 owners approved and agreed.

### 9. Government (`Toolchain/government`, `@rex/government`, repo `rs-government`) — P8, started 2026-10-31

**Purpose.** Authority, law, offices (what an office may do; Settlement records who holds it), taxation and spending,
property rights, enforcement, military organisation, diplomacy, succession, legitimacy; censorship and suppression of
communication; polity formation, expansion and fragmentation, war decisions and collapse (moved here from History,
2026-10-31); communities to empires. Legitimacy gained or lost by mechanism, never assigned.
**Never owns:** who holds an office (Settlement), the individual decision (Cognition), culture (Society).
**Reads from:** Society (organisations, grievances, legitimacy inputs), Economy (taxable flows), Settlement (offices,
property), Cognition (rulers are minds). **Writes to:** laws, offices' powers, tax rules, enforcement capacity,
polities. **Read by:** Economy (taxes, property rights), Society, Settlement, Cognition (what is permitted), History.
**State:** design approved (GOV-Q1–Q8; authority is computed from resources, enforcement capability, recognition,
relationships and compliance, never a stored score, formula provisional, Rex); repo at d04b4dc; 15 planned rows; law
record as executable data, breach evaluation and the office-powers answer to Settlement queued; demonstration: an
English manor c. 1300. DUP-62 approved: Government owns what an office may do, Settlement who holds it.

### 10. Knowledge & Technology (`Toolchain/knowledge`, `@rex/knowledge`, repo `rs-knowledge`) — P9, started 2026-10-31

**Purpose.** Discovery, invention, capability and diffusion as mechanisms: a society develops a technology from
resources, knowledge, tools, manufacturing capability, energy, skilled labour, incentives, institutions, communication
and experimentation, earlier than history if the capabilities exist, never if they don't (Rex). Possibility,
knowledge, invention, adoption and deployment are distinct states. Holds **collective knowledge with loss**: what a
society knows as recorded and transmitted knowledge, the bridge between one mind's belief and "what the town knows".
**Never a tech tree.**
**Never owns:** the individual's beliefs (Cognition), the transmission network (Society), the reference dates
(Catalogue).
**Reads from:** Cognition (individual knowledge and inference), Society (transmission, institutions), Economy (tools,
materials, incentives), Catalogue (reference). **Writes to:** capability states per society, diffusion. **Read by:**
Economy (recipes become possible), Government, History.
**State:** design approved (KNT-Q1–Q4: five states with "invented" meaning a working method present here;
propositions and techniques, no technique names another; media are techniques; Cognition decides at agent resolution,
K&T aggregates); repo at dce94db; 7 planned rows; collective knowledge stock with loss implemented in its first unit;
diffusion waits on Society's contact port.

### 11. History (`Toolchain/history`, `@rex/history`, repo `rs-history`) — P10–P11, started 2026-10-31

**Purpose.** A thin composition and validation layer, **the backend record of what occurred (Rex, 2026-10-31)**:
long-step aggregation of settlements and polities, the resolution hand-off at civilisation scale, historical
initialisation from documented conditions, and the comparison of simulated trajectories against real history on the
eleven indicators (≥70 % similarity, provisional) with multiple seeds, systematic error told apart from stochastic
variation; Seshat and cliodynamic models as yardsticks. **Never determines what happens, and no mechanism in any
engine reads it.** What people in the world know of the past is Cognition's, by fallible routes.
**Reads from:** every engine's state over time; Catalogue for baselines. **Writes to:** the record and the validation
reports only.
**State:** design approved (HIST-Q1–Q4: owning engines write their own coarse forms, History owns the series across
the switch and the agreement check; declared labelled boundary inputs allowed at a region's edge, never outcomes; the
scoring amendments define the 70 %; X1 starts from a documented Catalogue village); repo at bfb1336; 1 planned row;
resolution-aware aggregation and checks landed; X1 is its harness specification.

## How they connect

Direction of dependency (an arrow means "reads from"; the Kernel is under all of them):

```
Reality  →  Life  →  Cognition  →  Society  →  Government
   │          │          │             │            │
   └──────────┴──────────┴──→ Economy ←┴────────────┘
                              ↕
                          Settlement
Catalogue → (reference for all)      Knowledge & Technology ← Cognition, Society, Economy
History ← (observes all; read by none)
```

Built and combined-tested today: Settlement ↔ Economy (the thirty-day benchmark); Reality → Life (the human-week
checkpoint and water-ledger tests, inside one package; the split names interfaces IF-29 to IF-36). Kernel under every
engine: adopted by all, but the registry keeps no kernel rows, the harness has not been rerun since the recovery, and
Cognition reaches it only through host stubs. Built but not yet passing: Life → Settlement and Economy (labour in
person-hours): population supply exists, `hours()` fails CONTRACTS §18, and no combined test exists (DUP-26, 28, 29
open). Every other arrow is a registered planned interface (IF-1 to IF-47) and a gap in the registry's
`integration_gaps` until a combined test exists. Fourteen shared contract rows (`shared.*`) belong to no engine: they
are the contracts between engines, not mechanisms.

Five seams where a second gear is most likely to be built by mistake, all approved overlap groups in batch 2b (Rex,
2026-10-31), closing as their units land: organisations (DUP-58, Economy's built row vs Society), households (DUP-59, Economy P5 vs
Society P6), transmission (DUP-60, Society's network vs Cognition's communication vs Knowledge & Technology's
diffusion; proposal: one network, three kinds of content), and collective knowledge (DUP-61, Cognition vs Society vs
Knowledge & Technology), and office powers (DUP-62, Settlement's built row vs Government). Overlap groups overall: 65, of which 7 closed, 25 closing, 33 proposed (batches 3–5 unwritten). Three mechanisms
registered 2026-10-31 as planned with owners but no design: records as
physical objects (Economy the object, Cognition the content; IF-40, IF-41), inference from remaining evidence
(Cognition), collective knowledge with loss (Knowledge & Technology on Society's network).

## What this file is not

Not the roadmap (`ROADMAP.md` has phases and acceptance tests), not the registry (`REGISTRY.md` has every mechanism
with its owner and V&V state), not the decision log (`ENGINES.md`). When those three and this file disagree, the
registry wins on ownership, ENGINES.md on decisions, and this file is corrected.
