# realism-phys audit notes (physical/chemical/environment + infrastructure)

Rows: 67 in realism-phys.jsonl (58 built, 9 planned; the last is inferred). Tests: 237 `it(` across 21 files in realism/test (README/PHASES say 231 at 2026-10-30; the number counts all modules, not just this batch). In-batch files: still 18, atmosphere 27, environment 14, ecology 10, reactions 18, registry 3, library 2 + library-loader 2, independence 5, checkpoint1 4, checkpoint2 4, perf 1.

## Architecture (one paragraph)
`World` holds the clock `t` (s), a `Registry` (substances, materials, components), a `Graph` (typed port edges), a `Trace` (transfers, checks, notes, crises) and an `env` bag. State lives in lumped `Component`s (mass, one temperature, `contents[]` of substance/phase/kg, `condition`, free-form `props`). Mechanisms are `Process` objects `{name, every, step(world, dt)}` added to a `Scheduler`, which runs them in a fixed declared order each fast step (usually 1 s; slow processes every N steps), then does `t += dt` and `world.afterStep()`, which folds new trace transfers into declared conservation ledgers (substance mass, per-element atom counts) and records pass/fail checks. Modules couple only through shared component state and `props` (room temperature/contents/rh/ppm, `body.props.outputs` by library id, `place.props.wbgt_c`) and through order of processes; every mass or energy move is a traced transfer. Numbers come from `data/*.json` and `data/library/*.json` through `library.ts`; several modules regex-parse formulas out of the library's text cells. There is no event queue, no spatial model beyond the host-supplied `Grid`, and energy is not a world ledger (checked in tests).

## What registry.ts and graph.ts are
`registry.ts` is an ENTITY registry: substances (molar mass, cp by phase, hhv, density, melt/boil, source URL, provenance), materials (cp, maxTemperatureC, corrodedBy), components (kind, material, mass, T, contents, ports, condition, props), plus helpers (heatCapacity, addContent with Kahan carry). `graph.ts` is a list of typed edges between component ports. Neither holds mechanisms, owners, units, dependencies or invariants. Therefore a platform-wide MECHANISM registry does not exist in the realism code; it must be new. It can reuse the entity registry's ids (substance/material/component ids) as shared vocabulary, and `provenance` on substance rows already approximates PLATFORM.md section 6 provenance classes. `library.ts` row ids (e.g. `ecology.depletion_rules.overnight-stock-update`) are the closest thing to stable mechanism ids; modules already emit "outputs by id" using them.

## 1. Duplicates / overlaps
- Carbon+O2 combustion: `src/physics.ts carbonCombustion` + `src/process.ts combustionProcess` (30 MJ/kg, CO ramp 0.15..0.05) vs data record `data/reactions.json comb_c_full` run by `src/reactions.ts reactionProcess` (-393510 J/mol = 32.8 MJ/kg, minO2 0.15) vs library `chemistry.reactions` comb_c_full/comb_c_starved (doc) vs `src/atmosphere.ts fireFlows` (library cargo-fire rates). Four fire/charcoal descriptions. README says the old path is kept deliberately.
- Charcoal heat of combustion: `physics.HHV.charcoal` 30.0e6, `substances.json` charcoal hhv 30.0e6, derived 32.8e6 from reactions.json. Charcoal cp: physics `CP.charcoal` 1000 vs substances.json 999.08. `CP.copper` 385 vs materials.json copper 390.
- Saturation vapour pressure: `physics.ts waterVapourPressure` (Antoine, Pa) vs `environment.ts vapourPressureHpa` (Magnus, hPa, RH percent); airway 47 mmHg from library (`atmosphere.lib().waterMmHg`) vs Antoine at 37 C.
- Latent heat: `waterLatentHeat(T)` vs constant `SWEAT_LATENT` 2.43e6 in `physics.ts` L98 (physiology).
- Ideal gas: `physics.molesInVolume` vs `atmosphere.litresToMoles`; `R_GAS = 8.314` literal.
- VO2 = 3.5 mL/kg/min/MET: `physics.metabolicHeat` (literal 3.5), `atmosphere.bodyGasFlows` and `respiratoryState` (library-parsed). Body CO2 output also in physiology (outside batch).
- Evaporation: ASHRAE pool (`process.evaporationProcess`) vs physiology's Lewis-relation skin evaporation.
- Hypothermia: `environment.coldWater` table outcome vs physiology core-temperature drift.
- Initial room air and outside humidity literal in `lab/still.ts` L49-51 vs `atmosphere.baselineAir()`/`airContents()`/`OUTSIDE_WATER_KG_PER_KG`.
- Wear: `process.wearProcess` (placeholder) vs `equipment.json wear` table (8 rows, data twin); Phase 9 planned to generalise.
- Brick: `physics.BRICK_WALL` (cp 790) vs materials.json `wall_brick` cp 790 and `brick` cp 900.
- Hb saturation formula lives in atmosphere.ts but the table belongs to `circulation.blood_gas`.

## 2. Unit problems
- RMR is kcal/day, `metabolicHeat` is W (physiology rescales between them).
- RH: percent in environment.ts, fraction in `room.props.rh`; capped at 1.5.
- Pressure: Pa (physics) and mmHg (atmosphere/physiology) both in play; conversions via `MMHG_PER_PA`.
- Time: ecology in days with r per year; gas flows L/min, ACH per hour, process dt seconds; slow processes get `dt*every`.
- Grid transport uses fractions per step (diffusion, rise, settle), not physical D, so results depend on cell size and dt.
- Host-units stocks (`ecology`) have no unit; `Stock.B` is "biomass or head count".

## 3. Circular / ownership conflicts
- `process.ts` imports `physiology.ts` and `atmosphere.ts`; `atmosphere.ts` imports `physiology.ts` (bodyOutputs) and `physiology` reads `physics`, `atmosphere` outputs, and `environment` imports `physiology`. Import-level cycles are not present (all via physics/library), but run-order coupling is: breathing must follow roomAir and physiology; physiology reads `place.props.wbgt_c` written by environment.
- Sweat/skin water ownership split between `process.bodyProcess` (delegates to physiology) and atmosphere (gas) with the room humidity: one water ledger shared, ownership is by convention.

## 4. Planned / missing (PHASES-6-PLUS.md; nothing built, awaiting Rex's order)
Phase 6 mechanics (rigid body, friction, collisions, articulated), 7 fluids, 8 optics, 9 materials, 10 metabolism as flux, 11 waste/sanitation/decomposition, 12 genes and ageing. Not in docs, my inference: weather/climate generator, solar geometry, mixture distillation, whole-world energy ledger, geology, oceans, structural/construction mechanics (domain A lists these; none planned in realism docs). Also noted: no spatial/aggregated resolution hand-off beyond `Grid.uniform()`.

## 5. Pirate-specific in universal / universal only in pirate docs
- `environment.exposure` terrain rows are pirate places (below decks, galley, tavern, Guinea coast); `environment.climate/sun/period_climate` are Jamaica (G instances, per MIGRATION).
- `controlProcess` (skill 0-100), `thermometerProcess` drift, `wearProcess`, `crisis.ts` "no silent death", `ecology.dailyCatch` (Fishing skill q), crop names (cane, pease), turtle crawls/nesting beaches rows in `ecology.depletion_rules`.
- The still scenario itself (`lab/still.ts`) mirrors the pirate galley still; `world.env.outsideC` default "Caribbean day".
- Universal formulas whose authoritative statement lives in pirate docs: ENGINE.md, PHYSIOLOGY.md, BODY.md under `Games/RPG's/pirate-ship/files/pirate-ship/` (cited as source keys ENG-*, GAS-BOX, CHM-BP); the engine cites doc keys rather than carrying the derivation.
