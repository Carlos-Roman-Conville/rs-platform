# The simulation engines: owners, boundaries, lanes (2026-10-30)

**Read `ENGINE_MAP.md` first** (controller, 2026-10-31): the stable one-page-per-engine reference, what each of the eleven
engines does, owns, reads and writes, and how they connect. This file is the dated decision log and the authority on *why*.

**Mission (2026-10-30, later the same day):** the project is now the universal reality and civilisation
simulation platform, with the pirate game as one plugin. Read `PLATFORM.md` first; this file remains the engine
map and is kept current by the controller.

Rex's architecture (2026-10-30, worked out with ChatGPT and adopted): a family of reusable simulation engines
under `Toolchain/`, with the pirate ship (`Games/RPG's/pirate-ship`) as the first game that uses them through
adapters. Rules Rex set the same day:

- **One authoritative owner per system.** Everyone else consumes its outputs through documented interfaces.
- **Every universal engine is independent of pirate-ship**, with stable interfaces between engines.
- **Ownership is not activity.** An owner session stays idle until a concrete research or implementation task
  is ready. No session is started merely to produce documentation.
- Every owner ends each turn with five lines: responsibility, latest commit, tests passing, what is blocked on
  Rex, next proposed task.
- **Historical first (Rex, 2026-10-30).** The game is based on realism, so wherever reliable historical or
  real-world data exists it fills the answer: starting population, wages, prices, religion, technology, burial
  customs, household structure, economic organisation. Rex decides only where no data exists or the data
  conflicts. Every value carries one of three labels: **researched** (with its source), **estimate** (derived
  from research, the derivation shown), **fiction** (Rex's or a faction's). History sets the starting conditions
  and constraints; the simulated mechanisms decide what follows, so outcomes may leave history.
- **Nothing is a fixed property that mechanisms could produce (Rex, 2026-10-30).** A town's culture is not a
  setting; it emerges from its individuals (personality, upbringing, memories, beliefs, needs), their relationships
  and organisations, its institutions and material conditions, and feeds back into how children are raised and
  what is approved or punished. No "rebellion meter": enough hungry, angry people with a way to coordinate is a
  rebellion. Deterministic given the same inputs and seed; stochastic only where real uncertainty exists.
- The ordering principle: physics decides what can happen, biology what an organism can do, cognition what it
  attempts, society the institutions and incentives around the attempt. The game supplies the objectives.

## The approved organisation (Rex, 2026-10-30, on the audit; `AUDIT.md` §6, `ROADMAP.md`)

| Engine | Responsibility | State |
|---|---|---|
| **Kernel** | shared time and scheduling, event ordering and causality, stable ids, units and dimensional validation, seeded RNG, snapshots and replay, cross-engine transaction boundaries. **Infrastructure only: it never owns a scientific or economic formula** (Rex) | new; P0; Kernel keeper to start |
| **Reality** (Physical Reality) | mechanics, thermodynamics, chemistry, fluids, optics, materials, environment; **weather and climate as a major P2 subsystem, generated from physics (solar heating, pressure gradients, humidity, instability, ocean evaporation, terrain, circulation, surface water), never drawn from a table** (Rex); climate = a region's statistics and boundary conditions, weather = the atmospheric state over time | **separate engine since 2026-10-31** (`rs-reality`); code still in `realism/` until SPLIT.md's moves land; mechanics (P2) starts in `Toolchain/reality/` |
| **Life** (Life & Species) | anatomy, physiology, metabolism, genetics, development, health; every organism as a species configuration, plants, pollinators, food web, decomposition | **separate engine since 2026-10-31** (`rs-life`); code in `realism/` until the split lands |
| **Catalogue** | scientific, historical, geographic and fictional reference data; tags, never unlocks | new; P4, researchable in parallel once ids and contracts exist |
| **Settlement** | property, buildings, construction, workforce assignments | built, kept independent |
| **Economy** | production, consumption, prices, trade, accounting | built, kept independent |
| **Society** | population, culture, organisations, collective behaviour | new; P6 |
| **Cognition** | perception, memory, learning, individual decisions | **started 2026-10-30** (Rex: begin now, in parallel, under refinement A): a baseline decision engine first (perception and subjective world, needs and goals, knowledge and memory with wrong beliefs, action generation and selection, learning), policy `a_t = π(o_t, m_t, n_t, p)` with the personality structure p a null model in the baseline; Rex's light-and-crystal / eight-function theory is the second layer, changing how experience is processed, never assigning behaviours to types; first benchmark the hungry-pair resource scenario under identical seeds; design and units for Rex's approval before code |
| **Government** | laws, political authority, institutions, enforcement | new; P8; architecture may be researched while P6–P7 build |
| **Knowledge & Technology** | discovery, invention, capabilities, diffusion | new; P9 |
| **History** | historical initialisation, reconstruction and comparison; **a thin composition and validation layer, never a scripted-outcome engine**: it describes what happened in the simulation, it never determines what must happen (Rex) | new; P10–P11 |

**Cellular biology (Rex, 2026-10-30):** a foundational layer of Life & Species between chemistry and tissues,
not a top-level engine (`CELLULAR.md`): ATP production and use, DNA damage and repair, telomeres, senescence,
mitochondrial function, proteostasis, stem-cell populations, epigenetic regulation, inflammation and immune
signalling, cell death and replacement. Modelled as **cell populations with representative states** (size,
capacity, energy, damage, repair, senescent fraction, turnover), never trillions of cells; resolution raised
locally for an experiment. **Ageing is an emergent output of it**, never a timer on organ performance; two people
of the same age differ by their histories. It also underlies muscle growth, nutrition, disease, wound healing,
cancer, toxicology and reproduction, and gives other species their own turnover and regeneration by parameters.
Established cellular processes are labelled apart from simplified or experimental ageing models. Not before P0
and P1: the registry keeper audits metabolism, muscle adaptation, medicine, genetics and organ ageing for what
moves under cellular ownership first.

**Resolution of the biology (Rex, 2026-10-30, refining the above):** cells and DNA are simulated as compact
mathematical representations that preserve their causal effects, never in their real form. Three separate records
per organism: (1) a **genetic profile**, stable inherited information for development and reproduction, as
chromosome segments carrying trait-associated variants (linkage, polygenic effects, dominance, interactions), never
independent trait sliders or an average of the parents; (2) a **cellular and developmental state** (repair
capacity, accumulated damage `D(t+1) = D(t) + damage − repair`, regeneration, adaptation), per representative
tissue population; (3) the **organism state** (anatomy, organs, muscles, nutrients, immunity, capabilities). A
character sheet is a view of these records, never a second source of numbers. A trait like muscular growth is
`ΔM = f(G, T, N, H, R)` (genetics, training stimulus, nutrition, hormones and development, recovery): nobody
inherits a Strength score. Named characters get tissue-level detail; distant populations aggregate genetic and
health distributions.

**Success measures (Rex, 2026-10-30):** the platform is a **generative** model of reality, not only a predictive
one. Two evaluations of equal weight: **historical reconstruction** (does the engine reproduce observed patterns
from documented starting conditions) and **generative plausibility** (do new societies obey physical, biological,
economic and social constraints and emerge through coherent mechanisms, even along histories that never happened).
Each major subsystem proves itself with an **executable demonstration**, not with a pirate slice: an organism
ageing under different conditions; two fighters exchanging physically resolved actions; a settlement answering a
harvest failure; a population forming competing organisations; an institution gaining or losing legitimacy;
several societies developing and interacting over centuries. **Cliodynamics** (Turchin's structural-demographic
theory, the Seshat databank, the journal *Cliodynamics*) is an input and a yardstick for Society, Government and
History: it explains pressures and forecasts instability windows, not specific events, and its own record is
mixed; the test worth running is the platform against simpler cliodynamic models on cases neither was calibrated
on. More mechanisms never mean more accuracy by themselves; where the science is missing (cognition, cultural
change, institutional emergence, ageing rates) the platform holds explicit hypotheses and tests their consequences.

**Attraction and partner selection (Rex, 2026-10-30; registered, not built; after the Cognition baseline):**
attraction is never a universal attractiveness score. Five mechanisms with owners: the **physical phenotype**
(Life & Species: facial geometry such as eye spacing, jaw and proportions and symmetry; body structure, height,
frame, limb proportions; body composition, muscle and fat distribution; surface features; movement, posture,
gait; voice, scent, expression) emerging from genetics, development, nutrition, age, health and environment, so
the body charts carry every feature a person can be attracted to; **individual preferences** (Cognition) from
three interacting influences, biological (inherited and developmental tendencies), social (culture, family, peers,
status; a father pressing marriage within the bloodline, friends fixed on one feature) and experiential (personal
history, learned associations); **social influence** (Society: beauty ideals, family expectation, peer pressure,
status norms); **interpersonal attraction** (Cognition: connection, compatibility, familiarity, trust);
**reproductive behaviour** (Cognition + Life & Species: motivation, partner selection, fertility, conception).
Attraction is `A_ij(t) = F(P_i, X̂_ij, C_i, E_i, R_ij, S_t)` (own preferences, the other *as perceived*, cultural
influence, experience, relationship history, current state), proposed. **Attraction ≠ partner choice ≠ sexual
behaviour ≠ reproduction:** a person may choose a less attractive partner under pressure or reject a socially
preferred one; some people experience little or no sexual or romantic attraction and that is not a malfunction.
Personality shapes what is attended to and how it is weighed, never "Se users prefer muscular partners". Rex's
rule: no norm that "girls like chads and guys like blondes"; variety with consistent inherited and transmitted
factors.

**Style and presentation (Rex, 2026-10-30; a shared planned mechanism, not an engine):** phenotype = what someone
physically is; style = how they choose or learn to present themselves; perceived attractiveness = how another
individual reads the combination. Components and owners: clothing (fit, silhouette, colour, fabric, revealing or
modest: Economy's goods and inventory, chosen by Cognition); grooming (hair, facial hair, cosmetics, hygiene:
organism state + Cognition); accessories (jewellery, piercings, tattoos: body + inventory); personal aesthetic
(gothic, refined, rugged, flamboyant, minimalist: Cognition); behavioural presentation (posture, mannerisms,
speech, confidence displays: Cognition + biomechanics); cultural interpretation (fashion, class signals,
religious dress, status symbols: Society). Style emerges from materials, money, climate, norms, preferences and
what a person has learned attracts others, and can be changed deliberately to influence perception, a feedback
loop across Cognition, Society, Economy and attraction. **Style is never a guaranteed indicator of personality:**
it emits signals that others interpret through their own beliefs, rightly or wrongly. It serves identity, social
judgement and belonging beyond romance.

**General preference learning (Rex, 2026-10-30; the abstraction under attraction; registered, built after the
baseline):** no catalogue of attraction types and no separate formula per thing a person can like. Cognition
gets reusable mechanisms: (1) **semantic representation** of observable and inferred characteristics, abilities,
behaviours, identities and relationships (artist, rebel, kind, intelligent) tied to observed behaviour and to one
another; (2) **individual preferences** `P_i,k(t)` toward any characteristic k, positive, negative, neutral or
context-dependent; (3) **associative learning, generalisation and causal misattribution** from experience (meets
one artist, generalises toward artists, or toward expressive people, or toward admired people, by what the mind
*attributes* the feeling to, rightly or wrongly); (4) **social transmission** of preferences (family, peers,
institutions, culture); (5) **contextual evaluation** of combinations, nonlinear (confidence only with kindness;
rebellion only when read as principled); (6) separate representations of attraction, romantic attachment, sexual
motivation, partner selection and reproductive intention. Baseline `A_ij = Σ_k P_i,k · X̂_ij,k` over the other *as
perceived*, proposed, with interactions and context to follow. Predispositions exist before experience as
distributions and tendencies; not every preference is equally malleable: **sexual orientation is never freely
rewritten by reward, punishment or social pressure.** The same mechanisms serve admiration, distrust,
occupational preference, aesthetic taste and aversion; attraction is one consumer.

**Communication and information transmission (Rex, 2026-10-30 late evening, with ChatGPT; registered, not built;
after the Cognition baseline is stable):** a universal subsystem **owned by Cognition**, with interfaces to Reality,
Economy, Society, Government, Knowledge & Technology and the Kernel. It covers speech, gesture, writing, signals,
rumour and deception; persuasion, negotiation and suppression; not only conversation. The chain: the sender's mind
(knowledge, beliefs, goals, intentions, communication style) → a message in a **medium** → transmission through
Reality (distance, sound, visibility, interference, detection) → the receiver's perception, comprehension, trust and
interpretation → belief updating → consequences (agreement, rejection, negotiation, learning, cooperation, conflict).
Rules: **a message delivers information; the receiving mind decides what it means.** Persuasion is never a charisma
roll against a resistance: a message changes a specific part of the listener's evaluation (belief about quality,
evidence of usefulness, actual cost, affordability, future opportunity, social benefit) and can be logically strong
yet irrelevant to the listener's real objection, fail, or strengthen opposition; `B_{t+1} = F(B_t, M, S, T, E)`
(existing beliefs, message and evidence, source credibility, trust history, the listener's state) is a conceptual
shape, proposed, not an established equation. **Transmission ≠ comprehension ≠ belief acceptance ≠ behavioural
compliance.** Each medium has properties (range, speed, capacity, fidelity, persistence, accessibility,
detectability, cost); Knowledge & Technology says which media a society has, Reality the physical limits, Cognition
what is said and how it is read, Society the networks it spreads through. Suppression (Government: censorship,
enforcement) reduces communication and changes its form (trusted links, secret channels, notes), each alternative
with its own cost, delay, error and **a chance of detection**; suppression never automatically produces rebellion
(it may succeed, breed resentment without action, or grow alternative networks). Personality shapes which arguments
are generated and attended to, never one technique per type; communication competence is learned. The layer reuses
Cognition's existing perception (a message is a Stimulus) and belief-update mechanisms, never a second
belief-changing system. First experiments, in order: two merchants negotiating an item when one knows something the
other doesn't (Cognition + Economy + Kernel); rumour through a small settlement; communication under restriction.

**Conversational plausibility, organic flow (Rex, 2026-10-31, with ChatGPT; part of the communication subsystem,
planned):** a reply answers *why you are saying this, why now, and how it fits between us*, never a keyword. Saying
"buried treasure" to a stranger unlocks nothing: they may say "what?", assume a pitch, grow suspicious, laugh or wait
for an explanation. Cognition keeps a **conversation state** beside personality: shared context (what both know, what
was just said, whether the remark has an understandable link); perceived intention (help, flirting, threat, joke,
fishing, time-wasting); willingness to engage (want of company, somewhere to be, safety, interest); relationship and
boundaries (what may be asked of this person, how much explanation they expect, how readily they forgive
awkwardness); current emotional and bodily state (loneliness, embarrassment, irritation, fatigue, fear, urgency,
distraction); conversational history (interruptions, ignored answers, unexplained topic changes, shown listening,
repairs). **Tolerance for nonsense** (Rex: "willingness to put up with bullshit") is the effort a mind will spend
understanding you before disengaging, from affection, curiosity, obligation, expected benefit, available attention
and how the exchange has gone. The next response is a **choice** among answering, asking for clarification,
interpreting, redirecting, challenging or leaving, through the existing decision mechanism; **awkwardness emerges**
when expectations do not line up, **lingering** when someone still wants contact but has no confident next move
(hesitating, repeating, a weak follow-up, staying after the other has begun closing). Coherence earns no trust by
itself ("what's your interest in the powder?"). Personality influences these, never decides them: openness is not
willingness to talk to a stranger; a reserved person may want company tonight; a lonely one may tolerate a clumsy
approach or read it as rejection. This is where **Big Five metrics** become useful as a *measurement* of the
emergent behaviour (T-2 compares derived traits with McCrae & Costa 1989), never as a driver. Goal: smoothness,
awkwardness, abruptness and repair arise from what each person understands and wants; an urgent warning may
interrupt anything, an unrelated remark may work between close friends, a clumsy person may still be welcomed.
**C-Q12 decided (Rex, 2026-10-31):** conversational tolerance is a **derived assessment, never a need** like hunger
and never an independently draining "patience bar". Its causes stay separate records: social need (current want of
connection), available attention (effort that can be spent), relationship and expectations (trust, whether the
exchange is expected to be worthwhile), interaction history (confusion, irritation, interest, successful repairs).
From those the mind derives whether another turn feels worth attempting; the assessment may be cached for
efficiency. The same confusing remark may exhaust a busy stranger, intrigue a researcher, delight a close friend.
**Shared context means what each person *believes* is shared:** one may think an introduction explained everything
while the other still has no idea why they are being approached; the mismatch yields confusion without a script.

**Cultural salience and the zeitgeist in attraction (Rex, 2026-10-30 late evening, with ChatGPT; registered, not
built; after the Cognition baseline, inside preference learning §13):** two inputs to attraction are represented
**independently**: perceived **social valuation** `V_i` (what the surrounding community admires, endorses, rewards;
Society supplies it) and perceived **sensory appeal** `S_i` (what is visibly fashionable or physically appealing;
read from the phenotype and style as perceived). **Cultural salience** is how often and how prominently a
characteristic appears in a person's environment; Society determines which styles, characteristics and behaviours
are prominent or rewarded, Cognition what each individual notices, how it is interpreted and whether it moves
attraction. Baseline shape, proposed: `A_i = F(V_i, S_i, C_i, E_i)` with `C_i` the cognitive-function weighting and
`E_i` experience and learned associations. Within the eight-function model the functions carry **hypotheses, never
laws**: Fe sensitive to collective valuation, Se to sensory presentation, Fi to personal significance, Si to
familiarity and remembered ideals, Ne to novelty, Ni to symbolic meaning and anticipated trajectory, Te to
demonstrated competence, Ti to coherence of thought. Fe and Se shape *sensitivity*, never conformity: **awareness
of a trend, personal evaluation of it, willingness to conform to it, and attraction toward people displaying it are
four separate outcomes.** A style can be fashionable without a person liking it, and attractive to someone despite
their community's disapproval. Feedback loop: people adopt styles, others react, reactions move social popularity,
popularity moves future preferences.

**Dynamic function allocation, the light and the crystal (Rex, 2026-10-30 late evening, with ChatGPT; registered,
not built; personality layer DESIGN §9, after the baseline):** the type hierarchy is a **baseline**, never a fixed
allocation per decision. An ESTP generally favours Se, but Ti, Fe or Ni can be the primary influence on a given
decision by situation, experience and motivation, and the variation **emerges mathematically, never by hardcoded
exceptions**. Proposed, provisional: active influence of function f at time t
`A_f(t) = B_f·R_f(t)·L_f(t)·M_f(t) / Σ_j B_j·R_j(t)·L_j(t)·M_j(t)` with `B_f` the baseline preference (the light),
`R_f` relevance to the situation, `L_f` learned competence and habit (part of the crystal), `M_f` motivational and
emotional modulation; a softmax over function scores is preferred in implementation. **Experience changes the
activation conditions**: repeated consequences raise how strongly a situation activates a function (a painful record
of appearance-led choices raises future-oriented evaluation when choosing partners), and misattribution is possible
(an aversion to a feature instead of a lesson about compatibility), giving different trajectories from one
baseline. **Attention allocation ≠ evaluation influence**: a function can receive most of the processing without
deciding the action. A dominant function has a statistical tendency to more allocation; an inferior one is never
prevented from leading a decision. (Rex's paste was cut off mid-sentence at this last point; the rest is to be
supplied.)

**Planetary terrain and resource formation (Rex, 2026-10-30 late evening, with ChatGPT; registered, not built; a
subsystem of Physical Reality, never a top-level engine; built with the P2 roadmap beside mechanics, materials,
fluids and geology):** resources exist in the environment before any chemistry or synthesis can make anything, so
the world must supply base materials with a cause. The chain: planetary and geological initial conditions (crust,
rock types, tectonic history, climate) → geology (formations, faults, mineral deposits) → hydrology (rivers,
drainage, groundwater) → climate (rainfall, temperature, wind) → geomorphology (erosion, sediment transport,
deposition) → soils and ecosystems (soil development, vegetation, habitat suitability, biological resources) → a
resource-bearing world (timber, stone, clay, ores, freshwater, crops, wildlife). **No biome loot tables:** a deposit
or stock exists where geological, hydrological, climatic and ecological processes make it plausible (iron from
mineralisation, sediment and weathering; gold hydrothermal and placer; clay from weathering and deposition;
limestone from carbonate sedimentation; timber from species suitability, climate, soil, light, competition; fish
from habitat, food webs, temperature, oxygen, reproduction; farmland from soil, water, nutrients, climate). **Every
resource has quantity, quality, accessibility and location**: a forest is trees with species, age, dimensions and
biomass, never "forest = 100 wood"; an ore body has composition, volume, grade and extraction difficulty.
Generation is **hierarchical and constraint-based**, never a replay of planetary history: provinces and broad
elevation → drainage with erosion and deposition → formations and plausible deposits → soils from parent material,
climate and terrain → vegetation and wildlife → conversion to a game's representation; the Kernel's seeded RNG makes
a world reproducible. **Conservation:** mined ore leaves the deposit, harvested biomass leaves the forest, sediment
moves from one place to another, consumed water comes from somewhere; Economy never creates a physical resource
because a recipe ran. Owners: **Reality** owns physical existence, location, composition and conservation; **Economy**
extraction activity, inventories, processing, trade, valuation; **Settlement** buildings, parcels, infrastructure;
**game adapters** convert the physical terrain into their maps, tiles or blocks (elevation → tile height; formation
→ underground block types; deposit volume and grade → mineable blocks; soil → farm tiles; biomass → harvestable
trees; groundwater → wells; material properties → tools and construction). The old **Runeworld** design
(`Games/P games/Runeworld`: DESIGN.md §16, BUILD_PLAN.md M1; a 2,000 × 2,000 block world with underground layers,
ore veins, caves, harvestable blocks with material properties and tool requirements, chunked seeded persistence,
deterministic replay, resource chains forestry → woodworking → carpentry and mining → smelting → metalworking) is
**reference material for the interface**, never the platform's physical model: the platform never represents the
planet as blocks. Required: deterministic seeds, material-conservation tests, geological plausibility checks and
cross-domain integration tests. The registry keeper checks for existing world-generation mechanisms (pirate
`world/`, ECOLOGY, population) before any row is added, so none is duplicated.

**Terrestrial and aquatic ecosystem foundation (Rex, 2026-10-30 late evening, in his own words and with ChatGPT;
registered, not built; subsystems of Physical Reality and Life & Species, never new top-level engines; the
research domain is the Caribbean of the pirate era, the mechanisms universal):**
- **Principle (Rex):** anything that predates another thing must exist mathematically for the later thing to
  emerge from it, with the exceptions of literal DNA detail and literal grains of dirt; as many pre-environmental
  factors as possible, to real-world conditions. Represent the causal variables that affect the outcome, never every
  molecule, cell, bee or grain.
- **Chain:** physical Earth (geology, terrain, solar energy, atmosphere, **wind and pressure**, water) → soil and
  nutrients (weathering, organic matter, pH, N, P, K, water retention, microbial activity) → primary producers
  (trees, grasses, crops, algae, phytoplankton) → consumers and interactions (pollinators, herbivores, predators,
  parasites, decomposers) → society and economy (agriculture, forestry, fishing, food supply, trade, settlement
  growth); interconnected with feedback, not one-way.
- **Soils (Rex):** emulate real data; a plant on poor, acid, alkaline or nutrient-poor soil, or without water from
  the hydrology, grows poorly or not at all, **by species tolerance**: deficiency reduces growth gradually before
  preventing it. Soil nutrient transfer, gain and spread must be real (decomposition, mineralisation, erosion,
  deposition, runoff).
- **Plants (Rex):** the same architecture and level of detail as humans: a genetic profile, a developmental state
  (age, root and shoot biomass, leaf area, stored carbohydrate, maturity) and a current organism state (hydration,
  nutrient status, stress, damage, disease); physiology from photosynthesis, respiration, maintenance, water stress,
  light, temperature. **Species are added one at a time, each researched for the conditions it needs**
  (`tree.md`, `plant.md` and per-species profiles to follow); first set proposed: West Indian mahogany, sugarcane,
  red mangrove, turtle grass. Reproduction distinguishes pollen and seed, spores, vegetative; cross-pollination and
  inheritance through the genetic profile.
- **Pollinators (Rex):** populations, never rendered individuals: abundance, foraging range, activity, habitat,
  breeding and mortality at their natural values, to the same mathematical detail as humans; expected visits
  `V_ij = N_i · a_i · p_ij · Δt` as a starting approximation, then pollen transfer, compatibility and conditions;
  wind pollination, self-pollination and animal seed dispersal as separate mechanisms.
- **Food web (Rex):** algae and plants → fish and herbivores → carnivores, with **decomposers** and detritus so
  nutrients return to soil and water and energy dissipates; Caribbean pirate-era flora and fauna to control scope;
  overfishing, forest clearing and runoff change populations through the same equations, never event scripts.
- **Geology and weather (Rex):** wind and pressure simulation are missing and are needed for weather from physics
  (phase 13) and for the deeper geology; general distribution of materials in the earth with the conditions that
  predate them; plate tectonics, volcanism and lava flow allowed. Two timescales: **world formation** (a plausible
  geological history or real Earth data establishes formations, deposits, terrain and soils once) and the **active
  world** (erosion, sediment, soil change, vegetation, water, mining, occasional geological events during play);
  fast processes update often, growth and populations on longer intervals, through the Kernel's scheduler.
- **Owners:** Physical Reality: geological formation, mineral distribution, pressure, wind, hydrology, soil
  formation, erosion, physical nutrient transport. Life & Species: plant physiology, growth, reproduction,
  pollination, animal physiology, ecological interactions, population dynamics, decomposition. Economy reads
  stocks and writes extraction; conservation rules as in the terrain paragraph above.
- Research-heavy: per-species profiles are belt units with web tools, labelled researched / estimate per value,
  evidence levels per PLATFORM §4. Testing per PLATFORM §11b. (Rex's paste was cut off after "Allow geological
  history to establish initial conditions…"; the rest is to be supplied.)

**Soil mechanics and excavation (Rex, 2026-10-31, with ChatGPT; registered, not built; a consumer of three
universal systems, never a game rule):** soil is a mixture with measurable properties (bulk density, grain-size
distribution, moisture, cohesion, internal friction angle, porosity, compaction, organic matter, rock content), one
record serving agriculture, groundwater, erosion, landslides, foundations and digging alike. Excavation = tool
geometry and the body's force, speed and fatigue (Life & Species, biomechanics) against soil shear strength
(Mohr–Coulomb `τ_f = c' + σ' tan φ'`, evidence level 1) in Physical Reality (materials, phase 9; contact mechanics
6b), with the Kernel keeping time, events and the persistent change. Work `W = ∫F·dx` bounds what a stroke loosens
and moves; a weaker body removes less, a skilled one spends less energy per volume; wet clay and dry sand differ by
their properties, never by a `diggingPower` number. **Conservation:** excavated mass leaves the terrain as spoil
that can be piled, moved, processed or used as fill; the hole changes terrain geometry, so water collects or
infiltrates, slopes and foundations may lose support, all through the same mechanisms. **Excavation stability** (dry
sand slumps at steep angles, cohesive soil holds temporarily by moisture and load, rock holds or needs support by
fractures and stress) is the same material mechanics engineers use, and gives mining, tunnelling and fortification
their rules. **Adaptive resolution:** a distant hillside is elevation, layers and aggregate quantities; a field is
per-cell soil properties; an active dig subdivides into volumetric cells; a landslide invokes the detailed
deformation calculation while it lasts; the resulting geometry and material distribution persist without further
computation (PLATFORM §9). Games supply only the dig command and its presentation. **Three tightenings (Rex,
2026-10-31):** one authoritative soil *model* but many spatial *records*, since layers and locations differ in
composition, moisture, compaction and strength, and spoil keeps the properties of the material it came from; force
alone never sets excavation time, which also depends on tool geometry, motion, available mechanical power, fatigue,
and lifting or transporting the spoil, so failure prediction is one part of a stroke, not the whole; conservation
accounts for displaced material but calculates no consequence, so flooding still needs the water-flow mechanics and
undermining still needs the stability calculation.

**Gaps noted from a field survey (Rex, 2026-10-31; candidates, registered as planned, owner Physical Reality
unless stated; none scheduled):** checked against ENGINES, REGISTRY, ROADMAP and PHASES-6-PLUS. **Absent
everywhere:** fire dynamics (ignition and spread by fuel, moisture, oxygen and heat transfer; smoke and ventilation;
ships, towns, powder); tides and currents as distinct from waves and weather (coastal navigation; Catalogue or
Reality by region); rotational dynamics and leverage (torque, balance, footing, pulleys, capstans, recoil: a strong
body still fails a lift with poor footing or leverage; phase 6 mechanics must include it); granular mechanics (sand,
gravel, grain, spoil settling, piling, sliding, compacting; beside soil mechanics); structural mechanics as load
paths (beams, joints, hulls, roots; bending, buckling, progressive collapse; materials phase 9 has fracture, not
load paths; Settlement construction consumes it); sail forces and ship stability (fluids phase 7 has buoyancy, not
these). **Partly present, to be made explicit:** tribology (wear of tools, bearings, ropes; materials degradation has
corrosion and decay), dissolved-material transport in water (salt, nutrients, pollutants; hydrology rows carry
water, not what it carries), vector- and water-borne transmission in disease ecology. **Already covered:** fluids,
optics, acoustics (planned), hydrology, biogeochemistry and decomposition, epidemic expected value. **Two process
rules adopted:** (1) every mechanism contract answers five questions, *what enters, what leaves, what accumulates,
what limits the rate, what makes it fail*; the registry adds "rate limiter" and "failure mode" to the §7 contract
fields and the kernel's check script may warn when they are empty; (2) numerical simulation practice is a Kernel
and Reality responsibility in its own right: time-step stability, consistent updating of coupled systems (water
changes soil strength, soil movement changes water flow), sensitivity of outcomes to uncertain inputs, scale
selection, calibration and validation beyond ledger balance (PLATFORM §11a item 5 names stability; this widens it).
Learning priority Rex adopted: mechanics → water and material transport → soil and decomposition → structural
failure, simulation methods alongside.

**Five Cognition directions (Rex, 2026-10-31 ~01:10–01:45, with ChatGPT; planned, for the Cognition keeper to
record in DESIGN as (Rex); Rex may brief that keeper directly):**
1. **Memory sits below personality.** Stages: attention (what is noticed: goals, interests, danger, novelty,
   distraction, existing knowledge) → encoding (what becomes a memory, in what detail) → consolidation (what becomes
   durable; sleep is a biological influence here) → retrieval (what the situation or another's remark brings back) →
   communication (what is mentioned, concealed or questioned: remembering and saying are separate acts). Three
   witnesses of one dockside argument remember different things by attention, experience, goals and state, with no
   type-specific memory rule. Neuroscience (Reality) owns the biological constraints; Cognition owns attention and
   remembering; the personality label is **descriptive**: dispositions influence behaviour, the label describes the
   resulting pattern (Rex's correction of "personality weights these"). A measured trait used to predict attention is
   an empirical approximation, never a neural mechanism. "Grey matter" is not a capacity number.
2. **Gaze and eye contact** are a large factor in social interaction: the visible behaviour (where, how long, looking
   away, expression, posture, distance) is separate from the observer's interpretation (attraction, anger, curiosity,
   challenge, submission, mere attention) and from the response (return, smile, avoid, question, approach, defend).
   Interpretation is **several hypotheses with likelihoods**, shifted by each new cue, carried forward and revised;
   randomness represents uncertainty, never replaces causes; weights researched and calibrated, no "three seconds
   means attraction"; cultural and individual differences and misunderstanding included; it feeds attention and memory
   of the encounter. Part of the communication subsystem (nonverbal).
3. **Intermittent characters** (pirate plugin: story and town keepers; Cognition supplies continuity): people whose
   lives intersect the player's only sometimes: regular (annual visitor, seasonal worker), irregular but explainable
   (a ship's route, weather, repairs, business), conditional (family, debt, need, wanting to see you), apparently
   one-time. **Continuity during absence**: they return changed, remember the last conversation, come for a new
   reason; simulated only enough to account for meaningful change. An expected person may fail to arrive, and that
   absence matters without becoming a quest.
4. **Tattoos, body features, names** (style and presentation above): separate the feature, its intended meaning
   (belonging, religion, rebellion, remembrance, taste) and the observer's interpretation, which may be wrong;
   "exotic" means unfamiliar *to this observer*, never a property of the name or person. Cultural tattoos may encode
   rebellion factors.
5. **Drugs alter the person, not only the state (Rex, firmly).** Repeated exposure to cannabis, methamphetamine,
   cocaine, heroin can lastingly change how someone thinks, reacts and relates, including the **reasoning process
   itself**: association speed, what counts as evidence, how certain they become, whether contradictions are noticed,
   working memory, checking of conclusions, belief updating. The baseline must be alterable by history, never reset
   when the substance wears off. Separate processes, each substance its own researched model (Reality neurology and
   pharmacokinetics own the biology; Cognition the altered processes): immediate effects (attention, arousal,
   inhibition, perception, body); tolerance and dependence, withdrawal apart from intoxication; learning and craving
   (people, places, situations associated with relief or reward); longer-term adaptation and recovery on their own
   timescales with individual variability (lasting ≠ irreversible); injury or illness as a separate pathway. A
   formula for lasting change in brain chemistry and synapses that later shows as personality presentation is the
   research target; the personality measurement describes the resulting pattern.

**Experience pipeline and memory model (Rex, 2026-10-31, given directly to the Cognition keeper; DESIGN §16,
planned):** perception filter (the extraverted function decides what is weighted) → encoding (the introverted
function) → chemical response (Reality: neurology and endocrine) → re-interpretation of the body state, externally
and internally; **that second read is the emotion**. Experience feeds stages 1, 2 and 4. **Memory is three values:
stored, retrievable, articulable**; it is not Si's. Stored = event + interpretation + body state; retrieval can
re-trigger the chemistry. Each function has a memory profile (Si, Fi, Ti, Ni, Fe given; Se, Ne, Te open, C-Q16);
functions in a stack modify each other's memory. The emotion's description is irrelevant to the objective output,
which is what the person says afterwards and how. **Requirement (Rex):** every brain and body chemical present, with
cited physiological effects; **Life** owns them (`body.circuit_outputs`, `body.transmitter_levels`,
`body.hormone_levels`, REAL-29, planned post-P1), Cognition reads them (`mind.appraisal`, `mind.recalled_body_state`).
Next from Rex: how memory affects interpretation.

**Rex's questions of 2026-10-31 evening (recorded; no code):** (1) **Why not split Physical Reality from Life &
Species now** rather than keep them intertwined in `realism/`? Proposed for Rex's decision: split at the registry
and port level now (every row is already tagged domain A or B; the contract between them, physics → physiology
reads such as heat transfer → thermoregulation, becomes explicit kernel ports), and split the package when phase 6
mechanics starts, since mechanics is pure physics and is the natural first inhabitant of a separate `physics`
package; Reality keeper to estimate the cost. (2) **Engine interplay today**: Kernel adopted by all engines; Settlement
↔ Economy contracted and integration-benchmarked (thirty days); Reality → Settlement and Economy through
`LabourSupply` (person-hours from population; combined test 2757 queued); Reality → pirate adapters (stats,
medicine, weather, food). **Not yet:** Cognition → Economy (an NPC's wants and refusals shaping demand and labour
offers) has no built edge; Cognition outputs intentions with no economic consumer, and Economy's consumption is
per-capita with no individual input. Registered as a planned interface 2026-10-31. (3) **Species**: multiple species
in as much chemical and biological detail as possible with compact cellular representation, never full cellular
determination, as the cellular-biology and three-record paragraphs state. (4) **World change** (a tree dies,
decomposes, bacteria eat it and are eaten, waste feeds the soil, down to how crude oil forms) is the ecosystem
foundation: Life & Species owns decomposition, the food web and nutrient return; Physical Reality owns burial,
diagenesis and deposit formation in the world-formation stage. (5) **Simulate more to find what is missing**: Rex's
instinct matches the executable-demonstration rule; proposed process: after each phase lands, one integrated
scenario run whose failures are logged as missing mechanisms (registry `integration_gaps`), starting with the
thirty-day settlement with bodies eating from inventory once the food group (DUP-21) is built.

**Reality and Life are separate engines (Rex, 2026-10-31 evening):** **Reality** (`rs-reality`) is the physical
world and nothing alive: physics, mechanics, chemistry, gases and atmosphere, optics and acoustics, materials,
terrain and geology, climate and weather. **Life** (`rs-life`) is every organism as a species configuration: species
records, phenotype, physiology (nutrition, neurology, endocrine, capacity), ageing, reproduction, illness, plants,
pollinators, the food web and decomposition. Cognition stays a third engine: a mind is not a body; it reads body
signals and senses from Life (what a body perceives, `body.detectability`, is a Life output computed from Reality's light and sound) and outputs intentions. Rules: Life owns what a body can do,
Cognition what the mind attempts (no behaviour rules in species records); a species' cognition settings (senses,
needs, lookahead, language, personality slot on or off) live with its species record in Life, Cognition supplies the
engine. **Transition:** today's `realism` package is mixed; the Reality & Species keeper splits it by belt units,
physical modules moving to `reality` with every cross-read an explicit kernel port, mechanics (phase 6) starting in
`reality` directly; the backup job mirrors `realism` to `rs-life` until the split lands; one keeper for both until
then, two afterwards. Registry: rows re-owned by their existing domain tag (A → Reality, B → Life); Cognition's
`body.*` ports move from "Reality writes" to "Life writes" (same ids). This supersedes "today inside `realism/`;
split from Life when mechanics makes it necessary" above.

**History is the backend record; knowledge of history is Cognition's (Rex, 2026-10-31):** the History engine is
the written record of what occurred in the simulation, a backend concept: it aggregates, compares against real
history for validation, and never determines what happens or is read by anyone in the world. What a person knows of
the past comes only through Cognition, by fallible routes: **memory** of events lived through (attention, encoding,
consolidation, retrieval, as §14 and §16 set out); **written records**, where one knows only what the writer chose to
record and how, and only if the medium persisted (communication subsystem: persistence, fidelity, accessibility);
**inference from evidence** that remains (perception plus belief update, which may be wrong); and **oral
transmission** (communication plus memory across people). Those beliefs about the past, not the backend record,
drive choices through the ordinary decision mechanism. The record and the beliefs diverge by design: myth,
propaganda, lost knowledge and archaeology arise from the gap without scripts. **Written and oral transmission are
one kind of thing (Rex, 2026-10-31):** the passing of data between minds, with the same fallibility; oral is worse
because every hop re-encodes it through a new mind, where a written record is re-encoded once by its writer and then
only decays with its medium. **Three mechanisms with no owner yet (flagged 2026-10-31):** records as physical objects
(an Economy good, of a material decaying by Reality's rules, carrying information with the medium's persistence and
fidelity); inference from remaining evidence (Cognition, planned, no design); collective knowledge stocks with loss,
the bridge between one mind's belief and "what the town knows", at the seam of Cognition, Society and Knowledge &
Technology. No engine is missing; Knowledge & Technology, Society and Catalogue are the unstarted engines this rule
leans on, and K&T must be built as recorded and transmitted knowledge with loss, never a tech tree. Consequence for the roadmap (review
finding 1): polity formation, war decisions and collapse belong to Government and Society; History keeps aggregation
and the harness.

**Institutions, government and religion emerge (Rex, 2026-10-31, with ChatGPT; planned mechanisms for Society,
Government and Cognition; none built):** no government type is ever assigned ("at population 1,000, unlock
monarchy"). The engines compute the **distribution of authority**; monarchy, council, republic and the rest are
recognisable configurations of power, succession, institutions and legitimacy that may result, by many pathways
(negotiation, conquest, inheritance, religious authority). Illustrative chain: individuals and households (needs,
beliefs, relationships, resources) → coordination and conflict (cooperation, disputes, shared threats, resource
competition) → organisations (leadership, membership, rules, obligations) → institutionalised authority (recognised
offices, enforcement, succession, revenue) → a governmental configuration. **Religion in three parts:** Cognition owns
individual supernatural belief, interpretation, spiritual experience, conviction and doubt; Society owns shared
doctrine, ritual, religious communities, transmission and collective identity; Government owns religious law, official
recognition, restriction and religious authority in political institutions; movements spread, fragment, merge, reform
or vanish through those mechanisms, never a growth meter. **Laws are executable institutional rules as data**, never
text or a modifier: jurisdiction, regulated action, condition, legal consequence, enforcing body, exceptions. Cognition
decides whether someone attempts the act, Reality and Life whether it succeeds, Settlement records the property
interest, Government whether an enforceable violation occurred; **a law can exist and not be obeyed**, and enforcement
can fail for want of resources, witnesses, cooperation or legitimacy. **Eight mechanisms to register planned:**
institution formation and dissolution; authority acquisition and delegation; rule creation and amendment; institutional
compliance (a rule's existence ≠ obedience); belief-system formation; doctrinal transmission and divergence;
institutional succession; jurisdiction and competing authority. Next conceptual milestone: institutions emerging from
people interacting rather than being set as starting conditions.

**Semantic systems, "semantically fluid, never illogical" (Rex, 2026-10-31 night, given directly to the Cognition
keeper; DESIGN §18, planned):** `meaning(signal, context)` changes its output while the function's definition stays
fixed; each mind holds per-term **meaning pools**; an undeclared change of meaning within one argument is an error
(equivocation). Two speeds: **selection** (fast, context picks within one interaction) and **reconstruction** (slow: a
new meaning is built when none fits, kept if the group reinforces it, so the pool drifts). **Bubble exposure history**
builds the pool: narrow exposure universalises one bubble's meanings, wide exposure resolves by the bubble one is in.
Function profiles as hypotheses: Fe large pool, context selection, low reconstruction threshold, group-driven; Ti one
meaning per reasoning chain, explicit redefinition, notices mid-argument switches; Te one meaning anchored to the shared
external standard and pushes others to it; Fi fixed internal referent plus a lossy encoder to public words. Symmetry:
Fe/Ti many outlines vs one structure; Te/Fi shared vs private standard. Conflict emerges (Ti sees equivocation, Fe sees
rigidity), never scripted. Open: C-Q18 reconstruction vs selection in Fe; C-Q19 Se/Si/Ne/Ni profiles. Quantities
`mind.meaning_pool`, `mind.bubble_exposure` (registry).

**Weather validation (Rex, 2026-10-30):** monthly normals within a tolerance are necessary, not sufficient; the
generator must also match rainfall frequency, dry-spell duration, temperature variability, wind distributions,
seasonal patterns and extreme-event frequency, with variable-specific tolerances and independent observational
data, never one universal 10 %.

**Kernel adoption (Rex, 2026-10-30):** adopting shared time, ordering, ids and seeded randomness must not silently
change existing results: the thirty-day settlement simulation gives the same outputs under equivalent initial
conditions unless a correction is documented. **Mortality:** Reality decides biological failure (a crisis before
every death); the game's fate system decides what a dead character becomes; the two rules are compatible.

Refinements Rex set with the approval: **(A)** dependency-based parallelism: a phase starts when what it reads
from is ready, never "the previous phase finished"; **(B)** overlap closure removes duplicate *authority*, not
every related calculation: a detailed and an aggregate computation may coexist when one owner holds the state and
the aggregation interface is documented; the registry distinguishes legitimate aggregation from contradictory
duplication. The benchmark structure (England and Tokugawa Japan for development; Norse Greenland and Copán held
out; Iceland reserve) is approved provisionally: periods, weights and the 70 % target stay provisional until data
coverage and the eleven indicators are audited. No disruptive migration starts until the affected keepers agree
ownership and acceptance tests. The 47 overlap groups are presented in prioritised batches, first shared time,
state ownership, metabolism, fatigue, labour and mortality.

## Engines as they stand today (historical table, 2026-10-30 morning; superseded)

**The current engine table is "The approved organisation" above, as amended by the dated paragraphs; this table is kept as history and is not maintained** (review finding 3, 2026-10-31).

| Engine | Folder | Owner session | State | Priority |
|---|---|---|---|---|
| Reality & Species (physics, chemistry, environment, materials, biology, species) | `realism/` | body-and-world keeper | built: 239 tests; mechanics/biomechanics layer missing; **P2 mechanics is the next phase after P1 (Rex, 2026-10-30)** | high |
| Settlement (land, property, buildings, businesses, workforce, construction) | `settlement/` | settlement keeper | built: step 2, 23 tests; waits on Rex's Q1, Q5, Q6, Q7, Q10 | medium |
| Economy (production, trade, consumption, labour, markets) | `economy/` | economy keeper (started 2026-10-30) | built: steps 2–8, 25 tests (E1–E14: production, consumption, spoilage, shortage, prices, trade, shipments, accounting, labour quotes, the three-port sim); contract with Settlement agreed; next the pirate adapter and the thirty-day benchmark | high |
| Government (laws, authority, institutions, taxes, enforcement) | not created | none yet | nothing | design after Economy; boundaries agreed with Settlement first |
| Cognition & Interaction (perception, memory, learning, decisions, communication, social behaviour) | not created | none yet | nothing; the alignment engine in the pirate repo is the nearest thing | research and architecture after Government; the bar simulator as an early test |

~~Society = Economy + Government + population + culture~~ (superseded 2026-10-30 by the boundary row below: Society is its own engine of organisations and collective behaviour, never a folder of the engines under it). Settlement is Society's physical and institutional layer.

## Scope added 2026-10-30 (Rex: "every facet of life except evolution")

| Engine | Added responsibilities |
|---|---|
| Reality & Species | **Mechanics** (gravity, force, momentum, collisions, friction, fluid forces), **optics** (light propagation, reflection, absorption, visibility; darkness is the absence of light reaching an observer, supernatural darkness a fictional mechanism of its own), fluid dynamics, materials (deformation, fracture, corrosion, decay); the **full lifecycle**: digestion → absorption → metabolism and cellular energy as flux (ATP availability, never a stored pool) → heat → waste and excretion (faeces, urine, CO₂) → sanitation, soil, water quality, disease exposure, **decomposition**; genes and ageing acting through organ capacity, enzyme activity and regulation, never as global modifiers |
| Cognition & Interaction (future) | individual beliefs, preferences, learning, memory, behavioural variability; how a person interprets an experience (blames the government, the merchants, outsiders, themselves, or stays loyal) |
| Society (future) | cultural transmission, social networks, collective action, organisations (families, churches, guilds, cults, political groups); culture as the emergent output of individuals and institutions |
| Government (future) | institutional rules, authority, political systems, enforcement; burial permissions, sanitation rules |
| Settlement | cemeteries (parcels, grave capacity, burial infrastructure), sanitation infrastructure, land use |
| Economy | burial services (coffins, labour, transport, land), waste management, resource flows |
| Pirate game (town keeper) | **`town/CULTURE.md` per town**: the starting conditions only, never the engine: starting beliefs and religious preference (changeable when an outside cult gains influence), customs including burial and death customs, the economic and political arrangement (capitalist, communal, feudal: an institutional structure, not the culture itself), the economic situation, historical context, local practices. Historical research fills it; factions and time anomalies add alternatives (consecrated ground, burial at sea, bodies preserved or transformed) |

Culture, economic system, political system and religion are separate dimensions that interact: a town can be
Catholic, under a monarchy, with private merchant ownership and strong mutual aid, all at once.

## Shared infrastructure still missing

- **Universal time and events:** one scheduler across timescales (milliseconds to years); each engine ticks at
  its own scale.
- **Universal state and causality:** each engine owns its part of a causal chain (physics → anatomy → medicine →
  physiology → cognition → economy → society) with no duplicated ownership of state.

## Game-specific keepers (pirate-ship, never engines)

| Keeper | Owns | Priority |
|---|---|---|
| story | characters, quests, factions, transformations, consequences | maintain |
| town | FACILITIES.md, the starting port's configuration, locales, ownership rows | medium, waits on Rex |
| combat | pirate fighting rules and encounters; consumes realism's physics | resume walkthrough |
| bestiary | creature definitions, biological profiles, provenance, journal entries, encounter data; never physiology | maintain |
| balance | alignment, endings, reachability, fate constraints | paused |
| art | character and environment assets | paused |

## Boundaries Rex set on 2026-10-30 (the five overlaps)

| Overlap | Boundary |
|---|---|
| Settlement ↔ Economy | Economy started; its first task is the interface agreement with Settlement, then an independent economic sim; thirty-day autonomous settlement sim as the first integration benchmark |
| Population | demography moves to Society when a Society-side owner exists; Reality keeps biological reproduction, ageing and mortality |
| Culture and organisations | reserved for the Society layer; Story keeps fictional faction identities and narratives. Society is not a folder of Economy + Government + Population: it must represent organisations and collective behaviour (a pirate faction is at once an economic actor, a political organisation and a social group) without duplicating the engines under it |
| Alignment ↔ Cognition | the alignment engine in the pirate repo stays pirate-specific; the eight-function personality model becomes one optional cognitive model inside the future Cognition engine |
| `STATS.md` (pirate repo) | the Reality & Species keeper is its **editing coordinator**: it makes the edits and keeps the scientific mechanisms under each attribute consistent. It is not the design authority: gameplay attributes, progression and balance stay Rex's. Combat and Story submit proposed changes to it instead of editing |

## Contracts to agree before code

- **Settlement ↔ Economy: agreed 2026-10-30.** `CONTRACTS.md` is byte-identical in `economy/` and `settlement/`
  (Settlement's side: `settlement` commit 2c4223c, 26 tests). Seven items in its §12 are open for Rex: goods
  types (GOODS.md Open 1–8), `port.cash` as treasury (Q7), who values property for an unpriced sale, whether
  named characters' spending is simulated, the price formula, wage levels and whether quotes move them (Q10),
  whether an idle fixture counts (Q9).
- **Settlement ↔ Government:** Settlement records who holds an office; Government defines what the office may do.
- **Realism ↔ Combat / Bestiary:** realism owns physics and physiology; combat and bestiary read them.
- **Story ↔ Cognition:** story defines motives and history; cognition computes decisions from them.

## Log

| Date | What |
|---|---|
| 2026-10-30 | File opened from Rex's reorganisation; cargo-research session archived; owners and the three new lanes recorded |
| 2026-10-30 | Economy keeper started; the five overlap boundaries and the `STATS.md` coordinator recorded |
| 2026-10-30 | Settlement ↔ Economy contract agreed; economy engine built to step 8 (25 tests); seven contract items open for Rex |
| 2026-10-30 | Rex: historical data fills answers first (three value labels); culture emerges from individuals; cemeteries and `town/CULTURE.md`; mechanics, optics, excretion, decomposition, cellular energy, genes and ageing added to Reality's scope |
| 2026-10-30 | Rex approved overlap batch 2 (all 12 owners; DUP-38 and DUP-49 refined; four answers and a sleep flag recorded in `OVERLAPS-BATCH-2.md` "Rex's decisions") and picked **P2 mechanics** as Reality's first phase after P1 (REAL-12). The pirate game never fixes a universal item list; appetite splits Reality / Cognition / Society / game |
| 2026-10-30 | Rex: communication and information transmission registered as a planned Cognition-owned subsystem (medium properties, persuasion by changing the listener's evaluation, suppression with detection chance); to build after the Cognition baseline; registry keeper asked to add planned rows and interfaces |
| 2026-10-30 | Rex: cultural salience / social valuation vs sensory appeal as independent attraction inputs (Fe/Se hypotheses, four separate outcomes), and dynamic function allocation `A_f(t)` with attention ≠ decision authority; both registered as planned for the personality layer after the baseline |
| 2026-10-30 | Rex: planetary terrain and resource formation registered as a planned Physical Reality subsystem (causal resource formation, quantity/quality/accessibility/location, conservation, hierarchical generation; Runeworld as interface reference, never the physical model); P2 roadmap |
| 2026-10-30 | Rex: terrestrial and aquatic ecosystem foundation registered as planned (soils to real data, plants with the human three-record architecture added one researched species at a time, pollinator populations, Caribbean food web with decomposers, wind and pressure for weather, two geological timescales); testing cost rule PLATFORM §11b |
| 2026-10-31 | Rex: soil mechanics and excavation registered as planned (soil property record, Mohr–Coulomb shear, work-bounded strokes, spoil conservation, excavation stability, adaptive resolution); consumer of materials, biomechanics, terrain and the Kernel |
| 2026-10-31 | Rex: field-survey gaps registered as planned (fire, tides and currents, rotational dynamics and leverage, granular mechanics, structural load paths, sail forces and ship stability; tribology, dissolved transport and disease vectors made explicit); two process rules: five-question contract fields (rate limiter, failure mode) and numerical-simulation practice |
| 2026-10-31 | Rex: conversational plausibility added to the planned communication subsystem (conversation state, tolerance budget, response as a choice, awkwardness and lingering emergent, Big Five as measurement not driver) |
| 2026-10-31 | Rex: C-Q12 decided, conversational tolerance is a derived assessment over separate causes (social need, attention, relationship, history), cacheable, never a need; shared context is each party's belief of what is shared |
| 2026-10-31 | Rex: five Cognition directions planned (memory stages below personality with the label descriptive; gaze as hypotheses with likelihoods; intermittent characters with continuity in absence; feature vs meaning vs interpretation for tattoos and names; drugs lastingly alter the person and the reasoning process, substance-specific models) |
| 2026-10-31 | Rex (to the Cognition keeper directly): experience pipeline and three-value memory model recorded as DESIGN §16; Reality to supply every chemical with cited effects (REAL-29) |
| 2026-10-31 | Rex: Reality and Life split into two engines now (`rs-reality`, `rs-life`); realism package split by belt units, mechanics starts in reality; registry re-owns rows by domain tag; Cognition body ports move to Life |
| 2026-10-31 | Independent organisation review (controller's sub-agent): dependency direction clean, Kernel fence real; twelve findings routed (History over-scoped, organisations/households/transmission multi-homed, stale tables, providers invisible to the registry check, realism single process, V&V overclaims, ownerless shared rows, Catalogue startable); ENGINES tables corrected |
| 2026-10-31 | Rex: History is the backend record only; knowledge of the past is Cognition's through memory, written records, inference from evidence and oral transmission, and those beliefs drive choices; History's roadmap scope narrows to aggregation and the harness |
| 2026-10-31 | `ENGINE_MAP.md` written as the stable reference for all eleven engines (six built, five not started) and their connections; this file stays the decision log |
| 2026-10-31 | Rex: institutions, government and religion emerge, never assigned; laws as executable rules data; religion split Cognition / Society / Government; eight planned mechanisms registered |
| 2026-10-31 | Rex approved batch 2b, X1, the Catalogue design and the Life design (answers in the PLATFORM log row of the same date); approval markers may be queued in the catalogue and life lanes |
| 2026-10-31 | Rex (to the Cognition keeper directly): semantic systems model, meaning pools, selection vs reconstruction, bubble exposure; DESIGN §18 planned |
