# CHAINS: causal-chain completeness audit

*Registry keeper, 2026-11-01, at Rex's direction (relayed by the controller). It is a targeted audit of three chains and
seven structures, not a broad review.*

**Sources.** Only committed files were used:
- rs-platform `registry/mechanisms.json`, `quantities.json` and `graph.json` at ef498c9;
- kernel a3c4314, realism 75e4fc2 and cognition 2106314.

Every link cites a registry row. Nothing here is a new rule. Where a link has no row or no quantity, it says
**missing**, and the gap is recorded in `graph.json` → `integration_gaps.interface_gaps` as CG-1 to CG-18.

**Columns:**
- **Quantity:** the registry id and its unit.
- **Mechanism:** the row that moves the quantity.
- **Parameters:**
  - *researched* means evidence level 1–3 with cited sources.
  - *estimate* means level 4–6.
  - *null+flag* means "to research per unit", with no values yet.
- **Engine:** the owning engine after the Reality/Life split.
- **State:** built, planned or missing.

## Summary

| Chain | Links | Built | Planned | Missing | Its demonstration |
|---|---|---|---|---|---|
| 1. Ecological (sunlight to soil nutrients) | 10 | 1 (human side only) | 6 | 3 | X1 covers links 1.3–1.6 for one crop and people. The return half (1.7–1.10) is outside X1. |
| 2. Human lifecycle (conception to death ledger) | 7 | 2 | 4 | 1 | Nothing yet. The realism checkpoints 1 and 2 exercise 2.4 and 2.7. |
| 3. One cognitive decision | 10 | 4 | 3 | 3 | The hungry pair exercises 3.3–3.5 and 3.9–3.10 with built rows. Its body, environment and resolution are bench stubs. |

**What blocks the chains most:**
- **Chain 1:** no row writes PAR, root-zone soil water, plant uptake or excreta nitrogen. With those missing, the
  nitrogen balance cannot close.
- **Chain 2:** energy expenditure has no growth, thermoregulation or reproduction term.
- **Chain 3:** no row owns turning an intention into a physical outcome. Cross-engine events have no typed contract.

## Chain 1: ecological

Sunlight → soil water and nutrients → plant growth → herbivore consumption → metabolism → movement → excretion →
decomposition → soil nutrients.

| # | Link | Quantity (id, unit) | Mechanism row | Parameters | Engine | State |
|---|---|---|---|---|---|---|
| 1.1 | Sunlight at the place | `place.par` mol/m^2/d | No writer: LIFE-2 says Reality writes it in phases 8, 13 and 16. `realism.optics.light_visibility` (planned, phase 8) has the sun path by date and latitude. `realism.env.daylight` (built) gives only `is_day` from the host's month row. | null+flag | reality | **missing** (CG-1) |
| 1.2a | Rain and air dryness | `place.rain` mm/d, `place.vpd` kPa | No writer (LIFE-2). | null+flag | reality | **missing** (CG-2) |
| 1.2b | Soil water | `world.soil_water` m^3/m^3 | No writer. `realism.terrain.hydrology` (planned) writes `world.groundwater` m3 and `world.drainage`, but not root-zone water. | null+flag | reality | **missing** (CG-2) |
| 1.3 | Soil nutrients available | `world.soil_nutrient_pool` kg (N, P and K; total and plant-available) | `realism.terrain.soils` (planned, ev 4) is the only writer and integrates every flux. A built proxy exists: `realism.eco.soil_fertility`, an index f from 0 to 1 (ev 4, library conf low; DUP-51 open). | null+flag; the proxy is an estimate | reality | planned |
| 1.4 | Plant uptake and growth | Uptake flux: **no id**. `world.plant_state` (record) and `world.vegetation_stock` (record, kg) | `realism.plant.physiology` (planned, ev 2) covers photosynthesis, respiration and water stress. IF-38 (soils → plants) is planned. `realism.terrain.vegetation_stocks` (planned) is in DUP-53 (open). Species data: `realism.anatomy.species_profile` (plant part planned). The X1 crop's data is in realism 2810 (*Saccharum officinarum*: 29 researched, 4 estimate, 14 null). | species data researched or null+flag; the mechanism is null+flag | life | planned. The uptake quantity is **missing** (CG-3). The row's inputs do not yet list the LIFE-2 quantities (CG-4). |
| 1.5 | Herbivore consumption | `world.trophic_flux` kg/a. For people: `body.kcal_in` kcal and `body.pool_contents` kg | Animals: `realism.ecology.food_web` and `realism.ecology.animal_populations` (planned, population level; DUP-50 open). People: `realism.nutrition.eat_meal` (built, ev 4) through IF-36 from `economy.inventory.holdings`. Harvest into inventory is IF-42 (planned). | null+flag (animals); estimate (people) | life | planned (animals); built (people) |
| 1.6 | Metabolism | `body.rmr` kcal/d, `body.expenditure` kcal, `body.heat` W | People: `realism.physiology.rmr` (built, ev 2) and `realism.physiology.energy_expenditure` (built, ev 1). Animals: the `species_profile` RMR column (Kleiber for the horse; built; tested in `realism:independence-horse`). Wild populations: inside `animal_populations` (planned). | researched | life | built (people and the horse); planned (wild animals) |
| 1.7 | Movement | Energy: `body.expenditure` (MET). Displacement: **no id** | The energy cost is built (MET in `energy_expenditure`). `realism.mech.articulated_locomotion` (planned) covers the body. No Reality or Life row moves an organism across places; only the plugin `pirate.align.step` does. | null+flag | reality / life | energy built; position **missing** (CG-5) |
| 1.8 | Excretion | `body.urine` kg/s (water only). Faeces and excreta nitrogen: **no id** | `realism.physiology.urine` is built (ev 2). `realism.waste.sanitation_decomposition` (planned, phase 11; DUP-45 has no decision) routes excreta to a place. There is no animal excretion row. | null+flag | life | urine water built; nutrient excretion **missing** (CG-6) |
| 1.9 | Decomposition | `world.detritus` kg, `world.mineralisation_flux` kg/a | `realism.ecology.decomposition` (planned, ev 2; owner confirmed by Rex 2026-10-31). Burial passes to `realism.terrain.burial_diagenesis` (IF-28). | null+flag | life | planned |
| 1.10 | Back to soil nutrients | `world.mineralisation_flux` into `world.soil_nutrient_pool`. Losses: `world.nutrient_flux` kg/a | IF-39 (decomposition → soils, planned). `realism.terrain.nutrient_transport` (planned) writes fluxes and never the stock. | null+flag | life → reality | planned |

### Nitrogen mass balance: ΔN_soil = inputs + returned − uptake − losses

| Term | Registry id | Writer | State |
|---|---|---|---|
| ΔN_soil | `world.soil_nutrient_pool` (N, P and K in one quantity, unit kg, described as "per area") | `realism.terrain.soils` | planned. No N-only quantity exists, and the area is not in the unit (CG-9). |
| inputs: deposition, biological fixation, manure or fertiliser | none. The ecosystem invariant names atmospheric input as a declared boundary. Manure exists only as an index step in `realism.eco.soil_fertility` (+0.03 f per 10 t/ha). | none | **missing** (CG-7) |
| returned: mineralisation and excreta | `world.mineralisation_flux` kg/a; excreta has no id | `realism.ecology.decomposition`; none for excreta | planned and missing (CG-6) |
| uptake | none | none | **missing** (CG-3) |
| losses: runoff, leaching and erosion | `world.nutrient_flux` kg/a | `realism.terrain.nutrient_transport` | planned |
| losses: denitrification and volatilisation | none | none | **missing** (CG-8) |
| the check itself | an element ledger | `realism.infra.world_conservation` (built, ev 1; mass and element atoms, tolerance 1e-9; integrated in checkpoints 1 and 2). The kernel's `ConservedQuantity` is in kernel src/resolution.ts. | The mechanism exists. No test covers N across soil, plant, animal and detritus. |

### Microbiology dependency check

| Process | Microbial role | Rows | State |
|---|---|---|---|
| Digestion | gut microbiota; fermentation in the hindgut and rumen for herbivores | `realism.anatomy.feed_gate` (built, gut function gates absorption) and `realism.nutrition.absorption` (built, fixed fractions). `realism.metab.flux_digestion_atp` (planned) covers gastric emptying and transit. No row has a microbial term. | **missing** (CG-10) |
| Decomposition | decomposer activity | `realism.ecology.decomposition` (planned) has "microbial activity by temperature, moisture and pH" as a rate. There is no decomposer population. | planned, as a rate only |
| Nutrient cycling | mineralisation and immobilisation, nitrification, denitrification, N fixation | `realism.terrain.soils` lists "microbial activity" as a soil field. No row computes these transformations. | **missing** (CG-7, CG-8) |
| Pathogens | infection | `realism.medicine.disease_course` (built), `realism.medicine.wounds` (built, infection roll), `realism.medicine.transmission_ecology` (planned) | built and planned |

### What X1 exercises

The ROADMAP's X1 loop uses links 1.3 (soils, with hydrology held simple), 1.4 (one food plant), harvest (IF-42), 1.5
for people (IF-36, DUP-21) and 1.6 for people (built).

X1 does not cover 1.1 (PAR), herbivores, 1.7–1.10 or the nitrogen balance.

**Open for the controller:** X1's acceptance (1) says mass closes across soil, plant, inventory and bodies. Mass that
leaves a body as faeces has no destination row (CG-6). So X1 needs either a declared boundary for body outputs or
the waste row. The registry does not choose which (CG-11).

## Chain 2: human lifecycle

Conception → genetic profile → maturation → metabolism and energy accounting → tissue populations → ageing → death
ledger.

| # | Link | Quantity (id, unit) | Mechanism row | Parameters | Engine | State |
|---|---|---|---|---|---|---|
| 2.1 | Conception | `body.conception` (record) | `realism.reproduction.fertility_conception` (planned). It reads `mind.sexual_behaviour` from `cognition.reproduction.behaviour` (planned). | null+flag | life | planned |
| 2.2 | Genetic profile | **No quantity id.** Record 1 is `realism.records.genetic_profile` (a row). `realism.development.maturation` lists the row id as an input. | `realism.genetics.inheritance`, `.recombination` and `.mutation` (planned): one recombined copy per chromosome, never an average | null+flag | life | planned. The quantity id is **missing** (CG-12). |
| 2.3 | Maturation | `body.developmental_state` and `body.neural_development` (records) | `realism.development.maturation` (planned). IF-48 goes to Cognition. It owns hormonal development until an endocrine row exists. DUP-17 freezes all age multipliers. | null+flag | life | planned |
| 2.4 | Metabolism and energy accounting | `body.kcal_in` kcal, `body.rmr` kcal/d, `body.expenditure` kcal, `body.glycogen` g, `body.fat_kg` kg, `body.mass` kg | `realism.nutrition.eat_meal`, `realism.physiology.rmr`, `realism.physiology.energy_expenditure`, `realism.nutrition.energy_store` and `realism.nutrition.body_mass`: all built and integrated (checkpoints 1 and 2) | researched (ev 1–2); eat_meal is an estimate (ev 4) | life | built, with gaps below |
| 2.5 | Tissue populations, dN/dt = B − D | **No quantity ids** for cell births, deaths or viable mass | `realism.cellular.population_state` (planned; outputs empty; its equation is damage, D(t+1) = D + damage − repair), `realism.cellular.death_replacement` and `realism.cellular.stem_cell_pools` (planned). The first implementation is realism 2815 (plants first), not yet landed. | null+flag | life | planned. The B − D equation and its quantities are **missing** (CG-15). |
| 2.6 | Ageing | organ capacity (through population_state) | `realism.cellular.ageing_emergent` (planned; "never a timer") and `realism.genes.ageing_capacity` (planned). Five built age-keyed effects are frozen under DUP-17. | null+flag; the frozen effects are estimates | life | planned |
| 2.7 | Death ledger | `body.crisis` (record); `body.deathrateperhour` 1/h | `realism.infra.crisis_record` (built, ev 6): `declareDeath` throws without a non-survived crisis and a cause. Causes come from `realism.anatomy.crisis_floors`, `realism.nutrition.starvation_limit`, `realism.medicine.disease_course` and `realism.circulation.bleeding_class` (all built). The population count is `society.population.demography` (planned, reads `body.crisis`). The record is `history.record.backend` (planned). | estimate (ev 3–6) | life → society, history | built (individual); planned (population, history) |

### Energy accounting: ΔE_stored = absorbed − expended, with each joule spent once

| Term | Row | State |
|---|---|---|
| absorbed | `realism.nutrition.eat_meal` → `body.kcal_in`. `realism.nutrition.absorption` (`body.fraction_kept`) and `realism.anatomy.feed_gate` (`body.absorbed_nutrients`) cover nutrients. `energy_store` lists its input as "intake". | built. The row does not say whether energy enters as eaten or as absorbed (CG-13). |
| maintenance | `realism.physiology.rmr` (Mifflin-St Jeor; Kleiber for the horse) | built. It enters M through scale = RMR / metabolicHeat(1), so maintenance and activity are one number counted once. |
| activity | `realism.physiology.energy_expenditure` (MET × scale) | built |
| growth | none. `realism.development.maturation` has no energy term. | **missing** (CG-14) |
| thermoregulation | `realism.physiology.heat_balance` (built) moves heat but adds no metabolic cost. Shivering cost exists only in the plugin row `pirate.doc.physiology.thermal_cost` (planned). | **missing** in Life (CG-14) |
| reproduction | none (gestation, lactation) | **missing** (CG-14) |
| ΔE_stored | `realism.nutrition.energy_store`: glycogen first, then fat at 7700 kcal/kg. Invariant: balance = stored + unplaced (1e-3 J). Test: intake − heat − work = stored. | built |
| one joule, once | Two built rows compute the metabolic rate again. `realism.thermo.metabolic_heat` (VO2 = 3.5·MET·mass, recomputed in `atmosphere.bodyGasFlows`) is in no group. `realism.nutri.rmr_mifflin` is in DUP-24, owner approved and restatement pending. | Watch item. No double count has been shown. |

## Chain 3: one cognitive decision

Environment and body state → perception → cognition → intention → physical and social resolution → changed
environment, body, beliefs and memory → next step.

The seed is the hungry pair: `cognition:hungry-pair`, cognition test/bench-world.test.ts (144 epochs, with replay).

| # | Link | Quantity (id, unit) | Mechanism row | Parameters | Engine | State | Hungry pair |
|---|---|---|---|---|---|---|---|
| 3.1 | Environment signal | `world.signal_at_point` (record) | `realism.signal.at_point` (planned; physics only). IF-37 is planned. | null+flag | reality | planned | stub: fixture stock and items |
| 3.2 | Body state to the mind | `body.hunger_signal` 1, `body.pain` 1, `body.capacity_functional` 1 | `realism.nutrition.hunger_fullness` (documented-only, ev 6; DUP-49); `realism.medicine.pain` (built); capacity has no writer (DUP-15) | estimate | life | hunger documented-only; pain built; capacity **missing** (CG-16) | stub: fixture hunger values 0.6 and 0.1 |
| 3.3 | Perception | `body.detectability` 1 → `mind.observation` | `realism.perception.detectability` (planned, ev 2) feeds `cognition.perception.detect` (built, signal detection theory) and `cognition.attention.allocate` (built) | estimate (ev 4) | life → cognition | built in Cognition; d' is a host stub | yes, with stubs |
| 3.4 | Cognition | `mind.belief`, `mind.need_priority`, `mind.goal_progress`, `mind.candidates`, `mind.expected_utility` | `cognition.belief.update`, `.needs.drive`, `.goals.objectives`, `.memory.episodic`, `.decision.generate` and `.decision.evaluate` (built) | estimate (ev 4); evaluate failed validation V2 jointly | cognition | built | yes |
| 3.5 | Intention | `mind.intention` (record); kernel event type `cognition.intention` | `cognition.decision.select` (built; Luce choice with commitment) | estimate | cognition | built | yes |
| 3.6 | Physical resolution | the attempt's outcome: **no id** | IF-43 says Reality and Life decide success. `realism.contact.contact_event` (planned) covers contact and IF-3 makes wounds. `realism.mech.articulated_locomotion` is planned. Eating is resolved through IF-36 (built). No row resolves an intention into a physical outcome in general. `shared.action.kind` (planned) is only the vocabulary. | null+flag | reality / life | **missing** (CG-16) | stub: the bench's `world.resolve` (fixture rules, `fightProbability`) |
| 3.7 | Social resolution | `economy.trade.trade` (built). The edge IF-18 is planned. IF-43 (law), IF-46 (affordances) and the communication rows are planned. | as listed | estimate / null+flag | economy, government, society | trade built; the edges planned (IF-26, IF-27 already recorded) | stub: ask, give and trade by fixture |
| 3.8 | Changed environment and body | `economy.inventory.holdings` (built), `body.kcal_in` through `eat_meal` (built) | as listed | as listed | economy, life | built, but not joined to Cognition | stub: fixture hunger falls 0.6 → 0.35 |
| 3.9 | Changed beliefs and memory | `mind.prediction_error`, `mind.attribution`, `mind.episode`, `mind.belief` | `cognition.learning.outcome`, `.learning.attribution`, `.memory.episodic` and `.belief.update` (built) | estimate | cognition | built | yes |
| 3.10 | Next step | the kernel clock and event bus | kernel src/scheduler.ts, runner.ts and events.ts (built; no registry row) | none | kernel | built | yes (144 epochs, replay) |

## The seven structures

| Structure | What the registry has | Gaps |
|---|---|---|
| **Spatial compartments** | Quantity scopes `place`, `world`, `body` and `mind`. `realism.gas.room_box` (built) is the air compartment. `shared.contract.terrain_resolution` (planned) refines cells on demand. | No row defines the place or cell record itself. `world.*` stocks described "per area" carry unit kg (CG-9). |
| **Shared material ledger** | `realism.infra.world_conservation` (built, ev 1): mass and element atoms. The substrate ledger is named in IF-31, IF-34 and IF-36. `economy.inventory.holdings` (built, goods). `settlement.ledger.pay` (built, money). The kernel's `ConservedQuantity` (kernel src/resolution.ts; test/resolution.test.ts). | The kernel conservation and resolution service has no registry row (CG-17). No cross-engine test covers N or soil mass. Harvest (IF-42) and decomposition return (IF-39) are planned. |
| **Species configuration without false equivalence** | `realism.anatomy.species_profile` (LIFE-3): one record per species, every value labelled researched, estimate or fiction, or null with a flag; no species name in src/. DUP-23 keeps species parameters apart from current physiology. People use Mifflin-St Jeor; the horse uses Kleiber (`realism:independence-horse`). | The plant part is planned, with data landing (realism 2808–2810). `realism.physiology.rmr` falls back to 1 kcal/kg/h when height, age or sex is missing. That is a cross-species default (see uncertainty). |
| **Lifecycle transitions** | conception (planned) → maturation (planned; "ends where ageing begins") → adult `realism.development.trait_change` (planned) → `realism.cellular.ageing_emergent` (planned) → crisis and death (built) → `society.population.demography` (planned) | Only death is built. Birth has no built path into demography. The genetic profile has no quantity (CG-12). |
| **Adaptive resolution** | PLATFORM §9. Kernel `ResolutionService` with `switchTo` and conserved quantities within a tolerance (built). `shared.contract.terrain_resolution` (planned). Knowledge rows at summary resolution (planned). Regional subdivision in `population_state` (refinement B). `realism:epidemic-vs-individuals` (built: the aggregate matches 1,000 individual cases). | The kernel service has no row (CG-17). No chain-1 or chain-2 row declares its resolutions yet. |
| **Uncertainty representation (no silent constants)** | Evidence level on every row. The LIFE-3 rule: every value labelled, or null with a flag. Government: legitimacy is null, never 0. Schema 4 adds `vv.record.numerical.sensitivity`. | `sensitivity` is null on all 579 rows. Built chain rows carry constants with only a row-level source: rmr's fallback; energy_store's fat floor (3 kg) and glycogen cap (400 g); starvation_limit's 60 % of start mass; soil_fertility's +0.03, +0.02, −0.02 and ×0.5 (conf low). No per-value label is visible in the registry for these. The owners hold the answer. |
| **Cross-engine event contracts** | `KernelEvent {id, t, source, type, payload, cause}` (kernel src/events.ts, built). The typed records are `body.crisis`, `body.conception`, `realism.contact.contact_event`, `economy.shortage.event` and `mind.intention`. | The payload is `unknown`. No registry or kernel.json lists event types with their payload schema, producer and consumers. kernel.json ports declare quantities only (CG-18). |

## Gaps recorded (integration_gaps.interface_gaps)

| Id | Gap | Holder (to propose; the registry decides nothing) |
|---|---|---|
| CG-1 | `place.par` has no writer | Reality (LIFE-2: phases 8, 13, 16) |
| CG-2 | `place.rain`, `place.vpd` and `world.soil_water` have no writer | Reality |
| CG-3 | No plant uptake flux quantity (water, N, P, K) | Life with Reality (substrate ledger) |
| CG-4 | `realism.plant.physiology` inputs omit the LIFE-2 quantities | Life |
| CG-5 | No row moves an organism between places | Reality / Life |
| CG-6 | No excreta mass or nutrient quantity (people or animals); DUP-45 is undecided | Life |
| CG-7 | No nitrogen inputs (deposition, fixation, manure as mass) | Reality / Life |
| CG-8 | No gaseous nitrogen losses (denitrification, volatilisation) | Reality / Life |
| CG-9 | Soil pools and fluxes join N, P and K in one kg quantity with no per-area unit | Reality |
| CG-10 | No gut microbial digestion term | Life |
| CG-11 | X1 conservation has no destination for body outputs | controller / Rex |
| CG-12 | The genetic profile has no quantity id | Life |
| CG-13 | energy_store's input is "intake": eaten or absorbed is unstated | Life |
| CG-14 | Expenditure has no growth, thermoregulation or reproduction term | Life |
| CG-15 | Tissue populations have no B − D equation or quantities | Life (realism 2815) |
| CG-16 | No row resolves an intention into a physical outcome; capacity has no writer (DUP-15) | Reality / Life, with the controller |
| CG-17 | The kernel conservation and resolution service has no registry row | Kernel |
| CG-18 | Events have no typed contract (type, payload, producer, consumers) | Kernel / controller |
