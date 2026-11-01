# CHAINS: causal-chain completeness audit

*Registry keeper, 2026-11-01, at Rex's direction (relayed by the controller), revised the same day for Rex's
addendum. **Approved by Rex 2026-11-01: integration first (see "Approved").** A targeted audit of three chains and seven structures, not a broad review.*

**Sources.** Only committed files were used:
- rs-platform `registry/mechanisms.json`, `quantities.json` and `graph.json` at 8fcfdf8;
- kernel a3c4314, realism 75e4fc2 and cognition 2106314.

Every link cites a registry row. Nothing here is a new rule. Every gap is recorded in `graph.json` →
`integration_gaps.interface_gaps` (CG-1 to CG-25; IF-26 and IF-27 were already there).

**Rex's completeness rule (addendum 2026-11-01).** A link is complete only if three things hold:
- one mechanism's output is a valid input to the next;
- their units, timescales and state ownership are compatible;
- where two engines describe one physical transfer, it is one transfer. For example, plant nitrogen uptake and soil
  nitrogen loss are one quantity, never two calculations.

**Failure types (Rex):**
- **Missing mechanism:** no equation or no implementation. This audit marks which:
  - *missing (no equation)* means no row states how the quantity is computed: work for **mathematics**.
  - *missing (not implemented)* means a row states the formulation, but nothing is built: work for **implementation**.
- **Broken connection:** both sides exist, but they do not exchange the required quantity. This is work for
  **integration**.
- **Invalid coupling:** they exchange it, but units, assumptions, timescales or conservation conflict, or one
  transfer is calculated twice. This is also work for **integration**.

**Other columns:**
- **Quantity:** the registry id and its unit.
- **Parameters:**
  - *researched* means evidence level 1–3 with cited sources.
  - *estimate* means level 4–6.
  - *null+flag* means "to research per unit", with no values yet.
- **State:** built, planned or missing.

## Result: what the gaps call for

| Investment | What it fixes | Count |
|---|---|---|
| **Mathematics** (missing, no equation) | CG-1, 2, 5, 6, 7, 8, 10, 11, 14, 15, 16, 18 | 12 gaps |
| **Implementation** (missing, not implemented) | 10 planned chain links whose rows state a formulation (1.3, 1.5 animals, 1.6 wild animals, 1.9, 1.10, 2.1, 2.3, 2.6, 2.7 population, 3.1); CG-24 and CG-25 (Cognition's two Life inputs are host stubs) | 10 links + 2 gaps |
| **Integration: broken connection** | CG-3, 4, 12, 17, 23; IF-26, IF-27 | 7 gaps |
| **Integration: invalid coupling** | CG-9, 19, 20, 21, 22; CG-13 if the owner confirms it | 5 gaps (+1 to confirm) |

**Readings:**
- **Chain 1** is mostly a mathematics problem. Its missing pieces are equations nobody has written: PAR, soil water,
  nitrogen inputs and gaseous losses, excretion, and microbial digestion. It also has the worst couplings:
  - the built soil-fertility index drains soil separately from plant uptake (Rex's own example);
  - plant biomass is held in two quantities;
  - Economy goods are unitless while Life ingests kilograms.
- **Chain 2** is mathematics for the energy terms (growth, thermoregulation, reproduction) and for tissue
  populations, and implementation for the rest.
- **Chain 3** is integration and one mathematics gap. Everything from perception to intention is built. What's
  missing is the resolution of an intention into an outcome (CG-16) and the connections out of `mind.intention`
  (IF-26, IF-27).

The choice of next investment is Rex's. This table is the evidence for it.

## Approved: integration first (Rex, 2026-11-01)

**Status: approved.** Rex approved the integration-first investment order. No new top-level engine and no duplicate
mechanism may be introduced.

**The rule (PLATFORM §7a, controller 2026-11-01):** one transfer per physical flow. Δsource = −q and
Δdestination = +q happen in one transaction, and losses are accounted separately. This holds for nutrients, water,
mass, energy and money alike.

**The order:**
1. **Priority 1: close the five invalid couplings.** For each shared physical flow, establish one authoritative
   quantity and one conservation-preserving transfer. That means eliminating the duplicate biomass and soil-fertility
   calculations, resolving the unit mismatches, aligning the timescales, and separating N, P and K into their own
   quantities.
2. **Priority 2: close the broken connections.** Intention-to-outcome resolution comes first, then the physical
   resource, nutrition and Cognition-to-Economy interfaces.
3. **Priority 3: write Chain 1's missing ecological equations,** then the remaining lifecycle and decision-chain
   gaps. These are research units now (web tools), with implementation later. Independent mathematical research may
   run in parallel, but implementation respects unresolved dependencies and registry ownership.

**Testing:** targeted tests for each corrected coupling or interface. Larger integrated demonstrations run at
milestones, not after every minor change.

**Evidence required to close a gap:** the responsible unit; the equation (the transfer, with Δsource = −q and
Δdestination = +q); the unit; the authoritative owner; and the verification result (a targeted test at a commit).
The registry keeper re-audits the commit and fills the closure record below.

### Assignments

| Pri | Gap | Failure type | What closes it | Owner | Agreeing |
|---|---|---|---|---|---|
| 1 | CG-20 | invalid coupling | One soil-nutrient transfer: harvest and uptake leave the soil pool once, so the built `realism.eco.soil_fertility` drain stops being a second calculation (DUP-51, DUP-53) | Reality | Life |
| 1 | CG-21 | invalid coupling | One authoritative plant biomass quantity (`world.plant_state` vs `world.vegetation_stock`), with the other a declared aggregate (DUP-53) | Life | Reality |
| 1 | CG-19 | invalid coupling | Goods carry mass (kg per unit, owned once by Economy) and name a Life food id; energy stays Life's (food.kcalPerKg, E = m · e_food), so IF-36 and IF-42 transfer kg (amended 2026-11-01, Economy and Life agreed) | Economy | Life |
| 1 | CG-9 | invalid coupling | N, P and K as separate quantities; area in the unit (or per-cell scope declared) | Reality | Life |
| 1 | CG-22 | invalid coupling | A stated rule for integrating fast fluxes into the soil and water stocks; aligned timescales | Reality | Life, Kernel (scheduler) |
| 1 | CG-13 | invalid coupling (to confirm) | Confirm whether energy enters `energy_store` as eaten or as absorbed; fix if it is counted twice or lost | Life | — |
| 2 | CG-16 | missing (no equation), prioritised by Rex | Intention-to-outcome resolution. IF-43 puts success with Reality and Life. | Cognition (lead, as the controller assigned) | Reality, Life, Economy |
| 2 | IF-26 | broken connection | `mind.intention` to Economy demand | Cognition | Economy |
| 2 | IF-27 | broken connection | `mind.intention` to labour offers (LabourSupply) | Cognition | Economy, Settlement |
| 2 | CG-3 | broken connection | The plant uptake quantity (water, N, P, K), one transfer from the soil pool | Life | Reality |
| 2 | CG-4 (**closed**) | broken connection | `realism.plant.physiology` reads the LIFE-2 quantities | Life | Reality |
| 2 | CG-12 (**closed**) | broken connection | A quantity id for the genetic profile | Life | — |
| 2 | CG-23 | broken connection | Population and individual consumption joined across resolutions | Life | Economy |
| 2 | CG-17 (**closed**) | broken connection | A registry row for the kernel's `ConservedQuantity` and `ResolutionService` | Kernel | registry keeper |
| 2 | CG-18 | missing (no equation), assigned by the controller | Typed event contracts (type, payload, producer, consumers) | Kernel | controller, all engines |
| 3 | CG-1, 2, 5, 6, 7, 8, 10, 11, 14, 15 | missing (no equation) | Research units (web tools) by each holder; implementation later | holders in the gap table | — |

### Controller decisions after approval (2026-11-01)

- **§7a transfer service: go, and built.** The kernel's `transfer()` (row `kernel.transfer`, kernel unit 3006, a7459c8; transfer.test.ts 20/20, registry re-audit) does the debit,
  credit, record and check inside `kernel.transaction`. It is bookkeeping only, with no formula and no unit conversion.
  Every engine's flows go through it, and the CG-19, CG-20 and CG-21 fixes adopt it. After kernel v0.1.0 the ledgers
  migrate in paired units: Economy's goods stock ledger (`adjust`, `economy.stock_changes`; takeMass and addMass first)
  and Settlement's money ledger (CONTRACTS §3). Economy has no money ledger.
  **First migration (2026-11-01):** Economy's goods ledger `economy.goods` (economy 5068, 1e79dbe, on kernel v0.1.1): buy and sell legs and shipment
  dispatch and arrival go through `transfer()` (account = inventory id or `shipment:<id>`; quantity = good id; unit count). Production, spoilage,
  consumption and the mass commands keep `adjust`, since they are not transfers between two holders. Registry rerun: goods-ledger T1–T6 8/8 at
  economy 85a173e. **Money and goods in one transfer (CONTRACTS §20, 2026-11-01):** each buy and sell is one `transfer()` with a
  money leg (`settlement.money`) and a goods leg (`economy.goods`) under process `economy.trade.trade`; a refusal in either leg rolls both back
  (settlement 898243b, pirate 1ae7e99, economy 20e53a7; registry reruns: economy trade-batch + goods-ledger 14/14 at 1b29ae8, settlement
  transfer-batch 10/10). No leg refuses on balance: whether an account may go negative is Rex's (Q19, ECON-26).
- **CG-18 events contract: yes.** `registry/events.json` is owned by the registry keeper. Its first rows are `shared.action.outcome` (CG-16) and `settlement.post_filled` (IF-27). Since 2026-11-01 it holds 36 bus types from kernel 3011's inventory; `settlement.post_filled` is retired (the bus type is `postFilled`), and lists are typed `of: 'record'` (kernel 5067), so there are no event warnings. The kernel's checker landed (kernel 3007, c171702): the belt check passes with one advisory warning, because `stimuli` has no element type yet. The kernel's
  `checkEventContracts` (unit 3007) warns, never fails, until the file is populated. The first unit is the event inventory.

### In progress

| Gap | Unit | Equation | Unit of q | Owner | Verification planned |
|---|---|---|---|---|---|
| CG-13 | {CG13} (Life, with Reality to number) | kept = eaten × absorbedFraction(energy) → intake; Δfood = −E_eaten, Δbody = +E_kept, Δwaste = +(E_eaten − E_kept) | J | Life | realism test/nutrition.test.ts "energy enters absorbed (CG-13)" |
| CG-21 | realism 3015 (Life's {CG21}; needs 2815 and 3001) | `world.plant_state` is the only biomass store; `world.vegetation_stock` = Σ biomass over records in a region (a derived read, never integrated); coarsen/refine conserves to 1e-12 | kg | Life (Reality agrees) | the unit's coarsen/refine conservation test |
| CG-3 | realism 3015 (needs 2815 and 3001) | Δsoil_avail_X = −q, Δplant_X = +q per element, one transaction; ids `world.plant_uptake_water`, `_n`, `_p`, `_k` (planned) | kg per plant record per step | Life (Reality agrees) | the unit's transfer test |
| CG-23 | Life phase 19 | trophic_flux = Σ kg eaten by individually resolved consumers + cohort consumption of population-resolved ones, never both for one consumer; E = m × e_food | kg | Life (Economy agrees) | with phase 19 |
| CG-9 | realism 3001 (needs 3000); ports in realism 3021 (needs 3001: process `realism.ecology.soils` writes `world.soil_{n,p,k}` and `stock.f`) | `world.soil_nutrient_pool` split into `world.soil_n`, `world.soil_p`, `world.soil_k` (kg per cell; the cell carries areaM2); fluxes `world.mineralisation_flux_{n,p,k}` and `world.nutrient_flux_{n,p,k}` (kg/d per cell). The old ids are retired as aliases (registry, 2026-11-01). | kg; kg/d | Reality (Life agrees) | realism 3001's tests |
| CG-20 | realism 3000 (sourced removal per tonne and manure N, P, K), then 3001 | `transferNutrient`: pool −q, account +q, one trace record. Harvest is one transfer of yield × removal, and nothing from the soil when `uptakeByPlant` (the plant's uptake already moved it). f is a derived Liebig view (`stock.f`). | kg | Reality (Life agrees) | 3001: `one transfer`, `no clamp`, `uptake once` |
| CG-22 | realism 3001 (needs kernel 3006; accepted by Reality 2026-11-01, no buffer of any kind) | A pool changes only by transfer through kernel `transfer()` at the flux's own step; formation once per world; pedogenesis per year, also by transfer (gears/soil-integration.md). The rows' timescale text is updated in the registry. | — | Reality (Life, Kernel agree) | 3001: `integration rule` (daily vs hourly, 1e-9) |
| CG-16, IF-26, IF-27 | proposals with Reality, Life, Economy and Settlement (Cognition leads) | contract `shared.action.resolution` (planned): `resolve(intention, truth) → {status, stimuli, transfers}`, one `kernel.transaction` per intention with its `kernel.transfer`s and the outcome event (cause = the intention id) | per transfer | Cognition (lead); agreed by Reality, Life and Economy, Settlement agreed IF-27 (2026-11-01). Settlement 3047 landed (7e49d3c): `hire` takes `cause?` and emits `settlement.post_filled` then `shared.action.outcome`; U24 6/6 on the registry keeper's rerun. That verifies Settlement's resolver part. Cognition's `terms?` landed at f53f16d (intention-terms 4/4). IF-27 still needs two pieces. (1) The LabourSupply provider, which the controller assigned to Life: it reads the latest `work` or `refuse_work` intention and answers the pure queries `hours(person, role, day)` and `reservationWage?`. It changes nothing and passes no cause. (2) The host's `hire` command, which carries the intention id as `cause` through Settlement's `apply`: the contract row `shared.host.work_resolution` (controller). It's built in the kernel harness by the Kernel keeper after v0.1.0, and specified by the History keeper in X1; in a game, the game adapter plays the same role. **Built:** kernel 5006 at f452432 (`harness/work-resolution.ts`, after v0.1.0 ac08916); work-resolution 10/10 on the registry keeper's rerun. IF-27 now waits only on Life's provider. The host never decides the wage. Specified in history DESIGN §3.8 (0c53036); X1 seam S6's gate checks H1–H4. **Accepted (controller ruling, a declared default for Rex to overrule):** Life's `hours(person, role, day) > 0` (availability included) **and** a vacant post for the intention's `target`: a Settlement role id or post id that the mind knows through its affordances (IF-46), per the controller's role ruling, option (a). A role resolves to the first vacant post of that role by stable id; a post id resolves directly. With no target, the intention fails with reason "no target". `terms` stays numbers only. There is no wage comparison until Rex decides ECON-24. A rejection resolves to `failed`, with the reason among the stimuli. Economy's wage-quote floor stays with Rex (ECON-24); the outcome event is `shared.action.outcome` (CG-18). Contract text: cognition DESIGN §2.4 (1e229d1, unit 3043; d6abcdc, unit 3046). C-Q25 decided by the controller: a refusal is `failed`. C-Q26 (headcount, CG-23) goes to Life | resolver units: Reality after 3020; Life after kernel 3006 + economy 2999; Economy 3045 after economy 3010; Settlement 3047 |

### Closure record

| Gap | Unit | Equation | Unit of q | Owner | Verification | Re-audit |
|---|---|---|---|---|---|---|
| CG-17 | none: the code already existed; registered by the registry keeper from the Kernel keeper's proposal | refine is accepted only if every declared conserved quantity matches within its tolerance; coarsen installs the exact aggregate; `transaction` restores every participant on failure | owner-declared per quantity | Kernel | `test/resolution.test.ts` and `test/transaction.test.ts`: 23/23 at kernel 309a317 (code unchanged since a3c4314) | registry keeper 2026-11-01. Rows `kernel.resolution.handoff` and `kernel.transaction` are built; integrated: no (no registered consumer yet) |
| CG-4 | registry edit (registry keeper, from the Life keeper's decision) | — (an input list) | — | Life | `realism.plant.physiology` reads the eleven LIFE-2 ids plus `place.t` and `air.ppm_gases`; registry rebuild and belt check exit 0 | registry keeper 2026-11-01. Realism 2815's environment interface reads them. |
| CG-12 | registry edit (registry keeper, from the Life keeper's decision) | — (a record id) | record | Life | `organism.genetic_profile` (scope `organism`, writer `realism.records.genetic_profile`, planned), read by maturation; registry rebuild and belt check exit 0 | registry keeper 2026-11-01 |
| CG-19 | economy 2999 (da23966), 3010 (2fef178); 3045 (4192e27) for IF-26 | `takeMass`: Δinventory = −q with q = units × `Good.weight`; `eatMeal({food, kg: q})`: Δbody = +q, in one kernel transaction; energy stays Life's (E = m · `food.kcalPerKg`) | kg (`economy.mass_taken`; `economy.good_mass_per_unit` kg/count) | Economy (Life agrees) | economy `test/mass.test.ts` M1–M9, `test/food-to-body.test.ts` F1–F5 (exact −q/+q, kept + waste = q·kcalPerKg to 1e-9, a forced failure rolls back both engines), `test/intention.test.ts`: 28/28 at economy 4192e27 | registry keeper 2026-11-01. Quantities built; ports declared at economy 730e54f (unit 5049), belt check exit 0 |

## Chain 1: ecological

Sunlight → soil water and nutrients → plant growth → herbivore consumption → metabolism → movement → excretion →
decomposition → soil nutrients.

| # | Link | Quantity (id, unit) | Mechanism row | Parameters | Engine | State | Failure type |
|---|---|---|---|---|---|---|---|
| 1.1 | Sunlight at the place | `place.par` mol/m^2/d | No writer (LIFE-2: Reality, phases 8, 13 and 16). `realism.optics.light_visibility` (planned) has the sun path but no PAR. `realism.env.daylight` (built) gives only `is_day` from the host's month row. | null+flag | reality | missing | missing (no equation): CG-1 |
| 1.2 | Rain, air dryness, soil water | `place.rain` mm/d, `place.vpd` kPa, `world.soil_water` m^3/m^3 | No writer. `realism.terrain.hydrology` (planned) writes `world.groundwater` m3 and `world.drainage` only. | null+flag | reality | missing | missing (no equation): CG-2 |
| 1.3 | Soil nutrients | `world.soil_nutrient_pool` kg (N, P and K in one quantity, "per area") | `realism.terrain.soils` (planned, sole writer). The built proxy `realism.eco.soil_fertility` is an index f from 0 to 1 (DUP-51 open). | null+flag; the proxy is an estimate | reality | planned | missing (not implemented); invalid coupling: CG-9, CG-20, CG-22 |
| 1.4 | Plant uptake and growth | uptake: **no id**; `world.plant_state` (record); `world.vegetation_stock` (record, kg) | `realism.plant.physiology` (planned); `realism.terrain.vegetation_stocks` (planned); IF-38 planned. Species data: realism 2810 (*Saccharum officinarum*: 29 researched, 4 estimate, 14 null). | species data researched or null+flag | life | planned | broken connection: CG-3, CG-4; invalid coupling: CG-21 |
| 1.5 | Herbivore consumption | animals: `world.trophic_flux` kg/a; people: `body.kcal_in` kcal, `body.pool_contents` kg | `realism.ecology.food_web` and `.animal_populations` (planned; DUP-50 open). People: `realism.nutrition.eat_meal` (built) through IF-36 from `economy.inventory.holdings` (built). Harvest is IF-42 (planned). | null+flag / estimate | life | planned (animals), built (people) | missing (not implemented) for animals; invalid coupling: CG-19; broken connection: CG-23 |
| 1.6 | Metabolism | `body.rmr` kcal/d, `body.expenditure` kcal, `body.heat` W | `realism.physiology.rmr`, `.energy_expenditure` (built). Horse: `species_profile` Kleiber (built). Wild animals: inside `animal_populations` (planned). | researched | life | built (people, horse) | complete for people and the horse; missing (not implemented) for wild animals |
| 1.7 | Movement | energy: `body.expenditure`; displacement: **no id** | MET cost built. `realism.mech.articulated_locomotion` (planned). Only the plugin `pirate.align.step` moves anything. | null+flag | reality / life | energy built | missing (no equation): CG-5 |
| 1.8 | Excretion | `body.urine` kg/s (water); excreta mass and N: **no id** | `realism.physiology.urine` (built). `realism.waste.sanitation_decomposition` (planned, no outputs; DUP-45 undecided). | null+flag | life | urine built | missing (no equation): CG-6 |
| 1.9 | Decomposition | `world.detritus` kg, `world.mineralisation_flux` kg/a | `realism.ecology.decomposition` (planned); burial goes through IF-28 | null+flag | life | planned | missing (not implemented) |
| 1.10 | Back to soil | `world.mineralisation_flux` → `world.soil_nutrient_pool`; losses `world.nutrient_flux` kg/a | IF-39 (planned); `realism.terrain.nutrient_transport` (planned; fluxes only) | null+flag | life → reality | planned | missing (not implemented); invalid coupling: CG-9, CG-22 |

### Coupling check (units, timescales, ownership, one transfer)

| Pair | Finding | Type |
|---|---|---|
| soils ↔ plant (1.3 → 1.4) | **One transfer, two calculations.** The built `realism.eco.soil_fertility` drains soil on harvest (f −= crop demand). That is independent of any plant uptake, which has no quantity at all. This is Rex's example: uptake and soil loss must be one quantity. | invalid coupling (CG-20); broken connection (CG-3) |
| soils ↔ fluxes (1.3, 1.10) | The pool is kg "per area" with no area in the unit; the fluxes are kg/a. N, P and K share one quantity, so the N balance cannot be read off it. | invalid coupling (CG-9) |
| soils ↔ fast processes | The timescale of `realism.terrain.soils` and `.hydrology` is "generation once per world; slow change per year". The plant uptake and mineralisation they integrate run on the fast scheduler ("fast processes often"). The registry states no rule for integrating the fast fluxes into a yearly stock. | invalid coupling (CG-22) |
| plant biomass (1.4) | Two quantities for one stock: `world.plant_state` (plant.physiology, fast) and `world.vegetation_stock` (vegetation_stocks, yearly), with no declared aggregation (DUP-53 open). | invalid coupling (CG-21) |
| plant → inventory → body (IF-42, IF-36) | IF-42 and IF-36 require mass ("harvested mass = biomass removed"; "hands over mass"). As registered, `economy.material.produce`, `.inventory.holdings` and `.consumption.demand` count goods unitless, while `eat_meal` takes kg and kcal. No row converts a good to mass or energy. | invalid coupling (CG-19) |
| animal ↔ person consumption (1.5) | Populations consume biomass in kg/a (`trophic_flux`); individuals eat kcal per meal. No aggregation joins the two resolutions. | broken connection (CG-23) |
| `plant.physiology` inputs | The row reads soil, groundwater and wind but not the LIFE-2 quantities it needs (PAR, VPD, rain, soil water). | broken connection (CG-4) |

### Nitrogen mass balance: ΔN_soil = inputs + returned − uptake − losses

| Term | Registry id | Writer | Type |
|---|---|---|---|
| ΔN_soil | `world.soil_nutrient_pool` (N, P and K together) | `realism.terrain.soils` (planned) | invalid coupling (CG-9) |
| inputs: deposition, fixation, manure as mass | none (manure is only an index step in `eco.soil_fertility`) | none | missing (no equation): CG-7 |
| returned | `world.mineralisation_flux` kg/a; excreta: none | decomposition (planned); none | missing (not implemented); missing (no equation): CG-6 |
| uptake | none | none | broken connection: CG-3 (and CG-20, the duplicate drain) |
| losses: runoff, leaching, erosion | `world.nutrient_flux` kg/a | `realism.terrain.nutrient_transport` (planned) | missing (not implemented) |
| losses: denitrification, volatilisation | none | none | missing (no equation): CG-8 |
| the check | element ledger | `realism.infra.world_conservation` (built, element atoms, tolerance 1e-9) | Built. No test covers N across soil, plant, animal and detritus. |

### Microbiology dependency check

| Process | Rows | Type |
|---|---|---|
| Digestion: gut microbiota, hindgut and rumen fermentation | `realism.anatomy.feed_gate`, `realism.nutrition.absorption` (built, fixed fractions); `realism.metab.flux_digestion_atp` (planned); no microbial term | missing (no equation): CG-10 |
| Decomposition | `realism.ecology.decomposition` (planned): microbial activity is a rate by temperature, moisture and pH; there is no decomposer population | missing (not implemented) |
| Nutrient cycling: mineralisation and immobilisation, nitrification, denitrification, fixation | `realism.terrain.soils` lists "microbial activity" as a field; no row computes the transformations | missing (no equation): CG-7, CG-8 |
| Pathogens | `realism.medicine.disease_course`, `.wounds` (built); `.transmission_ecology` (planned) | built / planned |

### What X1 exercises

X1 uses links 1.3 (hydrology held simple), 1.4 (one crop), IF-42, 1.5 for people (IF-36) and 1.6 for people.

It meets three of the invalid couplings head on: CG-19 (unitless goods against kg), CG-20 (the duplicate soil drain)
and CG-21 (two biomass quantities). Its acceptance (1), mass closing across soil, plant, inventory and bodies, cannot
pass until those are resolved.

**Open for the controller or Rex (CG-11):** mass leaving a body as faeces has no destination row.

## Chain 2: human lifecycle

Conception → genetic profile → maturation → metabolism and energy accounting → tissue populations → ageing → death
ledger.

| # | Link | Quantity (id, unit) | Mechanism row | Parameters | Engine | State | Failure type |
|---|---|---|---|---|---|---|---|
| 2.1 | Conception | `body.conception` (record) | `realism.reproduction.fertility_conception` (planned); reads `mind.sexual_behaviour` (planned) | null+flag | life | planned | missing (not implemented) |
| 2.2 | Genetic profile | **no quantity id**; `realism.development.maturation` lists the row `realism.records.genetic_profile` as its input | `realism.genetics.inheritance`, `.recombination`, `.mutation` (planned) | null+flag | life | planned | broken connection: CG-12 |
| 2.3 | Maturation | `body.developmental_state`, `body.neural_development` (records) | `realism.development.maturation` (planned; IF-48; DUP-17 freeze) | null+flag | life | planned | missing (not implemented) |
| 2.4 | Metabolism and energy | `body.kcal_in` kcal, `body.rmr` kcal/d, `body.expenditure` kcal, `body.glycogen` g, `body.fat_kg` kg | `eat_meal`, `rmr`, `energy_expenditure`, `energy_store`, `body_mass` (built, integrated in checkpoints 1 and 2) | researched (ev 1–2); eat_meal is an estimate | life | built | missing (no equation): CG-14; invalid coupling to confirm: CG-13 |
| 2.5 | Tissue populations, dN/dt = B − D | **no ids** for births, deaths or viable mass | `realism.cellular.population_state` (planned; empty outputs; equation is damage only), `.death_replacement`, `.stem_cell_pools` (planned); realism 2815 has not landed | null+flag | life | planned | missing (no equation): CG-15 |
| 2.6 | Ageing | organ capacity through population_state | `realism.cellular.ageing_emergent`, `realism.genes.ageing_capacity` (planned); five age effects frozen under DUP-17 | null+flag | life | planned | missing (not implemented) |
| 2.7 | Death ledger | `body.crisis` (record) | `realism.infra.crisis_record` (built; no death without a crisis and a cause), fed by `crisis_floors`, `starvation_limit`, `disease_course`, `bleeding_class` (built). `society.population.demography` and `history.record.backend` (planned). | estimate | life → society, history | built (individual) | complete for individuals; missing (not implemented) for population and history |

### Energy accounting: ΔE_stored = absorbed − expended, each joule spent once

| Term | Row | Type |
|---|---|---|
| absorbed | `eat_meal` → `body.kcal_in`. Absorption fractions (`body.fraction_kept`) and `feed_gate` cover nutrients. `energy_store`'s input is "intake". | invalid coupling **to confirm** (CG-13). If energy enters as eaten while absorption is applied elsewhere, either the unabsorbed energy is lost from the ledger or absorption is counted twice. The owner holds the answer. |
| maintenance and activity | `rmr` enters M through scale = RMR / metabolicHeat(1); MET sets the activity. One number, counted once. Units are consistent: kcal/d → W → kcal. | complete |
| growth | none | missing (no equation): CG-14 |
| thermoregulation | `heat_balance` (built) moves heat but adds no metabolic cost. Only the plugin `pirate.doc.physiology.thermal_cost` (planned) has one. | missing (no equation): CG-14 |
| reproduction | none (gestation, lactation) | missing (no equation): CG-14 |
| ΔE_stored | `energy_store` (daily): balance = stored + unplaced (1e-3 J). The test checks intake − heat − work = stored. Expenditure accumulates each step and closes daily; the timescales are compatible. | complete |
| one joule, once | `realism.thermo.metabolic_heat` (built) recomputes VO2 = 3.5·MET·mass in `atmosphere.bodyGasFlows`, a second calculation of the same metabolic rate (in no group). `realism.nutri.rmr_mifflin` is in DUP-24 (restatement pending). | watch item: no double count shown, but it's a duplicate calculation of one rate |

## Chain 3: one cognitive decision

Environment and body state → perception → cognition → intention → physical and social resolution → changed
environment, body, beliefs and memory → next step.

The seed is the hungry pair: `cognition:hungry-pair`, cognition test/bench-world.test.ts (144 epochs, with replay).

| # | Link | Quantity (id, unit) | Mechanism row | Engine | State | Hungry pair | Failure type |
|---|---|---|---|---|---|---|---|
| 3.1 | Environment signal | `world.signal_at_point` (record) | `realism.signal.at_point` (planned); IF-37 planned | reality | planned | stub (fixture stock and items) | missing (not implemented) |
| 3.2 | Body state to the mind | `body.hunger_signal` 1, `body.pain` 1, `body.capacity_functional` 1 | `realism.nutrition.hunger_fullness` (documented-only); `realism.medicine.pain` (built); capacity has no writer (DUP-15) | life | partial | stub (hunger 0.6 / 0.1) | missing (not implemented): CG-24; missing (no equation): CG-16 for capacity |
| 3.3 | Perception | `body.detectability` 1 → `mind.observation` | `realism.perception.detectability` (planned) → `cognition.perception.detect`, `.attention.allocate` (built) | life → cognition | Cognition built; d' is a host stub | yes, with stubs | missing (not implemented): CG-25 |
| 3.4 | Cognition | `mind.belief`, `.need_priority`, `.goal_progress`, `.candidates`, `.expected_utility` | `cognition.belief.update`, `.needs.drive`, `.goals.objectives`, `.memory.episodic`, `.decision.generate`, `.decision.evaluate` (built) | cognition | built | yes | complete (evaluate failed validation V2; that is validation, not coupling) |
| 3.5 | Intention | `mind.intention` (record); kernel event `cognition.intention` | `cognition.decision.select` (built) | cognition | built | yes | complete inside Cognition |
| 3.6 | Physical resolution | outcome: **no id** | IF-43 says Reality and Life decide success. `realism.contact.contact_event` (planned), IF-3, `realism.mech.articulated_locomotion` (planned); eating through IF-36 (built). `shared.action.kind` (planned) is only the vocabulary. | reality / life | missing | stub (`world.resolve`, fixture rules) | missing (no equation): CG-16 |
| 3.7 | Social resolution | `economy.trade.trade` (built); IF-18, IF-43, IF-46 (planned) | as listed | economy, government, society | trade built | stub (ask, give, trade by fixture) | broken connection: IF-26, IF-27 (`mind.intention` has no built consumer) |
| 3.8 | Changed environment and body | `economy.inventory.holdings`, `body.kcal_in` (built) | as listed | economy, life | built, not joined to Cognition | stub (hunger 0.6 → 0.35) | broken connection (IF-26) and invalid coupling (CG-19) on the same path |
| 3.9 | Changed beliefs and memory | `mind.prediction_error`, `.attribution`, `.episode`, `.belief` | `cognition.learning.outcome`, `.attribution`, `.memory.episodic`, `.belief.update` (built) | cognition | built | yes | complete |
| 3.10 | Next step | the kernel clock and event bus | kernel src/scheduler.ts, runner.ts, events.ts (built) | kernel | built | yes (144 epochs, replay) | complete; the events are untyped (CG-18) |

**Coupling note:** the units are compatible on every built Cognition link (0–1 quantities and records). The open
couplings are where Cognition meets other engines: `mind.intention` (unit null, a record) has no consumer that
accepts it (IF-26, IF-27, IF-43), and the kernel event carries it as an `unknown` payload (CG-18).

## The seven structures

| Structure | What the registry has | Gaps | Type |
|---|---|---|---|
| **Spatial compartments** | Scopes `place`, `world`, `body` and `mind`; `realism.gas.room_box` (built); `shared.contract.terrain_resolution` (planned) | No row defines the place or cell record. `world.*` stocks "per area" carry unit kg (CG-9). | missing (no equation); invalid coupling |
| **Shared material ledger** | `realism.infra.world_conservation` (built: mass and element atoms); the substrate ledger (IF-31, IF-34, IF-36); `economy.inventory.holdings` (goods, unitless); `settlement.ledger.pay` (money); kernel `ConservedQuantity` | The goods ledger and the mass ledger don't share units (CG-19). The kernel service has no row (CG-17). No cross-engine N or soil-mass test. | invalid coupling; broken connection |
| **Species configuration without false equivalence** | `realism.anatomy.species_profile` (LIFE-3: labelled values, no species name in src/); DUP-23; Mifflin-St Jeor for people, Kleiber for the horse | The plant part is planned, with data landing (realism 2808–2810). `realism.physiology.rmr` falls back to 1 kcal/kg/h for any species missing height, age or sex: a cross-species default. | invalid coupling (assumption), for the owner to judge |
| **Lifecycle transitions** | conception → maturation → trait_change → ageing_emergent (all planned) → crisis and death (built) → demography (planned) | Only death is built. The genetic profile has no quantity (CG-12). | missing (not implemented); broken connection |
| **Adaptive resolution** | PLATFORM §9; kernel `ResolutionService` (built, conserved quantities within a tolerance); `terrain_resolution` (planned); `realism:epidemic-vs-individuals` (built) | The kernel service has no row (CG-17). No chain-1 or chain-2 row declares its resolutions. Population and individual consumption are not joined (CG-23). Soil timescales conflict (CG-22). | broken connection; invalid coupling |
| **Uncertainty (no silent constants)** | Evidence levels; LIFE-3 labels (null+flag); legitimacy null, never 0; schema 4 `numerical.sensitivity` | `sensitivity` is null on all 579 rows. These constants carry only a row-level source: rmr fallback; fat floor 3 kg; glycogen cap 400 g; starvation at 60 % of start mass; soil_fertility steps +0.03, +0.02, −0.02 and ×0.5 (conf low). | owners to label; not a chain failure type |
| **Cross-engine event contracts** | `KernelEvent {id, t, source, type, payload, cause}` (kernel, built); typed records `body.crisis`, `body.conception`, `contact_event`, `economy.shortage.event`, `mind.intention` | The payload is `unknown`. No list of event types with payload schema, producer and consumers exists (CG-18). | missing (no equation) |

## Gaps recorded (integration_gaps.interface_gaps)

| Id | Gap | Failure type | Holder (to propose; the registry decides nothing) |
|---|---|---|---|
| CG-1 | `place.par` has no writer | missing (no equation) | Reality |
| CG-2 | `place.rain`, `place.vpd`, `world.soil_water` have no writer | missing (no equation) | Reality |
| CG-3 | No plant uptake quantity (water, N, P, K) between soils and plants | broken connection | Life with Reality |
| CG-4 | **closed 2026-11-01**: `realism.plant.physiology` inputs omitted the LIFE-2 quantities | broken connection | Life |
| CG-5 | No row moves an organism between places | missing (no equation) | Reality / Life |
| CG-6 | No excreta mass or nutrient quantity; DUP-45 undecided | missing (no equation) | Life |
| CG-7 | No nitrogen inputs (deposition, fixation, manure as mass) | missing (no equation) | Reality / Life |
| CG-8 | No gaseous nitrogen losses | missing (no equation) | Reality / Life |
| CG-9 | Soil pools and fluxes: N, P and K in one kg quantity, "per area" with no area unit | invalid coupling | Reality |
| CG-10 | No gut microbial digestion term | missing (no equation) | Life |
| CG-11 | X1: body outputs (faeces) have no destination | missing (no equation) | controller / Rex |
| CG-12 | **closed 2026-11-01**: the genetic profile had no quantity id; maturation reads a row id | broken connection | Life |
| CG-13 | energy_store reads "intake": eaten or absorbed is unstated | invalid coupling, to confirm | Life |
| CG-14 | Expenditure has no growth, thermoregulation or reproduction term | missing (no equation) | Life |
| CG-15 | Tissue populations have no B − D equation or quantities | missing (no equation) | Life (realism 2815) |
| CG-16 | No row resolves an intention into a physical outcome; capacity has no writer (DUP-15) | missing (no equation) | Reality / Life, with the controller |
| CG-17 | **closed 2026-11-01**: the kernel conservation and resolution service had no registry row | broken connection | Kernel |
| CG-18 | Events have no typed contract | missing (no equation) | Kernel / controller |
| CG-19 | Economy goods are unitless while IF-36 and IF-42 require mass and Life takes kg and kcal | invalid coupling | Economy with Life |
| CG-20 | Soil nutrient loss on harvest (built `eco.soil_fertility`) is calculated apart from plant uptake | invalid coupling | Reality / Life (DUP-51, DUP-53) |
| CG-21 | Plant biomass in two quantities (`world.plant_state`, `world.vegetation_stock`) with no aggregation | invalid coupling | Life (DUP-53) |
| CG-22 | The soils and hydrology timescale is yearly while the fluxes they integrate run fast; no integration rule | invalid coupling | Reality / Life |
| CG-23 | Population consumption (kg/a) and individual consumption (kcal per meal) are not joined | broken connection | Life |
| CG-24 | `body.hunger_signal`'s writer is documented-only; Cognition reads a host stub | missing (not implemented) | Life |
| CG-25 | `body.detectability`'s writer is planned; Cognition reads a host stub | missing (not implemented) | Life / Reality |
