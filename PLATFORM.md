# The reality simulation platform: mission and directive (Rex, 2026-10-30)

**Read this, then `ENGINE_MAP.md` (what each engine is for), then `ENGINES.md` (the decision log).** It records Rex's change of mission, given 2026-10-30 in his own words and in
a directive he worked out with ChatGPT and adopted. Everything below marked **(Rex)** is his; the rest is the
controller's organisation of it.

## 1. The mission

**(Rex)** We are no longer building a pirate simulator. We are building a **universal reality, life and
civilisation simulation platform**: Earth-like physics, organisms, human behaviour, societies, civilisations,
technology and history, produced by interconnected causal and mathematical mechanisms. It must run with no game,
graphics, narrative or player. A game is an interface and a set of objectives layered over a simulated reality.

**(Rex)** The pirate RPG becomes **one plugin** of the platform: it selects a time window, a region, and what the
catalogue allows (§6), and layers its story, factions, alignment, supernatural elements and progression on top. It
never defines a universal rule. Its story, combat, alignment, bestiary, town and art work stays intact, parked on
the back end, not interconnected with the platform for now.

**(Rex)** The scope is "every facet of life except evolution": lumber per wall and the techniques for each kind of
wall, every method of production of everything, gravity, forces, light and darkness, decay, digestion, waste. The
test of success is a **civilisation-scale** sim: a society becomes a village, city, kingdom, republic or empire by
its conditions; nations go to war for the reasons humans actually have; it can produce outcomes that never
happened, not replays.

## 2. The philosophy

**(Rex)** Explain outcomes by their mechanisms; never hardcode the outcome. No technology because its year
arrived; no war because a script said so; no rebellion because a meter hit a threshold; no production because a
building is labelled a factory; no strength because of a level. Mathematise history: find the gears behind why a
society reaches human sacrifice, why a revolution eats its own. The sim builds on itself: more turning gears is
better, **the one danger is overlapping gears** (two mechanisms for the same thing, built because the second author
forgot the first). Deterministic given the same inputs and seed; stochastic only where real uncertainty exists;
different seeds may give different histories, and that is a feature.

## 3. The seven domains

| Domain | Covers | Today |
|---|---|---|
| A. Physical reality (**Reality** engine since 2026-10-31) | physics, chemistry, materials, thermodynamics, gravity, motion, optics, fluids, geology, atmosphere, weather, oceans, energy, degradation; construction mechanics, structural engineering, material requirements, manufacturing feasibility | `Toolchain/realism` (thermodynamics, gases, chemistry built; mechanics, optics, materials planned, PHASES-6-PLUS) |
| B. Life and species (**Life** engine since 2026-10-31) | anatomy, organs, muscle, neurology, genetics, metabolism, nutrition, cellular energy, reproduction, development, ageing, disease, injury, healing, waste, decomposition, death; humans first, then other species by configuration | `Toolchain/realism` and the `body/` docs |
| C. Cognition and interaction | perception, memory, learning, personality (the eight-function model as one configurable model, never hardcoded), goals, decisions, emotion, communication, relationships, variability | `Toolchain/cognition` (baseline accepted 2026-10-30; personality v1 opt-in; communication, memory stages, experience pipeline planned) |
| D. Economy and production | extraction, agriculture, manufacturing, construction, labour, trade, transport, markets, currencies, scarcity, pricing, ownership, investment, consumption; capitalism never assumed; every process grounded in materials, tools, knowledge, labour, energy, conditions | `Toolchain/economy` (25 tests), `Toolchain/settlement` (26 tests), contract agreed |
| E. Government and institutions | authority, law, offices, taxation, spending, property rights, enforcement, military organisation, diplomacy, succession, legitimacy; communities to empires | nothing; future lane |
| F. Society and culture | population, households, kinship, religion, norms, traditions, organisations, class, cultural transmission, collective action, migration, cooperation, conflict, rebellion; culture emerges from individuals, institutions, material conditions and history; a culture profile seeds it | `world/POPULATION.md` only; future lane |
| G. Civilisation and history | settlements, cities, states, nations, empires, technology development, armies, international relations, expansion, collapse, transitions; why societies get their institutions, technologies, wars and practices | nothing; the roadmap must show it |

## 4. Mathematising history

**(Rex)** Research and formalise historical mechanisms wherever evidence exists, from history, science,
economics, demography, political science, anthropology and psychology. Each mechanism is labelled by evidence
quality: (1) established physical or mathematical relationship; (2) empirically supported statistical
relationship; (3) historical observation and interpretation; (4) simplified simulation approximation; (5)
hypothetical or experimental model; (6) fictional mechanism. Historical events are evidence for building and
testing models, never scripts; competing explanations are kept, not collapsed to one.

## 5. Historical reconstruction as the validation test

**(Rex)** Pick several real societies with very different environments, institutions, resources, technologies and
outcomes. Initialise from documented conditions at an earlier date, run without forcing the outcome, compare the
trajectory with history. Target: **at least 70% similarity (a reality differential of at most 30%)**, measured by
explicit indicators, never a subjective score: population, settlement growth, resource availability, production,
technology, institutional change, territory, conflict, political stability, migration, cultural and religious
change; each indicator and their combined trajectory. Multiple runs, controlled conditions, recorded seeds;
systematic error told apart from stochastic variation. Societies used for development are never the only ones
used for validation. A failed reconstruction is investigated for the missing mechanism, input or interaction. The
70% is a provisional development target, not a claim.

## 6. Technology emerges; the catalogue tags, never unlocks

**(Rex)** Invention dates are reference information. A society develops a technology from resources, knowledge,
tools, manufacturing capability, energy, skilled labour, incentives, institutions, communication and
experimentation; earlier than history if the capabilities exist, never if they don't. Possibility, knowledge,
invention, adoption and deployment are distinct states.

**(Rex)** A **universal reference catalogue** tags every entity, substance, organism, technology, institution,
practice and phenomenon: stable id, names, classification, geographic origin and spread, culture or civilisation,
earliest evidence, period or date range, discovery / invention / identification / adoption dates, sources,
confidence, and the provenance class (real, prehistoric, mythological, fantasy, science fiction, original fiction;
several may apply). Thorough enough to say "this region, this country, this locale, this period". Two uses:
**game configuration** (a pirate game asks for the Caribbean, 1690–1720, and gets historically grounded starting
conditions; a medieval or dark-ages game asks for its own) and **unconstrained life simulation**, where the
catalogue never grants anything because its date arrived. Historical metadata is never an invisible progression
script.

## 7. No duplicate mechanisms: the registry

**(Rex)** Every mechanism has one authoritative owner. Before any new subsystem, formula, table or document, the
author searches the registry for an equivalent. Every mechanism carries a contract: stable id; owning engine;
inputs and units; outputs and units; internal state; mathematical formulation; dependencies; timescale and update
frequency; conservation rules or invariants; sources and evidence quality (§4); approximations and limitations;
validation tests; downstream consumers. Subsystems talk through explicit interfaces; no engine applies a second
penalty for an effect owned elsewhere (dehydration changes one biological state; everything else reads it). The
registry (`REGISTRY.md`, with a dependency graph) must expose duplicated calculations, conflicting ownership,
circular dependencies and incompatible units. The registry is the controller's main tool.

**One transfer per physical flow (Rex, 2026-11-01, from CHAINS.md):** every physical quantity that moves between
stores is one transaction with one source and one destination, `Δ_source = −q` and `Δ_destination = +q` written together,
with losses and transformations accounted separately; never two independent calculations of the same flow (the
built soil-fertility drain beside plant nitrogen uptake was the first violation found). The rule applies to every
transfer: nutrients, water, mass, energy, money.

## 8. Documentation: one gear per file

**(Rex)** Each gear is its own small `.md` that feeds a larger one: `PHYSICS.md` names the domain; gravity,
mechanics, optics, fluids and thermodynamics each have their own file; higher systems reference, never rewrite,
a formula. Documentation mirrors executable ownership. Source data and implementation stay in sync.

## 9. Resolution

Different resolutions for the same mechanisms: an individual nearby in full physiological, cognitive and physical
detail; a distant village as aggregated demography and economy; a civilisation in long steps until an event needs
finer ones. Finer resolution refines the aggregate, never contradicts it.

## 10. What is preserved

Nothing is deleted or rewritten: `Toolchain/realism`, `economy`, `settlement`, the scientific reference library,
and all pirate-ship content (story, combat, alignment, bestiary, town, art, STARTING_TOWN.md, CULTURE.md). Keepers
keep their responsibilities until a reassignment is approved. This is evolution of the architecture, not a
rebuild.

## 11. How the work is run (Rex, 2026-10-30)

- **The controller outputs; the sub-agents build.** The controller session coordinates architecture, ownership,
  dependencies, priorities and integration, and reports to Rex. It does not build.
- **Every sub-agent session is Opus 5.5** (`claude-opus-5-5`), never Fable.
- **Build units go through the conveyor belt** (`Games/Card Games/_agent/run_queue.py`, lanes `realism`,
  `settlement`, `economy`, `pirate-ship`; `BELT.md`, `RULES.md`, `WORK.template.md`): Codex for engine logic,
  Cursor Composer for data, tests and UI, Claude Sonnet for platform work, Haiku for checks. Keepers write WORK
  files and gates; the runner decides pass or fail. Quality is never traded for tokens: a unit that needs design
  judgement stays with an Opus keeper.
- Every keeper ends every turn with five lines (responsibility, latest commit, tests, blocked on Rex, next task)
  and keeps `HQ/handoffs/<keeper>/HANDOFF.md` and `ISSUES.md` current.
- Historical first; three value labels (`ENGINES.md`).

## 11a. Mathematical verification and validation (Rex, 2026-10-30)

The keepers are responsible for researching, selecting, implementing, testing and validating the mathematics.
Rex is never the one who finds a wrong formula, an unrealistic parameter, a numerical instability or a
contradiction between mechanisms; he decides what the simulator must represent and approves major design choices,
and he can ask why a simulation behaves as it does and get a traceable, evidence-backed answer.

Three states, never conflated: **implemented** (the code exists and its unit tests pass) ≠ **integrated** (it is
wired to the mechanisms it reads and feeds, through registry ports) ≠ **validated** (its behaviour, alone and in
combination, matches independent evidence within declared tolerances). The registry records all three per mechanism.

For every mechanism the owner provides: (1) the scientific sources and the model used; (2) inputs, outputs, units,
assumptions, conditions of applicability; (3) **verification** tests, that the mathematics is implemented as
stated; (4) **validation** against independent empirical data where any exists, with tolerances; (5) numerical
stability, conservation and boundary-condition tests; (6) **integration** tests with the mechanisms it is
connected to (heat transfer and thermoregulation together, not only apart); (7) automated detection of duplicate
effects and conflicting state ownership (the Kernel check script); (8) a report of accuracy, uncertainty,
limitations and unresolved scientific questions. A validation specification is part of every belt unit's Gate.

When a model fails validation, the owner investigates, corrects and reruns without Rex diagnosing it. Owners may
autonomously fix implementation defects against the approved model inside their boundary. A change to the
scientific model itself, to an architectural assumption, or an unvalidated hypothesis is recorded and reviewed
before it becomes authoritative. Where no validated model exists, the approximation or hypothesis is labelled
(§4 levels 4–6) and an experiment to evaluate it is designed.

Qualification: an agent testing its own implementation is not independence. Validation needs independent
reference data, competing models where they exist, a re-audit by the registry keeper, Haiku check units that did
not write the code, and the held-out benchmarks; for cognition and civilisation-scale behaviour, explicit
uncertainty is the honest result.

## 11b. Testing cost (Rex, 2026-10-30 late evening)

**(Rex)** Test enough to know things function reasonably well; constant testing must not cost as much as building.
Three levels, applied by every keeper when writing Gates: (1) **mechanism tests**, small and deterministic, for
equations, units, conservation and boundary conditions, run with every unit; (2) **integration tests**, run only
when a shared interface or contract changes; (3) **scientific validation**, periodic comparisons against
independent data, never on every change. Not every change reruns the full thirty-day harness or a full engine
suite: a unit's Gate runs the filtered suite for what it touched plus the mandatory cheap checks. **Mandatory
regardless of cost:** conservation checks, destructive-operation safeguards, and the tests of any shared contract
that was modified. The distinction is redundant testing versus meaningful verification; §11a's states
(implemented, integrated, validated) are unchanged.

## 12. The controller's immediate assignment (Rex, 2026-10-30), and its state

| # | Item | State |
|---|---|---|
| 1 | Update mission and architecture docs | this file; `ENGINES.md` points here |
| 2 | Audit the existing engines against the seven domains | the audit session (`HQ/handoffs/registry/`) |
| 3 | Missing foundational mechanisms and duplicated responsibilities | the audit session |
| 4 | Mechanism ownership registry and dependency graph | the audit session: `REGISTRY.md`, `registry/` |
| 5 | Separate universal requirements from pirate-specific ones | the audit session |
| 6 | Review whether the engine organisation needs expansion or regrouping | the audit session proposes; Rex approves |
| 7 | Update the master development dashboard to the new mission | pending (the Game dashboard, `Card Games/progress`, port 8098) |
| 8 | Phased roadmap by dependencies with acceptance tests | the audit session: `ROADMAP.md` |
| 9 | Preserve repositories, commits, tests, keepers | nothing removed |
| 10 | Present the reorganisation for approval before any disruptive migration | the audit session reports; the controller presents; Rex approves |

## Log

| Date | What |
|---|---|
| 2026-10-30 | Mission changed from pirate simulator to the universal reality platform; directive recorded; run rules (controller outputs, Opus 5.5 sub-agents, belt) recorded; settlement and economy lanes added to the belt; audit session started |
| 2026-10-30 | Rex approved the Cognition design (C-Q1–C-Q8 as proposed, personality after the baseline, crude formulas with codex fingerprints) and added a universal motivational architecture (Maslow for categories not priority; SDT; homeostatic/allostatic; RL; `M_i = w_i·D_i·S_i` proposed); Reality owns biological signals, Cognition owns appraisal and selection, personality owns processing. Cognition lane released |
| 2026-10-30 | Cognition lane opened at Rex's direction (baseline decision engine first, personality second; design before code) |
| 2026-10-30 | Rex approved the Kernel P0 design (ms ticks; harness in `kernel/harness/`; `money` and `count` base dimensions; year length deferred to Catalogue/History) and all 14 batch-1 overlap owners. The kernel lane is released; keepers start P1 groups as they agree acceptance tests |
| 2026-10-30 | Audit delivered (`AUDIT.md`, `REGISTRY.md`, `GRAPH.md`, `ROADMAP.md`). Rex approved the engine organisation and the P0–P11 order with refinements A (dependency parallelism) and B (duplicate authority, not every calculation); Kernel infrastructure-only; weather a physics-generated P2 subsystem; benchmark structure provisional. Items 2–6 and 8 done; 7 (dashboard) and 10 (migrations, per batch) remain. GitHub: `Pirate-game` and `Reality-simulator` pushed |
| 2026-10-30 | Rex approved overlap batch 2 (all 12 owners; DUP-38 and DUP-49 refined; four answers and a sleep flag recorded in `OVERLAPS-BATCH-2.md` "Rex's decisions") and picked **P2 mechanics** as Reality's first phase after P1 (REAL-12). The pirate game never fixes a universal item list; appetite splits Reality / Cognition / Society / game |
| 2026-10-30 | Rex: testing cost rule (§11b): three levels, filtered gates, full harness never per change; conservation, safeguards and modified-contract tests stay mandatory. Ecosystem foundation registered as planned (ENGINES.md) |
| 2026-10-30 | **P0 closed** (kernel b71411a, 23:59): all re-checks green across kernel, settlement, economy, realism and the pirate web suite. Same evening: kernel and economy repos recovered after I-1048 (kernel 392f7bc, economy e366b49); registry rebuilt; ecosystem foundation registered (11 rows, DUP-54); P1b and batch-2 units queued under §11b gates |
| 2026-10-31 | Rex: GitHub becomes the off-site backup, one repo per engine under `Carlos-Roman-Conville/rs-*` (rs-platform, rs-kernel created; realism, settlement, economy, cognition, backup to follow), pushed **only by the backup job**; keepers and belt units still never push. Toolchain root becomes the `rs-platform` repo (closes CTRL-12). The subtree sync into `Reality-simulator` is retired |
| 2026-10-31 | Rex: every engine has an active keeper; Life, Catalogue, Society, Government, Knowledge & Technology and History keepers started, design first; seven new belt lanes |
| 2026-10-31 | Rex approved: overlap batch 2b (DUP-58–62, owners as proposed, collective knowledge under K&T); X1 the first integrated experiment as drafted; the Catalogue design (CAT-Q1–Q6 yes); the Life design (LIFE-Q1 multiply except Liebig's minimum among nutrients, Q2 resolution by distance, Q3 the design is tree.md/plant.md, Q4 Creole cane first, Q5 then cassava or plantain, a grass, a reef fish and its algae) |
| 2026-10-31 | Rex approved kernel DESIGN §16 (CTRL-22): tagged immutable releases installed from the local backup mirror, tarball as fallback, exact commits pinned, consumers upgrade only in paired units, compatible versions recorded per run; **releases cover bug fixes and behavioural changes consumers need, not only interface changes; release commits are preserved off-machine** (GitHub rs-* mirrors, BKP-9). Live links stay forbidden |
| 2026-10-31 | Rex approved the Society (SOC-Q1–8), Government (GOV-Q1–8), Knowledge & Technology (KNT-Q1–4) and History (HIST-Q1–4) designs as the controller recommended, with two refinements: **GOV-Q1** authority is calculated from underlying mechanisms and observable conditions (resources, enforcement capability, institutional recognition, social relationships, compliance), never an independent power score; the formula is provisional and subject to validation. **SOC-Q2** historical charter forms are reference components, not an exhaustive menu; novel organisations must be able to emerge from valid combinations of mechanisms. Also approved: DUP-33 and DUP-32 acceptance-text amendments; REAL-33 option (a), Process S with sourced constants. Held until after the usage reset: C-Q10 and the T-1/T-2 scenario design. Rules restated: testing proportional to implementation (§11b); report only genuinely new decisions; never reopen settled ones |
| 2026-11-01 | Rex released the T-1/T-2 scenario build (S1→S3→S2→S4→S5→S6) with F1–F13 frozen; SC-4: no dedicated Neuroticism mechanism, investigate emergence from stress, appraisal, physiology and learning, a later stress-response experiment; SC-5: mixed-type gatherings with controlled runs holding the social environment fixed; record internal processing (attention, interpretation, alternatives, evaluation, learning) as well as actions; the wanted result is which mechanisms give stable, context-dependent, or no differences |
| 2026-11-01 | Rex: all engine repos pushed to GitHub (`Carlos-Roman-Conville/rs-*`, twelve repos including rs-platform and rs-backup) by the backup job's off-site step run on his instruction; off-site pushing becomes standing (every mirror cycle). The fine-grained token for the backup account remains the open hardening item (BKP-13) |
| 2026-11-01 | Rex: a targeted **causal-chain completeness audit** (`CHAINS.md`, registry keeper) for three chains, ecological (sunlight → soil → plant → herbivore → metabolism → excretion → decomposition → soil), human lifecycle (conception → genetics → maturation → energy accounting → tissue populations → ageing → death) and one cognitive decision (perception → intention → resolution → changed world and mind): per link the quantity, equation, parameter source, owner and state; plus the seven structural checks and a microbiology dependency check. The main problem is not a shortage of equations but every quantity having a causal origin, one owner and a consistent path |
| 2026-11-01 | Rex: CHAINS.md link rule, output of one mechanism must be a valid input to the next (units, timescale, ownership; one physical transfer is one quantity); gaps classified as missing mechanism / broken connection / invalid coupling; no new foundational mechanisms commissioned until the audit is done |
| 2026-11-01 | Rex approved CHAINS.md's integration-first order: (1) the five invalid couplings, one authoritative quantity and one conserving transfer per shared flow, duplicate biomass and soil-fertility calculations eliminated, units and timescales aligned, N/P/K separated; (2) the seven broken connections, intention-to-outcome resolution and the resource, nutrition and Cognition→Economy interfaces first; (3) chain 1's missing equations, then the lifecycle and decision chains; research in parallel, implementation respects unresolved dependencies; targeted tests, integrated demonstrations at milestones; CHAINS.md updated per closed gap with unit, equation, owner, verification. Rule §7a: one transfer per physical flow |
| 2026-11-01 | Kernel **v0.1.0** tagged (ac08916), the first pinned release under DESIGN §16; consumers upgrade in paired units; the IF-27 hire step landed in the harness |

