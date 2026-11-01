# The eleven engines: what each does and how they connect

**Status:** the stable reference (controller, 2026-10-31). `ENGINES.md` is the dated decision log and stays the
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

Three rules bind all eleven: one authoritative owner per mechanism (the registry tracks it); explain outcomes by
mechanisms, never by scripts, dates, levels or meters; nothing is a fixed property that a mechanism could produce.

## Six engines exist

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
**State:** 149 tests; adopted by all five other engines; the thirty-day three-engine harness lives here.

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
(`realism/SPLIT.md`) moves it out module by module; 80 registry rows, 43 built.

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
**State:** the bulk of today's `realism/`: 134 registry rows, 84 built, 286+ tests; population and demography sit here
until Society exists.

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
**State:** 42 tests; 26 registry rows, 21 built; pirate adapter and thirty-day benchmark. The food group (DUP-21) is approved,
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
**State:** 307 tests; CB-1 to CB-7 pass; V1 is verification only (validated: no), V2 recorded as a failure, not tuned; 13 rows
built, integrated with stubs; personality v1 opt-in, 16 types collapse to 3 behaviours in the hungry pair (T-3).

## Five engines do not exist yet

### 7. Catalogue — P4; can start now (its only input, P0, is complete)

**Purpose.** The universal reference catalogue: every entity, substance, organism, technology, institution, practice
and phenomenon with stable id, names, classification, geographic origin and spread, culture, earliest evidence, dates
of discovery, invention, identification and adoption, sources, confidence, provenance class (real, prehistoric,
mythological, fantasy, science fiction, original fiction). **Tags, never unlocks (Rex):** a date is reference
information; nothing exists in the world because its year arrived. Two uses: game configuration ("Caribbean,
1690–1720" gives historically grounded starting conditions) and unconstrained simulation. Also the reference truth
that beliefs and History are compared against.
**Reads from:** Kernel (ids). **Read by:** every engine for reference data and labels; game adapters for starting
conditions; History for validation baselines.
**Today:** no keeper, no package; a second catalogue is quietly forming in the pirate `STARTING_TOWN.md`,
`CULTURE.md`, `TECHNOLOGY.md` and `economy/RESEARCH.md`, which should become its first fixture.

### 8. Society — P6

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
**Today:** 10 planned rows (organisation actors, household structure, institution formation, doctrine transmission, religious community among them); factions split between pirate story
docs and `factions.json`; culture and organisations have no built owner (CTRL-6; DUP-58, DUP-59 proposed).

### 9. Government — P8

**Purpose.** Authority, law, offices (what an office may do; Settlement records who holds it), taxation and spending,
property rights, enforcement, military organisation, diplomacy, succession, legitimacy; censorship and suppression of
communication; polity formation, expansion and fragmentation, war decisions and collapse (moved here from History,
2026-10-31); communities to empires. Legitimacy gained or lost by mechanism, never assigned.
**Never owns:** who holds an office (Settlement), the individual decision (Cognition), culture (Society).
**Reads from:** Society (organisations, grievances, legitimacy inputs), Economy (taxable flows), Settlement (offices,
property), Cognition (rulers are minds). **Writes to:** laws, offices' powers, tax rules, enforcement capacity,
polities. **Read by:** Economy (taxes, property rights), Society, Settlement, Cognition (what is permitted), History.
**Today:** 7 planned rows (authority acquisition and delegation, rule creation and amendment, the law record as executable data, compliance and enforcement, succession, competing jurisdiction); one overlap with Settlement's built office-powers row (DUP-62: Government owns what an office may do, Settlement who holds it). Architecture may be researched while P6 and P7 build.

### 10. Knowledge & Technology — P9

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
**Today:** 3 planned rows: media availability, technique diffusion, collective knowledge stock (DUP-61).

### 11. History — P10–P11

**Purpose.** A thin composition and validation layer, **the backend record of what occurred (Rex, 2026-10-31)**:
long-step aggregation of settlements and polities, the resolution hand-off at civilisation scale, historical
initialisation from documented conditions, and the comparison of simulated trajectories against real history on the
eleven indicators (≥70 % similarity, provisional) with multiple seeds, systematic error told apart from stochastic
variation; Seshat and cliodynamic models as yardsticks. **Never determines what happens, and no mechanism in any
engine reads it.** What people in the world know of the past is Cognition's, by fallible routes.
**Reads from:** every engine's state over time; Catalogue for baselines. **Writes to:** the record and the validation
reports only.
**Today:** 1 planned row, `history.record.backend`; the kernel harness is its seed.

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
open). Every other arrow is a registered planned interface (IF-1 to IF-45) and a gap in the registry's
`integration_gaps` until a combined test exists. Fourteen shared contract rows (`shared.*`) belong to no engine: they
are the contracts between engines, not mechanisms.

Five seams where a second gear is most likely to be built by mistake, all proposed overlap groups in batch 2b and
watched by the registry: organisations (DUP-58, Economy's built row vs Society), households (DUP-59, Economy P5 vs
Society P6), transmission (DUP-60, Society's network vs Cognition's communication vs Knowledge & Technology's
diffusion; proposal: one network, three kinds of content), and collective knowledge (DUP-61, Cognition vs Society vs
Knowledge & Technology), and office powers (DUP-62, Settlement's built row vs Government). Three mechanisms registered 2026-10-31 as planned with owners but no design: records as
physical objects (Economy the object, Cognition the content; IF-40, IF-41), inference from remaining evidence
(Cognition), collective knowledge with loss (Knowledge & Technology on Society's network).

## What this file is not

Not the roadmap (`ROADMAP.md` has phases and acceptance tests), not the registry (`REGISTRY.md` has every mechanism
with its owner and V&V state), not the decision log (`ENGINES.md`). When those three and this file disagree, the
registry wins on ownership, ENGINES.md on decisions, and this file is corrected.
