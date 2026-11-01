# pirate-world audit notes (100 rows in pirate-world.jsonl)

Scope read: world/ (5), science/ (7 read, SCIENTIFIC_EQUIPMENT headings and sections 1, 3, 4, catalogue state), balance/ALIGNMENT.md (sections 1-9 plus run-downs), economy/GOODS.md (headings, 3c/3e/3f/3h, Open), REGIONS.md, ATLANTIC-MAP.md (structure), combat/COMBAT.md (sections 1-7). Code: web/src/alignment, economy, settlement, world/adapters; Toolchain realism, economy, settlement src.

## 1. Duplicates and overlaps (both homes)
- Pressure with altitude: world/ATMOSPHERE.md section 2 = realism/src/physics.ts:12 pressureAtAltitude and atmosphere.ts altitudeAir. Doc is the spec, code is the owner.
- Box model dC/dt: science/ENGINE.md section 2 ("Box model of a room") = world/GAS_DYNAMICS.md section 2 = realism atmosphere.ts roomAirProcess. Doc duplicate.
- Combustion heat of charcoal: ENGINE.md 30 MJ/kg (physics.ts HHV) vs CHEMISTRY.md comb_c_full 32.8 MJ/kg (and comb_c_starved 10 MJ/kg). Conflicting values.
- Combustion gas: atmosphere.ts fireFlows/lampFlows (fixed L/min rates from GAS_DYNAMICS section 3) vs process.ts combustionProcess + reactions.ts (stoichiometry). Two sources of CO2/CO.
- Saturation vapour pressure: physics.ts waterVapourPressure (Antoine) vs environment.ts vapourPressureHpa (Magnus 17.27/237.7).
- Person as gas source (0.25/0.2 L/min) vs VO2 = 3.5 mL/kg/min x MET in physiology/ENGINE.md.
- Vector/mosquito multipliers: ENVIRONMENT.md exposure table (environment.ts) vs medicine exposure table (adapters/medicine.ts multiplierOf).
- Season/dry-wet definition: ENVIRONMENT.md climate Season column vs ECOLOGY.md calendar.
- Human mortality: population.ts famine x1.5 and background death rates vs per-body starvation, ageing and disease in nutrition/physiology/medicine. Hunger can kill by two paths.
- Labour availability: population.ts labour (adults x health x (1-sick)) vs settlement staffing.ts/labour provider vs economy labour.ts supply; labour per hectare in ECOLOGY crops vs recipes.json labourPerUnit.
- Food: population foodDays, economy consumption per-capita, realism nutrition per body, adapters/food.ts ration. Four food accounts.
- Spoilage: economy spoilagePerDay (no temperature) vs adapters/food.ts keepsOf.
- Wear: equipment wear (SCIENTIFIC_EQUIPMENT section 4), settlement decay.ts building bands, realism process.wearProcess. Three wear models; structural mechanics planned.
- Wages: settlement post.wage vs economy wageQuote.
- Injury: COMBAT.md wound ladder and HP vs realism medicine.ts inflictWound, circulation bleedingClass, crisis.ts.
- Muscle/fatigue: COMBAT.md section 4b and Endurance pool vs realism muscular.ts (built) and nutrition energy balance.
- Units table: PHYSICS.md stub says shared units table open; GAS_DYNAMICS section 1 is the only one.

## 2. Unit problems
- ACH: ENGINE.md Q = ACH V / 3600 (per second) vs GAS_DYNAMICS Q = ACH V / 60 (per minute); code uses flow per minute x 60.
- Population rates per 1000 per year vs daily tick /365 (consistent) but "health" is unitless 0-1 scalar blending several states.
- Ecology: K in "catch-days per ground per year", r per year, B/K ratio daily (r/365): unit of B is catch-days, not kg; cannot link to goods mass without a conversion.
- Price: base prices all null, no currency unit defined (GOODS Open 2: money or goods).
- Crops: yield in t/ha, soil f unitless index, labour person-days/ha: no mass or nutrient balance.
- WBGT_ERROR_C is null (error unknown).

## 3. Ownership conflicts / circularity
- Weather: ENVIRONMENT.md (daily Markov, in web adapter places.ts only) feeds ECOLOGY (rain), POPULATION (fever season) and ATMOSPHERE (wind); ECOLOGY and POPULATION in turn feed economy. Weather generator not in realism (no source for it in Toolchain/realism/src).
- Ship speed: ENVIRONMENT section 3 supplies point-of-sail factors, PIRATE.md 5a owns base speed. Split.
- Food-source pairs: ALIGNMENT institutions develop only if "bodies supplied" (story data) and ECOLOGY farm yield: a game meter and an ecology figure both claim the town's food.
- Atmosphere vs circulation: alveolar gas in atmosphere.ts, blood gases in circulation.ts, breathing drive in neurology.ts: three files for one respiratory chain.
- CHEMISTRY.md "smoke Eyesight x0.6" is a direct vision multiplier while ATMOSPHERE says one pathway; COMBAT.md also sets Eyesight dips from head wounds. Needs a single capability owner.

## 4. Planned / missing (named in docs)
Gas grid (done in code, doc stale); free-energy possibility and equilibrium (CHEMISTRY, none in code); assembly pipeline (313-row catalogue exists as data, no engine); equipment wear; PHYSICS.md (stub; energy ledger, mechanics, optics, electricity); hurricane approach; rain catch; sailing model; recruit pool; migration-out pressure; faction influence and Act II world state; fate/form system; combat resolution (no code); detection, sound; flinch; GOODS Open 1-8 (slave trade; money or goods; granularity; raw vs manufactured; live cargo; cultural column; names; cask size); GOODS items 9-11 skills/occupations/STATS. Missing generic mechanisms: knowledge diffusion through trade/migration, climate forcing, prices from cost of production, currency, government (tax step is an empty stub in settlement wages.ts publicWorks).

## 5. Pirate-specific inside universal, and the reverse
- Date-gated or level-gated (PLATFORM section 2, 6):
  - ENVIRONMENT period_climate: hurricane weight x0.25 before 1715, x0.6 after; code places.ts weightOf(year) parses the multiplier from table text by regex.
  - TECHNOLOGY.md / SCIENTIFIC_EQUIPMENT availability common/rare/none per item for 1650-1730 (101/83/128); 13 rows relabelled "none (anomaly)" because dated after 1730; Newcomen "in the period but not in the islands" is a hand exclusion. The "anomaly plug" exists only because availability is a list.
  - GOODS 3c/3f skill bands Novice..Master gate recipes ("some items need a certain level besides"); COMBAT section 5 band-unlocked techniques; REGIONS section 5 level cap rises per region and best tech last.
  - DISCOVERY/JOURNAL anomaly note compares game date to history date: label only, no unlock (compatible).
  - ALIGNMENT institutions transform at sleep when owner region reached; thresholds 15/30 classify characters (rule by meter threshold; fiction, parked).
- Pirate data in the universal realism library: climate (Kingston station), population rates (England, Jamaica, Miskito), settlers = prosperity x reputation, tavern/hold volumes, turtle/boucan stocks, Caribbean crops. Reputation is a game meter inside population.ts.
- Universal things living only in pirate docs: weather Markov chain, ocean currents, sailing speed, hurricane model, human settlement cohorts, discovery states, journal, assembly pipeline, knowledge rule (GOODS 3f), detection/sound.
- Alignment charts hardcode MBTI-type response arrows (16 charts): should be superseded by the Cognition personality model (C), not extended.
- Positive: adapters/medicine.ts dipFactor and stats.ts capabilityToday implement one pathway per formula, worst dip counts; combat should hang on this.
