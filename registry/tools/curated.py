# Curated audit data (registry keeper, 2026-10-30): restatement links, overlap groups, unit issues.
# Every "owner" here is a PROPOSAL for Rex, never a decision.

# Id renames: rows a reader filed under another engine's namespace although they describe docs or refs.
RENAME_PREFIX = {
    # pirate-body rows that restate realism code
    "physiology.": "pirate.doc.physiology.",
    "circulation.": "pirate.doc.circulation.",
    "anatomy.": "pirate.doc.anatomy.",
    "nutrition.": "pirate.doc.nutrition.",
    "medicine.": "pirate.doc.medicine.",
    "muscular.": "pirate.doc.muscular.",
}
# pirate-world rows filed as settlement.* (they are restatements in pirate docs/adapters)
RENAME_EXACT = {
    "settlement.production.q_min": "pirate.ref.settlement.production_q",
    "settlement.decay.condition": "pirate.ref.settlement.condition_decay",
    "settlement.projects.labour_days": "pirate.ref.settlement.project_labour_days",
    "settlement.staffing": "pirate.ref.settlement.staffing",
    "settlement.wages_rent": "pirate.ref.settlement.wages_rent",
    "settlement.lease_expiry": "pirate.ref.settlement.lease_expiry",
}

# restatement id (after rename) -> authoritative mechanism id
RESTATES = {
    "pirate.doc.physiology.rmr": "realism.physiology.rmr",
    "pirate.doc.physiology.activity_energy": "realism.physiology.energy_expenditure",
    "pirate.doc.physiology.ventilation": "realism.gas.ventilation_drive",
    "pirate.doc.physiology.sleep_alertness": "realism.physiology.sleep_debt",
    "pirate.doc.physiology.circadian": "realism.physiology.circadian",
    "pirate.doc.physiology.heat_stress": "realism.physiology.wbgt_core_drift",
    "pirate.doc.physiology.sweat_rate_doc": "realism.physiology.sweat",
    "pirate.doc.physiology.cold_immersion": "realism.env.cold_water_immersion",
    "pirate.doc.physiology.hydration": "realism.physiology.hydration_band",
    "pirate.doc.physiology.overnight": "realism.physiology.core_state",
    "pirate.doc.physiology.acclimatisation": "realism.physiology.acclimatisation",
    "pirate.doc.physiology.thermal_cost": "realism.physiology.heat_balance",
    "pirate.doc.circulation.do2": "realism.circulation.o2_delivery",
    "pirate.doc.circulation.blood_volume": "realism.circulation.normal_blood_volume",
    "pirate.doc.circulation.sao2": "realism.gas.hb_saturation",
    "pirate.doc.circulation.bleeding": "realism.circulation.bleed_rate",
    "pirate.doc.circulation.cardiac_events": "realism.circulation.hazards",
    "pirate.doc.circulation.regulation_loops": "realism.circulation.regulation_loops",
    "pirate.doc.anatomy.organ_cascade": "realism.anatomy.organ_function",
    "pirate.doc.anatomy.damage_repair": "realism.anatomy.damage_repair",
    "pirate.doc.anatomy.crisis_death": "realism.anatomy.crisis_floors",
    "pirate.doc.anatomy.tissue_integrity": "realism.anatomy.tissue_collagen",
    "pirate.doc.anatomy.species_profile": "realism.anatomy.species_profile",
    "pirate.neuro.pk": "realism.neurology.pk",
    "pirate.neuro.occupancy": "realism.neurology.occupancy",
    "pirate.neuro.clocks": "realism.neurology.tolerance_dependence_withdrawal",
    "pirate.neuro.circuits": "realism.neurology.circuits",
    "pirate.neuro.breathing_drive": "realism.neurology.breathing_drive",
    "pirate.neuro.baseline": "realism.neurology.baseline_drivers",
    "pirate.doc.nutrition.requirements": "realism.nutrition.requirement",
    "pirate.doc.nutrition.absorption": "realism.nutrition.absorption",
    "pirate.doc.nutrition.deficiency_pools": "realism.nutrition.pools",
    "pirate.doc.nutrition.energy_balance": "realism.nutrition.energy_store",
    "pirate.doc.nutrition.glycogen_factor": "realism.nutrition.energy_store",
    "pirate.doc.nutrition.starvation_stages": "realism.nutrition.starvation_limit",
    "pirate.doc.medicine.exposure": "realism.medicine.disease_course",
    "pirate.doc.medicine.disease_course": "realism.medicine.disease_course",
    "pirate.doc.medicine.wounds": "realism.medicine.wounds",
    "pirate.doc.medicine.pain_shock": "realism.medicine.pain",
    "pirate.doc.medicine.treatments": "realism.medicine.treatment_claims",
    "pirate.doc.medicine.healing": "realism.medicine.healing_multiplier",
    "pirate.doc.medicine.immunity": "realism.medicine.immunity",
    "pirate.doc.medicine.air_conditions": "realism.medicine.air_conditions",
    "pirate.doc.muscular.3cc": "realism.muscular.fatigue_3cc",
    "pirate.doc.muscular.adaptation": "realism.muscular.adaptation_day",
    "pirate.phys.aerobic_banister": "realism.muscular.banister",
    "pirate.atm.pressure_altitude": "realism.atmos.barometric_pressure",
    "pirate.atm.alveolar_gas": "realism.gas.alveolar_po2",
    "pirate.atm.ventilation_ach": "realism.gas.room_box",
    "pirate.atm.baseline_composition": "realism.gas.room_box",
    "pirate.gas.box_model": "realism.gas.room_box",
    "pirate.gas.grid": "realism.gas.grid_transport",
    "pirate.gas.sources": "realism.gas.sources_sinks",
    "pirate.gas.sinks": "realism.gas.sources_sinks",
    "pirate.gas.exposure_dose": "realism.gas.exposure_accumulation",
    "pirate.gas.heavy_layering": "realism.gas.thresholds_layering",
    "pirate.env.wbgt": "realism.env.wbgt_bom",
    "pirate.env.diurnal_temperature": "realism.env.diurnal_curve",
    "pirate.env.wind_chill_cold_water": "realism.env.wind_chill",
    "pirate.env.exposure_by_place": "realism.env.exposure_by_terrain",
    "pirate.eco.schaefer_stock": "realism.eco.logistic_stock",
    "pirate.eco.recovery": "realism.eco.msy_collapse_recovery",
    "pirate.eco.fished_out": "realism.eco.fished_out_catch",
    "pirate.eco.cpue_catch": "realism.eco.fished_out_catch",
    "pirate.eco.soil_fertility": "realism.eco.soil_fertility",
    "pirate.pop.cohort_tick": "realism.population.cohort_tick",
    "pirate.pop.epidemic": "realism.population.epidemic",
    "pirate.pop.famine": "realism.population.famine",
    "pirate.pop.migration": "realism.population.migration",
    "pirate.pop.labour_supply": "realism.population.labour",
    "pirate.sci.registry_scheduler_trace": "realism.infra.scheduler",
    "pirate.sci.sensible_latent_antoine": "realism.thermo.water_vapour_pressure",
    "pirate.sci.combustion": "realism.chem.carbon_combustion_charcoal",
    "pirate.sci.heat_transfer": "realism.thermo.heat_flow_UA",
    "pirate.sci.measurement_drift": "realism.infra.thermometer_drift",
    "pirate.sci.control_noise": "realism.infra.operator_control",
    "pirate.sci.reaction_rate": "realism.chem.reaction_extent",
    "pirate.sci.equipment_wear": "realism.equip.wear_by_temperature",
    "pirate.goods.price_shortage_rule": "economy.price.rule",
    "pirate.goods.shortage": "economy.shortage.event",
    "pirate.goods.consumption": "economy.consumption.demand",
    "pirate.goods.spoilage": "economy.spoilage",
    "pirate.goods.abstract_production_shipments": "economy.production.abstract_market",
    "pirate.goods.wage_quote": "economy.labour.wage_quote",
    "pirate.goods.recipe_rule": "economy.recipe.definition",
    "pirate.ref.settlement.production_q": "settlement.production.constraint_Q",
    "pirate.ref.settlement.condition_decay": "settlement.building.condition_decay",
    "pirate.ref.settlement.project_labour_days": "settlement.project.construction",
    "pirate.ref.settlement.staffing": "settlement.business.staffing",
    "pirate.ref.settlement.wages_rent": "settlement.wage.pay",
    "pirate.ref.settlement.lease_expiry": "settlement.expiry",
}

# Overlap groups. kind: duplicate (same quantity computed twice), conflict (values/units disagree),
# ownership (two owners claim it / none), double-penalty (one cause, several effects), interface (wiring broken).
# owner = proposed authoritative mechanism (or a planned/new one), never a decision.
GROUPS = [
 ("DUP-1","duplicate+conflict","Carbon/charcoal combustion: four descriptions, two heats of combustion (30.0 vs 32.8 MJ/kg)",
  ["realism.chem.carbon_combustion_charcoal","realism.chem.reaction_extent","realism.chem.heat_per_kg","realism.gas.sources_sinks","pirate.sci.combustion"],
  "realism.chem.reaction_extent (the stoichiometric reaction record); physics.ts carbonCombustion and atmosphere fireFlows become callers/derived. 30 MJ/kg (charcoal, impure) and 32.8 MJ/kg (pure carbon) may both be right for different substances: record charcoal and graphite as two substances rather than pick one."),
 ("DUP-2","duplicate+unit","Water saturation vapour pressure: Antoine (Pa) in physics.ts vs Magnus (hPa, RH in percent) in environment.ts; room.props.rh is a fraction",
  ["realism.thermo.water_vapour_pressure","realism.env.wbgt_bom","pirate.sci.sensible_latent_antoine"],
  "realism.thermo.water_vapour_pressure; environment calls it; RH is a fraction everywhere."),
 ("DUP-3","duplicate","Latent heat of water: waterLatentHeat(T) vs constant SWEAT_LATENT 2.43e6",
  ["realism.thermo.water_latent_heat","realism.physiology.sweat"],"realism.thermo.water_latent_heat evaluated at skin temperature."),
 ("DUP-4","duplicate","Ideal gas: physics.molesInVolume vs atmosphere.litresToMoles, literal R",
  ["realism.gas.ideal_gas","realism.gas.units"],"realism.gas.ideal_gas."),
 ("DUP-5","duplicate+conflict","Oxygen use per MET computed three times; physiology scales energy to the body's RMR, atmosphere's O2/CO2 exchange does not (disagree for any body whose RMR is not 1 kcal/kg/h, e.g. the horse)",
  ["realism.thermo.metabolic_heat","realism.gas.breathing_process","realism.physiology.energy_expenditure","pirate.doc.physiology.activity_energy"],
  "realism.physiology.energy_expenditure owns metabolic rate; heat, metabolic water and gas exchange all read its one output."),
 ("DUP-6","overlap","Evaporation: ASHRAE pool evaporation vs Lewis-relation skin evaporation (different surfaces, same psychrometrics)",
  ["realism.thermo.surface_evaporation","realism.physiology.sweat"],"keep both; share one psychrometric helper (DUP-2)."),
 ("DUP-7","duplicate","Hypothermia: cold-water immersion outcome table vs physiology core temperature (cold side planned)",
  ["realism.env.cold_water_immersion","realism.physiology.core_state","realism.physiology.cold_water","pirate.doc.physiology.cold_immersion"],
  "realism.physiology.core_state once its cold side is built; the immersion table becomes validation data."),
 ("DUP-8","duplicate","Still scenario hard-codes room air and outside humidity that atmosphere owns",
  ["realism.infra.still_scenario","realism.gas.room_box"],"realism.gas.room_box baseline air."),
 ("DUP-9","duplicate","Degradation in four homes: equipment wear by temperature, building condition decay, goods spoilage, planned materials decay",
  ["realism.equip.wear_by_temperature","settlement.building.condition_decay","economy.spoilage","realism.materials.deformation_fracture_decay","pirate.sci.equipment_wear","pirate.goods.spoilage"],
  "realism.materials.deformation_fracture_decay (planned Phase 9) owns physical and organic degradation; settlement keeps condition as a state that reads it; economy spoilage reads realism decay rates for perishables."),
 ("DUP-10","conflict","Material constants twice: brick cp (physics BRICK_WALL 790 vs materials.json brick 900), copper cp 385 vs 390, charcoal cp 1000 vs 999.08",
  ["realism.thermo.brick_wall_constants","realism.infra.component_registry"],"data/materials.json and substances.json; physics.ts constants read them."),
 ("DUP-11","ownership","Haemoglobin saturation coded in atmosphere.ts, documented as circulation's (CIRCULATION.md §1a)",
  ["realism.gas.hb_saturation","pirate.doc.circulation.sao2"],"realism circulation (blood gas); atmosphere supplies alveolar PO2 only."),
 ("DUP-12","duplicate","Sleep pressure as two states: physiology sleep_debt/alertness vs neurology hours_awake/adenosine/arousal",
  ["realism.physiology.sleep_debt","realism.physiology.alertness","realism.neurology.sleep_wake","pirate.doc.physiology.sleep_alertness"],
  "realism.neurology.sleep_wake owns sleep pressure; physiology alertness becomes a read of it."),
 ("DUP-13","duplicate","Fatigue in five places: whole-body MET-hours, per-group 3CC, Banister fatigue, the doc's fatigueDay, the Endurance pool",
  ["realism.physiology.fatigue_met_hours","realism.muscular.fatigue_3cc","realism.muscular.banister","pirate.phys.fatigue_day","pirate.body.endurance_pool","pirate.combat.endurance_efficiency"],
  "realism.muscular.fatigue_3cc (local) and realism.physiology.fatigue_met_hours (systemic), with a declared relation; the pool and Efficiency are pirate gameplay reads, never a third fatigue."),
 ("DUP-14","conflict+unit","aerobic_today: code outputs DO2 at max cardiac output in mL O2/min; docs treat it as an index (pool = Endurance x aerobic_today/40); Banister 'performance' a third aerobic measure",
  ["realism.circulation.aerobic_today","realism.muscular.banister","pirate.phys.aerobic_banister","pirate.body.endurance_pool"],
  "realism.circulation.aerobic_today (mL O2/min); any index is a pirate adapter conversion with its unit stated."),
 ("DUP-15","double-penalty","Work capacity as four separate multipliers (heat, hydration, endurance-hydration, starvation x0.8) plus the doc's work capacity; hydration and bleeding table rows name game attributes (Endurance, Wits, Strength) and would stack",
  ["realism.physiology.wbgt_core_drift","realism.physiology.hydration_band","realism.nutrition.starvation_limit","realism.circulation.bleeding_class","pirate.body.work_capacity","pirate.body.strength_today","pirate.combat.functional_capacity"],
  "a new universal mechanism realism.capacity.functional (the universal core of BODY.md: one combination rule over biological states, worst-dip or product stated once); STATS attributes and combat read it through the pirate adapter (web/src/world/adapters/stats.ts capabilityToday is the right pattern)."),
 ("DUP-16","double-penalty","Vitamin C below 300 mg drives four consequences: deficiency stage, collagen loss, healing x3, and a separate scurvy disease row",
  ["realism.nutrition.pools","realism.anatomy.tissue_collagen","realism.medicine.healing_multiplier","realism.medicine.disease_course"],
  "one pathway: nutrition pool -> anatomy collagen state; healing reads collagen, not vitamin C; 'scurvy' is the name of that state, not a second disease course."),
 ("DUP-17","duplicate","Age effects in four unlinked places (physiology ageing table no code reads, medicine healing by age, muscular age gate, neurology dopamine decline) plus STATS ageing",
  ["realism.physiology.ageing_curves","realism.medicine.healing_multiplier","realism.muscular.adaptation_day","realism.neurology.baseline_drivers","pirate.stats.ageing_max","pirate.phys.ageing_curves"],
  "realism.genes.ageing_capacity (planned Phase 12): ageing acts through organ capacity; the four effects become reads."),
 ("DUP-18","ownership+conflict","Banister impulse-response: table in physiology library, code in muscular.ts, physiology flags say not implemented; constants k1/k2 0.4/42, 0.4/7 in prose vs 1 and 1.3 in table",
  ["realism.physiology.banister_table","realism.muscular.banister","pirate.phys.aerobic_banister"],"realism.muscular.banister; one constant set with its source."),
 ("DUP-19","duplicate","Mortality from five sources with no shared cause-of-death ledger: circulation hazards, medicine fatal draw, anatomy crisis floors, population background/epidemic/famine",
  ["realism.circulation.hazards","realism.medicine.disease_course","realism.anatomy.crisis_floors","realism.infra.crisis_record","realism.population.cohort_tick","realism.population.epidemic","realism.population.famine"],
  "individual death: realism.anatomy.crisis_floors via realism.infra.crisis_record (one cause-of-death ledger); aggregate death: population, calibrated so the aggregate equals the mean of individuals (PLATFORM §9: finer refines, never contradicts)."),
 ("DUP-20","duplicate","Population epidemic reimplements medicine exposure/course as expected values; keeps its own health, foodDays, seasonedShare",
  ["realism.population.epidemic","realism.medicine.disease_course","pirate.pop.epidemic"],
  "realism.medicine.disease_course owns the course; the aggregate reads the same parameters; a test checks mean agreement."),
 ("DUP-21","duplicate","Food in four accounts: population foodDays, economy per-capita consumption, per-body nutrition, pirate adapters/food.ts rations; hunger can kill by two paths",
  ["realism.population.famine","economy.consumption.demand","realism.nutrition.eat_meal","realism.nutrition.starvation_limit","pirate.goods.consumption"],
  "economy.consumption.demand moves goods out of inventory; realism.nutrition owns intake and starvation per body; population famine becomes the aggregate of nutrition status (economy PLAN step 11)."),
 ("DUP-22","ownership","Body water in four ledgers (body contents, waterDeficitKg, glycogen-bound water, blood volume); body mass has no single owner (nutrition, circulation, physiology); drug mass booked twice",
  ["realism.physiology.water_balance","realism.nutrition.energy_store","realism.nutrition.body_mass","realism.circulation.blood_ledger","realism.neurology.pk"],
  "realism.physiology.water_balance owns body water; realism.nutrition.body_mass the mass; others write deltas through them."),
 ("DUP-23","duplicate","Blood volume per kg and resting cardiac output in anatomy species profile and circulation",
  ["realism.anatomy.species_profile","realism.circulation.normal_blood_volume","realism.circulation.cardiac_output"],
  "realism.anatomy.species_profile holds the species parameter; circulation reads it."),
 ("DUP-24","duplicate","Resting metabolic rate: Mifflin (physiology), Kleiber (anatomy), host-set props.rmr_kcal_day, physics.restingMetabolicRate",
  ["realism.physiology.rmr","realism.nutri.rmr_mifflin","realism.anatomy.species_profile","pirate.doc.physiology.rmr"],
  "realism.physiology.rmr with the equation chosen per species profile."),
 ("DUP-25","duplicate","Gas tolerance thresholds in anatomy respiratory profile, medicine air conditions and atmosphere thresholds",
  ["realism.anatomy.respiratory_profile","realism.medicine.air_conditions","realism.gas.thresholds_layering"],
  "realism.gas.thresholds_layering for exposure, realism.medicine.air_conditions for effects; anatomy keeps species tolerance data only."),
 ("DUP-26","duplicate+unit","Labour supply in five homes: population labour (health applied twice), settlement LabourProvider, economy LabourSupplyProvider, ecology labour per hectare, recipes labourPerUnit; worker-days vs hours (Q15), hoursPerDay 10 vs 11 (SET-12)",
  ["realism.population.labour","shared.labour.provider_draw","shared.contract.labour_supply_provider","settlement.production.labour_cap","economy.recipe.rates","pirate.eco.crops_table"],
  "Society (population) supplies person-hours; settlement assigns; economy prices; one unit: person-hours."),
 ("DUP-27","duplicate","Stock creation by three paths (settlement Q -> produce, economy abstract market, host addStock); production recorded twice (DayProduction vs producedLast)",
  ["settlement.production.constraint_Q","economy.material.produce","economy.production.abstract_market","economy.market.observed_production"],
  "economy.material.produce is the only way goods appear; settlement computes capacity Q; one production record (economy's)."),
 ("DUP-28","duplicate","Wages: settlement pays a fixed Post.wage; economy wage_quote is a query nothing consumes",
  ["settlement.wage.pay","settlement.wage.set_wage","economy.labour.wage_quote"],
  "economy.labour.wage_quote sets the level (once Rex answers Q10/§12.6); settlement.wage.pay executes it."),
 ("DUP-29","duplicate","Two labour-supply interfaces, neither implemented",
  ["shared.labour.provider_draw","shared.contract.labour_supply_provider"],"one interface, implemented by the future Society population."),
 ("DUP-30","duplicate","Ledger, Rates and equipment list declared in both engines (StubLedger/LedgerRow vs Transaction)",
  ["settlement.ledger.pay","shared.contract.ledger_provider","economy.recipe.rates","settlement.production.equipment_cap"],
  "settlement ledger (contract agreed); shared types in one package."),
 ("DUP-31","duplicate","Shortage computed twice inside economy (unclamped in consumption, clamped in queries.shortage)",
  ["economy.consumption.demand","economy.shortage.event"],"economy.shortage.event."),
 ("DUP-32","duplicate","Reducer, Runner, ctx, mint, must, finite copied in three engines; three id schemes",
  ["settlement.infra.reducer_replay","economy.infra.reducer_replay","settlement.infra.id_scheme","economy.infra.id_scheme","realism.infra.component_registry"],
  "a shared kernel package (new, infra)."),
 ("DUP-33","duplicate","Clocks: realism scheduler (1 s), settlement day, economy day, StubLedger day, alignment tick, BODY.md overnight tick; nothing converts between them",
  ["realism.infra.scheduler","settlement.infra.tick_scheduler","economy.infra.tick_scheduler","shared.contract.day_order","pirate.body.overnight_tick","pirate.align.step"],
  "a universal time and event scheduler (new, ENGINES.md 'shared infrastructure still missing')."),
 ("DUP-34","ownership","Weather generator exists only in pirate game code (places.ts daily Markov chain, replays from day 1); realism has none",
  ["pirate.env.weather_markov","pirate.env.climate_monthly","realism.env.place_process"],
  "realism environment (a universal weather and climate mechanism); the Caribbean climate rows stay plugin data."),
 ("DUP-35","duplicate","Vector/mosquito exposure multipliers in environment exposure table and pirate adapters/medicine.ts multiplierOf; season defined in ENVIRONMENT climate and ECOLOGY calendar",
  ["realism.env.exposure_by_terrain","pirate.eco.calendar","pirate.env.climate_monthly"],"realism.env.exposure_by_terrain; one season definition in environment."),
 ("DUP-36","duplicate","Injury: COMBAT wound ladder, HP and Endurance pool vs realism medicine wounds, circulation bleeding, crisis",
  ["pirate.combat.wound_ladder","pirate.combat.regional_damage_dip","realism.medicine.wounds","realism.circulation.bleeding_class","realism.anatomy.crisis_floors"],
  "realism owns injury physiology; combat reads it (CMB-11's proposed §9 interfaces)."),
 ("DUP-37","double-penalty","Vision dips from several sources: CHEMISTRY smoke 'Eyesight x0.6', COMBAT head-wound dips, (optics planned)",
  ["pirate.body.head_attrs_today","pirate.combat.regional_damage_dip","realism.optics.light_visibility"],"the capability aggregator (DUP-15) with optics as the physical input."),
 ("DUP-38","duplicate","'State' multiplier stated three ways (STATS 6 items, BODY 3, PSYCHOLOGY 6); drinkFactor a STATS placeholder while neurology produces the real output",
  ["pirate.body.state_multiplier","pirate.stats.performance","pirate.psych.pushes","realism.neurology.circuits"],
  "pirate BODY.md for the multiplier (pirate gameplay); neurology for intoxication."),
 ("DUP-39","duplicate","Town alignment rule in code (web/src/alignment) and in town ENDINGS/UPGRADES docs",
  ["pirate.align.town_aggregate","pirate.align.perfect_town"],"pirate balance code; docs point to it."),
 ("DUP-40","duplicate+unit","Room box model written in three places (ENGINE.md, GAS_DYNAMICS.md, atmosphere.ts) with ACH converted /3600 in one doc and /60 in the other",
  ["realism.gas.room_box","pirate.gas.box_model","pirate.atm.ventilation_ach"],"realism.gas.room_box; docs point to it."),
 ("DUP-41","ownership","Population and demography live in Reality (population.ts, world/POPULATION.md) but belong to Society (CTRL-5); population takes a game 'reputation' input",
  ["realism.population.cohort_tick","realism.population.migration","realism.population.labour","pirate.pop.vital_rates","pirate.pop.recruit_pool"],
  "a Society engine (new); Reality keeps biological reproduction, ageing and mortality (ENGINES.md boundary)."),
 ("DUP-42","ownership","Taxation: settlement wages.ts publicWorks is an empty stub; taxes belong to the future Government engine",
  ["settlement.wage.pay","settlement.authority.office_powers"],"Government (new); settlement records office holders only (ENGINES.md contract)."),
 ("DUP-43","ownership","Property valuation (PriceProvider.valueOf) declared, never implemented or called; money created/destroyed by credit/debit outside conservation, no money-supply owner",
  ["shared.contract.price_provider","economy.price.rule","settlement.ledger.pay"],"economy (pricing and money supply), pending Rex §12.3."),
 ("DUP-44","ownership","Inventory identity: Project.account used as both money holder and inventory id; economy keys inventories by inv.* with a separate holder",
  ["settlement.project.construction","shared.contract.inventory_ownership","economy.inventory.holdings"],"economy owns inventories; settlement passes an inventory id distinct from the account."),
 ("DUP-45","overlap","Burial, sanitation, waste scoped in three engines (settlement PACKAGES §8, economy PLAN step 12, realism Phase 11)",
  ["settlement.scope_added.cemetery_sanitation_landuse","economy.burial_waste","realism.waste.sanitation_decomposition"],
  "keep the ENGINES.md split (settlement: land and infrastructure; economy: services and flows; realism: decomposition and exposure); a contract before code."),
 ("DUP-46","duplicate","Personality: 16 hand-authored MBTI response charts in alignment, STATS personality type and sliders, PSYCHOLOGY.md",
  ["pirate.align.response_chart","pirate.stats.personality_type","pirate.stats.personality_sliders","pirate.psych.pushes"],
  "Cognition (new) with the eight-function model as one optional configurable model (decided, CTRL-7); the pirate charts stay pirate."),
 ("DUP-47","ownership","Endurance pool owned three ways: formula in BODY §3 (with heatFactor), PHYSIOLOGY §6 (without), spent by COMBAT",
  ["pirate.body.endurance_pool","pirate.combat.endurance_efficiency","pirate.phys.fatigue_day"],"pirate BODY.md (pirate gameplay over DUP-13's universal fatigue)."),
]

UNITS = [
 ("UNIT-1","realism.circulation.blood_ledger / realism.nutrition.pools","circulation writes blood_lost_ml (mL); nutrition's iron-loss rule reads blood_lost_l (L); nothing writes blood_lost_l, so haemorrhage never costs iron outside tests","a wiring bug, not a design question"),
 ("UNIT-2","realism.env.wbgt_bom / room.props.rh","relative humidity in percent in environment.ts, a fraction in room props (capped at 1.5)","one unit: fraction"),
 ("UNIT-3","pirate.gas.box_model / pirate.atm.ventilation_ach","ENGINE.md Q = ACH V/3600 (per second); GAS_DYNAMICS.md Q = ACH V/60 (per minute); code uses per-minute flow","docs restate the code's unit"),
 ("UNIT-4","realism.circulation.aerobic_today","mL O2/min in code; an index ~20-65 (divided by 40) in PHYSIOLOGY/BODY docs","see DUP-14"),
 ("UNIT-5","realism.physiology.rmr / realism.thermo.metabolic_heat","kcal/day vs W; kcal (props) vs J (trace) via KCAL_J","SI internally, kcal only at the edge"),
 ("UNIT-6","realism.gas.* / realism.atmos.barometric_pressure","Pa (physics) and mmHg (atmosphere, physiology) both in use; converted by MMHG_PER_PA","acceptable; declare per interface"),
 ("UNIT-7","realism.eco.logistic_stock","step in days, r per year; stock B in 'catch-days' or head count, not kg: cannot join goods mass","state biomass in kg or head with a conversion"),
 ("UNIT-8","realism.gas.grid_transport","diffusion, rise and settle as fractions per step: results depend on cell size and dt","physical D (m2/s) and velocities"),
 ("UNIT-9","realism.population.* / realism.medicine.* / realism.circulation.*","per year /365, per day, per second, per hour: conversions inline and undocumented; circulation hazards mix units per event","declare a timescale per mechanism (registry field)"),
 ("UNIT-10","realism.nutrition.pools","sodium/magnesium loss reads sweat_kg as litres","explicit density"),
 ("UNIT-11","shared.labour.* / settlement.production.labour_cap / economy.recipe.rates","worker-days vs hours per unit (Q15); hoursPerDay 10 (no source) vs 11 (Voth, SET-12); wage per day ignores hours","person-hours"),
 ("UNIT-12","economy.*","money, weight and volume unitless; base prices null; Good.weight stored, never used; no currency unit (GOODS Open 2)","a currency and mass unit per good"),
 ("UNIT-13","settlement.day / economy.day / StubLedger.day / realism t","three day counters plus seconds; economy.tick takes no day argument though CONTRACTS §9 says tick(N)","one clock (DUP-33)"),
 ("UNIT-14","pirate.eco.crops_table / realism.eco.soil_fertility","yield in t/ha with a unitless soil index; no nutrient or mass balance","soil nutrients in kg/ha"),
 ("UNIT-15","realism.neurology.baseline_drivers","neurology reads props pain, hunger, fever, starvation_stage, liver_function; medicine writes outputs['medicine.pain'], anatomy outputs.liver; nothing writes hunger, fever or starvation_stage","interface by registry id, not prop name"),
]

# Refinement B (Rex, 2026-10-30): closure removes duplicate AUTHORITY, not every related calculation.
# authority classes:
#   duplicate-authority : two homes own or compute the same state/value; one must become a read
#   aggregation         : a detailed and an aggregate computation coexist legitimately, provided one owner
#                         holds the state and the aggregation interface is documented
#   mixed               : part legitimate aggregation, part duplicate authority (both named)
#   ownership-gap       : no owner, or the owner is in the wrong engine
#   shared-part         : distinct mechanisms that should share a helper or a boundary contract
AUTH = {
 "DUP-1": ("duplicate-authority", ""), "DUP-2": ("duplicate-authority", ""), "DUP-3": ("duplicate-authority", ""),
 "DUP-4": ("duplicate-authority", ""), "DUP-5": ("duplicate-authority", ""), "DUP-6": ("shared-part", ""),
 "DUP-7": ("duplicate-authority", "the immersion table may stay as validation data"),
 "DUP-8": ("duplicate-authority", ""),
 "DUP-9": ("mixed", "building and equipment condition are legitimate aggregate states over physical decay; spoilage's own constant rate is a duplicate"),
 "DUP-10": ("duplicate-authority", ""), "DUP-11": ("duplicate-authority", ""), "DUP-12": ("duplicate-authority", ""),
 "DUP-13": ("mixed", "per-muscle 3CC (detail) and whole-body MET-hours (aggregate) may coexist with a declared relation; the doc fatigueDay and the pool are duplicates"),
 "DUP-14": ("duplicate-authority", ""), "DUP-15": ("duplicate-authority", ""), "DUP-16": ("duplicate-authority", ""),
 "DUP-17": ("duplicate-authority", ""), "DUP-18": ("duplicate-authority", ""),
 "DUP-19": ("mixed", "individual and aggregate mortality coexist legitimately (one per resolution); the five individual sources without one cause ledger are duplicate authority"),
 "DUP-20": ("aggregation", "the population epidemic is the expected-value aggregate of medicine's course; legitimate once it reads medicine's parameters and a test checks mean agreement"),
 "DUP-21": ("mixed", "population foodDays is an aggregate of nutrition; the adapter rations and economy per-capita consumption are two authorities for one flow"),
 "DUP-22": ("duplicate-authority", ""), "DUP-23": ("duplicate-authority", ""), "DUP-24": ("duplicate-authority", ""),
 "DUP-25": ("duplicate-authority", ""),
 "DUP-26": ("mixed", "population labour (aggregate supply) and settlement assignment (detail) are legitimate layers; the two provider interfaces and two units are duplicates"),
 "DUP-27": ("duplicate-authority", ""), "DUP-28": ("duplicate-authority", ""), "DUP-29": ("duplicate-authority", ""),
 "DUP-30": ("duplicate-authority", ""), "DUP-31": ("duplicate-authority", ""), "DUP-32": ("duplicate-authority", ""),
 "DUP-33": ("mixed", "different tick rates per engine are legitimate under one clock; independent counters with no conversion are duplicate authority over time"),
 "DUP-34": ("ownership-gap", ""), "DUP-35": ("duplicate-authority", ""), "DUP-36": ("duplicate-authority", ""),
 "DUP-37": ("duplicate-authority", ""), "DUP-38": ("duplicate-authority", ""), "DUP-39": ("duplicate-authority", ""),
 "DUP-40": ("duplicate-authority", "doc-level only"), "DUP-41": ("ownership-gap", ""), "DUP-42": ("ownership-gap", ""),
 "DUP-43": ("ownership-gap", ""), "DUP-44": ("duplicate-authority", ""), "DUP-45": ("shared-part", ""),
 "DUP-46": ("ownership-gap", "the universal model does not exist; the pirate charts stay pirate (CTRL-7)"),
 "DUP-47": ("duplicate-authority", ""),
}
# Presentation batches (batch 1 set by the controller 2026-10-30; 2-5 proposed by the registry keeper)
BATCH = {}
for b, ids in {
    1: [33, 32, 22, 44, 5, 24, 13, 14, 18, 26, 28, 29, 19, 20],
    2: [15, 16, 17, 37, 38, 47, 12, 11, 23, 25, 21],
    3: [1, 2, 3, 4, 6, 7, 8, 10, 40, 9],
    4: [27, 30, 31, 43, 45, 42],
    5: [34, 35, 36, 39, 41, 46],
}.items():
    for i in ids: BATCH[f"DUP-{i}"] = b
assert sorted(BATCH) == sorted(AUTH) and len(BATCH) == 47

# Rex, 2026-10-30 (ENGINES.md "The approved organisation"): cellular biology, a foundational Life & Species layer
# (CELLULAR.md) of cell populations with representative states; ageing emergent, never a timer. Planned rows.
_CELL_HOME = "Toolchain/realism/CELLULAR.md (planned; ENGINES.md 'Cellular biology', Rex 2026-10-30)"
_CELL = [
 ("population_state", "Cell populations with representative states",
  "per tissue: cell count, size, capacity, energy, damage, repair, senescent fraction, turnover; resolution raised locally for an experiment"),
 ("atp_flux", "Cellular ATP production and use (flux, never a stored pool)",
  "substrate oxidation and mitochondrial capacity supply ATP flux; demand from work, synthesis, repair"),
 ("mitochondrial_function", "Mitochondrial function", "capacity and efficiency per population; damage lowers it"),
 ("dna_damage_repair", "DNA damage and repair", "damage inflow (oxidative, toxic, radiation) against repair capacity"),
 ("telomeres", "Telomere attrition", "per division in dividing populations"),
 ("senescence", "Cellular senescence", "senescent fraction from damage and telomeres; secretes inflammatory signals"),
 ("proteostasis", "Proteostasis", "protein synthesis, folding and clearance capacity against load"),
 ("stem_cell_pools", "Stem-cell populations", "pool size and output set turnover and regeneration"),
 ("epigenetic_regulation", "Epigenetic regulation", "regulatory state changing expression with history"),
 ("inflammation_signalling", "Inflammation and immune signalling", "cytokine-level signals between populations"),
 ("death_replacement", "Cell death and replacement", "apoptosis, necrosis, replacement from stem pools; organ capacity = f(population)"),
 ("ageing_emergent", "Ageing as an emergent output", "organ capacity decline emerges from the states above; never a timer on organ performance"),
]
EXTRA_ROWS = [{
    "id": f"realism.cellular.{k}", "name": n, "engine": "realism", "home": _CELL_HOME, "status": "planned",
    "domain": "B", "scope": "universal", "inputs": [], "outputs": [], "state": "planned",
    "formulation": f, "dependencies": [], "timescale": "planned", "invariants": "planned",
    "sources": "to research; established processes labelled apart from simplified or experimental ageing models (Rex)",
    "evidence": "?", "approximations": "cell populations with representative states, never individual cells",
    "tests": "none", "consumers": ["metabolism", "muscle adaptation", "nutrition", "medicine", "healing", "toxicology", "reproduction", "organ capacity"],
    "notes": "registry task R-CELL after P0 and P1: audit what moves under cellular ownership (DUP-17 among it)",
    "audit_batch": "rex-2026-10-30",
} for k, n, f in _CELL]

# Interfaces that look like overlaps but are hand-offs (recorded so nobody 'closes' them).
INTERFACES = [
 ("IF-1", "realism.infra.crisis_record", "pirate.align.fates_forms",
  "Death to fate: Reality decides biological failure, with a crisis before every death; the pirate fate system decides what a dead character becomes. The two rules are compatible (Rex, 2026-10-30). This is a hand-off, never an overlap: the plugin reads the death, and Reality never reads the fate.",
  ["DUP-19", "DUP-20"]),
]

# Decisions per overlap group. state: proposed -> closing (owner approved) -> closed (re-audited).
# progress: ordered events {date, step: agreed | units queued | closed, by, commit?, note?}.
DECISIONS = {}
for _n in [33, 32, 22, 44, 5, 24, 13, 14, 18, 26, 28, 29, 19, 20]:
    DECISIONS[f"DUP-{_n}"] = {"decision": "owner approved as proposed (Rex, 2026-10-30; OVERLAPS-BATCH-1.md)",
                              "state": "closing", "progress": []}

# --- closure events (append-only) ---
DECISIONS["DUP-44"]["progress"] += [
    {"date": "2026-10-30", "step": "agreed", "by": "Settlement + Economy", "note": "CONTRACTS.md s15"},
    {"date": "2026-10-30", "step": "closed", "by": "Settlement keeper",
     "commit": "settlement efc72cf; economy d84785a; pirate-ship fc83089",
     "note": "Project.inventory apart from Project.account; U16 and I1b"},
    {"date": "2026-10-30", "step": "re-audited", "by": "registry keeper",
     "note": "committed CONTRACTS.md byte-identical in both repos (md5 0fe282f5); settlement 27/27 incl. U16; pirate src/economy 4/4 incl. I1, I1b, I2"},
]
DECISIONS["DUP-44"]["state"] = "closed"
for _g in ("DUP-26", "DUP-28", "DUP-29"):
    DECISIONS[_g]["progress"].append({"date": "2026-10-30", "step": "contract proposed", "by": "Settlement keeper",
        "note": "settlement CONTRACTS s16 (one LabourSupply interface in person-hours) and s17; economy P1.md 2c4caa3; not yet agreed"})

# Row patches from closed groups (applied by build.py after the extracts are merged).
ROW_PATCHES = {
    "shared.contract.inventory_ownership": {"home": "Toolchain/settlement/CONTRACTS.md s2 and s15 (= Toolchain/economy/CONTRACTS.md)",
        "notes": "DUP-44 closed 2026-10-30: a project carries Project.inventory (economy inv.* ref) apart from Project.account (money)."},
    "settlement.project.construction": {"notes": "DUP-44 closed 2026-10-30 (settlement efc72cf): materials drawn from Project.inventory, wages paid from Project.account; U16."},
}

# --- 2026-10-30: CONTRACTS s16 Labour agreed (groups 10-12) ---
for _g in ("DUP-26", "DUP-28", "DUP-29"):
    DECISIONS[_g]["progress"] += [
        {"date": "2026-10-30", "step": "agreed", "by": "Settlement + Economy",
         "commit": "settlement 70e3117; economy 91e374a",
         "note": "CONTRACTS s16 Labour (economy P1.md rev 2 with Settlement amendments A and B); committed copies byte-identical (md5 c520e57f, registry check)"},
        {"date": "2026-10-30", "step": "units queued", "by": "Settlement + Economy",
         "note": "settlement belt units 2617-2619, economy 2627-2632, all after kernel stage 2615"},
    ]
EXTRA_ROWS.append({
    "id": "shared.contract.labour_supply", "name": "LabourSupply interface (person-hours), CONTRACTS s16",
    "engine": "shared", "home": "Toolchain/settlement/CONTRACTS.md s16 (= economy); declaration in settlement/src/providers.ts and economy/src/providers.ts (identical text) when units 2617-2619 / 2627-2632 pass",
    "status": "planned", "domain": "D", "scope": "universal",
    "inputs": [{"name": "market, role, day, pool", "unit": "ids"}],
    "outputs": [{"name": "person-hours supplied and drawn", "unit": "person*h/d"}],
    "state": "stateless interface; the host's population model holds supply",
    "formulation": "hours(market, role, day), draw(...), available(person, day), productivity(holder, role): CONTRACTS s16",
    "dependencies": ["realism.population.labour"], "timescale": "day", "invariants": "Settlement never draws more than hours() reports; the host's draw enforces the day's cap",
    "sources": "CONTRACTS.md s16 (agreed 2026-10-30)", "evidence": "4", "approximations": "productivity relative to a standard worker",
    "tests": "settlement scripts/check-contract-text.ts; economy E17; settlement U17 (wages)",
    "consumers": ["settlement.production.labour_cap", "settlement.project.construction", "economy.labour.wage_quote"],
    "notes": "replaces shared.labour.provider_draw and shared.contract.labour_supply_provider (DUP-29); aliases recorded when the units pass",
    "audit_batch": "settlement-keeper-2026-10-30",
})
ROW_PATCHES.update({
    "shared.labour.provider_draw": {"superseded_by": "shared.contract.labour_supply", "notes": "CONTRACTS s16 agreed 2026-10-30 (settlement 70e3117): merged into shared.contract.labour_supply; retired (alias) when settlement units 2617-2619 pass."},
    "shared.contract.labour_supply_provider": {"superseded_by": "shared.contract.labour_supply", "notes": "CONTRACTS s16 agreed 2026-10-30 (economy 91e374a): merged into shared.contract.labour_supply; retired (alias) when economy units 2627-2632 pass."},
    "settlement.wage.set_wage": {"notes": "CONTRACTS s16 (agreed 2026-10-30): the only writer of Post.wage besides addPost (settlement U17, units 2617-2619)."},
})
# Quantities agreed in CONTRACTS s16 (names proposed by the Settlement keeper); they exist once the units pass.
EXTRA_QUANTITIES = [
 {"id": "settlement.labour.hours_assigned", "unit": "person*h/d", "scope": "settlement", "writer": "settlement.production.labour_cap",
  "description": "per business per day: the sum of its filled posts' hours x productivity"},
 {"id": "settlement.project.labour_hours", "unit": "person*h", "scope": "settlement", "writer": "settlement.project.construction",
  "description": "a project's remaining labour (was worker-days)"},
 {"id": "economy.labourhoursperunit", "unit": "person*h", "scope": "economy", "writer": "economy.recipe.rates",
  "description": "CONTRACTS s16 field labourHoursPerUnit: person-hours per output unit; added beside labourPerUnit by economy unit 2627, which unit 2630 removes (name and unit set by the economy keeper, 2026-10-30)"},
 {"id": "population.labour.person_hours", "unit": "person*h/d", "scope": "population", "writer": "realism.population.labour",
  "description": "person-hours per day by category (adult men, adult women, elders, children); Reality's population supply (its unit 2636)"},
 {"id": "settlement.config.hours_per_day", "unit": "h/d", "scope": "settlement", "writer": None, "kind": "quantity", "role": "parameter", "owner": "Settlement config (host-set)",
  "description": "the standard working day, read where days meet hours; 10 proposed, 11 researched (SET-12, Rex)"},
]
for _q in EXTRA_QUANTITIES:
    _q.update({"status": "agreed (CONTRACTS s16, 2026-10-30); exists once its belt units pass", "unit_source": "kernel units table symbols (kernel keeper)"})

# --- Rex 2026-10-30, ENGINES.md "Resolution of the biology": three records per organism; genetics planned ---
_GEN_HOME = "Toolchain/realism (Life & Species; planned; ENGINES.md 'Resolution of the biology', Rex 2026-10-30)"
def _planned(id_, name, form, consumers, notes=""):
    return {"id": id_, "name": name, "engine": "realism", "home": _GEN_HOME, "status": "planned", "domain": "B",
            "scope": "universal", "inputs": [], "outputs": [], "state": "planned", "formulation": form,
            "dependencies": [], "timescale": "planned", "invariants": "planned",
            "sources": "to research; established processes labelled apart from simplified or experimental models (Rex)",
            "evidence": "?", "approximations": "compact mathematical representations preserving causal effects, never DNA or cells in real form",
            "tests": "none", "consumers": consumers, "notes": notes, "audit_batch": "rex-2026-10-30"}
EXTRA_ROWS += [
 _planned("realism.records.genetic_profile", "Record 1: genetic profile",
          "stable inherited information: chromosome segments carrying trait-associated variants (linkage, polygenic effects, dominance, interactions); never independent trait sliders or a parental average",
          ["realism.genetics.*", "realism.development.trait_change", "reproduction"]),
 _planned("realism.records.cellular_state", "Record 2: cellular and developmental state",
          "per representative tissue population: repair capacity, accumulated damage D(t+1) = D(t) + damage - repair, regeneration, adaptation",
          ["realism.cellular.*", "organ capacity"], "the state the realism.cellular.* mechanisms write"),
 _planned("realism.records.organism_state", "Record 3: organism state",
          "anatomy, organs, muscles, nutrients, immunity, capabilities (the existing realism body state, organised as one record)",
          ["realism.capacity.functional", "plugin views"], "today's body props and outputs are its precursor"),
 _planned("realism.genetics.recombination", "Recombination", "crossover between homologous chromosome segments at meiosis; linkage follows segment distance", ["realism.genetics.inheritance"]),
 _planned("realism.genetics.inheritance", "Inheritance", "each parent transmits one recombined copy per chromosome; the child's profile is a new genome, never an average", ["realism.records.genetic_profile"]),
 _planned("realism.genetics.mutation", "Mutation", "new variants at a per-segment rate per generation", ["realism.records.genetic_profile"]),
 _planned("realism.genetics.expression_response", "Gene expression responses", "variant effects expressed in response to training, nutrition, hormones, development and environment (with the epigenetic regulation row)",
          ["realism.development.trait_change", "realism.cellular.epigenetic_regulation"]),
 _planned("realism.development.trait_change", "Trait change from genes and conditions",
          "dM = f(G, T, N, H, R): genetics, training stimulus, nutrition, hormones and development, recovery (e.g. muscle growth); nobody inherits a Strength score",
          ["realism.muscular.adaptation_day", "realism.records.organism_state"], "the muscular adaptation already built is its first instance"),
 _planned("realism.genetics.population_distribution", "Aggregate genetic and health distributions",
          "distant populations carry distributions of variants and health states instead of individual genomes; named characters get tissue-level detail (refinement B: an aggregate of the individual records)",
          ["population (Society)", "History"]),
]
INTERFACES.append(("IF-2", "realism.records.organism_state", "pirate.stats.attribute_value",
  "Character sheet as a view (Rex, 2026-10-30): a character sheet is a view of the three organism records, never a second source of numbers. STATS.md attributes (Rex's gameplay design: scale, Poise, Efficiency) are computed from the records through the pirate adapter; nobody inherits a Strength score.",
  ["DUP-15", "DUP-17"]))
ROW_PATCHES.update({
    "realism.cellular.population_state": {"formulation": "per tissue population: size, capacity, energy, damage, repair, senescent fraction, turnover; damage D(t+1) = D(t) + damage - repair; writes realism.records.cellular_state"},
    "realism.cellular.dna_damage_repair": {"formulation": "D(t+1) = D(t) + damage inflow (oxidative, toxic, radiation) - repair capacity, per tissue population"},
    "pirate.stats.attribute_value": {"notes": "Rex 2026-10-30: the character sheet is a view of the three organism records (IF-2); genetic min-max per attribute to be reconciled with realism.records.genetic_profile in the R-CELL audit and the plugin track (PL); the 1-20 scale stays Rex's design."},
})

# --- PLATFORM.md §11a (Rex 2026-10-30): verification and validation ---
# Combined tests that run several mechanisms together (integration evidence). Members are registry ids.
_CK1 = ["realism.env.diurnal_curve", "realism.env.wbgt_bom", "realism.env.place_process", "realism.gas.room_box",
        "realism.gas.sources_sinks", "realism.gas.breathing_process", "realism.gas.alveolar_po2", "realism.gas.hb_saturation",
        "realism.gas.ventilation_drive", "realism.physiology.energy_expenditure", "realism.physiology.rmr", "realism.physiology.pal",
        "realism.physiology.sleep_debt", "realism.physiology.circadian", "realism.physiology.alertness",
        "realism.physiology.fatigue_met_hours", "realism.physiology.wbgt_core_drift", "realism.physiology.core_state",
        "realism.physiology.heat_balance", "realism.physiology.body_area", "realism.physiology.sweat",
        "realism.physiology.water_balance", "realism.physiology.urine", "realism.physiology.metabolic_water",
        "realism.physiology.hydration_band", "realism.nutrition.pools", "realism.nutrition.absorption",
        "realism.nutrition.eat_meal", "realism.nutrition.energy_store", "realism.nutrition.body_mass",
        "realism.nutrition.requirement", "realism.neurology.baseline_drivers", "realism.neurology.tone",
        "realism.neurology.circuits", "realism.neurology.sleep_wake", "realism.neurology.breathing_drive",
        "realism.infra.world_conservation", "realism.infra.scheduler", "realism.infra.trace"]
CHAINS = [
 {"id": "realism:checkpoint1-human-week", "test": "realism test/checkpoint1.test.ts, test/hydration-week.test.ts; examples/human-week.ts (CHECKPOINTS.md Checkpoint 1, 2540, 2565)",
  "complete": True, "conservation": "energy (intake - expenditure = storage within 1 %), body and body+room water, nutrient masses, room O2/CO2/N2 and elements, every step; all outputs finite",
  "members": _CK1},
 {"id": "realism:checkpoint2-human-wound", "test": "realism test/checkpoint2.test.ts; examples/human-wound.ts (CHECKPOINTS.md Checkpoint 2: partial, acceptance blocked)",
  "complete": False, "conservation": "blood received - lost = volume change (1e-6); every death opens a crisis",
  "members": _CK1 + ["realism.anatomy.assembly", "realism.anatomy.organ_function", "realism.anatomy.damage_repair",
      "realism.anatomy.tissue_collagen", "realism.anatomy.crisis_floors", "realism.anatomy.feed_gate",
      "realism.circulation.blood_ledger", "realism.circulation.normal_blood_volume", "realism.circulation.bleeding_class",
      "realism.circulation.bleed_rate", "realism.circulation.o2_delivery", "realism.circulation.cardiac_output",
      "realism.circulation.aerobic_today", "realism.circulation.volume_recovery", "realism.circulation.hazards",
      "realism.medicine.wounds", "realism.medicine.healing_multiplier", "realism.medicine.pain", "realism.medicine.process",
      "realism.muscular.fatigue_3cc", "realism.muscular.activation", "realism.infra.crisis_record"]},
 {"id": "realism:independence-horse", "test": "realism test/independence.test.ts; examples/horse-stable.ts (CHECKPOINTS.md Independence)",
  "complete": True, "conservation": "as checkpoint 1 for the modules used",
  "members": ["realism.physiology.energy_expenditure", "realism.physiology.rmr", "realism.physiology.heat_balance",
      "realism.gas.breathing_process", "realism.gas.room_box", "realism.anatomy.species_profile", "realism.anatomy.assembly",
      "realism.anatomy.organ_function", "realism.infra.world_conservation"]},
 {"id": "realism:still", "test": "realism test/still.test.ts (lab/still.ts)", "complete": True,
  "conservation": "substance mass and element atoms per step",
  "members": ["realism.infra.still_scenario", "realism.thermo.boiling", "realism.thermo.condensation_ntu",
      "realism.thermo.counterflow_ntu", "realism.thermo.natural_convection_cylinder", "realism.thermo.heat_flow_UA",
      "realism.thermo.water_vapour_pressure", "realism.thermo.water_latent_heat", "realism.chem.carbon_combustion_charcoal",
      "realism.infra.thermometer_drift", "realism.infra.operator_control", "realism.equip.wear_by_temperature",
      "realism.atmos.barometric_pressure", "realism.infra.world_conservation"]},
 {"id": "pirate:economy-I1-I2-thirty-days", "test": "pirate-ship web/src/economy/economy.test.ts I1, I1b, I2 (Toolchain/economy/TESTS.md)",
  "complete": True, "conservation": "every invariant of both engines checked daily for thirty days (ledger balances, stock non-negative)",
  "members": ["settlement.production.constraint_Q", "settlement.production.equipment_cap", "settlement.production.labour_cap",
      "settlement.wage.pay", "settlement.ledger.pay", "settlement.business.staffing", "settlement.project.construction",
      "settlement.building.condition_decay", "settlement.expiry", "settlement.infra.tick_scheduler",
      "economy.material.produce", "economy.material.available", "economy.inventory.holdings", "economy.recipe.rates",
      "economy.spoilage", "economy.consumption.demand", "economy.shortage.event", "economy.price.rule",
      "economy.accounting.view", "economy.infra.tick_scheduler", "shared.contract.material_provider",
      "shared.contract.ledger_provider", "shared.contract.settlement_reader", "shared.contract.day_order",
      "shared.contract.inventory_ownership"]},
 {"id": "economy:three-ports", "test": "Toolchain/economy examples/three-ports.ts; test/labour-and-sim.test.ts", "complete": True,
  "conservation": "ledger and stock invariants",
  "members": ["economy.production.abstract_market", "economy.trade.trade", "economy.trade.shipment", "economy.price.rule",
      "economy.consumption.demand", "economy.spoilage", "economy.shortage.event", "economy.labour.wage_quote",
      "economy.accounting.view", "economy.inventory.holdings", "economy.org.organisation"]},
]
# Validation evidence the registry keeper could find (independent data, not the source formula itself).
# None is yet re-audited as independent; "candidate" means a test compares with measured or published values.
VALIDATION_CANDIDATES = {
 "realism.atmos.barometric_pressure": "still.test: water boils at about 92.5 C at 2,256 m (measured boiling points at altitude)",
 "realism.thermo.water_boiling_point": "boiling point vs pressure against steam tables",
 "realism.physiology.sweat": "hydration-week: hot-fixture sweat 0.73 L/h inside the source's 0.5-2.5 L/h (same source as the cap: not independent)",
 "realism.gas.room_box": "checkpoint 1: CO2 peak within 1 % of the analytic box solution (verification of the equation, not validation)",
}
DECISIONS["DUP-44"]["progress"].append({"date": "2026-10-30", "step": "re-audited (11a criteria)", "by": "registry keeper",
    "note": "implemented: U16; integrated: I1b runs settlement and economy together through the contract (ports after P0); validated: n/a (an identity rule, no empirical behaviour)"})

# --- 2026-10-30: V&V results reported by owners, and reviews (Toolchain/REVIEWS.md) ---
VV_OVERRIDES = {
    "settlement.building.condition_decay": {"validated": "failed (SET-20)", "evidence": "VALIDATION.md (settlement 5a0603b): new to ruined in 850 days vs sourced years to decades; REVIEWS.md R-2"},
    "settlement.building.condition_output_factor": {"validated": "failed (SET-20)", "evidence": "as condition_decay; output factors level 5, no source"},
}
ROW_PATCHES.update({
    "settlement.building.condition_decay": {"evidence": 5, "evidence_note": "hypothesis, no source (settlement VALIDATION.md)"},
    "settlement.building.condition_output_factor": {"evidence": 5, "evidence_note": "hypothesis, no source (settlement VALIDATION.md)"},
})
for _g, _u, _n in [("DUP-22", "2623", "water ledger; plasma term waits on 2643's unit and sign"),
                   ("DUP-20", "2626", "epidemic aggregate from remaining susceptibles"),
                   ("DUP-19", "2633", "one death per body, one cause; starvation opens a crisis"),
                   ("DUP-13", "2634", "one work record drives local and systemic fatigue"),
                   ("DUP-14", "2635", "Banister clamp the only pathway into aerobic_today")]:
    DECISIONS[_g]["progress"] += [
        {"date": "2026-10-30", "step": "units queued", "by": "Reality keeper", "note": f"realism unit {_u}: {_n}; after kernel 2607"},
        {"date": "2026-10-30", "step": "model reviewed", "by": "registry keeper", "note": "REVIEWS.md R-1: accepted" + ("" if _u == "2634" else " with conditions")},
    ]

# Quantity kinds (kernel convention, kernel unit 2648): quantity (default) | categorical | record | text.
# Non-quantity kinds carry unit null and are exempt from parsing; a port joins only the same kind.
_BUNDLE = "a bundle of numeric quantities with different units; split into one quantity each when the owner declares kernel.json ports"
QUANTITY_KINDS = {
 "air.outputs_o2_frac_co2_ppm_sao2_cohb_ventilation_l_": ("record", _BUNDLE),
 "air.thresholds": ("record", "list of gas thresholds (data)"),
 "air.converted": ("record", _BUNDLE),
 "body.absorbed_nutrients": ("record", _BUNDLE + " (per-nutrient absorbed masses)"),
 "body.bodyoutputs_medicine": ("record", "medicine outputs keyed by library id"),
 "body.cascade_statement_kineticsseconds": ("text", "the cascade statement; kineticsSeconds is null"),
 "body.class_i_iv": ("categorical", "haemorrhage class: I | II | III | IV"),
 "body.conc": ("record", _BUNDLE + " (g/dL for alcohol, mg/L for other drugs)"),
 "body.crisis": ("record", "a crisis record (IF-1)"),
 "body.crisis_record": ("record", "a crisis record (IF-1)"),
 "body.effect": ("categorical", "treatment effect: cure | stop-bleeding | immunise | none"),
 "body.immune_level": ("categorical", "immunity: lifelong | partial | none"),
 "body.need": ("record", _BUNDLE + " (per-nutrient requirements in table units)"),
 "body.numbers": ("record", _BUNDLE),
 "body.organ_tissue_components_graph_edges": ("record", "organ and tissue components and their graph edges"),
 "body.pool_level": ("record", _BUNDLE + " (per-nutrient pools in mg, mcg or g)"),
 "body.rate": ("record", _BUNDLE + " (hazard rates per day, per hour or per event)"),
 "body.respiratoryprofile": ("record", "a species respiratory profile"),
 "body.stage": ("categorical", "withdrawal stage: none | onset | seizure | delirium"),
 "body.stage_incubating_ill": ("categorical", "disease stage: incubating | ill (and recovered/dead per medicine)"),
 "body.wound_record": ("record", "a wound record"),
 "component.thickness_0_228_m_rho_1920_cp_790_u_2_11_h_10": ("record", _BUNDLE + " (wall thickness m, density kg/m3, cp J/(kg K), U W/(m2 K), h W/(m2 K))"),
 "place.props_outputs_by_id": ("record", "place outputs keyed by library id"),
 "place.wet": ("categorical", "wet | dry"),
 "world.crisis_record": ("record", "a crisis record (IF-1)"),
 "world.edge_lookups": ("record", "graph edge lookups"),
 "world.rows_keyed_by_column": ("record", "library rows keyed by column"),
 "world.stillresult": ("record", "the still scenario's result"),
 "world.trace_checks": ("record", "trace checks"),
 "world.world_advanced": ("record", "the advanced world state"),
}
QUANTITY_UNIT_FIX = {"body.withdrawal_swing": ("1", "a dimensionless tone index (neurology)")}
for _g in ("DUP-13", "DUP-14"):
    DECISIONS[_g]["progress"].append({"date": "2026-10-30", "step": "agreed", "by": "Combat keeper",
        "note": "CMB-12; marker realism/done/combat-agreed-groups-7-8.md; the pool rule is Rex's, the pool formula and /40 are proposed"})

# --- Rex 2026-10-30: Contact and Impact Mechanics, a P2 subsystem of Physical Reality ---
_CI_HOME = "Toolchain/realism (Physical Reality, P2 Contact and Impact Mechanics; planned; Rex 2026-10-30, Reality keeper's brief)"
def _ci(k, name, form, outputs, consumers, notes=""):
    r = _planned(f"realism.contact.{k}", name, form, consumers, notes)
    r.update({"home": _CI_HOME, "domain": "A", "outputs": outputs})
    return r
EXTRA_ROWS += [
 _ci("limb_geometry", "Articulated-limb geometry",
     "segments with lengths, masses and joint angles (from mechanics' segment model); hand-held objects as rigid extensions",
     [{"name": "segment poses", "unit": "m, rad"}], ["realism.contact.collision_detection", "realism.contact.point_velocity_mass"]),
 _ci("collision_detection", "Continuous collision detection",
     "swept volumes between steps, so a fast blade cannot pass through a limb between ticks; first time of contact",
     [{"name": "contact point and time", "unit": "m, s"}], ["realism.contact.impact_impulse"]),
 _ci("point_velocity_mass", "Per-point velocity and effective mass",
     "velocity of the contact point on a blade or fist from the limb chain; effective mass at that point from the chain's inertia",
     [{"name": "point velocity", "unit": "m/s"}, {"name": "effective mass", "unit": "kg"}], ["realism.contact.impact_impulse"]),
 _ci("impact_impulse", "Impact impulse and energy",
     "impulse J = integral of F dt from relative velocity, effective masses and restitution; energy delivered from the same",
     [{"name": "impulse", "unit": "N*s"}, {"name": "energy", "unit": "J"}], ["realism.contact.penetration", "realism.contact.contact_event"]),
 _ci("penetration", "Simplified penetration against a material resistance profile",
     "depth from delivered energy against layered resistance (skin, fat, muscle, bone; cloth, leather, mail)",
     [{"name": "wound depth", "unit": "m (reported with an uncertainty interval)"}],
     ["realism.medicine.wounds", "realism.materials.deformation_fracture_decay"],
     "wound depth is reported with its uncertainty (Rex): a simplified model, evidence level 4-5"),
 _ci("contact_event", "The contact event (interface emitter)",
     "one record per contact: position, relative velocity, direction, duration, impulse (and penetration result)",
     [{"name": "contact event", "unit": "record"}],
     ["realism.medicine.wounds", "realism.anatomy.damage_repair", "realism.materials.deformation_fracture_decay", "pirate.combat.hit_and_location"],
     "the one source of hit location and impact for every consumer"),
]
INTERFACES += [
 ("IF-3", "realism.contact.contact_event", "realism.medicine.wounds",
  "Contact to injury: Physical Reality emits a contact event (position, relative velocity, direction, duration, impulse, penetration); anatomy and medicine read it to make the wound; materials read it for damage to objects and armour. Physical Reality never decides the wound; medicine never recomputes the impact.",
  ["DUP-36", "DUP-37"]),
 ("IF-4", "realism.contact.contact_event", "pirate.combat.hit_and_location",
  "Contact to the combat plugin: the pirate combat rules read the contact event for hit location and impact instead of rolling them (supersedes the plugin's regional dip as the source of hit location); combat keeps its own rules for turns, actions and choices.",
  ["DUP-36"]),
]
EXTRA_QUANTITIES.append({"id": "world.contact_event", "kind": "record", "unit": None, "scope": "world", "writer": "realism.contact.contact_event",
  "description": "contact event: position (m), relative velocity (m/s), direction (unit vector), duration (s), impulse (N*s), penetration depth (m, with uncertainty)"})
VV_PLANNED_SPECS = {
 "realism.contact.contact_event": [
   "V-C1 blade position: the same cut lands with different impulse and depth by where on the blade it strikes (point velocity and effective mass vary along the blade)",
   "V-C2 punch angle: the same punch delivers different impulse by the angle of incidence (normal vs oblique components)",
   "V-C3 grazing hit on a moving defender: relative velocity and contact duration, not the attacker's swing alone, set the impulse; a defender moving away receives less",
 ],
 "realism.contact.penetration": ["wound depth reported with an uncertainty interval; checked against published penetration or ballistic-gelatin data where it exists, else labelled unvalidated"],
}
ROW_PATCHES.update({
 "pirate.combat.regional_damage_dip": {"superseded_by": "realism.contact.contact_event", "notes": "Rex 2026-10-30: Contact and Impact Mechanics (P2) supersedes this as the source of hit location (IF-4); the dip may remain the adapter's read of the wound state."},
 "pirate.combat.hit_and_location": {"notes": "Rex 2026-10-30: hit location comes from realism.contact.contact_event once P2 lands (IF-4); the plugin keeps its turn and action rules."},
})
GROUPS[:] = [(g[0], g[1], g[2], g[3] + (["realism.contact.contact_event"] if g[0] in ("DUP-36", "DUP-37") else []),
              g[4] + (" Contact and Impact Mechanics (P2, Rex 2026-10-30) is the source of hit location and impact (IF-3, IF-4)." if g[0] in ("DUP-36", "DUP-37") else ""))
             for g in GROUPS]

# Owner-resolved naming clashes (REG-16). qid -> (writer, kind, note)
QUANTITY_WRITER_FIX = {
 "economy.state": ("economy.infra.reducer_replay", "record",
   "the whole EconomyState container: reduce() (src/reduce.ts) is the only path that produces a new state; a tick is the command {type:'tick'} through reduce; each step's mechanism writes its own quantities (economy keeper, 2026-10-30)"),
}

# --- Quantity vocabulary edits confirmed by owners (applied by schema2.py, in order) ---
ALIASES = [
 {"old": "economy.recipe.labour_hours_per_unit", "new": "economy.labourhoursperunit", "date": "2026-10-30", "kind": "quantity",
  "reason": "the economy keeper (the writer's owner) set the name; the old id was a settlement-keeper proposal published briefly in quantities.json"},
]
QUANTITY_OPS = [
 ("retire", "settlement.state", None, "the settlement state container, not a quantity: every command writes it through settlement.infra.reducer_replay (settlement keeper, 2026-10-30)"),
 ("retire", "settlement.events", None, "events are the reducer's return value, not a quantity (settlement keeper, 2026-10-30)"),
 ("split", "settlement.cap", [
     ("settlement.production.equipment_cap_units", "count/d", "settlement.production.equipment_cap", "units per day the line's fixtures allow"),
     ("settlement.production.labour_cap_units", "count/d", "settlement.production.labour_cap", "units per day the line's labour allows")],
  "one seed name for two caps; materials and utilities caps come from providers and need no settlement quantity (settlement keeper, 2026-10-30)"),
 ("writer", "settlement.ledger_row", "settlement.ledger.pay", "the only code path that appends ledger rows (record and pay in context.ts); title transfer asks pay to write (settlement keeper, 2026-10-30)"),
 ("retire", "settlement.wage_ledger_rows", "settlement.ledger_row", "an alias of settlement.ledger_row (kind wage); settlement.wage.pay asks pay to write (settlement keeper, 2026-10-30)"),
 ("merge", ["settlement.business_status", "settlement.business_status_dormant_staffed_producing"], ("settlement.business.status", "categorical",
     "Business.status: dormant | staffed | producing"),
  "one field written by two mechanisms (staffing sets dormant/staffed, production sets producing/staffed): a duplicate authority inside Settlement (SET-21, DUP-48); both writers kept visible until the owner's fix lands"),
]
QUANTITY_PATCH = {
 "settlement.config.hours_per_day": {"written_by": "host (config input)", "role": "config", "status": "agreed (CONTRACTS s16); a host input, not written by a mechanism (settlement keeper, 2026-10-30)"},
}
GROUPS.append(("DUP-48", "duplicate", "Business.status written by two mechanisms: settlement staffing (dormant/staffed) and production (producing/staffed); found by the settlement keeper while resolving REG-16 (SET-21)",
  ["settlement.business.staffing", "settlement.production.constraint_Q"],
  "settlement.business.staffing as the one writer (dormant or staffed); 'producing' becomes a reading of the production record (q > 0 that day) through the existing economic() query"))
AUTH["DUP-48"] = ("duplicate-authority", "inside one engine")
BATCH["DUP-48"] = "owner"
DECISIONS["DUP-48"] = {"decision": "owner fix inside its boundary: an implementation defect against an approved model (PLATFORM.md §11a); SET-21", "state": "closing",
  "progress": [{"date": "2026-10-30", "step": "agreed", "by": "Settlement keeper", "note": "unit to be queued after kernel 2615"}]}
# DUP-48 correction (settlement keeper, 2026-10-30): the single writer is production, not staffing.
GROUPS[:] = [(g[0], g[1], g[2], g[3],
              "settlement.production.constraint_Q as the one writer (sets dormant, staffed or producing once per day); staffing keeps its outcome in the tick context only, never in state; end-of-day value, state and the pirate golden unchanged (settlement keeper's final design)")
             if g[0] == "DUP-48" else g for g in GROUPS]
DECISIONS["DUP-48"]["progress"].append({"date": "2026-10-30", "step": "units queued", "by": "Settlement keeper",
    "note": "settlement 2654 (2654-settlement-one-status-writer), needs only kernel 2599 (moved from 2615 to break the deadlock with kernel 2600); it also names settlement.business.status once in settlement's kernel.json. On pass: writer = settlement.production.constraint_Q, staffing dropped from candidate_writers"})
QUANTITY_OPS.append(("writer", "settlement.business.status", "settlement.production.constraint_Q",
    "fix landing in settlement 2654 (DUP-48, SET-21): production sets dormant, staffed or producing once per day; staffing keeps its outcome in the tick context. Set 2026-10-30, ahead of the code, at the settlement keeper's request so kernel 2600 is not paused; re-audited when 2654 passes"))
DECISIONS["DUP-48"]["progress"].append({"date": "2026-10-30", "step": "registry writer set ahead of the code", "by": "registry keeper",
    "note": "writer = settlement.production.constraint_Q, staffing dropped; DUP-48 stays closing until 2654 passes and is re-audited"})

# --- 2026-10-30 re-audits: settlement 2654 (DUP-48) and 2646 (R-2, SET-20) ---
DECISIONS["DUP-48"]["progress"] += [
    {"date": "2026-10-30", "step": "closed", "by": "Settlement keeper", "commit": "settlement 8dc8fcb (unit 2654)",
     "note": "staffing.ts has no status write; production the only status writer in the tick; U21 one event per change; kernel.json names settlement.business.status once"},
    {"date": "2026-10-30", "step": "re-audited", "by": "registry keeper",
     "note": "verified: in src/tick only production.ts calls setStatus; settlement 51/51 tests, typecheck clean; kernel check-registry.ts on settlement/kernel.json exits 0. Residual (REG-21, not blocking): the closeBusiness command (commands.ts L495-499) also sets dormant on close, a command-path write of the same value that production writes at the next tick"},
]
DECISIONS["DUP-48"]["state"] = "closed"
VV_OVERRIDES["settlement.building.condition_decay"] = {
    "validated": "candidate (interim class model, REVIEWS.md R-2; VAL-D1 passing)",
    "evidence": "settlement 79a848a (unit 2646): decay by material class from config decayClasses (palm thatch 5 y, reed thatch 25, wood shingle 25, tile or slate 50; masonry and wattle-and-daub null, flagged). VAL-D1 verifies the model reaches each configured lifetime within 1 % (verification against the config, not independent validation); the lifetimes are secondary and partly modern sources; band shape and roof-life assumption level 5. Unclassified buildings do not decay and are listed by unvalidatedDecay (VAL-D1a)."}
VV_OVERRIDES["settlement.building.condition_output_factor"] = {
    "validated": "no (level 5 hypothesis, no evidence)",
    "evidence": "the band output factors are unchanged by 2646 and have no source; the earlier failure (SET-20) was the timescale, now replaced by the class model"}
ROW_PATCHES["settlement.building.condition_decay"].update({"home": "Toolchain/settlement/src/tick/decay.ts decay(); config decayClasses, exposure, decayShares (settlement 79a848a)",
    "notes": "SET-20 fixed by unit 2646 (79a848a), interim class model (REVIEWS.md R-2), DUP-9's interim aggregate until the materials mechanism (P2 Phase 9)"})

# --- Cognition (P7) baseline rows proposed by the cognition keeper, 2026-10-30 (Toolchain/cognition/DESIGN.md §2, §5) ---
_COG_HOME = "Toolchain/cognition/DESIGN.md §2, §5 (planned; proposed by the cognition keeper 2026-10-30; Rex approves P7)"
def _cog(k, name, ev, form, writes, reads, notes=""):
    return {"id": f"cognition.{k}", "name": name, "engine": "cognition", "home": _COG_HOME, "status": "planned", "domain": "C",
            "scope": "universal", "inputs": [{"name": x, "unit": "see quantities.json"} for x in reads],
            "outputs": [{"name": x, "unit": "see quantities.json"} for x in writes], "state": "planned", "formulation": form,
            "dependencies": [], "timescale": "planned", "invariants": "planned", "sources": "DESIGN.md Sources (to be confirmed per unit)",
            "evidence": ev, "approximations": "baseline decision engine; see DESIGN.md §2", "tests": "none",
            "consumers": [], "notes": notes, "audit_batch": "cognition-keeper-2026-10-30", "planned_writes": writes}
EXTRA_ROWS += [
 _cog("attention.allocate", "Attention allocation", "4", "attention shares over stimuli by need priority (form: evidence 2; mapping 4)", ["mind.attention_share"], ["mind.need_priority"]),
 _cog("perception.detect", "Perception (signal detection)", "4", "signal detection theory over detectability d' (SDT: evidence 2)", ["mind.observation"], ["body.detectability", "mind.attention_share"],
      "reads body.detectability (Reality writes, counting sensory capacity once: DUP-37); never applies eyesight or hearing again"),
 _cog("belief.update", "Belief update", "4", "belief revision from observations and testimony, with conservatism (evidence 2)", ["mind.belief"], ["mind.observation", "mind.testimony"]),
 _cog("memory.episodic", "Episodic memory", "4", "episodes stored with prediction error; retrieval probability by forgetting curve (evidence 2)", ["mind.episode", "mind.retrieval_p"], ["mind.prediction_error"]),
 _cog("needs.drive", "Needs and drives", "4", "felt drive and priority from bodily deficit signals and safety beliefs", ["mind.need_deficit", "mind.drive", "mind.need_priority"], ["body.hunger_signal", "body.pain", "mind.belief"],
      "boundary (agreed 2026-10-30): Reality writes the deficit signal, Cognition the felt drive and priority; the drive never feeds back a second physiological effect; sleep reads the one sleep pressure (DUP-12)"),
 _cog("goals.objectives", "Goals and objectives", "4", "progress toward host-given goals from outcomes", ["mind.goal_progress"], []),
 _cog("decision.generate", "Action generation", "4", "candidate actions from the repertoire, beliefs and functional capacity", ["mind.candidates"], ["mind.belief", "body.capacity_functional"],
      "never computes strength or capacity: reads body.capacity_functional (DUP-15)"),
 _cog("decision.evaluate", "Action evaluation", "4", "expected utility with loss aversion (lambda: evidence 2)", ["mind.expected_utility"], ["mind.belief", "mind.episode", "mind.drive"]),
 _cog("decision.select", "Action selection", "4", "Luce choice (evidence 2) with commitment (evidence 5)", ["mind.intention"], ["mind.expected_utility"]),
 _cog("learning.outcome", "Learning from outcomes", "4", "prediction error from outcome events", ["mind.prediction_error"], []),
 _cog("learning.attribution", "Attribution", "5", "a read-out of belief.update before and after (never a second update): who or what is blamed", ["mind.attribution"], ["mind.belief"]),
 _cog("personality.slot", "Personality-model slot", None, "structural: modulates the attention, evaluation, selection and learning hooks; the null model by default", [], [],
      "DUP-46 proposed universal home (batch 5: Rex approves); the pirate charts and STATS sliders stay pirate (CTRL-7)"),
 _cog("personality.eight_function", "Eight-function personality model (second layer)", "5", "Rex's theory as a hypothesis, one optional configuration of the slot (DESIGN.md §9)", [], [], "CTRL-7; design only"),
] + [_cog(k, n, None, "reserved: named so nobody else builds it (DESIGN.md §5)", [], [], note) for k, n, note in [
 ("skill.practice", "Skill acquisition and decay", "the universal form of STATS skill, rust and talent (power law of practice and decay)"),
 ("emotion.appraisal", "Emotion appraisal", "the universal home of PSYCHOLOGY.md's stress and fear inputs; the pirate meters stay pirate"),
 ("communication.language", "Communication and language", "will write mind.testimony"),
 ("relationship.trust", "Relationships and trust", "the pirate hearts and trust stay pirate gameplay"),
 ("planning.lookahead", "Planning and lookahead", ""),
]]
_MIND = [("mind.attention_share", "1", "cognition.attention.allocate"), ("mind.observation", "record", "cognition.perception.detect"),
         ("mind.belief", "record", "cognition.belief.update"), ("mind.episode", "record", "cognition.memory.episodic"),
         ("mind.retrieval_p", "1", "cognition.memory.episodic"), ("mind.need_deficit", "1", "cognition.needs.drive"),
         ("mind.drive", "1", "cognition.needs.drive"), ("mind.need_priority", "1", "cognition.needs.drive"),
         ("mind.goal_progress", "1", "cognition.goals.objectives"), ("mind.candidates", "record", "cognition.decision.generate"),
         ("mind.expected_utility", "1", "cognition.decision.evaluate"), ("mind.intention", "record", "cognition.decision.select"),
         ("mind.prediction_error", "1", "cognition.learning.outcome"), ("mind.attribution", "record", "cognition.learning.attribution")]
for _id, _u, _w in _MIND:
    EXTRA_QUANTITIES.append({"id": _id, "kind": "record" if _u == "record" else "quantity", "unit": None if _u == "record" else _u,
        "scope": "mind", "writer": _w, "description": "Cognition baseline (DESIGN.md §5)", "status": "proposed (cognition keeper 2026-10-30); exists once P7 units pass"})
EXTRA_QUANTITIES += [
 {"id": "mind.testimony", "kind": "record", "unit": None, "scope": "mind", "writer": None, "written_by": "host (until cognition.communication.language)",
  "description": "what others tell an individual", "status": "proposed; host input"},
 {"id": "body.hunger_signal", "kind": "quantity", "unit": "1", "scope": "body", "writer": "realism.nutrition.hunger_fullness",
  "description": "the physiological hunger deficit signal (0-1); Cognition reads it as the hunger deficit, never writes it", "status": "proposed; the writer row is documented-only (to agree with the Reality keeper)"},
 {"id": "body.capacity_functional", "kind": "quantity", "unit": "1", "scope": "body", "writer": None,
  "description": "functional capacity per action class (0-1); written by the planned universal capacity mechanism of DUP-15", "status": "proposed; writer pending DUP-15 (batch 2)"},
 {"id": "body.detectability", "kind": "quantity", "unit": "1", "scope": "body", "writer": None,
  "description": "d' per observer, cue and channel: the signal at the observer (P2 optics, acoustics) with the observer's sensory capacity counted once (DUP-37); renamed from the proposed percept.detectability", "status": "proposed; writer pending P2 (a host-set stub until then)"},
]
ALIASES.append({"old": "percept.detectability", "new": "body.detectability", "date": "2026-10-30", "kind": "quantity",
  "reason": "a per-observer value in the body scope; never registered under the old name (cognition keeper's proposal)"})

GROUPS.append(("DUP-49", "duplicate", "Decision rows inside the nutrition library: 'appetite' (hunger x palatability x state, per food offered) and 'eating-rule' (eats if appetite > 0.3 or hunger > 0.8) decide what a person does, which is Cognition's drive, priority and selection; found by the Reality keeper against the cognition keeper's input contract (cognition DESIGN.md §8)",
  ["realism.nutrition.hunger_fullness", "cognition.needs.drive", "cognition.decision.select", "pirate.nutr.hunger_appetite"],
  "Reality keeps fullness and hunger as body signals (body.hunger_signal; the 'drive' wording becomes 'signal'); appetite's palatability and the eating rule go to Cognition (needs.drive, decision.select), or to the game where they are its content, and become restatements in nutrition.json. No code exists for either row"))
AUTH["DUP-49"] = ("duplicate-authority", "documented-only on both sides; nothing built")
BATCH["DUP-49"] = 2
QUANTITY_PATCH["settlement.business.status"] = {"external_writers": ["command closeBusiness (row settlement.business.open; settlement/src/commands.ts): sets dormant at once so a closed business reads dormant for the host and the story immediately; any later command that opens or closes a business likewise"],
    "writer_note": "inside the tick, settlement.production.constraint_Q is the only writer (DUP-48 closed); commands are external writers (REG-21, settlement keeper 2026-10-30)"}

# Rex approved the Cognition design 2026-10-30 (cognition 0291ac8); the needs.drive amendment (DESIGN.md §2.2).
for _r in EXTRA_ROWS:
    if _r["id"].startswith("cognition."):
        _r["home"] = "Toolchain/cognition/DESIGN.md (design approved by Rex 2026-10-30, cognition 0291ac8; lane running)"
ROW_PATCHES["cognition.needs.drive"] = {
    "formulation": "priority by motivational-pressure share: M_i = w_i * D_i * S_i, priority_i = M_i / sum(M) (replaces the drive-gradient share); reward = homeostatic drive reduction D(h) - D(h'); needs are data records {id, category, source: signal | appraisal | accumulator, setpoint, weight, salience tags}, never an enum (Rex's amendment, DESIGN.md §2.2)",
    "sources": "Cannon 1932 (homeostasis); Sterling & Eyer 1988 (allostasis); Deci & Ryan 2000 (self-determination theory); Maslow 1943 (classification only); Wahba & Bridwell 1976 (the critique of Maslow's hierarchy); RL, expected utility and active inference cited each with its evidence level (DESIGN.md §2.2)",
    "evidence": 4,
    "evidence_note": "homeostatic drive reduction rests on established physiology (2); the pressure-share priority is a modelling choice (4); Maslow is used for classification only",
    "state": "M_i is internal (no quantity); writes mind.need_deficit, mind.drive, mind.need_priority",
    "notes": "open: C-M1 need interactions, C-M2 urgency thresholds, C-M3 allostatic anticipation and long-term goals. Boundary: Reality writes the deficit signal (body.hunger_signal); this row the felt drive and priority (DUP-49)",
}

# --- Rex 2026-10-30, ENGINES.md "Attraction and partner selection": registered as planned, not built before the Cognition baseline (P7) passes ---
_ATT_HOME = "Toolchain/ENGINES.md 'Attraction and partner selection' (Rex 2026-10-30; planned, after the P7 Cognition baseline)"
_ATT_INV = ("attraction != partner choice != sexual behaviour != reproduction (four distinct quantities, none derived as a copy of another); "
            "no universal attractiveness score exists anywhere; asexuality (little or no sexual or romantic attraction) is a valid parameter region, never a malfunction; "
            "personality shapes what is attended to and how it is weighed, never a fixed type-to-feature preference; no population-wide norm of who prefers whom (variety from consistent inherited and transmitted factors)")
def _att(id_, name, eng, dom, form, writes, reads, consumers, notes=""):
    return {"id": id_, "name": name, "engine": eng, "home": _ATT_HOME, "status": "planned", "domain": dom, "scope": "universal",
            "inputs": [{"name": x, "unit": "see quantities.json"} for x in reads], "outputs": [{"name": x, "unit": "see quantities.json"} for x in writes],
            "state": "planned", "formulation": form, "dependencies": [], "timescale": "planned", "invariants": _ATT_INV,
            "sources": "to research per unit (evidence levels stated); ENGINES.md", "evidence": "?", "approximations": "planned",
            "tests": "none", "consumers": consumers, "notes": notes, "audit_batch": "rex-2026-10-30-attraction", "planned_writes": writes}
EXTRA_ROWS += [
 _att("realism.phenotype.physical", "Physical phenotype", "realism", "B",
      "a phenotype quantity set per organism: facial geometry (eye spacing, jaw, proportions, symmetry); body structure (height, frame, limb proportions); composition (muscle and fat distribution); surface features; movement, posture, gait; voice, scent, expression; emerging from genetics, development, nutrition, age, health and environment. Never an attractiveness score",
      ["body.phenotype"], ["realism.records.genetic_profile", "realism.records.organism_state"],
      ["cognition.perception.detect", "cognition.attraction.interpersonal"],
      "Life & Species (inside realism until the split); depends on P3 genetics and development (realism.genetics.*, realism.development.trait_change); the body charts carry every feature a person can be attracted to"),
 _att("cognition.preference.partner", "Individual partner preferences", "cognition", "C",
      "per-person preference weights over perceived phenotype and traits (P_i), from three interacting influences: biological (inherited and developmental tendencies), social (culture, family, peers, status, read from Society) and experiential (personal history, learned associations through memory and learning)",
      ["mind.partner_preference"], ["realism.records.genetic_profile", "society.partner_norms", "mind.episode"],
      ["cognition.attraction.interpersonal"], "preferences vary by person; no type or sex sets them"),
 _att("society.influence.partner_choice", "Social influence on partner choice", "society", "F",
      "beauty ideals, family expectation (e.g. a father pressing marriage within the bloodline), peer pressure (friends fixed on one feature), status norms: pressures on the individual, delivered to Cognition's appraisal",
      ["society.partner_norms"], [], ["cognition.preference.partner", "cognition.emotion.appraisal", "cognition.reproduction.behaviour"],
      "Society engine (P6, future); a pressure, never a decision: the individual may reject a socially preferred partner"),
 _att("cognition.attraction.interpersonal", "Interpersonal attraction", "cognition", "C",
      "A_ij(t) = F(P_i, X_hat_ij, C_i, E_i, R_ij, S_t): own preferences, the other as perceived (X_hat from perception, never the true phenotype), cultural influence, experience, relationship history (connection, compatibility, familiarity, trust), current state; form proposed",
      ["mind.attraction"], ["mind.partner_preference", "mind.observation", "society.partner_norms", "mind.episode", "mind.belief", "mind.drive"],
      ["cognition.reproduction.behaviour"], "a directed pair quantity; zero or near-zero for some people is a valid region (asexuality)"),
 _att("cognition.reproduction.behaviour", "Partner choice and sexual behaviour", "cognition", "C",
      "motivation and partner selection as decisions (through decision.evaluate and select) reading attraction, pressures and needs; sexual behaviour as a separate act; each a separate quantity",
      ["mind.partner_choice", "mind.sexual_behaviour"], ["mind.attraction", "society.partner_norms", "mind.need_priority"],
      ["realism.reproduction.fertility_conception"], "a person may choose a less attractive partner under pressure or reject a preferred one"),
 _att("realism.reproduction.fertility_conception", "Fertility and conception", "realism", "B",
      "fertility state and conception probability from physiology (age, health, nutrition, cycle); conception creates the child's genetic profile through realism.genetics.inheritance",
      ["body.conception"], ["mind.sexual_behaviour", "realism.records.organism_state"],
      ["realism.genetics.inheritance", "society.influence.partner_choice"], "Life & Species; P3 reproduction (AUDIT §2 B)"),
]
INTERFACES += [
 ("IF-5", "realism.phenotype.physical", "cognition.perception.detect",
  "Phenotype to perception (Rex 2026-10-30): Life & Species writes the phenotype; Cognition perceives it as the perceived other X_hat (with the observer's attention and sensory capacity) and attraction reads only X_hat, never the true phenotype or any score.", []),
 ("IF-6", "society.influence.partner_choice", "cognition.emotion.appraisal",
  "Society pressures to Cognition appraisal (Rex 2026-10-30): beauty ideals, family expectation, peer pressure and status norms reach the individual as appraised pressures; Society never chooses the partner.", []),
 ("IF-7", "cognition.reproduction.behaviour", "realism.reproduction.fertility_conception",
  "Partner choice to reproduction (Rex 2026-10-30): Cognition's partner choice and sexual behaviour are inputs to Life & Species fertility and conception; conception never follows from attraction or choice directly.", []),
]
for _id, _sc, _k, _w, _desc in [
 ("body.phenotype", "body", "record", "realism.phenotype.physical", "the physical phenotype quantity set (face, structure, composition, surface, movement, voice, scent, expression); no attractiveness score"),
 ("mind.partner_preference", "mind", "record", "cognition.preference.partner", "per-person preference weights P_i over perceived features and traits"),
 ("society.partner_norms", "society", "record", "society.influence.partner_choice", "beauty ideals, family expectation, peer pressure, status norms acting on an individual"),
 ("mind.attraction", "mind", "quantity", "cognition.attraction.interpersonal", "A_ij(t), directed from i to j (0-1); distinct from choice, behaviour and reproduction"),
 ("mind.partner_choice", "mind", "record", "cognition.reproduction.behaviour", "the chosen partner (or none); distinct from attraction"),
 ("mind.sexual_behaviour", "mind", "record", "cognition.reproduction.behaviour", "sexual acts as events; distinct from choice and reproduction"),
 ("body.conception", "body", "record", "realism.reproduction.fertility_conception", "a conception event creating a new genetic profile; distinct from behaviour"),
]:
    EXTRA_QUANTITIES.append({"id": _id, "kind": _k, "unit": "1" if _k == "quantity" else None, "scope": _sc, "writer": _w, "description": _desc,
        "status": "planned (Rex 2026-10-30, attraction and partner selection); exists once its units pass, after the P7 baseline"})

# --- Rex 2026-10-30, ENGINES.md "Style and presentation": a shared planned mechanism (not an engine); components owned per engine ---
_STY_HOME = "Toolchain/ENGINES.md 'Style and presentation' (Rex 2026-10-30; a shared planned mechanism, not an engine; after the P7 Cognition baseline)"
_STY_INV = ("style is never a guaranteed indicator of personality: it emits signals that observers interpret through their own beliefs and may get wrong; "
            "phenotype (what someone physically is) != style (how they present) != perceived attractiveness (how another reads the combination); "
            "presentation is never an attractiveness score; worn items are inventory items, never a second copy of goods")
def _sty(id_, name, eng, dom, form, writes, reads, consumers, notes=""):
    return {"id": id_, "name": name, "engine": eng, "home": _STY_HOME, "status": "planned", "domain": dom, "scope": "universal",
            "inputs": [{"name": x, "unit": "see quantities.json"} for x in reads], "outputs": [{"name": x, "unit": "see quantities.json"} for x in writes],
            "state": "planned", "formulation": form, "dependencies": [], "timescale": "planned", "invariants": _STY_INV,
            "sources": "to research per unit (evidence levels stated); ENGINES.md", "evidence": "?", "approximations": "planned",
            "tests": "none", "consumers": consumers, "notes": notes, "audit_batch": "rex-2026-10-30-style", "planned_writes": writes}
_STY_CONSUMERS = ["cognition.perception.detect", "cognition.attraction.interpersonal", "society.presentation.interpretation", "cognition.relationship.trust"]
EXTRA_ROWS += [
 _sty("economy.presentation.worn_items", "Clothing and accessories worn", "economy", "D",
      "which inventory items a person wears now (clothing: fit, silhouette, colour, fabric, revealing or modest; jewellery and other worn accessories): a worn flag on held goods, never a second copy; the choice is Cognition's",
      ["presentation.worn"], ["economy.inventory.holdings", "mind.presentation_choice"], ["shared.presentation.set"],
      "Economy owns the goods and their state (wear, cost, availability by money and climate); Cognition decides what to put on"),
 _sty("realism.presentation.grooming_state", "Grooming state", "realism", "B",
      "hair and facial hair (growth from the organism, cut or styled by choice), cosmetics, hygiene: part of the organism state, changed by grooming acts Cognition chooses",
      ["body.grooming"], ["realism.records.organism_state", "mind.presentation_choice"], ["shared.presentation.set"],
      "organism state + Cognition: growth and soiling are the body's; the cut, style and cosmetics are chosen acts"),
 _sty("realism.presentation.body_modification", "Tattoos and piercings", "realism", "B",
      "permanent or semi-permanent marks on the body (tattoos, piercings, scars kept as marks): body state, made by chosen acts; jewellery worn in piercings is an inventory item (economy.presentation.worn_items)",
      ["body.modifications"], ["realism.records.organism_state", "mind.presentation_choice"], ["shared.presentation.set"],
      "body + inventory (Rex): the mark is the body's, the ornament the inventory's"),
 _sty("cognition.presentation.aesthetic", "Personal aesthetic and presentation choice", "cognition", "C",
      "a learned personal aesthetic (e.g. gothic, refined, rugged, flamboyant, minimalist) and the choice of what to wear, how to groom and what to modify, from materials, money, climate, norms, preferences and what the person has learned attracts or impresses others; may be changed deliberately to influence perception",
      ["mind.aesthetic", "mind.presentation_choice"], ["economy.inventory.holdings", "society.dress_codes", "mind.belief", "mind.episode", "mind.need_priority"],
      ["economy.presentation.worn_items", "realism.presentation.grooming_state", "realism.presentation.body_modification"],
      "the feedback loop (changing presentation to change how one is perceived) runs through this row; a later integration experiment beside attraction"),
 _sty("cognition.presentation.behavioural", "Behavioural presentation", "cognition", "C",
      "posture, mannerisms, speech style, confidence displays: chosen or habitual display behaviour, executed through biomechanics (movement and gait from the body)",
      ["presentation.behaviour"], ["body.phenotype", "realism.muscular.limb_strength", "mind.belief", "mind.drive"], ["shared.presentation.set"],
      "Cognition + biomechanics: Cognition chooses the display, the body's mechanics carry it out; gait itself stays phenotype"),
 _sty("society.presentation.interpretation", "Cultural interpretation of dress", "society", "F",
      "what presentation signals here: fashion, class signals, religious dress, status symbols, as data per society and period; delivered to observers' appraisal and beliefs, never as a verdict about the person",
      ["society.dress_codes"], ["body.presentation"], ["cognition.presentation.aesthetic", "cognition.belief.update", "cognition.emotion.appraisal"],
      "Society engine (P6, future); serves identity, social judgement and belonging beyond romance"),
 _sty("shared.presentation.set", "Presentation quantity set (aggregation)", "shared", "C",
      "the one presentation record per person read by observers: worn items, grooming, body modifications and behavioural presentation, aggregated (refinement B: each part keeps its owner; this row writes only the composed view)",
      ["body.presentation"], ["presentation.worn", "body.grooming", "body.modifications", "presentation.behaviour"], _STY_CONSUMERS,
      "perception reads it beside the phenotype (the perceived other); never recomputes any part"),
]
INTERFACES += [
 ("IF-8", "economy.inventory.holdings", "economy.presentation.worn_items",
  "Style to Economy (Rex 2026-10-30): what is worn is an inventory item; wearing it marks a held good, never copies it, so cost, wear and availability stay Economy's.", []),
 ("IF-9", "society.presentation.interpretation", "cognition.belief.update",
  "Style to Society (Rex 2026-10-30): what a presentation signals here (fashion, class, religion, status) is Society's data; observers read it into their own beliefs and appraisal, and Society never judges the person.", []),
 ("IF-10", "cognition.presentation.aesthetic", "shared.presentation.set",
  "Style to Cognition, the wearer (Rex 2026-10-30): why it was chosen; the wearer's aesthetic and choices set worn items, grooming and modifications, and may change them to change how they are perceived (the feedback loop).", []),
 ("IF-11", "shared.presentation.set", "cognition.perception.detect",
  "Style to Cognition, the observer (Rex 2026-10-30): perception reads the presentation beside the phenotype as part of the perceived other; what the observer infers about personality goes through the observer's beliefs and may be wrong; style is never a guaranteed indicator.", []),
]
for _id, _sc, _w, _desc in [
 ("presentation.worn", "presentation", "economy.presentation.worn_items", "the inventory items a person wears now (refs to held goods)"),
 ("body.grooming", "body", "realism.presentation.grooming_state", "hair, facial hair, cosmetics, hygiene state"),
 ("body.modifications", "body", "realism.presentation.body_modification", "tattoos, piercings and kept marks"),
 ("mind.aesthetic", "mind", "cognition.presentation.aesthetic", "the person's learned personal aesthetic"),
 ("mind.presentation_choice", "mind", "cognition.presentation.aesthetic", "chosen worn items, grooming acts and modifications"),
 ("presentation.behaviour", "presentation", "cognition.presentation.behavioural", "posture, mannerisms, speech style, confidence displays"),
 ("society.dress_codes", "society", "society.presentation.interpretation", "what presentation signals in this society and period"),
 ("body.presentation", "body", "shared.presentation.set", "the composed presentation record observers read beside body.phenotype"),
]:
    EXTRA_QUANTITIES.append({"id": _id, "kind": "record", "unit": None, "scope": _sc, "writer": _w, "description": _desc,
        "status": "planned (Rex 2026-10-30, style and presentation); exists once its units pass, after the P7 baseline"})

# --- Rex 2026-10-30, ENGINES.md "General preference learning": the abstraction under attraction; Cognition, planned, built after the baseline ---
_PREF_HOME = "Toolchain/ENGINES.md 'General preference learning' (Rex 2026-10-30; Cognition, planned, built after the P7 baseline)"
_PREF_REUSE = ("one set of mechanisms for every liking and disliking: attraction, admiration, distrust, occupational preference, aesthetic taste and aversion "
               "are consumers of these rows, never separate rows or a catalogue of attraction types (Rex)")
_PREF_INV = ("no separate formula per thing a person can like; preferences may be positive, negative, neutral or context-dependent; "
             "evaluation reads the other as perceived (X_hat), never the true characteristic; predispositions exist before experience as distributions; "
             "malleability differs by preference: sexual orientation is a fixed class, never rewritten by reward, punishment or social pressure")
def _pref(k, name, dom, form, writes, reads, consumers, notes="", eng="cognition", ev="?"):
    return {"id": k, "name": name, "engine": eng, "home": _PREF_HOME, "status": "planned", "domain": dom, "scope": "universal",
            "inputs": [{"name": x, "unit": "see quantities.json"} for x in reads], "outputs": [{"name": x, "unit": "see quantities.json"} for x in writes],
            "state": "planned", "formulation": form, "dependencies": [], "timescale": "planned", "invariants": _PREF_INV,
            "sources": "to research per unit (evidence levels stated); ENGINES.md", "evidence": ev, "approximations": "planned",
            "tests": "none", "consumers": consumers, "notes": notes, "audit_batch": "rex-2026-10-30-preference", "planned_writes": writes}
EXTRA_ROWS += [
 _pref("cognition.preference.semantic_representation", "Semantic representation of characteristics", "C",
       "a learned network of observable and inferred characteristics, abilities, behaviours, identities and relationships (artist, rebel, kind, intelligent), each tied to observed behaviour and to one another",
       ["mind.characteristic_model"], ["mind.observation", "mind.belief", "mind.episode"],
       ["cognition.preference.individual", "cognition.preference.associative_learning", "cognition.preference.contextual_evaluation"],
       "the vocabulary k over which preferences and perceptions are expressed; inferred characteristics are beliefs and may be wrong"),
 _pref("cognition.preference.individual", "Individual preference per characteristic", "C",
       "P_i,k(t): person i's weight toward characteristic k (positive, negative, neutral or context-dependent), with a malleability class; initial values from predispositions (distributions and tendencies), then updated by associative learning and social transmission",
       ["mind.preference"], ["mind.characteristic_model", "mind.preference_update", "society.transmitted_preference", "realism.records.genetic_profile"],
       ["cognition.preference.contextual_evaluation", "cognition.attraction.interpersonal", "cognition.presentation.aesthetic"],
       "the one writer of mind.preference; " + _PREF_REUSE),
 _pref("cognition.preference.associative_learning", "Associative learning and generalisation", "C",
       "pairs a felt outcome with the characteristics the mind attributes it to and generalises along the semantic network (meets one artist: toward artists, or expressive people, or admired people, by the attribution); writes an update the preference row applies, bounded by each preference's malleability class",
       ["mind.preference_update"], ["mind.attribution", "mind.characteristic_model", "mind.prediction_error", "mind.preference"],
       ["cognition.preference.individual"], "never moves a preference in the fixed class (sexual orientation)"),
 _pref("cognition.preference.misattribution", "Causal misattribution (read-out of attribution)", "C",
       "which characteristic the mind credits for a feeling, rightly or wrongly: a read-out of cognition.learning.attribution, never a second attribution update",
       [], ["mind.attribution"], ["cognition.preference.associative_learning"], "a restatement of cognition.learning.attribution (Rex: not a second mechanism)"),
 _pref("society.transmission.preferences", "Social transmission of preferences", "F",
       "preferences carried by family, peers, institutions and culture to an individual (as offered weights), an input to the preference row, never a write of it",
       ["society.transmitted_preference"], ["society.partner_norms", "society.dress_codes"], ["cognition.preference.individual"],
       "Society engine (P6, future)", eng="society"),
 _pref("cognition.preference.contextual_evaluation", "Contextual evaluation of combinations", "C",
       "V_i(x) = sum_k P_i,k * X_hat_x,k as the baseline (proposed), then nonlinear interactions and context (confidence valued only with kindness; rebellion only when read as principled)",
       ["mind.evaluation"], ["mind.preference", "mind.observation", "mind.characteristic_model", "mind.belief"],
       ["cognition.attraction.interpersonal", "cognition.decision.evaluate"], _PREF_REUSE),
]
RESTATES["cognition.preference.misattribution"] = "cognition.learning.attribution"
ROW_PATCHES.update({
 "cognition.attraction.interpersonal": {
    "formulation": "a consumer of general preference learning: baseline A_ij = sum_k P_i,k * X_hat_ij,k (cognition.preference.contextual_evaluation over a perceived person), with interactions and context to follow, plus relationship history and current state (connection, compatibility, familiarity, trust); proposed (ENGINES.md 'General preference learning')",
    "inputs": [{"name": x, "unit": "see quantities.json"} for x in ["mind.evaluation", "mind.preference", "mind.observation", "society.partner_norms", "mind.episode", "mind.belief", "mind.drive"]],
    "notes": "re-homed 2026-10-30 as a consumer of cognition.preference.* (Rex); a directed pair quantity; zero or near-zero for some people is a valid region (asexuality); attraction, romantic attachment, sexual motivation, partner selection and reproductive intention are separate representations"},
 "cognition.preference.partner": {
    "formulation": "a view, not a mechanism: P_i,k (cognition.preference.individual) in the partner context; biological, social and experiential influences arrive through predispositions, social transmission and associative learning",
    "planned_writes": [], "outputs": [],
    "superseded_by": "cognition.preference.individual",
    "notes": "re-homed 2026-10-30 (Rex, 'General preference learning'): no separate partner-preference mechanism; mind.partner_preference retired to mind.preference"},
 "cognition.presentation.aesthetic": {
    "notes": "aesthetic taste is mind.preference over style characteristics (General preference learning, Rex 2026-10-30), not a separate mechanism; this row keeps the choice of presentation. The feedback loop (changing presentation to change how one is perceived) runs through this row; a later integration experiment beside attraction"},
 "cognition.learning.attribution": {
    "notes": "a read-out of belief.update before and after (never a second update): who or what is blamed; also read by cognition.preference.misattribution (what a feeling is credited to, rightly or wrongly; Rex 2026-10-30)"},
})
EXTRA_QUANTITIES += [
 {"id": "mind.characteristic_model", "kind": "record", "unit": None, "scope": "mind", "writer": "cognition.preference.semantic_representation",
  "description": "the person's network of characteristics k tied to behaviour and to one another"},
 {"id": "mind.preference", "kind": "record", "unit": None, "scope": "mind", "writer": "cognition.preference.individual",
  "description": "P_i,k(t) per characteristic: weight (-1..1), context conditions, and malleability class",
  "attributes": {"malleability": "per preference: a class from fixed to high (classes to be defined in the unit); sexual orientation is in the fixed class and is never rewritten by reward, punishment or social pressure (Rex 2026-10-30)"}},
 {"id": "mind.preference_update", "kind": "record", "unit": None, "scope": "mind", "writer": "cognition.preference.associative_learning",
  "description": "proposed changes to P_i,k from experience, applied by the preference row within each malleability class"},
 {"id": "society.transmitted_preference", "kind": "record", "unit": None, "scope": "society", "writer": "society.transmission.preferences",
  "description": "preferences offered by family, peers, institutions and culture"},
 {"id": "mind.evaluation", "kind": "record", "unit": None, "scope": "mind", "writer": "cognition.preference.contextual_evaluation",
  "description": "V_i(x): how i values a perceived person, object or option; read by attraction, admiration, distrust, occupational choice, taste and aversion"},
]
for _q in EXTRA_QUANTITIES[-5:]:
    _q["status"] = "planned (Rex 2026-10-30, general preference learning); exists once its units pass, after the P7 baseline"
QUANTITY_OPS.append(("retire", "mind.partner_preference", "mind.preference",
    "re-homed (Rex 2026-10-30, General preference learning): partner preferences are mind.preference in the partner context; registered planned the same day, never built"))
INTERFACES.append(("IF-12", "society.transmission.preferences", "cognition.preference.individual",
  "Social transmission of preferences (Rex 2026-10-30): family, peers, institutions and culture offer preferences (society.transmitted_preference); the preference row weighs them within each malleability class and is their only writer; Society never sets a preference, and never moves the fixed class (sexual orientation).", []))

# --- 2026-10-30: economy unit 2630 passed (economy bb8ee31): labourPerUnit removed; labourHoursPerUnit required ---
QUANTITY_OPS.append(("retire", "economy.labourperunit", "economy.labourhoursperunit",
    "economy unit 2630 (bb8ee31): Rates are {unitsPerFixtureDay, labourHoursPerUnit}, both required; defineRecipe refuses the old field (commands.ts L72); re-audited by the registry keeper: no other use in economy/src; the pirate fixture uses labourHoursPerUnit (2629)"))
for _g in ("DUP-26", "DUP-28", "DUP-29"):
    DECISIONS[_g]["progress"].append({"date": "2026-10-30", "step": "unit passed", "by": "Economy keeper", "commit": "economy bb8ee31 (unit 2630)",
        "note": "worker-days field removed from the economy engine; economy.labourperunit retired to economy.labourhoursperunit (re-audited). Group stays closing until settlement 2617-2619 and Reality 2636 pass"})

# --- Rex 2026-10-30 (late evening, via the controller): overlap batch 2 approved with refinements (OVERLAPS-BATCH-2.md "Rex's decisions") ---
# Every group starts "closing": it moves only when the keepers named under "must agree" accept ownership and test.
_B2 = "Rex, 2026-10-30; OVERLAPS-BATCH-2.md"
for _g, _d in [
    ("DUP-15", "approved: one authoritative capacity calculation. Q3: no combination rule by default (product over-penalises, worst-dip ignores combined effects); the Reality keeper investigates empirical models; where evidence is unavailable a documented provisional model (PLATFORM s4 level 4) is used and tested against physiological observations. R-1 condition (b) of 2623 applies: hydration bands must not count the oxygen-delivery effect again"),
    ("DUP-16", "approved as proposed: collagen and healing consume nutrition state (one pathway)"),
    ("DUP-17", "approved: cellular ageing becomes authoritative when built; the existing approximations stay provisional (frozen, level 4)"),
    ("DUP-37", "approved: optics supplies physical conditions, organism perception gives functional vision (through group 1's capacity)"),
    ("DUP-38", "refined (Q1): no fixed item list at the universal level. Reality calculates individual conditions and their effects; the pirate game may aggregate them into six displayed states. BODY.md s2 defines the pirate aggregation, not a universal list; the game interface never determines the biological architecture"),
    ("DUP-47", "approved with refinement (Q2): the pool's own heat multiplier is removed (functional capacity already includes heat stress); the pool stays a game abstraction derived from the organism's current physiological capacity"),
    ("DUP-12", "approved with a flag: one authoritative homeostatic sleep-pressure state (adenosine, neurology sleep_wake); circadian influence is represented separately; the acceptance test must not let the one quantity stand for all of sleep"),
    ("DUP-11", "approved as proposed: circulation owns haemoglobin saturation; atmosphere supplies alveolar PO2"),
    ("DUP-23", "approved: species parameters (anatomy species profile) and current physiological calculations (circulation) stay separate"),
    ("DUP-25", "approved: exposure (atmosphere), species susceptibility (anatomy data) and medical consequences (medicine) have distinct owners"),
    ("DUP-21", "approved: inventory (Economy), consumption and physiological effects (nutrition; population aggregate) are different mechanisms"),
    ("DUP-49", "refined (Q4): palatability and the eating decision split across four owners: Reality hunger, satiety, taste perception, digestion and physiological responses; Cognition food preferences, anticipated enjoyment, appetite-related motivation and the decision to eat; Society cultural food norms, taboos and learned expectations; the pirate game period-specific foods, presentation and its intentional gameplay rules. Palatability is part sensory (Reality), part evaluative (Cognition)"),
]:
    DECISIONS[_g] = {"decision": f"{_d} ({_B2})", "state": "closing",
                     "progress": [{"date": "2026-10-30", "step": "owner approved", "by": "Rex (via the controller)", "note": "batch 2"}]}
DECISIONS["DUP-38"]["approved_owner"] = ("realism.neurology.circuits (with its pharmacokinetics) for intoxication and Reality for each individual condition and its effect; "
    "pirate BODY.md s2 for the pirate aggregation into displayed states (any count; STATS.md and PSYCHOLOGY.md cite it); no universal item list")
DECISIONS["DUP-49"]["approved_owner"] = ("four owners: Reality (realism.nutrition: hunger and satiety as body signals, body.hunger_signal; taste perception; digestion); "
    "Cognition (food preference, anticipated enjoyment, appetite motivation via cognition.needs.drive, the decision to eat via cognition.decision.select); "
    "Society (cultural food norms, taboos, learned expectations); pirate game (period foods, presentation, its gameplay rules)")
DECISIONS["DUP-47"]["approved_owner"] = "pirate BODY.md s3, computed in the pirate adapter from universal states only (group 1's capacity, batch 1's fatigue and aerobic capacity); no heat factor of its own"
DECISIONS["DUP-12"]["approved_owner"] = "realism.neurology.sleep_wake for homeostatic sleep pressure only; circadian timing represented separately; physiology alertness reads it"

# --- 2026-10-30 (successor registry keeper): re-audits of what landed during the restart ---
# DUP-22: realism 2d8057a (2623, parked at the game gate; still in queue/realism/failed) + 8cee7ac (2677, 2687; gate passed incl. pirate src/world 141).
DECISIONS["DUP-22"]["progress"] += [
    {"date": "2026-10-30", "step": "unit passed", "by": "Reality keeper", "commit": "realism 2d8057a (2623); 8cee7ac (2677, 2687)",
     "note": "2623's work committed but parked at the game gate (3 pirate src/world failures); 2687 landed 2677 and fixed the host-deficit initialisation; gate passed (engine 294, tsc clean, pirate world 141). 2623's unit file is still in failed/ (REG-24)"},
    {"date": "2026-10-30", "step": "re-audited (11a criteria)", "by": "registry keeper",
     "note": "implemented: every piece of 2623's Gate holds at HEAD (flags (2623) level 4 / unvalidated: plasma / report; 'validation (2623)' test; bodyMassDelta in nutrition and circulation; no b.mass -= in circulation); the test 'drinking 1 L moves water, deficit, mass and plasma ... within 1e-9' is the acceptance test. integrated: test/water-ledger.test.ts runs physiology, nutrition, circulation and atmosphere together; pirate src/world 141 passed. validated: no independent data, recorded with the experiment (flags (2623)/(2677) unvalidated: a matched sedentary turnover cohort; plasma sign and units, level 5). R-1 conditions (a) level 5 label and (c) red cells level 4: met; (b) carried to DUP-15"},
    {"date": "2026-10-30", "step": "closed", "by": "registry keeper"},
]
DECISIONS["DUP-22"]["state"] = "closed"
# DUP-20: realism 3b9d69f (2626, re-queued as 2709, gate passed).
DECISIONS["DUP-20"]["progress"] += [
    {"date": "2026-10-30", "step": "unit passed", "by": "Reality keeper", "commit": "realism 3b9d69f (2626 as 2709)"},
    {"date": "2026-10-30", "step": "re-audited (11a criteria)", "by": "registry keeper",
     "note": "implemented: population.test 'matches 1,000 individual medicine cases within three sample standard errors' (attack rate, case fatality, illness duration); population reads medicine's rangePoint / diseaseOutcomeDays (no own 'const point ='). integrated: that test runs medicine individuals against the population aggregate. validated: no independent joint attack/fatality/duration data (flag (2626) unvalidated; Angola suspected-case CFR 8.7 % inside the range is range compatibility only). R-1 condition met: force of infection a host input, level 4 gap until P3 transmission"},
    {"date": "2026-10-30", "step": "closed", "by": "registry keeper"},
]
DECISIONS["DUP-20"]["state"] = "closed"
# DUP-18: realism 5381e00 (2625 as 2708, gate passed). Re-audit does NOT pass: acceptance items open.
DECISIONS["DUP-18"]["progress"] += [
    {"date": "2026-10-30", "step": "unit passed", "by": "Reality keeper", "commit": "realism 5381e00 (2625 as 2708)",
     "note": "one constant set: Busso 1991 means (k1 0.048, k2 0.117, tau 38 / 1.9 d, P0 104.8) via Ceddia et al. 2025, marked researched; muscular owns the computation"},
    {"date": "2026-10-30", "step": "re-audit: not passed", "by": "registry keeper",
     "note": "one registry row and one code computation: yes. Open: (1) no published worked example reproduced; the source prints none, so the test checks the single-impulse closed form (REG-25); (2) the pirate PHYSIOLOGY.md s2 prose (k1 0.4/42, k2 0.4/7) and its rendered library table (42 / 7 days) at pirate-ship HEAD 11a8895 still carry the old constants (REG-25); (3) 2635's aerobic clamp normalisation was derived from the 42/7 constants and needs a re-check against the new set (REG-26). Stays closing"},
]
# Labour groups 10-12: settlement 2617 (e226b8f), 2619 (67c8766), pirate 2618 (75ec54f) passed and re-audited; Reality 2636 re-queued as 2713.
for _g in ("DUP-26", "DUP-28", "DUP-29"):
    DECISIONS[_g]["progress"] += [
        {"date": "2026-10-30", "step": "unit passed", "by": "Settlement keeper; pirate-ship", "commit": "settlement e226b8f (2617), 67c8766 (2619); pirate-ship 75ec54f (2618)"},
        {"date": "2026-10-30", "step": "re-audited (partial)", "by": "registry keeper",
         "note": "LabourSupply declared once per repo, byte-identical declarations (settlement and economy src/providers.ts); no labourPerUnit / labourDays / LabourProvider left in settlement src; Post.wage written only by addPost and setWage (commands.ts L536, L544); settlement suite 67 passed + 1 todo; committed CONTRACTS.md byte-identical incl. s18 (md5 c3b5d46f; REG-23 fixed). Waits on Reality 2713 (population labour supply, re-queue of 2636) before closing"},
    ]
CHAINS += [
 {"id": "realism:water-ledger", "test": "realism test/water-ledger.test.ts (2623, 2677, 2687)", "complete": True,
  "conservation": "water and body mass per transfer within 1e-9 kg; human-week mass balance within 1e-6 kg; blood volume and Hb mass unchanged by dehydration",
  "members": ["realism.physiology.water_balance", "realism.nutrition.body_mass", "realism.nutrition.energy_store",
              "realism.circulation.blood_ledger", "realism.gas.room_box"]},
 {"id": "realism:epidemic-vs-individuals", "test": "realism test/population.test.ts 'matches 1,000 individual medicine cases' (2626)", "complete": True,
  "conservation": "aggregate vs mean of 1,000 seeded individuals within three sample standard errors",
  "members": ["realism.population.epidemic", "realism.medicine.disease_course"]},
]
VV_OVERRIDES.update({
    "realism.physiology.water_balance": {"validated": "no (no independent data; flags (2623), (2677): a matched sedentary turnover cohort is the experiment; plasma term level 5)", "evidence": "re-audit 2026-10-30, DUP-22 closed"},
    "realism.population.epidemic": {"validated": "no (no joint attack/fatality/duration record; flag (2626); CFR range compatibility only)", "evidence": "re-audit 2026-10-30, DUP-20 closed"},
})

# --- Rex 2026-10-30 (late evening), ENGINES.md "Communication and information transmission": a universal subsystem owned by Cognition;
# registered as planned, built only after the Cognition baseline (P7) is stable. Every row planned/proposed; no code, no unit. ---
_COM_HOME = "Toolchain/ENGINES.md 'Communication and information transmission' (Rex 2026-10-30; owned by Cognition; planned, after the P7 baseline)"
_COM_INV = ("transmission != comprehension != belief acceptance != behavioural compliance (four distinct stages, none derived as a copy of another); "
            "a message delivers information, the receiving mind decides what it means; persuasion is never a charisma roll against a resistance: "
            "it changes a specific part of the listener's evaluation and may be irrelevant to the real objection, fail, or strengthen opposition; "
            "one belief-changing system (cognition.belief.update) and one perception (cognition.perception.detect: a message is a Stimulus); "
            "personality shapes which arguments are generated and attended to, never one technique per type; communication competence is learned; "
            "suppression never automatically produces rebellion")
def _com(k, name, dom, form, writes, reads, consumers, notes="", eng="cognition"):
    return {"id": k, "name": name, "engine": eng, "home": _COM_HOME, "status": "planned", "domain": dom, "scope": "universal",
            "inputs": [{"name": x, "unit": "see quantities.json"} for x in reads], "outputs": [{"name": x, "unit": "see quantities.json"} for x in writes],
            "state": "planned", "formulation": form, "dependencies": [], "timescale": "planned", "invariants": _COM_INV,
            "sources": "to research per unit (evidence levels stated); ENGINES.md", "evidence": "?", "approximations": "planned",
            "tests": "none", "consumers": consumers, "notes": notes, "audit_batch": "rex-2026-10-30-communication", "planned_writes": writes}
EXTRA_ROWS += [
 _com("cognition.communication.message", "Message representation", "C",
      "the message record: sender, intended receivers, medium, content as propositions and evidence offered, the sender's intent, time sent; speech, gesture, writing, signals, rumour and deception are all messages (deception: content the sender believes false)",
      [], [], ["cognition.communication.encode", "realism.communication.transmission", "cognition.communication.comprehend"],
      "the format only: world.message is written by encode; proposed, not an established schema"),
 _com("cognition.communication.encode", "Encoding: what is said and how", "C",
      "from the sender's knowledge, beliefs, goals, intentions and communication style to a message in a chosen medium; argument generation shaped by personality (which arguments come to mind), competence learned (cognition.skill.practice); under restriction the sender may choose an alternative channel (trusted link, secret channel, note), each with its own cost, delay, error and chance of detection",
      ["world.message"], ["mind.belief", "mind.intention", "world.medium_properties", "society.comm_network", "society.comm_restriction"],
      ["realism.communication.transmission"], "a sending decision runs through cognition.decision.select; encode shapes the content"),
 _com("shared.communication.medium", "Medium properties", "A",
      "per medium: range, speed, capacity, fidelity, persistence, accessibility, detectability, cost. Knowledge & Technology says which media a society has; Reality sets the physical limits; neither Cognition nor the game invents a medium's numbers",
      ["world.medium_properties"], ["society.available_media"], ["cognition.communication.encode", "realism.communication.transmission"],
      "shared (not an engine): a boundary record between Knowledge & Technology and Reality", eng="shared"),
 _com("realism.communication.transmission", "Transmission through Reality", "A",
      "what reaches each receiver, when and how degraded: distance, sound propagation, visibility (P2 optics, acoustics), interference and noise; a message carried by a person or an object travels with it; the signal's detectability at a receiver (including an unintended one) is the same d' perception reads (body.detectability)",
      ["world.message_received"], ["world.message", "world.medium_properties", "society.comm_network"],
      ["cognition.communication.perceive", "cognition.communication.detection"],
      "Physical Reality, P2 (acoustics, optics); Kernel interface: a message's delay is an event on the one kernel clock, delivered in order through the kernel's event ports (no own counter, DUP-33); no IF row until the kernel registers its ports", eng="realism"),
 _com("cognition.communication.perceive", "Perception of a message", "C",
      "a received message enters cognition.perception.detect as a Stimulus (attention, sensory capacity counted once); writes nothing of its own",
      [], ["world.message_received", "body.detectability", "mind.attention_share"], ["cognition.communication.comprehend"],
      "reuse of perception.detect (mind.observation), never a second perception (Rex)"),
 _com("cognition.communication.comprehend", "Comprehension", "C",
      "what the receiver understands from the perceived message: shared language and code, the receiver's prior beliefs and context; may differ from what the sender meant; the understood content becomes testimony",
      ["mind.testimony"], ["mind.observation", "mind.belief"], ["cognition.communication.credibility", "cognition.belief.update"],
      "the planned writer of mind.testimony (host input until built; cognition.communication.language was reserved for it)"),
 _com("cognition.communication.credibility", "Source credibility and trust", "C",
      "the receiver's credibility of this source for this content: trust history (cognition.relationship.trust), perceived expertise, the receiver's state; one per receiver-source pair",
      ["mind.source_credibility"], ["mind.testimony", "mind.episode", "mind.belief"], ["cognition.belief.update", "cognition.communication.persuasion"]),
 _com("cognition.communication.persuasion", "Persuasion: a change to a specific part of the evaluation", "C",
      "which component of the listener's evaluation the message bears on (belief about quality, evidence of usefulness, actual cost, affordability, future opportunity, social benefit) and whether that is the listener's real objection; the conceptual shape B_{t+1} = F(B_t, M, S, T, E) (beliefs, message and evidence, source credibility, trust history, listener state) is proposed, not an established equation; the change itself is made by belief.update",
      ["mind.evaluation_target"], ["mind.testimony", "mind.source_credibility", "mind.belief", "mind.expected_utility"],
      ["cognition.belief.update", "cognition.decision.evaluate"], "no resistance score, no charisma roll; may fail or strengthen opposition"),
 _com("cognition.communication.belief_update", "Belief update from a message (reuse)", "C",
      "a message changes beliefs only through cognition.belief.update (testimony weighted by credibility and the targeted component); writes nothing of its own",
      [], ["mind.testimony", "mind.source_credibility", "mind.evaluation_target"], ["cognition.belief.update"],
      "reuse, never a second belief-changing system (Rex); acceptance (belief) and compliance (behaviour, decision.select) stay separate"),
 _com("cognition.communication.detection", "Detection of communication", "C",
      "an observer (an enforcer, a rival, a bystander) perceives a message or channel not meant for them through its detectability at that observer; perception.detect does the detecting; writes nothing of its own",
      [], ["world.message_received", "body.detectability"], ["government.suppression.communication"],
      "reuse of perception; each covert alternative carries its own chance of detection (Rex)"),
 _com("government.suppression.communication", "Suppression of communication", "E",
      "censorship and enforcement rules restricting media, content or networks; reduces communication and changes its form; outcomes not fixed: it may succeed, breed resentment without action, or grow alternative networks",
      ["society.comm_restriction"], ["mind.observation"], ["cognition.communication.encode", "cognition.emotion.appraisal"],
      "Government engine (P8, future); a pressure on senders, never a decision for them", eng="government"),
 _com("knowledge.media.availability", "Media available to a society", "G",
      "which media (speech, signals, writing, print, ...) a society has and who can use them (literacy, access)",
      ["society.available_media"], [], ["shared.communication.medium"], "Knowledge & Technology engine (P9, future)", eng="knowledge"),
 _com("society.network.communication", "Communication networks", "F",
      "who talks to whom and how often: kinship, trade, neighbourhood, institutional and secret links; rumour spreads along them",
      ["society.comm_network"], ["mind.episode"], ["cognition.communication.encode", "realism.communication.transmission"],
      "Society engine (P6, future); the network a message travels, not its content", eng="society"),
]
INTERFACES += [
 ("IF-13", "cognition.communication.encode", "realism.communication.transmission",
  "Message to Reality (Rex 2026-10-30): Cognition writes the message and its medium; Reality alone decides what arrives where, when and how degraded; Cognition never delivers a message directly.", []),
 ("IF-14", "realism.communication.transmission", "cognition.communication.perceive",
  "Reality to perception (Rex 2026-10-30): a received message is a Stimulus read through cognition.perception.detect with its detectability; arrival is not comprehension.", ["DUP-37"]),
 ("IF-15", "knowledge.media.availability", "shared.communication.medium",
  "Knowledge & Technology to media (Rex 2026-10-30): K&T says which media a society has and who can use them; Reality bounds their physics; the medium record holds both.", []),
 ("IF-16", "society.network.communication", "realism.communication.transmission",
  "Society networks to transmission (Rex 2026-10-30): Society says who is linked to whom; transmission carries messages along those links and to anyone else in physical range.", []),
 ("IF-17", "government.suppression.communication", "cognition.communication.encode",
  "Government suppression to senders (Rex 2026-10-30): restrictions change what senders choose (form, channel, risk), each alternative with cost, delay, error and a chance of detection; suppression never decides behaviour and never produces rebellion by rule.", []),
 ("IF-18", "cognition.decision.select", "economy.trade.trade",
  "Negotiated agreement to Economy (Rex 2026-10-30): a bargain struck through communication is a decision; Economy executes the trade (goods, money, price); communication never moves goods or money, and Economy's prices and costs are the facts persuasion argues about.", []),
]
for _id, _sc, _k, _w, _desc in [
 ("world.message", "world", "record", "cognition.communication.encode", "a sent message: sender, intended receivers, medium, content (propositions, evidence), intent, time"),
 ("world.message_received", "world", "record", "realism.communication.transmission", "per receiver (intended or not): arrived or not, delay, degradation"),
 ("world.medium_properties", "world", "record", "shared.communication.medium", "per medium: range, speed, capacity, fidelity, persistence, accessibility, detectability, cost"),
 ("society.available_media", "society", "record", "knowledge.media.availability", "the media a society has and who can use them"),
 ("society.comm_network", "society", "record", "society.network.communication", "communication links between people (kin, trade, neighbourhood, institutional, secret)"),
 ("society.comm_restriction", "society", "record", "government.suppression.communication", "censorship and enforcement rules on media, content and networks"),
 ("mind.source_credibility", "mind", "quantity", "cognition.communication.credibility", "credibility of a source for a content, per receiver (0-1)"),
 ("mind.evaluation_target", "mind", "record", "cognition.communication.persuasion", "the evaluation component a message bears on and whether it is the listener's real objection"),
]:
    EXTRA_QUANTITIES.append({"id": _id, "kind": _k, "unit": "1" if _k == "quantity" else None, "scope": _sc, "writer": _w, "description": _desc,
        "status": "planned (Rex 2026-10-30, communication and information transmission); exists once its units pass, after the P7 baseline"})
ROW_PATCHES.update({
 "cognition.communication.language": {"notes": "reserved (DESIGN.md §5); expanded 2026-10-30 into the communication subsystem (cognition.communication.*, Rex): this row stays the learned language competence; mind.testimony's planned writer is cognition.communication.comprehend"},
})
VV_PLANNED_SPECS["cognition.communication.message"] = [
 "V-M1 two merchants (first experiment, Cognition + Economy + Kernel): two merchants negotiate one item; one knows something the other does not (for example a defect, or a coming shortage). Checks: (1) the four stages are recorded separately for every message (sent, received, understood, believed) and the outcome (agree, reject, counter) is a decision; (2) the informed merchant's arguments and the uninformed one's beliefs change only through belief.update; (3) an argument aimed at a component that is not the listener's real objection does not move the decision; (4) the agreed price executes through Economy's trade on the kernel clock, conserving goods and money; (5) repeat runs with different personalities and trust histories give different, explainable outcomes, never a fixed technique per type. Proposed; tolerance and data to be stated when the unit is written",
 "V-M2 rumour through a small settlement (second experiment): spread follows Society's network and transmission, with distortion at comprehension; proposed",
 "V-M3 communication under restriction (third experiment): suppression changes channel choice and volume; alternatives carry detection; no rebellion by rule; proposed",
]

# --- 2026-10-30: batch 2 groups 2, 7, 8, 9, 10 agreed (Reality keeper accepted ownership and tests; registry amended 7 and 10) ---
for _g, _t in [
    ("DUP-16", "as written: (1) collagen fixed + low vitamin C leaves healing unchanged; (2) depletion slows healing only via collagen; (3) no scurvy course on its own clock (scurvy a label over nutrition + collagen). Validation: deficiency-sign onset vs an opened human depletion study, else unvalidated line"),
    ("DUP-12", "(1) one homeostatic pressure state in neurology sleep_wake; 24 h awake raises it; physiology alertness and neurology arousal one output; (2) at constant hours awake pressure does not vary with clock time; circadian influence only from realism.physiology.circadian as a separate input (registry amendment: the circadian row exists); (3) medicine healing x1.2 reads the pressure; (4) human-week checkpoint unchanged within tolerance. Validation: rise/decay time constants vs an opened two-process-model source"),
    ("DUP-11", "as written: one saturation function, in circulation; atmosphere supplies alveolar PO2 only and reads saturation; alias air.sao2 -> body.sao2 recorded when the unit passes; atmosphere and circulation tests bit-identical before/after. Validation: curve vs an opened standard ODC (e.g. Severinghaus 1979) within its stated error"),
    ("DUP-23", "as written: one parameter per species in anatomy species_profile; human and horse values unchanged; no prose parse and no assembly equality check left. Validation: blood volume per kg vs an opened reference, else unvalidated line"),
    ("DUP-25", "as written: each threshold once, as data (a check greps the numeric thresholds); a body in 15 % O2 shows one effect computed in medicine; anatomy keeps species tolerance data only. Registry amendment: validation line, each threshold vs an opened exposure source, else unvalidated line"),
]:
    DECISIONS[_g]["progress"].append({"date": "2026-10-30", "step": "agreed", "by": "Reality keeper + registry keeper",
        "note": "acceptance test: " + _t + ". Belt (Codex, Haiku check) after realism p1b audit 2714"})

# --- Rex 2026-10-30 (late evening), ENGINES.md "Cultural salience and the zeitgeist in attraction" and
# "Dynamic function allocation, the light and the crystal": planned only, after the Cognition baseline; owner Cognition, Society for salience ---
_SAL_HOME = "Toolchain/ENGINES.md 'Cultural salience and the zeitgeist in attraction' (Rex 2026-10-30; planned, inside preference learning DESIGN §13, after the P7 baseline)"
_FA_HOME = "Toolchain/ENGINES.md 'Dynamic function allocation, the light and the crystal' (Rex 2026-10-30; planned, personality layer DESIGN §9, after the P7 baseline)"
_SAL_INV = ("perceived social valuation V_i and perceived sensory appeal S_i are independent inputs, never one score; "
            "awareness of a trend, personal evaluation of it, willingness to conform to it, and attraction toward people displaying it are four separate outcomes; "
            "a style can be fashionable without a person liking it, and attractive despite the community's disapproval; Society sets prominence, Cognition what each person notices and how it moves attraction")
_FA_INV = ("attention allocation != evaluation influence: a function can receive most of the processing without deciding the action; "
           "the type hierarchy is a baseline, never a fixed allocation per decision; variation emerges from the formula, never from hardcoded exceptions; "
           "an inferior function is never prevented from leading a decision; function-specific sensitivities are hypotheses (evidence 5), never laws")
def _sal(k, name, dom, form, writes, reads, consumers, notes="", eng="cognition", ev="?", home=None, inv=None, batch="rex-2026-10-30-salience"):
    return {"id": k, "name": name, "engine": eng, "home": home or _SAL_HOME, "status": "planned", "domain": dom, "scope": "universal",
            "inputs": [{"name": x, "unit": "see quantities.json"} for x in reads], "outputs": [{"name": x, "unit": "see quantities.json"} for x in writes],
            "state": "planned", "formulation": form, "dependencies": [], "timescale": "planned", "invariants": inv or _SAL_INV,
            "sources": "to research per unit (evidence levels stated); ENGINES.md", "evidence": ev, "approximations": "planned",
            "tests": "none", "consumers": consumers, "notes": notes, "audit_batch": batch, "planned_writes": writes}
EXTRA_ROWS += [
 _sal("society.culture.salience", "Cultural salience", "F",
      "how often and how prominently a style, characteristic or behaviour appears in a person's environment, and which are rewarded; feedback: people adopt styles, others react, reactions move popularity, popularity moves future preferences",
      ["mind.cultural_salience"], ["society.partner_norms", "mind.observation"], ["cognition.attraction.social_valuation", "cognition.attraction.sensory_appeal"],
      "Society engine (P6, future); per person (what that person's environment shows), hence the mind scope of its output", eng="society"),
 _sal("cognition.attraction.social_valuation", "Perceived social valuation", "C",
      "V_i: what the person perceives the surrounding community admires, endorses and rewards in another; read from Society's salience and norms through perception",
      ["mind.perceived_social_valuation"], ["mind.cultural_salience", "society.partner_norms", "mind.observation"], ["cognition.attraction.interpersonal"]),
 _sal("cognition.attraction.sensory_appeal", "Perceived sensory appeal", "C",
      "S_i: what is visibly fashionable or physically appealing to this person, read from phenotype and style as perceived (X_hat), never the true phenotype or a score",
      ["mind.perceived_sensory_appeal"], ["mind.observation", "mind.cultural_salience", "mind.partner_preference"], ["cognition.attraction.interpersonal"]),
 _sal("cognition.personality.function_sensitivity", "Function-specific sensitivities (hypotheses)", "C",
      "the C_i weighting of A_i = F(V_i, S_i, C_i, E_i), proposed: Fe collective valuation, Se sensory presentation, Fi personal significance, Si familiarity and remembered ideals, Ne novelty, Ni symbolic meaning and anticipated trajectory, Te demonstrated competence, Ti coherence of thought; sensitivity, never conformity",
      [], ["mind.function_allocation"], ["cognition.attraction.interpersonal", "cognition.preference.contextual_evaluation"],
      "a configuration of cognition.personality.slot (eight-function model, CTRL-7); parameters only, writes nothing", ev="5"),
 _sal("cognition.personality.function_allocation", "Dynamic function allocation A_f(t)", "C",
      "A_f(t) = B_f R_f(t) L_f(t) M_f(t) / sum_j B_j R_j(t) L_j(t) M_j(t) (proposed, provisional; a softmax over function scores preferred): B_f baseline preference (the light), R_f relevance to the situation, L_f learned competence and habit (part of the crystal), M_f motivational and emotional modulation; experience changes activation conditions (repeated consequences raise a situation's activation of a function), misattribution possible",
      ["mind.function_allocation"], ["mind.observation", "mind.episode", "mind.drive", "mind.prediction_error"],
      ["cognition.attention.allocate", "cognition.decision.evaluate", "cognition.personality.function_sensitivity"],
      "personality layer (DESIGN §9); writes the processing share per function, which is not the share of decision influence (Rex's paste was cut off at the last point; the rest to be supplied)",
      ev="5", home=_FA_HOME, inv=_FA_INV, batch="rex-2026-10-30-function-allocation"),
]
INTERFACES.append(("IF-19", "society.culture.salience", "cognition.attraction.social_valuation",
  "Cultural salience and social reward to attraction (Rex 2026-10-30): Society says which styles, characteristics and behaviours are prominent or rewarded around a person; Cognition decides what that person notices, how it is interpreted and whether it moves attraction; Society never sets attraction or conformity.", []))
for _id, _sc, _k, _w, _desc, _st in [
 ("mind.perceived_social_valuation", "mind", "quantity", "cognition.attraction.social_valuation", "V_i, per observer and other (0-1): perceived community valuation", "planned (Rex 2026-10-30, cultural salience)"),
 ("mind.perceived_sensory_appeal", "mind", "quantity", "cognition.attraction.sensory_appeal", "S_i, per observer and other (0-1): perceived sensory and fashion appeal", "planned (Rex 2026-10-30, cultural salience)"),
 ("mind.cultural_salience", "mind", "quantity", "society.culture.salience", "prominence of a characteristic in a person's environment (0-1); written by Society, read by Cognition", "planned (Rex 2026-10-30, cultural salience)"),
 ("mind.function_allocation", "mind", "quantity", "cognition.personality.function_allocation", "A_f(t), per function, processing share (0-1, sums to 1); not decision influence", "planned (Rex 2026-10-30, dynamic function allocation; evidence 5)"),
]:
    EXTRA_QUANTITIES.append({"id": _id, "kind": _k, "unit": "1", "scope": _sc, "writer": _w, "description": _desc, "status": _st + "; exists once its units pass, after the P7 baseline"})
ROW_PATCHES["cognition.attraction.interpersonal"] = {"notes": "a directed pair quantity; zero or near-zero for some people is a valid region (asexuality). Rex 2026-10-30 (cultural salience): baseline shape A_i = F(V_i, S_i, C_i, E_i), proposed; reads mind.perceived_social_valuation and mind.perceived_sensory_appeal as independent inputs (IF-19), and mind.function_allocation through the function sensitivities (evidence 5)"}

# --- 2026-10-30: DUP-49 (batch 2 group 12) agreed between Reality and Cognition; two body signals registered (cognition keeper's request) ---
EXTRA_QUANTITIES += [
 {"id": "body.satiety_signal", "kind": "quantity", "unit": "1", "scope": "body", "writer": "realism.nutrition.hunger_fullness",
  "description": "the physiological satiety (fullness) signal (0-1); Cognition reads it for the hunger need's deficit (cognition.needs.drive), never writes it",
  "status": "proposed (DUP-49, agreed Reality + Cognition 2026-10-30); the writer row is documented-only"},
 {"id": "body.taste_percept", "kind": "quantity", "unit": "1", "scope": "body", "writer": None,
  "attributes": {"indexed_by": "taste category (categorical)"},
  "description": "the sensory half of palatability: perceived taste intensity per taste category (0-1); Cognition's preference evaluation is the evaluative half (DESIGN §13)",
  "status": "proposed (DUP-49, agreed Reality + Cognition 2026-10-30); writer: a Reality taste-perception row, not yet registered"},
]
DECISIONS["DUP-49"]["progress"].append({"date": "2026-10-30", "step": "agreed", "by": "Reality + Cognition keepers",
    "note": "Cognition owns food preferences, anticipated enjoyment, appetite motivation and the eating decision (cognition.decision.select); Reality the body signals body.hunger_signal, body.satiety_signal and the sensory body.taste_percept; the nutrition library's 0.3 / 0.8 thresholds are not adopted. Cognition unit 2720 (Composer, doc) records the quantities in DESIGN §8"})

# --- 2026-10-30: Reality keeper's answers on DUP-18 (REG-25, REG-26) and the G7 / G10 amendments ---
DECISIONS["DUP-18"]["progress"].append({"date": "2026-10-30", "step": "fixes planned", "by": "Reality keeper",
    "note": "(1) worked example vs closed form sent to the controller as Rex's call; (2) pirate PHYSIOLOGY.md s2 prose and rendered table: a pirate-lane Composer unit once the kernel is restored; (3) 2712's WORK requires the clamp recomputed with tau 38 / 1.9 d, k1 0.048, k2 0.117, and a '(2635) open:' flag for Rex if it saturates, never a rescale"})
for _g in ("DUP-12", "DUP-25"):
    DECISIONS[_g]["progress"].append({"date": "2026-10-30", "step": "amendment accepted", "by": "Reality keeper"})

# --- 2026-10-30: the writer of body.taste_percept (DUP-49), registered at the Reality keeper's request: planned, no formula decided ---
EXTRA_ROWS.append({
    "id": "realism.perception.taste", "name": "Taste perception (sensory half of palatability)", "engine": "realism",
    "home": "Toolchain/realism (planned; post-P1 phase work, Reality keeper 2026-10-30; not part of the DUP-49 doc unit)",
    "status": "planned", "domain": "B", "scope": "universal",
    "inputs": [{"name": "food chemistry by taste category", "unit": "see quantities.json"},
               {"name": "anatomy senses integrity (realism library anatomy 'senses' row; no registry row yet)", "unit": "1"},
               {"name": "zinc status (realism.nutrition.pools)", "unit": "see quantities.json"}],
    "outputs": [{"name": "body.taste_percept", "unit": "1"}],
    "state": "planned", "formulation": "not decided: no numbers or formula yet (Reality keeper); the design is post-P1 phase work",
    "dependencies": ["realism.nutrition.pools"], "timescale": "planned",
    "invariants": "the sensory half only: what is tasted, never whether it is liked or eaten (Cognition's evaluative half, DUP-49); until built, Cognition treats the percept as absent, with no default value",
    "sources": "to research (evidence levels stated)", "evidence": "?", "approximations": "planned", "tests": "none",
    "consumers": ["cognition.preference.contextual_evaluation", "cognition.needs.drive"],
    "notes": "DUP-49 (batch 2 group 12): the DUP-49 realism unit adds a '(DUP-49) planned:' flag line naming this row",
    "audit_batch": "reality-keeper-2026-10-30", "planned_writes": ["body.taste_percept"]})
QUANTITY_PATCH["body.taste_percept"] = {"writer": "realism.perception.taste",
    "status": "proposed (DUP-49, agreed Reality + Cognition 2026-10-30); writer realism.perception.taste is planned, not built: absent until built, no default value"}

# --- Rex 2026-10-30 (late evening), ENGINES.md "Planetary terrain and resource formation": a planned subsystem of Physical Reality
# (owner Reality), built with P2 beside mechanics, materials, fluids and geology. Planned only; no code, no unit.
# Existing rows checked first (registry keeper): realism.eco.* stocks and soil fertility, pirate.eco.* crops and stocks, pirate.env.*
# climate and weather (DUP-34, 35), realism.env.exposure_by_terrain, realism.population.famine (foodDays: a store, not a terrain stock),
# settlement.land.*, economy.material.produce / production.abstract_market. Overlaps are DUP-50..53 below (proposed, batch 3). ---
_TER_HOME = "Toolchain/ENGINES.md 'Planetary terrain and resource formation' (Rex 2026-10-30; Physical Reality P2 subsystem; planned)"
_TER_INV = ("conservation: extracted or harvested mass leaves its stock, sediment moves from one place to another, consumed water comes from somewhere; "
            "Economy never creates a physical resource because a recipe ran; no biome loot tables: a deposit or stock exists only where geological, "
            "hydrological, climatic and ecological processes make it plausible; every resource has quantity, quality, accessibility and location; "
            "generation is hierarchical and constraint-based, never a replay of planetary history, and reproducible from the Kernel's seeded RNG; "
            "the platform never represents the planet as blocks")
def _ter(k, name, form, writes, reads, consumers, notes="", ev="4", eng="realism", dom="A", deps=None):
    return {"id": k, "name": name, "engine": eng, "home": _TER_HOME, "status": "planned", "domain": dom, "scope": "universal",
            "inputs": [{"name": x, "unit": "see quantities.json"} for x in reads], "outputs": [{"name": x, "unit": "see quantities.json"} for x in writes],
            "state": "planned", "formulation": form, "dependencies": deps or [], "timescale": "planned (generation once per world; slow change per year)",
            "invariants": _TER_INV, "sources": "to research per unit (evidence levels stated); ENGINES.md", "evidence": ev,
            "evidence_note": "registry's provisional level: established geoscience applied as constraint rules (level 4, approximation) until each unit states its sources",
            "approximations": "planned", "tests": "none", "consumers": consumers, "notes": notes,
            "audit_batch": "rex-2026-10-30-terrain", "planned_writes": writes}
EXTRA_ROWS += [
 _ter("realism.terrain.generation", "Hierarchical world generation (orchestration)",
      "the order of the constraint passes: provinces and broad elevation -> drainage with erosion and deposition -> formations and plausible deposits -> soils -> vegetation and wildlife -> conversion to a game's view; seeded from the Kernel's RNG; writes nothing of its own",
      [], ["world.geological_province", "world.elevation", "world.soil"], ["shared.contract.terrain_view"],
      "required tests (Rex): deterministic seeds, material-conservation tests, geological plausibility checks, cross-domain integration tests"),
 _ter("realism.terrain.provinces", "Geological provinces and broad elevation",
      "planetary and geological initial conditions (crust, rock types, tectonic setting and history, climate zone) as provinces with a base elevation",
      ["world.geological_province", "world.base_elevation"], [], ["realism.terrain.formations", "realism.terrain.geomorphology"]),
 _ter("realism.terrain.formations", "Formations and faults",
      "rock formations by depth and faults within a province (sedimentary, igneous, metamorphic units; carbonate sedimentation gives limestone)",
      ["world.formation"], ["world.geological_province", "world.elevation"], ["realism.terrain.mineral_deposits", "realism.terrain.soils", "shared.contract.terrain_view"]),
 _ter("realism.terrain.mineral_deposits", "Mineral deposits",
      "deposits where formation processes make them plausible (iron from mineralisation, sediment and weathering; gold hydrothermal and placer; clay from weathering and deposition): composition, volume, grade, accessibility and location; extraction removes mass",
      ["world.deposit"], ["world.formation", "world.sediment_flux", "world.drainage"], ["economy.material.produce", "shared.contract.terrain_view"],
      "owner of physical ore, stone and clay stocks (DUP-52)"),
 _ter("realism.terrain.hydrology", "Hydrology: drainage and groundwater",
      "rivers and drainage basins from elevation and rainfall; groundwater storage and flow; consumed water is drawn from a stock",
      ["world.drainage", "world.groundwater"], ["world.elevation", "world.formation"], ["realism.terrain.geomorphology", "realism.terrain.soils", "shared.contract.terrain_view"],
      "boundary with P2 weather's 'surface energy and water' (soil moisture, surface water): to agree when the weather rows are registered; one owner per state"),
 _ter("realism.terrain.geomorphology", "Geomorphology: erosion, sediment transport, deposition",
      "erosion, sediment transport and deposition change elevation over time and move mass between places (conserved)",
      ["world.elevation", "world.sediment_flux"], ["world.base_elevation", "world.drainage", "world.formation"],
      ["realism.terrain.mineral_deposits", "realism.terrain.soils", "settlement.land.parcel_split_merge", "shared.contract.terrain_view"],
      "the only writer of elevation after generation (provinces writes the base); erosion in realism.eco.soil_fertility is a candidate duplicate (DUP-51)"),
 _ter("realism.terrain.soils", "Soils",
      "soil development from parent material, climate, terrain and time: texture, depth, organic matter, nutrients, drainage class",
      ["world.soil"], ["world.formation", "world.elevation", "world.drainage", "world.sediment_flux"],
      ["realism.terrain.vegetation_stocks", "realism.eco.soil_fertility", "shared.contract.terrain_view"],
      "owner of soil state; the built fertility index becomes its aggregate or read (DUP-51)", dom="B"),
 _ter("realism.terrain.vegetation_stocks", "Vegetation stocks",
      "plants as stocks with species, age, dimensions and biomass from species suitability, climate, soil, light and competition (never 'forest = 100 wood'); harvest removes biomass",
      ["world.vegetation_stock"], ["world.soil", "world.drainage"], ["realism.terrain.wildlife_habitat", "economy.material.produce", "shared.contract.terrain_view"],
      "crops grown on farmland are vegetation under management (DUP-53)", dom="B"),
 _ter("realism.terrain.wildlife_habitat", "Wildlife habitat and stocks",
      "habitat suitability and wildlife (land and fish) as biomass by species and age from habitat, food webs, temperature, oxygen and reproduction; hunting and fishing remove biomass",
      ["world.wildlife_stock"], ["world.vegetation_stock", "world.drainage", "world.soil"], ["economy.material.produce", "realism.eco.logistic_stock", "shared.contract.terrain_view"],
      "detailed owner of animal stocks; the built logistic and MSY rows become its documented aggregate (DUP-50)", dom="B"),
 _ter("shared.contract.terrain_view", "Terrain view for game adapters",
      "the read-only view a game adapter converts into its own representation: elevation -> tile height; formation -> underground block types; deposit volume and grade -> mineable blocks; soil -> farm tiles; biomass -> harvestable trees; groundwater -> wells; material properties -> tools and construction",
      [], ["world.elevation", "world.formation", "world.deposit", "world.soil", "world.vegetation_stock", "world.groundwater"], [],
      "shared contract, not an engine; Runeworld (Games/P games/Runeworld DESIGN §16, BUILD_PLAN M1) is reference material for the interface only", eng="shared", dom="i", ev="?"),
]
INTERFACES += [
 ("IF-20", "realism.terrain.mineral_deposits", "economy.material.produce",
  "Physical stocks to Economy extraction (Rex 2026-10-30): extraction reads deposits, vegetation and wildlife stocks and writes removals that Reality checks against the stock (mass conserved); Economy owns the activity, inventories, processing, trade and valuation, never the physical existence of a resource.", ["DUP-52"]),
 ("IF-21", "realism.terrain.geomorphology", "settlement.land.parcel_split_merge",
  "Terrain to Settlement (Rex 2026-10-30): parcels, buildings and infrastructure read terrain (elevation, soil, drainage, deposits under the parcel); Settlement never edits terrain except through Reality's processes.", []),
 ("IF-22", "realism.terrain.generation", "shared.contract.terrain_view",
  "Terrain to game adapters (Rex 2026-10-30): a game converts the physical terrain into its maps, tiles or blocks through the read-only view; the conversion is the game's, the physics stays in Reality.", []),
]
for _id, _k, _u, _w, _desc in [
 ("world.geological_province", "record", None, "realism.terrain.provinces", "a province: crust, rock types, tectonic setting, climate zone"),
 ("world.base_elevation", "quantity", "m", "realism.terrain.provinces", "elevation at generation (before erosion and deposition)"),
 ("world.elevation", "quantity", "m", "realism.terrain.geomorphology", "current elevation (base plus erosion and deposition)"),
 ("world.formation", "record", None, "realism.terrain.formations", "rock formations by depth and faults"),
 ("world.deposit", "record", None, "realism.terrain.mineral_deposits", "a deposit: composition, volume (m3), grade, accessibility, location; mass leaves it on extraction"),
 ("world.drainage", "record", None, "realism.terrain.hydrology", "drainage network: rivers, basins, flow"),
 ("world.groundwater", "quantity", "m3", "realism.terrain.hydrology", "groundwater stored per area"),
 ("world.sediment_flux", "quantity", "kg/a", "realism.terrain.geomorphology", "sediment moved from one place to another (conserved)"),
 ("world.soil", "record", None, "realism.terrain.soils", "soil: texture, depth, organic matter, nutrients, drainage class"),
 ("world.vegetation_stock", "record", None, "realism.terrain.vegetation_stocks", "plants by species, age, dimensions and biomass (kg)"),
 ("world.wildlife_stock", "record", None, "realism.terrain.wildlife_habitat", "animals by species and age with biomass (kg); habitat suitability"),
]:
    _q = {"id": _id, "kind": _k, "unit": _u, "scope": "world", "writer": _w, "description": _desc,
          "status": "planned (Rex 2026-10-30, planetary terrain and resource formation; P2)"}
    if _id in ("world.deposit", "world.vegetation_stock", "world.wildlife_stock", "world.groundwater"):
        _q["external_writers"] = ["Economy extraction (removals only, checked by Reality against the stock; IF-20)"]
    EXTRA_QUANTITIES.append(_q)
# Candidate overlap groups found while registering (proposed for batch 3; nothing decided)
GROUPS += [
 ("DUP-50", "duplicate", "Animal stocks: built logistic stock, fished-out catch and MSY rows (and pirate Schaefer stock, nesting females) model fish as one biomass number; the planned wildlife row holds species and age (terrain registration 2026-10-30)",
  ["realism.terrain.wildlife_habitat", "realism.eco.logistic_stock", "realism.eco.fished_out_catch", "realism.eco.msy_collapse_recovery", "pirate.eco.schaefer_stock", "pirate.eco.nesting_females"],
  "realism.terrain.wildlife_habitat owns the stock by species and age; the logistic/MSY rows become its documented aggregate (refinement B); pirate rows restate"),
 ("DUP-51", "duplicate", "Soil: the built fertility index (yield, harvest drain, manure, fallow, erosion) and the pirate restatement vs the planned soils row; erosion also in geomorphology",
  ["realism.terrain.soils", "realism.eco.soil_fertility", "pirate.eco.soil_fertility", "realism.terrain.geomorphology"],
  "realism.terrain.soils owns soil state, realism.terrain.geomorphology erosion; the fertility index becomes a read or aggregate of soil state"),
 ("DUP-52", "ownership", "Economy can create physical goods with no physical source: host addStock, abstract-market production, recipes with no inputs (pirate fixture butchering); Rex: Economy never creates a physical resource",
  ["realism.terrain.mineral_deposits", "economy.material.produce", "economy.production.abstract_market", "realism.terrain.vegetation_stocks", "realism.terrain.wildlife_habitat"],
  "Reality owns physical stocks; Economy extraction removes from them (IF-20); host seeding and off-map abstract markets become declared boundary inputs, not creation"),
 ("DUP-53", "duplicate", "Crop yield: pirate rain factor and crop table compute yields directly from rain and a table; Rex: farmland yield from soil, water, nutrients and climate",
  ["realism.terrain.vegetation_stocks", "pirate.eco.crop_rain", "pirate.eco.crops_table", "realism.eco.soil_fertility"],
  "crops as managed vegetation (realism.terrain.vegetation_stocks) reading soils and weather; the pirate rows become restatements or adapter reads"),
]
AUTH.update({
 "DUP-50": ("aggregation", "a species-and-age stock (detail) and a logistic biomass stock (aggregate) may coexist once the aggregate reads the detailed owner"),
 "DUP-51": ("mixed", "a fertility index can be a legitimate aggregate of soil state; erosion computed in two places is duplicate"),
 "DUP-52": ("ownership-gap", "no physical owner of extracted resources today"),
 "DUP-53": ("duplicate-authority", ""),
})
for _g in ("DUP-50", "DUP-51", "DUP-52", "DUP-53"): BATCH[_g] = 3

# --- Rex 2026-10-30 (via the controller): DUP-18 Banister verification ---
DECISIONS["DUP-18"]["progress"].append({"date": "2026-10-30", "step": "verification half closed", "by": "Rex (via the controller)",
    "note": "the single-impulse closed-form test (realism test/muscular.test.ts, 5381e00) is approved as mathematical verification only; empirical validation against dated loads and measured performance is required before any claim of accuracy. Group stays closing on REG-25 (2) pirate PHYSIOLOGY.md s2 and REG-26 (the clamp, 2712)"})
VV_OVERRIDES["realism.muscular.banister"] = {"validated": "candidate (needs dated-load data)",
    "evidence": "implemented and verified: single-impulse closed form with the Busso 1991 means (5381e00), approved by Rex 2026-10-30 as verification only; validation needs dated training loads with measured performance (fit on part, predict the rest)"}

# --- Rex 2026-10-30 (late evening), ENGINES.md "Terrestrial and aquatic ecosystem foundation": subsystems of Physical Reality and
# Life & Species; research domain the Caribbean of the pirate era, mechanisms universal. Planned only; no code, no unit.
# Checked first (registry keeper): realism.atmos.barometric_pressure (built), pirate weather/climate (DUP-34), realism.eco.* stocks and
# soil fertility, pirate.eco.* crops and stocks, realism.population.famine (a food store, no overlap), realism.nutrition.* (human intake,
# no overlap), and tonight's planned terrain rows. New rows own state; earlier planned terrain rows are narrowed, never duplicated. ---
_ECO_HOME = "Toolchain/ENGINES.md 'Terrestrial and aquatic ecosystem foundation' (Rex 2026-10-30; planned; research domain Caribbean pirate era)"
_ECO_INV = ("conservation: nutrients (N, P, K) move between soil, water, plants, animals and detritus and are never created or lost except across a declared boundary "
            "(runoff to sea, leaching, atmospheric input, fixation); water moves between soil, plants, atmosphere and hydrology; biomass changes only by growth, "
            "consumption, harvest, death and decomposition, with energy dissipated as respiration heat and accounted; populations, never rendered individuals, for "
            "pollinators and animals; overfishing, clearing and runoff change populations through the same equations, never event scripts; deficiency reduces "
            "growth gradually before preventing it, by species tolerance; each species added one at a time with researched conditions")
def _eco(k, name, dom, form, writes, reads, consumers, ev, notes="", eng="realism"):
    return {"id": k, "name": name, "engine": eng, "home": _ECO_HOME, "status": "planned", "domain": dom, "scope": "universal",
            "inputs": [{"name": x, "unit": "see quantities.json"} for x in reads], "outputs": [{"name": x, "unit": "see quantities.json"} for x in writes],
            "state": "planned", "formulation": form, "dependencies": [], "timescale": "planned (Kernel scheduler: fast processes often, growth and populations on longer intervals)",
            "invariants": _ECO_INV, "sources": "to research per unit with web tools, values labelled researched / estimate; ENGINES.md", "evidence": ev,
            "evidence_note": "registry's provisional level for the mechanism class; each unit states its own",
            "approximations": "planned", "tests": "none", "consumers": consumers, "notes": notes,
            "audit_batch": "rex-2026-10-30-ecosystem", "planned_writes": writes}
EXTRA_ROWS += [
 # Physical Reality
 _eco("realism.atmos.pressure_wind", "Atmospheric pressure field and wind", "A",
      "surface and column pressure from the atmosphere's state; wind from pressure gradients with Coriolis and surface friction; the built barometric_pressure row is its altitude profile (a read)",
      ["air.pressure_field", "air.wind"], ["world.elevation"], ["realism.terrain.geomorphology", "realism.plant.abiotic_pollination", "realism.ecology.seed_dispersal"], "1",
      "needed for weather from physics (ROADMAP P2 weather, Rex's 'phase 13') and the deeper geology; the eventual owner of wind in DUP-34"),
 _eco("realism.terrain.nutrient_transport", "Nutrient transport", "A",
      "nutrients carried by runoff, leaching, erosion and deposition (with geomorphology's sediment and hydrology's water); writes fluxes, never the soil stock",
      ["world.nutrient_flux"], ["world.sediment_flux", "world.drainage", "world.soil_nutrient_pool"], ["realism.terrain.soils"], "2"),
 _eco("realism.terrain.geological_events", "Geological events in the active world", "A",
      "occasional events during play: earthquakes, volcanism and lava flow (plate tectonics allowed), changing formations and terrain; conserved mass",
      ["world.geological_event"], ["world.geological_province", "world.formation"], ["realism.terrain.geomorphology", "realism.terrain.formations"], "4",
      "the active-world counterpart of the once-run formation stage (realism.terrain.generation)"),
 # Life & Species
 _eco("realism.plant.physiology", "Plant physiology and growth", "B",
      "photosynthesis, respiration, maintenance, water stress, light and temperature response per plant (or cohort) using the three organism records (realism.records.*): genetic profile; developmental state (age, root and shoot biomass, leaf area, stored carbohydrate, maturity); current state (hydration, nutrient status, stress, damage, disease); species tolerance of pH, nutrients and water; primary producers include algae, phytoplankton and seagrass",
      ["world.plant_state"], ["world.soil", "world.soil_nutrient_pool", "world.soil_ph", "world.groundwater", "air.wind"],
      ["realism.terrain.vegetation_stocks", "realism.plant.reproduction", "realism.ecology.animal_populations", "realism.ecology.decomposition"], "2",
      "first species proposed (Rex): West Indian mahogany, sugarcane, red mangrove, turtle grass; tree.md, plant.md and per-species profiles are belt research units"),
 _eco("realism.plant.reproduction", "Plant reproduction", "B",
      "pollen and seed, spores, and vegetative reproduction as separate paths; fertilisation needs pollen transfer and compatibility; inheritance through realism.genetics.inheritance",
      ["world.seed_bank"], ["world.plant_state", "world.pollination_events"], ["realism.plant.physiology", "realism.ecology.seed_dispersal"], "4"),
 _eco("realism.ecology.pollinators", "Pollinator populations and visits", "B",
      "pollinator populations (abundance, foraging range, activity, habitat, breeding, mortality at natural values); expected visits V_ij = N_i a_i p_ij dt as a starting approximation, then pollen transfer, compatibility and conditions",
      ["world.pollinator_population", "world.pollination_events"], ["world.plant_state", "world.habitat_suitability"], ["realism.plant.reproduction"], "4",
      "populations, never rendered bees; the visits formula is a starting approximation (Rex)"),
 _eco("realism.plant.abiotic_pollination", "Wind and self-pollination", "B",
      "wind pollination from pollen release and air movement; self-pollination by species compatibility; separate from animal pollination",
      ["world.abiotic_pollination_events"], ["world.plant_state", "air.wind"], ["realism.plant.reproduction"], "4"),
 _eco("realism.ecology.seed_dispersal", "Seed dispersal", "B",
      "seed movement by animals, wind and water as separate mechanisms; establishment depends on the site's soil, water and light",
      ["world.seed_dispersal"], ["world.seed_bank", "world.wildlife_stock", "air.wind", "world.drainage"], ["realism.plant.physiology"], "4"),
 _eco("realism.ecology.animal_populations", "Herbivore, carnivore and fish populations", "B",
      "animal populations by species, trophic role and age: breeding, mortality, foraging and predation at natural values; land animals and fish; animal physiology at population level",
      ["world.wildlife_stock"], ["world.plant_state", "world.habitat_suitability", "world.trophic_flux"],
      ["realism.ecology.food_web", "realism.ecology.decomposition", "economy.material.produce", "realism.eco.logistic_stock"], "4",
      "owner of world.wildlife_stock (takes it over from realism.terrain.wildlife_habitat, which keeps habitat suitability); the built logistic and MSY rows become its aggregate (DUP-50)"),
 _eco("realism.ecology.decomposition", "Decomposition and mineralisation", "B",
      "decomposers and detritus: dead biomass breaks down, nutrients are mineralised back to soil and water, energy dissipates; microbial activity by temperature, moisture and pH",
      ["world.detritus", "world.mineralisation_flux"], ["world.plant_state", "world.wildlife_stock", "world.soil_ph"], ["realism.terrain.soils"], "2"),
 _eco("realism.ecology.food_web", "Food-web energy transfer", "B",
      "energy and mass transfer between trophic levels (algae and plants -> fish and herbivores -> carnivores; parasites; decomposers), with dissipation per level",
      ["world.trophic_flux"], ["world.plant_state", "world.wildlife_stock", "world.detritus"], ["realism.ecology.animal_populations"], "2"),
]
# Narrow tonight's planned terrain rows so nothing is owned twice (all planned; no code exists).
ROW_PATCHES.update({
 "realism.terrain.wildlife_habitat": {"name": "Wildlife habitat suitability", "planned_writes": ["world.habitat_suitability"], "outputs": [{"name": "world.habitat_suitability", "unit": "1"}],
    "formulation": "habitat suitability per species from vegetation, water, soil, temperature and oxygen (land and aquatic)",
    "notes": "narrowed 2026-10-30 (ecosystem registration): the animal stock moved to realism.ecology.animal_populations; this row keeps habitat suitability"},
 "realism.terrain.vegetation_stocks": {"notes": "2026-10-30 (ecosystem registration): the documented aggregate of realism.plant.physiology (stand biomass by species and age class, refinement B); crops grown on farmland are vegetation under management (DUP-53)"},
 "realism.terrain.soils": {"formulation": "soil formation from parent material, climate, terrain and time; soil chemistry: texture, depth, organic matter, pH, N/P/K pools, water retention, microbial activity; the only writer of the soil stocks, integrating the fluxes of nutrient transport, decomposition, plant uptake and harvest",
    "planned_writes": ["world.soil", "world.soil_ph", "world.soil_nutrient_pool"],
    "outputs": [{"name": "world.soil", "unit": "record"}, {"name": "world.soil_ph", "unit": "1"}, {"name": "world.soil_nutrient_pool", "unit": "kg"}],
    "notes": "extended 2026-10-30 (ecosystem registration, Rex: emulate real soil data); owner of soil state; the built fertility index becomes its aggregate or read (DUP-51)"},
 "realism.terrain.generation": {"name": "World formation stage (once-run geological history)",
    "notes": "Rex 2026-10-30 (ecosystem): two timescales; this is the once-run formation stage (a plausible geological history or real Earth data establishes formations, deposits, terrain and soils once); active-world processes run on the Kernel scheduler. Required tests: deterministic seeds, conservation, geological plausibility, cross-domain integration"},
})
QUANTITY_PATCH["world.wildlife_stock"] = {"writer": "realism.ecology.animal_populations",
    "description": "animal populations by species, trophic role and age with biomass (kg); land animals and fish"}
for _id, _sc, _k, _u, _w, _desc in [
 ("air.pressure_field", "air", "quantity", "Pa", "realism.atmos.pressure_wind", "surface pressure field"),
 ("air.wind", "air", "quantity", "m/s", "realism.atmos.pressure_wind", "wind velocity (speed, with direction as an attribute)"),
 ("world.nutrient_flux", "world", "quantity", "kg/a", "realism.terrain.nutrient_transport", "N, P, K moved by runoff, leaching, erosion and deposition"),
 ("world.geological_event", "world", "record", None, "realism.terrain.geological_events", "an earthquake, eruption or lava flow during play"),
 ("world.soil_ph", "world", "quantity", "1", "realism.terrain.soils", "soil pH (dimensionless)"),
 ("world.soil_nutrient_pool", "world", "quantity", "kg", "realism.terrain.soils", "soil N, P and K pools per area (indexed by nutrient)"),
 ("world.habitat_suitability", "world", "quantity", "1", "realism.terrain.wildlife_habitat", "habitat suitability per species (0-1)"),
 ("world.plant_state", "world", "record", None, "realism.plant.physiology", "per plant or cohort: the three organism records' plant fields"),
 ("world.seed_bank", "world", "record", None, "realism.plant.reproduction", "seeds, spores and propagules by species"),
 ("world.pollinator_population", "world", "record", None, "realism.ecology.pollinators", "pollinator populations by species"),
 ("world.pollination_events", "world", "record", None, "realism.ecology.pollinators", "expected animal visits and pollen transfer"),
 ("world.abiotic_pollination_events", "world", "record", None, "realism.plant.abiotic_pollination", "wind and self-pollination"),
 ("world.seed_dispersal", "world", "record", None, "realism.ecology.seed_dispersal", "seed movement by animals, wind and water"),
 ("world.detritus", "world", "quantity", "kg", "realism.ecology.decomposition", "dead organic matter per area"),
 ("world.mineralisation_flux", "world", "quantity", "kg/a", "realism.ecology.decomposition", "nutrients returned from detritus to soil and water"),
 ("world.trophic_flux", "world", "quantity", "kg/a", "realism.ecology.food_web", "biomass transferred between trophic levels (energy as an attribute)"),
]:
    EXTRA_QUANTITIES.append({"id": _id, "kind": _k, "unit": _u, "scope": _sc, "writer": _w, "description": _desc,
        "status": "planned (Rex 2026-10-30, ecosystem foundation)"})
# Candidate overlaps: extend tonight's batch-3 candidates and DUP-34 with the new owners
_ADD = {"DUP-50": ["realism.ecology.animal_populations"], "DUP-53": ["realism.plant.physiology"], "DUP-34": ["realism.atmos.pressure_wind"]}
GROUPS[:] = [(g[0], g[1], g[2], g[3] + _ADD.get(g[0], []),
              {"DUP-50": "realism.ecology.animal_populations owns animal stocks by species, trophic role and age; the logistic/MSY rows become its documented aggregate (refinement B); pirate rows restate",
               "DUP-53": "crops as managed plants: realism.plant.physiology (yield from soil, water, nutrients, climate by species tolerance), aggregated by realism.terrain.vegetation_stocks; the pirate rows become restatements or adapter reads"}.get(g[0], g[4]))
             for g in GROUPS]
GROUPS.append(("DUP-54", "duplicate", "Atmospheric pressure: built barometric pressure by altitude (a closed formula) vs the planned pressure field; the pirate climate table's wind and the sailing wind as data (ecosystem registration 2026-10-30)",
  ["realism.atmos.pressure_wind", "realism.atmos.barometric_pressure", "pirate.env.wind_sailing"],
  "realism.atmos.pressure_wind owns pressure and wind; barometric_pressure becomes its altitude profile (a read, kept for still.test); the sailing wind reads air.wind through the plugin adapter"))
AUTH["DUP-54"] = ("mixed", "the altitude profile is a legitimate part of the field; a second wind source is duplicate")
BATCH["DUP-54"] = 3
INTERFACES.append(("IF-23", "realism.ecology.animal_populations", "economy.material.produce",
  "Living stocks to Economy (Rex 2026-10-30): fishing, hunting, forestry and harvest read the population and plant stocks and write removals Reality checks (biomass conserved); overfishing and clearing change populations through the population equations.", ["DUP-50", "DUP-52"]))

# --- Rex 2026-10-31, ENGINES.md "Soil mechanics and excavation": Physical Reality, planned only; a consumer of three universal systems
# (materials, biomechanics, the Kernel), never a game rule. Checked first: realism.terrain.soils (sole writer of world.soil),
# realism.terrain.geomorphology (sole writer of world.elevation), realism.contact.penetration and realism.materials.deformation_fracture_decay
# (planned), realism.muscular.limb_strength, settlement.project.construction. One soil record; elevation keeps one writer. ---
_SM_HOME = "Toolchain/ENGINES.md 'Soil mechanics and excavation' (Rex 2026-10-31; Physical Reality, materials phase 9 and contact 6b; planned)"
_SM_INV = ("conservation: excavated mass equals spoil created (spoil can be piled, moved, processed or used as fill); the hole changes terrain geometry and water, "
           "slopes and foundations respond through the same mechanisms; one soil record serves agriculture, groundwater, erosion, landslides, foundations and digging; "
           "no diggingPower number: wet clay and dry sand differ by their properties, a weaker body removes less, a skilled one spends less energy per volume; "
           "games supply only the dig command and its presentation")
def _sm(k, name, form, writes, reads, consumers, ev, notes="", eng="realism", dom="A"):
    return {"id": k, "name": name, "engine": eng, "home": _SM_HOME, "status": "planned", "domain": dom, "scope": "universal",
            "inputs": [{"name": x, "unit": "see quantities.json"} for x in reads], "outputs": [{"name": x, "unit": "see quantities.json"} for x in writes],
            "state": "planned", "formulation": form, "dependencies": [], "timescale": "planned (per stroke while digging; persistent geometry afterwards)",
            "invariants": _SM_INV, "sources": "to research per unit; ENGINES.md", "evidence": ev, "evidence_note": "registry's provisional level; each unit states its own",
            "approximations": "planned", "tests": "none", "consumers": consumers, "notes": notes, "audit_batch": "rex-2026-10-31-soil-mechanics", "planned_writes": writes}
EXTRA_ROWS += [
 _sm("realism.soil.mechanical_properties", "Soil mechanical properties (part of the one soil record)",
     "the mechanical fields of world.soil: bulk density, grain-size fractions, moisture, cohesion, internal friction angle, porosity, compaction, organic matter, rock content, and their relations (cohesion and friction from grain size and moisture; compaction under load); writes nothing of its own: realism.terrain.soils stays the only writer of world.soil",
     [], ["world.soil", "world.groundwater"], ["realism.materials.shear_strength", "realism.terrain.excavation", "realism.terrain.excavation_stability", "settlement.project.construction"], "2",
     "one record, never a second soil state (controller 2026-10-31)"),
 _sm("realism.materials.shear_strength", "Soil shear strength (Mohr-Coulomb)",
     "tau_f = c' + sigma' tan phi' from the soil record's cohesion, friction angle and effective stress (pore pressure from moisture and groundwater); a function read by excavation, stability and foundations",
     [], ["world.soil", "world.groundwater"], ["realism.terrain.excavation", "realism.terrain.excavation_stability", "realism.contact.penetration"], "1",
     "materials (phase 9); the soil failure criterion contact penetration should read for soil targets (DUP-55)"),
 _sm("realism.terrain.excavation", "Excavation",
     "work-bounded removal: work W = integral F dx per stroke from the body's force, speed and fatigue (biomechanics: limb strength, articulated locomotion, fatigue, functional capacity) and the tool's geometry, against the soil's shear strength; loosened mass leaves the terrain as spoil; ore and stone removed also leave their deposit (IF-20)",
     ["world.excavation_removal", "world.spoil_stock"], ["world.soil", "body.capacity_functional", "world.deposit"],
     ["realism.terrain.geomorphology", "realism.terrain.excavation_stability", "economy.material.produce", "settlement.project.construction", "shared.contract.terrain_view"], "4",
     "writes removals and the spoil stock; realism.terrain.geomorphology applies removals to world.elevation (one writer); the Kernel keeps time, events and the persistent change"),
 _sm("realism.terrain.excavation_stability", "Slope and excavation-face stability",
     "slope and face stability by soil state (dry sand slumps at steep angles; cohesive soil holds temporarily by moisture and load) and rock fractures and stress (holds or needs support); a failure is an event moving conserved mass",
     ["world.slope_failure"], ["world.soil", "world.formation", "world.elevation", "world.groundwater"], ["realism.terrain.geomorphology", "settlement.project.construction"], "2",
     "the same material mechanics engineers use; gives mining, tunnelling and fortification their rules"),
 _sm("shared.contract.terrain_resolution", "Adaptive terrain resolution",
     "terrain cells refine on demand: a distant hillside is elevation, layers and aggregate quantities; a field is per-cell soil properties; an active dig subdivides into volumetric cells; a landslide invokes the detailed deformation calculation while it lasts; the resulting geometry and material distribution persist without further computation (PLATFORM §9); quantities conserved across refinement and coarsening",
     [], ["world.elevation", "world.soil", "world.formation"], ["realism.terrain.excavation", "realism.terrain.excavation_stability", "shared.contract.terrain_view"], "?",
     "a shared contract (not an engine) with the Kernel, which keeps the cells' events and persistence; no Kernel row exists yet", eng="shared", dom="i"),
]
ROW_PATCHES["realism.terrain.geomorphology"] = {"notes": "the only writer of elevation after generation (provinces writes the base); applies excavation removals and slope failures (2026-10-31) as well as erosion and deposition; erosion in realism.eco.soil_fertility is a candidate duplicate (DUP-51)"}
QUANTITY_PATCH["world.soil"] = {"description": "the one soil record: texture and grain-size fractions, depth, bulk density, porosity, moisture, compaction, cohesion, internal friction angle, organic matter, rock content, drainage class (pH and N/P/K are their own quantities); written only by realism.terrain.soils"}
for _id, _k, _u, _w, _desc in [
 ("world.excavation_removal", "record", None, "realism.terrain.excavation", "per stroke and cell: volume and mass removed (geomorphology applies it to elevation)"),
 ("world.spoil_stock", "record", None, "realism.terrain.excavation", "spoil piles: mass, volume, composition, location (mass equals what was excavated)"),
 ("world.slope_failure", "record", None, "realism.terrain.excavation_stability", "a slump or collapse: mass displaced and where"),
]:
    EXTRA_QUANTITIES.append({"id": _id, "kind": _k, "unit": _u, "scope": "world", "writer": _w, "description": _desc,
        "status": "planned (Rex 2026-10-31, soil mechanics and excavation)"})
QUANTITY_PATCH["world.spoil_stock"] = {"external_writers": ["Economy and Settlement (moving, processing or using spoil as fill, checked by Reality against the stock)"]}
INTERFACES += [
 ("IF-24", "realism.terrain.excavation", "settlement.project.construction",
  "Excavation to Settlement (Rex 2026-10-31): foundations, ditches and fill read the excavated geometry, spoil and the soil's bearing (shear strength, stability); Settlement never moves earth except through excavation.", []),
 ("IF-25", "shared.contract.terrain_view", "realism.terrain.excavation",
  "Game dig command to excavation (Rex 2026-10-31): a game supplies only the dig command (who, where, with which tool) and its presentation; the removal, spoil and consequences are Reality's.", []),
]
GROUPS.append(("DUP-55", "duplicate", "Tool against material resistance in two planned places: contact mechanics' penetration against a material resistance profile and excavation against soil shear strength; material failure also in the planned deformation-fracture row (soil mechanics registration 2026-10-31)",
  ["realism.materials.shear_strength", "realism.contact.penetration", "realism.terrain.excavation", "realism.materials.deformation_fracture_decay"],
  "realism.materials.shear_strength owns the soil failure criterion; contact penetration reads it when the target is soil; excavation is a sequence of contact events; deformation_fracture keeps solids"))
AUTH["DUP-55"] = ("shared-part", "distinct mechanisms that must share one material-failure criterion per material; nothing built on either side")
BATCH["DUP-55"] = 3

# --- 2026-10-31: economy integration tests for the seven pairs unit 2718's V&V warnings flag (economy keeper's candidates;
# test names verified at economy e366b49 by the registry keeper) ---
_E = "Toolchain/economy test/"
CHAINS += [
 {"id": "economy:E5-consumption", "test": _E + "markets.test.ts E5 'consumption draws the market's stock by the host's numbers' (e366b49)", "complete": True,
  "conservation": "market stock decreases by the drawn units", "members": ["economy.market.five_numbers", "economy.consumption.demand"]},
 {"id": "economy:E5-abstract-market", "test": _E + "markets.test.ts E5 'an abstract market adds its productionPerDay to its own stock' (e366b49)", "complete": True,
  "conservation": "market stock increases by productionPerDay", "members": ["economy.market.five_numbers", "economy.production.abstract_market"]},
 {"id": "economy:E7-shortage", "test": _E + "markets.test.ts E7 'a shortage event when stock falls under the target reserve' (e366b49)", "complete": True,
  "conservation": "event emitted at the threshold", "members": ["economy.market.five_numbers", "economy.shortage.event"]},
 {"id": "economy:E2-observed-production", "test": _E + "engine.test.ts E2 'the market records the day's production' (e366b49)", "complete": True,
  "conservation": "recorded production equals the day's output", "members": ["economy.market.five_numbers", "economy.market.observed_production"]},
 {"id": "economy:E3-replay", "test": _E + "engine.test.ts E3 'replaying the command log gives the same state' (a day with a tick; e366b49)", "complete": True,
  "conservation": "replayed state identical", "members": ["economy.market.five_numbers", "economy.infra.tick_scheduler"]},
 {"id": "economy:V1-goods-ledger", "test": _E + "validation.test.ts V1 goods ledger (365 days, every good accounted for; E6 spoilage is the partial cover; e366b49)", "complete": True,
  "conservation": "every good accounted for over 365 days", "members": ["economy.market.five_numbers", "economy.spoilage"]},
 {"id": "economy:E8-V4-price", "test": _E + "markets.test.ts E8 'price moves with shortage by the configured curve'; validation.test.ts V4 supply shock stability (e366b49)", "complete": True,
  "conservation": "price follows the configured curve; stable after a production shock", "members": ["economy.price.rule", "economy.market.observed_production"]},
 {"id": "economy:E14-three-ports", "test": _E + "labour-and-sim.test.ts E14 three-port sim deterministic; harness golden 'economy: three ports' (e366b49)", "complete": True,
  "conservation": "ledger and stock invariants; deterministic",
  "members": ["economy.market.five_numbers", "economy.consumption.demand", "economy.production.abstract_market", "economy.shortage.event",
              "economy.market.observed_production", "economy.infra.tick_scheduler", "economy.spoilage", "economy.price.rule"]},
]

# --- Schema 4 (Rex 2026-10-31): numerical sub-items of V&V item 5, filled per row by owners (vv.py reads this) ---
VV_NUMERICAL = {}   # row id -> {"stability": ..., "coupled_update_consistency": ..., "sensitivity": ...}

# --- Rex 2026-10-31, ENGINES.md "Gaps noted from a field survey": planned, owner Physical Reality, none scheduled.
# Checked first: combustion and fire as a gas source (built), pirate scenarios, the pirate current table and sailing speed (DUP-54),
# DUP-9 wear, tonight's nutrient transport, epidemic force of infection (R-1 gap) and the terrain mosquito multiplier (DUP-35). ---
_FS_HOME = "Toolchain/ENGINES.md 'Gaps noted from a field survey' (Rex 2026-10-31; candidate, planned, not scheduled)"
_FS_INV = ("each contract answers what enters, what leaves, what accumulates, what limits the rate and what makes it fail (schema 4); "
           "mass and energy conserved; coupled systems update consistently (water changes soil strength, soil movement changes water flow)")
def _fs(k, name, dom, form, writes, reads, consumers, ev, notes=""):
    return {"id": k, "name": name, "engine": "realism", "home": _FS_HOME, "status": "planned", "domain": dom, "scope": "universal",
            "inputs": [{"name": x, "unit": "see quantities.json"} for x in reads], "outputs": [{"name": x, "unit": "see quantities.json"} for x in writes],
            "state": "planned", "formulation": form, "dependencies": [], "timescale": "planned", "invariants": _FS_INV,
            "sources": "to research per unit; ENGINES.md", "evidence": ev, "evidence_note": "registry's provisional level; each unit states its own",
            "approximations": "planned", "tests": "none", "consumers": consumers, "notes": notes, "audit_batch": "rex-2026-10-31-field-survey", "planned_writes": writes}
EXTRA_ROWS += [
 _fs("realism.fire.dynamics", "Fire dynamics", "A",
     "ignition and spread by fuel, moisture, oxygen and heat transfer; burning rate; smoke production and its movement with ventilation; ships, towns, powder",
     ["world.fire_state"], ["world.vegetation_stock", "air.wind"], ["realism.gas.sources_sinks", "realism.gas.room_box", "settlement.project.construction"], "2",
     "the burning rate is the owner; combustion stoichiometry (realism.chem.carbon_combustion_charcoal) stays the chemistry; the gas sources' 'fire' term reads the burning rate (DUP-56)"),
 _fs("realism.ocean.tides_currents", "Tides and currents", "A",
     "astronomical tides and ocean currents as distinct from waves and weather, by region (Catalogue or Reality); coastal navigation reads them",
     ["world.tide", "world.current"], ["air.wind"], ["realism.fluids.sail_ship_stability", "realism.terrain.hydrology"], "2",
     "replaces the pirate current table as the source (DUP-57)"),
 _fs("realism.mech.rotational_leverage", "Rotational dynamics and leverage", "A",
     "torque, moment of inertia, balance, footing, pulleys, capstans, recoil: a strong body still fails a lift with poor footing or leverage; inside phase 6 mechanics with realism.mech.rigid_body_contact",
     [], [], ["realism.terrain.excavation", "realism.mech.articulated_locomotion", "realism.contact.contact_event"], "1",
     "a sub-row of phase 6 mechanics; writes nothing of its own (forces and torques on rigid bodies)"),
 _fs("realism.granular.mechanics", "Granular mechanics", "A",
     "sand, gravel, grain and spoil: settling, piling (angle of repose), sliding, compacting; beside soil mechanics",
     ["world.granular_pile"], ["world.spoil_stock", "world.soil"], ["realism.terrain.excavation_stability", "economy.inventory.holdings"], "2",
     "loose material; excavation_stability keeps in-situ faces and reads the angle of repose for loose spoil"),
 _fs("realism.structure.load_paths", "Structural mechanics: load paths", "A",
     "load paths through beams, joints, hulls and roots; bending, buckling, progressive collapse; materials phase 9 has fracture, not load paths",
     ["world.structural_state"], ["world.soil"], ["settlement.project.construction", "settlement.building.condition_decay", "realism.fluids.sail_ship_stability"], "1",
     "Settlement construction consumes it; foundations read the soil's bearing (shear strength)"),
 _fs("realism.fluids.sail_ship_stability", "Sail forces and ship stability", "A",
     "aerodynamic sail forces from apparent wind; hull resistance; heel, righting moment and capsize; fluids phase 7 (which has buoyancy)",
     ["world.vessel_motion"], ["air.wind", "world.current", "world.tide", "world.structural_state"], ["economy.trade.shipment"], "1",
     "replaces the pirate point-of-sail table and current term as the source of speed over ground (DUP-57); the pirate adapter reads it"),
 _fs("realism.materials.tribology_wear", "Tribology: wear of tools, bearings and ropes", "A",
     "wear from friction, load and sliding distance (Archard-type) beside corrosion and decay; explicit part of materials degradation",
     ["component.wear"], [], ["realism.equip.wear_by_temperature", "realism.terrain.excavation"], "2",
     "made explicit 2026-10-31 under realism.materials.deformation_fracture_decay; joins DUP-9 (degradation)"),
 _fs("realism.terrain.solute_transport", "Dissolved-material transport", "A",
     "salt, dissolved nutrients and pollutants carried by water (advection, dispersion, leaching) along hydrology's flows; hydrology carries water, this what it carries",
     ["world.solute_flux"], ["world.drainage", "world.groundwater"], ["realism.terrain.nutrient_transport", "realism.terrain.soils", "realism.ecology.animal_populations"], "2",
     "made explicit 2026-10-31 under hydrology; the owner of dissolved nutrient movement, which nutrient_transport now aggregates with sediment-bound nutrients"),
 _fs("realism.medicine.transmission_ecology", "Vector- and water-borne transmission", "B",
     "vector populations (mosquitoes and others) and water-borne pathogens give each person's exposure (force of infection) from habitat, water and contact; feeds medicine's course and the population epidemic",
     ["body.infection_exposure"], ["world.habitat_suitability", "world.solute_flux", "world.drainage"], ["realism.medicine.disease_course", "realism.population.epidemic"], "2",
     "made explicit 2026-10-31 under disease ecology; closes the R-1 gap on 2626 (force of infection a host input until transmission exists); the terrain mosquito multiplier becomes its read (DUP-35)"),
]
ROW_PATCHES["realism.terrain.nutrient_transport"] = {"formulation": "nutrients carried with sediment by erosion and deposition, plus dissolved nutrients from realism.terrain.solute_transport (an aggregate of the two); writes fluxes, never the soil stock",
    "notes": "2026-10-31: dissolved movement is owned by realism.terrain.solute_transport; this row aggregates it with sediment-bound nutrients"}
for _id, _sc, _k, _u, _w, _desc in [
 ("world.fire_state", "world", "record", None, "realism.fire.dynamics", "burning areas: fuel consumed, burning rate, heat release, smoke"),
 ("world.tide", "world", "quantity", "m", "realism.ocean.tides_currents", "tidal height by place and time"),
 ("world.current", "world", "quantity", "m/s", "realism.ocean.tides_currents", "ocean current velocity by place"),
 ("world.granular_pile", "world", "record", None, "realism.granular.mechanics", "loose piles: mass, angle, compaction"),
 ("world.structural_state", "world", "record", None, "realism.structure.load_paths", "member loads, deflection, buckling margin, failure"),
 ("world.vessel_motion", "world", "record", None, "realism.fluids.sail_ship_stability", "speed over ground, heading, heel, capsize state"),
 ("component.wear", "component", "quantity", "1", "realism.materials.tribology_wear", "wear fraction of a tool, bearing or rope"),
 ("world.solute_flux", "world", "quantity", "kg/a", "realism.terrain.solute_transport", "dissolved salt, nutrients and pollutants carried by water"),
 ("body.infection_exposure", "body", "quantity", "1/d", "realism.medicine.transmission_ecology", "force of infection per person and pathogen"),
]:
    EXTRA_QUANTITIES.append({"id": _id, "kind": _k, "unit": _u, "scope": _sc, "writer": _w, "description": _desc,
        "status": "planned (Rex 2026-10-31, field survey)"})
GROUPS += [
 ("DUP-56", "duplicate", "Fire: combustion stoichiometry and fire as a gas source are built, with pirate period scenarios; no burning rate, ignition or spread exists; the planned fire dynamics would own the rate (field survey 2026-10-31)",
  ["realism.fire.dynamics", "realism.gas.sources_sinks", "realism.chem.carbon_combustion_charcoal", "pirate.atm.scenarios", "pirate.sci.combustion"],
  "realism.fire.dynamics owns ignition, spread and burning rate; combustion stays the chemistry; the gas sources' fire term reads the burning rate; pirate scenarios become inputs"),
 ("DUP-57", "duplicate", "Ship motion: the pirate speed over ground (daily speed x point-of-sail factor + current) and the ocean current table vs planned sail forces, ship stability, tides and currents (field survey 2026-10-31)",
  ["realism.fluids.sail_ship_stability", "realism.ocean.tides_currents", "pirate.env.wind_sailing", "pirate.env.currents"],
  "realism.fluids.sail_ship_stability and realism.ocean.tides_currents own motion and currents; the pirate rows become plugin data or adapter reads"),
]
AUTH.update({"DUP-56": ("ownership-gap", "no owner of the burning rate today"), "DUP-57": ("duplicate-authority", "")})
BATCH.update({"DUP-56": 3, "DUP-57": 3})
_ADD2 = {"DUP-9": ["realism.materials.tribology_wear"], "DUP-35": ["realism.medicine.transmission_ecology"]}
GROUPS[:] = [(g[0], g[1], g[2], g[3] + _ADD2.get(g[0], []), g[4]) for g in GROUPS]

# --- Rex 2026-10-31, ENGINES.md "Conversational plausibility, organic flow": part of the communication subsystem; planned (cognition keeper's request) ---
EXTRA_ROWS.append(_com("cognition.communication.conversation_state", "Conversation state and tolerance", "C",
    "per mind and partner: shared context, perceived intention, willingness to engage, relationship and boundaries, current emotional and bodily state, conversational history; tolerance for nonsense = the effort a mind will still spend understanding before disengaging (from affection, curiosity, obligation, expected benefit, attention, how the exchange has gone). The next response (answer, clarify, interpret, redirect, challenge, leave) is a choice through cognition.decision.select; awkwardness and lingering emerge, never scripted; personality influences, never decides; Big Five is a measurement of the emergent behaviour (T-2), never a driver",
    ["mind.conversation_state", "mind.conversation_tolerance", "mind.engagement_willingness"],
    ["mind.testimony", "mind.source_credibility", "mind.drive", "mind.episode", "mind.belief"],
    ["cognition.decision.generate", "cognition.decision.select"],
    "Rex 2026-10-31; whether tolerance becomes a need record under M_i or stays a separate state is open (C-Q12, Rex); cognition unit 2734 records the quantities in DESIGN §5"))
for _id, _k, _u, _desc in [
 ("mind.conversation_state", "record", None, "per mind and partner: shared context, perceived intention, willingness, relationship and boundaries, emotional and bodily state, conversational history"),
 ("mind.conversation_tolerance", "quantity", "1", "remaining tolerance budget (0-1): effort a mind will spend understanding before disengaging; need-record vs state open (C-Q12)"),
 ("mind.engagement_willingness", "quantity", "1", "willingness to engage with this partner now (0-1)"),
]:
    EXTRA_QUANTITIES.append({"id": _id, "kind": _k, "unit": _u, "scope": "mind", "writer": "cognition.communication.conversation_state", "description": _desc,
        "status": "planned (Rex 2026-10-31, conversational plausibility; cognition keeper); exists once its units pass, after the P7 baseline"})

# --- Rex 2026-10-31, C-Q12 decided (ENGINES.md; cognition keeper): conversation tolerance is a derived assessment; shared context is per-mind belief ---
QUANTITY_PATCH["mind.conversation_tolerance"] = {"writer": None, "role": "derived",
    "derived_from": ["mind.drive (the social-connection need's drive)", "mind.attention_share (cognition.attention.allocate)", "mind.belief (trust)", "mind.expected_utility (expected worth)", "mind.episode (interaction history)"],
    "description": "a derived assessment (0-1) made when the next turn is evaluated from separate causes; may be cached; never a need record, never a draining bar (Rex, C-Q12 decided 2026-10-31)",
    "status": "planned, derived (no writer); nothing implemented"}
EXTRA_QUANTITIES.append({"id": "mind.believed_shared_context", "kind": "record", "unit": None, "scope": "mind", "writer": "cognition.communication.conversation_state",
    "description": "per mind and partner: what this mind believes is shared with the partner (a belief, one of conversation_state's parts; never one record both parties hold)",
    "status": "planned (Rex 2026-10-31, C-Q12 decided); nothing implemented"})
ROW_PATCHES["cognition.communication.conversation_state"] = {
    "planned_writes": ["mind.conversation_state", "mind.engagement_willingness", "mind.believed_shared_context"],
    "outputs": [{"name": x, "unit": "see quantities.json"} for x in ["mind.conversation_state", "mind.engagement_willingness", "mind.believed_shared_context"]],
    "notes": "Rex 2026-10-31, C-Q12 decided: tolerance is a derived assessment (mind.conversation_tolerance, no writer) from the social-connection drive, attention, trust and expected worth, and history, evaluated per turn; shared context is each mind's own belief (mind.believed_shared_context). Verification state: planned, nothing implemented; the commits document the proposed design and do not demonstrate the behaviour. Cognition unit 2736 records this in DESIGN §5 and §12"}

# --- Rex 2026-10-31, ENGINES.md "Five Cognition directions" (cognition keeper's request; cognition unit 2737 records DESIGN §14). Planned; nothing implemented ---
_FIVE_HOME = "Toolchain/ENGINES.md 'Five Cognition directions' (Rex 2026-10-31; planned; cognition DESIGN §14)"
_FIVE_INV = ("the personality label is descriptive: dispositions influence behaviour, the label describes the resulting pattern (Rex's correction); "
             "a measured trait used to predict behaviour is an empirical approximation, never a neural mechanism; no type-specific rule; "
             "randomness represents uncertainty, never replaces causes")
def _five(k, name, form, writes, reads, consumers, notes, ev="?"):
    return _sal(k, name, "C", form, writes, reads, consumers, notes, ev=ev, home=_FIVE_HOME, inv=_FIVE_INV, batch="rex-2026-10-31-cognition-five")
EXTRA_ROWS += [
 _five("cognition.memory.encoding", "Memory encoding",
       "what becomes a memory and in what detail, from what was attended (goals, interests, danger, novelty, distraction, existing knowledge) and the person's state",
       [], ["mind.observation", "mind.attention_share", "mind.drive"], ["cognition.memory.consolidation", "cognition.memory.episodic"],
       "a stage under cognition.memory.episodic; writes nothing of its own until the cognition keeper splits the writer of mind.episode (one writer); C-Q13 open (which memory parameters Reality's neurology constrains)"),
 _five("cognition.memory.consolidation", "Memory consolidation",
       "what becomes durable; sleep is a biological influence (a Reality input from neurology sleep_wake)",
       [], ["mind.episode"], ["cognition.memory.retrieval"],
       "a stage under cognition.memory.episodic; reads realism.neurology.sleep_wake; writes nothing of its own until the writer split; C-Q13 open"),
 _five("cognition.memory.retrieval", "Memory retrieval",
       "what the situation or another's remark brings back; remembering and saying are separate acts (saying is cognition.communication.encode)",
       [], ["mind.episode", "mind.observation", "mind.testimony"], ["cognition.decision.evaluate", "cognition.communication.encode"],
       "mind.retrieval_p stays written by cognition.memory.episodic until the cognition keeper proposes the split; C-Q13 open"),
 _five("cognition.communication.gaze", "Gaze and nonverbal interpretation",
       "the visible behaviour (where, how long, looking away, expression, posture, distance) is separate from the observer's interpretation, held as several hypotheses with likelihoods (attraction, anger, curiosity, challenge, submission, mere attention) revised by each cue; cultural and individual differences and misunderstanding included; the response (return, smile, avoid, question, approach, defend) is an intention through cognition.decision.select",
       ["mind.gaze_hypotheses"], ["mind.observation", "mind.belief"], ["cognition.attention.allocate", "cognition.memory.encoding", "cognition.decision.select"],
       "part of the communication subsystem (nonverbal); weights researched and calibrated, no 'three seconds means attraction'; C-Q14 open (hypothesis set and calibration)"),
 _five("cognition.continuity.absence", "Continuity of minds during absence",
       "a person absent from the player's view is simulated only enough to account for meaningful change: returns changed, remembers the last conversation, comes for a new reason; an expected person may fail to arrive",
       [], ["mind.episode", "mind.belief", "mind.drive"], [],
       "advances existing mind states at coarse resolution (PLATFORM §9), writes nothing of its own; who these people are is the pirate plugin's (story and town keepers)"),
 _five("cognition.substance.adaptation", "Lasting substance adaptation of reasoning processes",
       "repeated exposure lastingly changes reasoning-process parameters (association speed, what counts as evidence, certainty, noticing contradictions, working memory, checking conclusions, belief updating); separate processes per substance: immediate effects, tolerance and dependence, withdrawal, learning and craving, longer-term adaptation and recovery (lasting != irreversible); never reset when the substance wears off",
       ["mind.process_baseline"], ["mind.episode", "mind.prediction_error"], ["cognition.belief.update", "cognition.decision.evaluate", "cognition.attention.allocate"],
       "Reality neurology and pharmacokinetics own the biology (reads realism.neurology.circuits outputs); each substance its own researched model; C-Q15 open (which parameters a substance may move)"),
]
for _id, _w, _desc in [
 ("mind.gaze_hypotheses", "cognition.communication.gaze", "per observer and partner: interpretation hypotheses with likelihoods, revised by each cue"),
 ("mind.process_baseline", "cognition.substance.adaptation", "reasoning-process parameters as altered by history; never reset when a substance wears off"),
]:
    EXTRA_QUANTITIES.append({"id": _id, "kind": "record", "unit": None, "scope": "mind", "writer": _w, "description": _desc,
        "status": "planned (Rex 2026-10-31, five Cognition directions); nothing implemented"})
ROW_PATCHES["cognition.personality.function_sensitivity"] = {"notes": "a configuration of cognition.personality.slot (eight-function model, CTRL-7); parameters only, writes nothing. Rex 2026-10-31: the personality label is descriptive; dispositions influence behaviour and the label describes the resulting pattern (correction of 'personality weights these')"}

# --- 2026-10-31: memory writer split (cognition keeper's proposal; Rex's to overrule): episodic stays the sole writer until the stages are built ---
for _k, _fut in [("cognition.memory.encoding", "mind.episode"), ("cognition.memory.consolidation", "mind.memory_durability"), ("cognition.memory.retrieval", "mind.retrieval_p")]:
    ROW_PATCHES[_k] = {"notes": f"sub-stage of cognition.memory.episodic; writes nothing until built; when built it takes over {_fut} in the same commit that changes kernel.json, and episodic retires to an alias for the three stages (cognition keeper 2026-10-31, Rex's to overrule); C-Q13 open"}
EXTRA_QUANTITIES.append({"id": "mind.memory_durability", "kind": "quantity", "unit": "1", "scope": "mind", "writer": None,
    "description": "per-episode durability (0-1) set by consolidation; sleep a Reality input",
    "status": "planned; no writer until cognition.memory.consolidation is built (cognition keeper 2026-10-31)"})

# --- 2026-10-31: REG-28 re-audit of the Cognition baseline against committed files (cognition HEAD 3a2bdcd; PLATFORM §11a, §11b).
# Full suite on the clean HEAD: 27 files, 307 tests passed. kernel.json declares process cognition.tick with 12 mechanisms and their ports.
# The 5 reserved rows (communication.language, emotion.appraisal, relationship.trust, skill.practice, planning.lookahead) have no module: stay planned.
# rate_limiter / failure_mode: DESIGN.md states neither for these rows, so they stay null. ---
_COG_C = "cognition 3a2bdcd"
_COG_TESTS = {
 "cognition.attention.allocate": ("src/attention.ts", "test/attention.test.ts"),
 "cognition.perception.detect": ("src/perception.ts", "test/perception.test.ts"),
 "cognition.belief.update": ("src/beliefs.ts", "test/beliefs.test.ts"),
 "cognition.memory.episodic": ("src/memory.ts", "test/memory.test.ts"),
 "cognition.needs.drive": ("src/needs.ts", "test/needs.test.ts"),
 "cognition.goals.objectives": ("src/needs.ts (goals), src/evaluate.ts (goal reward)", "test/needs.test.ts, test/evaluate.test.ts"),
 "cognition.decision.generate": ("src/actions.ts", "test/actions.test.ts"),
 "cognition.decision.evaluate": ("src/evaluate.ts", "test/evaluate.test.ts"),
 "cognition.decision.select": ("src/select.ts, src/policy.ts", "test/select.test.ts, test/policy.test.ts"),
 "cognition.learning.outcome": ("src/learning.ts", "test/learning.test.ts"),
 "cognition.learning.attribution": ("src/learning.ts", "test/learning.test.ts"),
 "cognition.personality.slot": ("src/personality.ts", "test/personality.test.ts"),
 "cognition.personality.eight_function": ("src/personality/eight-function/v1.ts", "test/personality-v1.test.ts, test/personality-versions.test.ts"),
}
_COG_TICK = [k for k in _COG_TESTS if k != "cognition.personality.eight_function"]
for _k, (_src, _t) in _COG_TESTS.items():
    ROW_PATCHES.setdefault(_k, {})
    ROW_PATCHES[_k].update({"status": "built", "home": f"Toolchain/cognition/{_src} ({_COG_C})", "tests": f"Toolchain/cognition {_t} ({_COG_C}; suite 307/307)"})
CHAINS += [
 {"id": "cognition:hungry-pair", "test": "Toolchain/cognition test/bench-world.test.ts ('hungry pair kernel integration': 144 body/cognition/resolution epochs, replay) and test/bench-acceptance.test.ts (DESIGN §6 fixture; rules verified, never validated; cognition 3a2bdcd)",
  "complete": True, "conservation": "stock + eaten + held conserved; canonical traces repeat; one causal outcome per intention",
  "members": _COG_TICK},
 {"id": "cognition:personality-versions", "test": "Toolchain/cognition test/personality-versions.test.ts; bench/personality-versions.ts runs the hungry pair per personality version (DESIGN §9 T-3; cognition 3a2bdcd)",
  "complete": True, "conservation": "as the hungry pair", "members": ["cognition.personality.eight_function", "cognition.personality.slot", "cognition.decision.select", "cognition.attention.allocate"]},
]
_INTEG = f"yes (kernel ports, {_COG_C}, 2026-10-31): kernel.json process cognition.tick; hungry-pair kernel integration test"
for _k in _COG_TICK:
    VV_OVERRIDES[_k] = {"validated": "no (no independent data)", "integrated": _INTEG, "evidence": "REG-28 re-audit 2026-10-31"}
VV_OVERRIDES["cognition.memory.episodic"] = {"validated": "yes (V1 single-episode forgetting, 2026-10-30: raw-scale power-fit R2 0.99999983 > Table 4 median 0.92; validation/V1-forgetting.md)",
    "integrated": _INTEG, "evidence": "V1 pass (re-audited 2026-10-31 from validation/V1-forgetting.md and data/v1-results.json at 3a2bdcd); also exercised by V2, whose failure is recorded on the choice rows"}
for _k in ("cognition.decision.evaluate", "cognition.decision.select"):
    VV_OVERRIDES[_k] = {"validated": "failed (V2 repeated choice from experience, 2026-10-30: competition problem-level MSD 0.0319; trial-level MSD >= 0.00527 vs the IBL criterion 1.5 x 0.0005; trial-level score parked C-Q7)",
        "integrated": _INTEG, "evidence": "V2 recorded in validation/V2-repeated-choice.md (Erev et al. 2010 data; Gonzalez & Dutt 2011 reference) at 3a2bdcd"}
VV_OVERRIDES["cognition.personality.eight_function"] = {"validated": "no (no independent data)",
    "integrated": f"yes (hungry pair per personality version, {_COG_C}, 2026-10-31)", "evidence": "REG-28 re-audit 2026-10-31; Rex's theory as a hypothesis (evidence 5)"}
for _q in ["mind.attention_share", "mind.observation", "mind.belief", "mind.episode", "mind.retrieval_p", "mind.need_deficit", "mind.drive",
           "mind.need_priority", "mind.goal_progress", "mind.candidates", "mind.expected_utility", "mind.intention", "mind.prediction_error", "mind.attribution"]:
    QUANTITY_PATCH.setdefault(_q, {}).update({"status": f"built ({_COG_C}; kernel.json port; REG-28 re-audit 2026-10-31)"})

# --- 2026-10-31: REG-29 item 1 (cognition keeper): the RNG stream name is an alias of the built episodic row; moves to retrieval when built ---
ALIASES.append({"old": "cognition.memory.retrieve", "new": "cognition.memory.episodic", "date": "2026-10-31", "kind": "stream",
    "reason": "kernel.json stream for episodic retrieval noise (test/process.test.ts maps it to episodic; src/memory.ts documents it); renaming would change every seeded draw and invalidate REPORT and replay evidence; the alias moves to cognition.memory.retrieval when that stage is built (cognition keeper 2026-10-31)"})
# V2 is a joint failure of default theta across the instance-based chain (cognition keeper): recorded on episodic too, V1 pass kept
VV_OVERRIDES["cognition.memory.episodic"]["validated"] = ("yes (V1 single-episode forgetting, 2026-10-30: raw-scale power-fit R2 0.99999983 > Table 4 median 0.92); "
    "V2 failed (joint, default theta, C-V2: repeated choice MSD over the IBL criterion, with decision.evaluate and decision.select)")
for _k in ("cognition.decision.evaluate", "cognition.decision.select"):
    VV_OVERRIDES[_k]["validated"] = "failed (V2 joint, default theta, C-V2: competition problem-level MSD 0.0319; trial-level MSD >= 0.00527 vs the IBL criterion 1.5 x 0.0005; trial-level score parked C-Q7; with memory.episodic)"

# --- 2026-10-31: REG-29 items 2-5: host inputs until their writers are built (kernel unit 2738 warns on written_by "host", never fails) ---
QUANTITY_PATCH.setdefault("body.detectability", {})["written_by"] = "host (fixture stub, cognition DESIGN §8; until P2 optics/acoustics build the writer)"
QUANTITY_PATCH.setdefault("body.capacity_functional", {})["written_by"] = "host (fixture stub, cognition DESIGN §8; until DUP-15's realism.capacity.functional is built)"
QUANTITY_PATCH.setdefault("body.hunger_signal", {})["written_by"] = "host (fixture stub, cognition DESIGN §8; until realism.nutrition.hunger_fullness is built)"

# --- 2026-10-31: schema-4 fields for the 13 built Cognition rows, verbatim from cognition DESIGN §15 (commit 9320382; keeper proposal) ---
ROW_PATCHES.setdefault('cognition.attention.allocate', {}).update({'rate_limiter': "Attention shares `a_c = w_c/Σ w'` sum to 1 per mind per tick (§2.1 Bundesen; `allocateAttention` renormalises; proposed zero-total convention: no attended cues). (DESIGN §15, cognition 9320382)", 'failure_mode': 'No allocation when total weight is zero (proposed); invalid salience, relevance or hook output throws (`attention.ts`). (DESIGN §15, cognition 9320382)'})
ROW_PATCHES.setdefault('cognition.perception.detect', {}).update({'rate_limiter': "One detection pass per attended stimulus per tick; effective sensitivity `d'_eff = d'_c·√a_c` (§2.1) bounded by declared `d'` and the attention share. (DESIGN §15, cognition 9320382)", 'failure_mode': 'Misses and false alarms by SDT (`P_H`, `P_FA`, §2.1); wrong categorical or Weber-noisy real reports; explicit null observations when not detected; invalid shares, criterion or stream draw throws (`perception.ts`). (DESIGN §15, cognition 9320382)'})
ROW_PATCHES.setdefault('cognition.belief.update', {}).update({'rate_limiter': 'Conservatism `η ∈ (0,1]` on each update (§2.3); between observations, categorical relaxation `λ_b` and real drift `q_k·Δt` (§2.3). (DESIGN §15, cognition 9320382)', 'failure_mode': 'Wrong or false priors by design (§2.3); under-update when `η < 1`; testimony weighted by reliability `r_j`; kind or support mismatch throws (`beliefs.ts`). (DESIGN §15, cognition 9320382)'})
ROW_PATCHES.setdefault('cognition.memory.episodic', {}).update({'rate_limiter': 'Retrieval probability from activation `B_e`, threshold `τ`, noise `s`, decay `d` (§2.3 ACT-R); one stream draw per retrieval attempt (`cognition.memory.retrieve`, §7). (DESIGN §15, cognition 9320382)', 'failure_mode': 'Forgetting and failed retrieval when the draw exceeds `P_retrieve(e)`; `P̂` underweights irretrievable episodes (§2.3); invalid decay, context or stream throws (`memory.ts`). (DESIGN §15, cognition 9320382)'})
ROW_PATCHES.setdefault('cognition.needs.drive', {}).update({'rate_limiter': 'Motivational priorities `priority_i = M_i/Σ_j M_j` with `M_i = w_i D_i S_i` (§2.2); drive `D(h)` uses host parameters `n`, `m`. (DESIGN §15, cognition 9320382)', 'failure_mode': 'Mis-priorities from wrong deficits (Reality signals, appraisal beliefs, accumulator `dh/dt = 1/τ_soc`, §2.2); missing inputs or non-unit deficits throw (`needs.ts`). (DESIGN §15, cognition 9320382)'})
ROW_PATCHES.setdefault('cognition.goals.objectives', {}).update({'rate_limiter': 'Host standing goals with `p_g ∈ [0,1]`; reward term `V_g·Δp_g` per update (§2.2; `goalReward`). (DESIGN §15, cognition 9320382)', 'failure_mode': 'Progress and reward follow host-supplied `goalProgress`, not ground truth; out-of-range progress throws (`needs.ts`, `mind.ts`). (DESIGN §15, cognition 9320382)'})
ROW_PATCHES.setdefault('cognition.decision.generate', {}).update({'rate_limiter': 'Candidates are repertoire entries whose believed preconditions meet `θ_pre` (proposed 0.5) and whose capacity `≤ body.capacity_functional` (§2.4); personality hook may reorder or add compounds (§9). (DESIGN §15, cognition 9320382)', 'failure_mode': 'Actions omitted when preconditions or capacity fail; invalid repertoire or hook output throws (`actions.ts`). (DESIGN §15, cognition 9320382)'})
ROW_PATCHES.setdefault('cognition.decision.evaluate', {}).update({'rate_limiter': 'One `EU(a)` per candidate with one-step lookahead and discount `γ` (§2.4); `P̂` from theory plus retrievable episodes (§2.3). (DESIGN §15, cognition 9320382)', 'failure_mode': 'Wrong expected utility from mistaken beliefs and `P_theory`; loss aversion `λ` on negative outcomes (§2.4); unknown predicted need or goal throws (`evaluate.ts`). (DESIGN §15, cognition 9320382)'})
ROW_PATCHES.setdefault('cognition.decision.select', {}).update({'rate_limiter': 'At most one newly minted intention per re-choice; softmax with `β` (§2.4 Luce); commitment keeps the current intention while `max_a EU(a) − EU(ι) ≤ κ` (§2.4, §5). (DESIGN §15, cognition 9320382)', 'failure_mode': 'A worse action chosen by the softmax draw; kept intention when advantage within `κ`; invalid utilities, `κ`, or stream draw throws (`select.ts`). (DESIGN §15, cognition 9320382)'})
ROW_PATCHES.setdefault('cognition.learning.outcome', {}).update({'rate_limiter': "Runs when an outcome event's `cause` is this mind's intention id (§2.5, §7); records `δ = r_obs − EU(ι)` and optionally encodes an episode. (DESIGN §15, cognition 9320382)", 'failure_mode': 'Wrong learning signal from misperceived outcomes (§2.5); unknown or already-settled intentions get empty feedback (`process.ts`); timeline or outcome-space mismatch throws (`learning.ts`). (DESIGN §15, cognition 9320382)'})
ROW_PATCHES.setdefault('cognition.learning.attribution', {}).update({'rate_limiter': 'Attributed cause is the latent with largest KL move from its prior, else "chance" if no move exceeds `ε_attr` (§2.5); ties by declared latent order. (DESIGN §15, cognition 9320382)', 'failure_mode': 'Misattribution when the wrong latent wins or none clears `ε_attr`; duplicate latent ids or invalid reliability update throws (`learning.ts`). (DESIGN §15, cognition 9320382)'})
ROW_PATCHES.setdefault('cognition.personality.slot', {}).update({'rate_limiter': 'Structural null model: identity on pertinence, interpret, generate and learning hooks (§9 `nullPersonality`; DESIGN §5 registry n/a). (DESIGN §15, cognition 9320382)', 'failure_mode': 'Baseline adds no failure beyond the hooked rows; when a non-null model is configured, hooks may mis-modulate `π`, `η`, `κ`, learning rate and `d` (§9). (DESIGN §15, cognition 9320382)'})
ROW_PATCHES.setdefault('cognition.personality.eight_function', {}).update({'rate_limiter': 'Switched on only after baseline CB-1–CB-7 (§9 C-Q4); v1 adjusts declared parameters through the four hooks when configured (`personality/eight-function/v1.ts`). (DESIGN §15, cognition 9320382)', 'failure_mode': 'Hypothesis-level wrong modulation when enabled (§9 level 5); invalid stack or parameters throw in v1 (`personality/eight-function/v1.ts`). (DESIGN §15, cognition 9320382)'})

# --- 2026-10-31: Rex's experience pipeline and memory model (cognition DESIGN §16, unit 2746; cognition keeper's request). Planned; nothing built ---
EXTRA_QUANTITIES += [
 {"id": "mind.appraisal", "kind": "record", "unit": None, "scope": "mind", "writer": "cognition.emotion.appraisal",
  "description": "the interpretation a mind forms of an event (stage 2 of Rex's experience pipeline); Reality's neurology reads it to produce the chemical response",
  "status": "planned (Rex 2026-10-31, cognition DESIGN §16); writer is the reserved emotion.appraisal row, not the built belief.update (registry keeper's choice, the cognition keeper may overrule)"},
 {"id": "mind.recalled_body_state", "kind": "record", "unit": None, "scope": "mind", "writer": "cognition.memory.retrieval",
  "description": "the body state stored with an episode and re-emitted on retrieval (a remembered betrayal re-raises the heart rate); Reality's neurology reads it",
  "status": "planned (Rex 2026-10-31, cognition DESIGN §16); writer cognition.memory.retrieval when built (§14.1)"},
]
ROW_PATCHES.setdefault("cognition.emotion.appraisal", {}).update({"planned_writes": ["mind.appraisal"], "outputs": [{"name": "mind.appraisal", "unit": "record"}],
    "notes": "reserved (DESIGN §5); the universal home of PSYCHOLOGY.md's stress and fear inputs; 2026-10-31 (DESIGN §16): writes mind.appraisal, the event interpretation Reality's neurology (realism.neurology.circuits) reads; the pirate meters stay pirate"})
_MEM16 = " Rex 2026-10-31 (DESIGN §16): memory splits into stored / retrievable / articulable, with per-function profiles as hypotheses (Se, Ne, Te open, C-Q16); episode records carry the body state at encoding; nothing built."
for _k in ("cognition.memory.encoding", "cognition.memory.consolidation", "cognition.memory.retrieval"):
    ROW_PATCHES[_k]["notes"] += _MEM16
ROW_PATCHES["cognition.memory.retrieval"]["notes"] += " Will also write mind.recalled_body_state."

# --- 2026-10-31: batch-1 re-audit after every P1 unit landed (realism c642101; kernel 0e9871e with P0 at b71411a; settlement 0d76869;
# economy e366b49; pirate-ship d65ba20). Committed files only; §11b: gate logs read, targeted tests rerun where a gate had not run them. ---
_D = "2026-10-31"
def _ev(g, step, note, commit=None, by="registry keeper"):
    e = {"date": _D, "step": step, "by": by, "note": note}
    if commit: e["commit"] = commit
    DECISIONS[g]["progress"].append(e)
# Closed
_ev("DUP-5", "unit passed", "physiology owns metabolic oxygen demand (metabolicRateW, oxygenLitresPerMin); physics' MET helper called only by physiology", "realism 4c7e6f9 (2621)", by="Reality keeper")
_ev("DUP-5", "re-audited (11a criteria)", "implemented: test/energy-oxygen.test.ts (human and horse hours close energy, O2, CO2 and room elements); gate 2621 passed. integrated: atmosphere reads metabolic_w (src/atmosphere.ts); energy-oxygen and independence tests run physiology and atmosphere together. validated: Weir oxygen energy within 1 % (0.46 %, flags/atmosphere.md); horse VO2 misses its published band, recorded as it.fails with the experiment (flags/atmosphere.md (2621) unvalidated)")
_ev("DUP-5", "closed", "")
DECISIONS["DUP-5"]["state"] = "closed"
_ev("DUP-13", "unit passed", "one activity schedule drives local (3CC) and systemic (MET-hours) fatigue", "realism c0ed753 (2634 as 2711)", by="Reality keeper")
_ev("DUP-13", "re-audited (11a criteria)", "implemented: test/fatigue.test.ts 'one schedule drives local and systemic fatigue' (rerun by the registry keeper at c642101: 11/11; the gate had not run this file). integrated: engine test runs physiology, muscular fatigue and nutrition together; pirate stats.test 'the adapter keeps no fatigue counter of its own' (677f1bb, 2638). validated: validation (2634) tests against Ainsworth 2011 MET values and Vernillo 2018 force decline; (2634) report line. R-1: accepted without conditions. Note: the 'activation share = 3CC effort, level 4' wording is only marked proposed (Reality, a one-line flag)")
_ev("DUP-13", "closed", "")
DECISIONS["DUP-13"]["state"] = "closed"
_ev("DUP-19", "unit passed", "one death per body with one exact cause matching an open crisis", "realism 5e9a866 (2633 as 2710)", by="Reality keeper")
_ev("DUP-19", "re-audited (11a criteria)", "implemented: test/mortality.test.ts 'one cause per individual death (2633)' (a death without an open crisis of that cause throws; a second death throws; 1,000 seeded individuals vs the aggregate within three SE); checkpoint2 declares death by crisis id; gate 2710 passed. integrated: pirate adapters/medicine.ts flushes crises and the pirate settlement test checks them against the engine records; starvation opens a crisis. validated: 'validation (2633)' boundaries vs independent reference rows; no-data lines with experiments (flags anatomy, nutrition, medicine). IF-1 holds (nothing in src reads a fate). R-1 (a) successor named (cellular layer, never a timer); (b) organ floors level 5 in gears/anatomy-crisis-floors.md, pirate ANATOMY.md points back. Caveat: the pirate 30-day run resolves no crisis, so its one-cause check is vacuous there")
_ev("DUP-19", "closed", "")
DECISIONS["DUP-19"]["state"] = "closed"
# Not passed: stay closing with the exact gap
_ev("DUP-24", "re-audit: not passed", "implemented and integrated pass: one physiology.restingMetabolicRate (src/physiology.ts:235), anatomy.speciesRmr delegates, no former home left (fe6322f, 2620). GAP: no validation record: no independent RMR comparison and no '(2620) unvalidated:' line with an experiment (flags/physiology.md has only NOTE (2620)). Owner: Reality keeper, one unit")
_ev("DUP-14", "re-audit: not passed", "implemented: circulation.test 'one aerobic training pathway (2635)' (2405d78, 2712); REG-26 done: gears/aerobic-training-clamp.md recomputed with the current constants, saturates at L = 0.256 MET-h/day, flagged '(2635) open:' for Rex (flags/physiology.md:50), no rescale. validated: DO2 x 0.9 vs FRIEND men 20-29 (baseline). GAP: not integrated: no code outside tests feeds muscular.trainingFactor into circulation's trainingFactor, and the pirate host does not run circulation (aerobic_today unavailable); no combined Banister -> circulation -> adapter test. Owner: Reality keeper (host wiring through a pirate-lane unit and its test); the saturation scale is Rex's")
_ev("DUP-18", "re-audit: not passed", "verification half closed by Rex; pirate 5d4e088 (2637) fixed the rendered table (38 / 1.9 / 0.048 / 0.117). GAP: pirate PHYSIOLOGY.md s2 prose at d65ba20 still states tau_fit 42 and tau_fat 7 (L140-141), the calibration paragraph 'with tau 42 and 7' (L149-151) and Open item 5 'the 42/7 constants' (L483); realism flags/physiology.md:27 still says s2 disagrees. Owner: Reality keeper (a pirate-lane doc unit, then the flag line)")
for _g in ("DUP-26", "DUP-28", "DUP-29"):
    _ev(_g, "unit passed", "population labour supply in person-hours through the one LabourSupply declaration; health applied once to capacity", "realism a89fbf9 (2636 as 2713; recheck passed at b220e2d)", by="Reality keeper")
    _ev(_g, "re-audit: not passed", "settlement, economy and pirate parts passed earlier; CONTRACTS.md byte-identical (c3b5d46f). GAP 1: realism hours() returns total capacity, while CONTRACTS s18 says it returns what is left after the day's grants (flags/ecology-and-population.md NOTE (2636) says so). GAP 2: no committed test runs populationLabourSupply with settlement or economy or through the pirate PortLabour / runDay, so 'assigned hours never exceed supplied hours' is unverified for population supply. Owner: Reality keeper. Q15 (two lines sharing workers) is Rex's and blocks only that clause of DUP-26's test; SET-12 and REG-15 do not block")
_ev("DUP-33", "re-audit: not passed", "implemented in the harness: harness/thirty-days.test.ts 'P0 one clock for thirty days' asserts each day view equals floor(T/DAY) and worldTime = T/SECOND, and fails a skipped or doubled day; replay.test same-seed equality (kernel b71411a). GAP 1: the acceptance clause 'no engine increments a counter of its own' fails: settlement src/tick/index.ts:20 and economy src/tick/index.ts:100 still increment their day (kept by kernel DESIGN.md b71411a with an equality assert), and realism added day counters (population.ts, ecology.ts, medicine.ts at c642101); the economy StubLedger day, the alignment tick and the overnight tick are off the clock. GAP 2: the harness has not been rerun since the 22:53 recovery (last passes 2680, 2610). Owner: Kernel keeper (derive the views from the clock, or the controller asks Rex to amend the acceptance text); Reality for its new counters")
_ev("DUP-32", "re-audit: not passed", "implemented in part: settlement and economy import kernel ids, context and reduce; realism uses the kernel rng; engine suites passed above baseline in 2693-2695 and harness goldens 2697 (all before the 22:53 deletion). GAP 1: no kernel test refuses an id minted under another engine's prefix (test/ids.test.ts covers mint, widening, qualify only; the design moved to '<engine>/<id>' qualification but the acceptance text was never amended). GAP 2: leftovers: economy src/providers.ts:68 hand-mints txn ids; realism src/circulation.ts:31 its own finite (maybe intended). GAP 3: the re-check runs predate the recovery. Owner: Kernel keeper (test or amended text via the controller); Economy for the txn mint")

# --- 2026-10-31: Reality keeper's fix units for the batch-1 gaps (queued, not yet passed) ---
for _g, _n in [("DUP-24", "realism 2750: measured-RMR reference rows plus validation (2620) or an unvalidated line"),
               ("DUP-14", "realism 2751: assembled bodies feed muscular.trainingFactor into circulation each step, pure aerobicToday, combined Banister -> circulation test; then pirate 2755: the characters adapter reads aerobicToday, removes the 'unavailable' limitation, combined Banister -> adapter test"),
               ("DUP-18", "pirate 2753: PHYSIOLOGY.md s2 lines and Open item 5 cite the table; then realism 2754 refreshes flags/physiology.md:27"),
               ("DUP-26", "realism 2752: hours() returns what is left after the day's grants (CONTRACTS s18) with a test; then a Settlement-queued combined provider test through the settlement and economy adapters"),
               ("DUP-28", "as DUP-26 (realism 2752, then the Settlement combined test)"),
               ("DUP-29", "as DUP-26 (realism 2752, then the Settlement combined test)"),
               ("DUP-33", "Reality asked the Kernel keeper for the counter rule; one Codex unit applies it to realism's counters")]:
    DECISIONS[_g]["progress"].append({"date": "2026-10-31", "step": "units queued", "by": "Reality keeper", "note": _n})

# --- 2026-10-31 (Rex's questions, via the controller): Cognition -> Economy individual demand and labour, planned ---
INTERFACES += [
 ("IF-26", "cognition.decision.select", "economy.consumption.demand",
  "Individual wants to Economy demand (planned; Rex 2026-10-31): intentions to acquire or consume (and refusals) aggregate into market demand, replacing the host's per-capita consumption numbers; Economy never decides what a person wants. Joins the built chain Economy -> Settlement (wage channel: economy.labour.wage_quote -> settlement.wage.set_wage; LabourSupply, CONTRACTS s16).", []),
 ("IF-27", "cognition.decision.select", "shared.contract.labour_supply",
  "Individual labour offers to the LabourSupply contract (planned; Rex 2026-10-31): intentions to work or refuse work (at a wage, for an employer) become labour offers beside the population's aggregate supply; today wages are the posted median with no individual input.", []),
]
INTERFACE_GAPS = [
 {"interface": "IF-26", "from": "cognition", "to": "economy", "state": "planned, no built edge",
  "gap": "Cognition outputs intentions (mind.intention) with no consumer; Economy demand is per-capita host numbers with no individual input",
  "joins": "Economy -> Settlement wage channel (built, tested: pirate I4a/I4b) and LabourSupply (CONTRACTS s16)"},
 {"interface": "IF-27", "from": "cognition", "to": "shared contract (settlement, economy)", "state": "planned, no built edge",
  "gap": "labour supply is the population aggregate only; wages are posted-median with no individual offer or refusal",
  "joins": "LabourSupply (CONTRACTS s16; settlement and economy built, population supply closing in DUP-26)"},
]

# --- Rex 2026-10-31: the decomposition and nutrient-cycle chain, and burial to fossil fuels in the formation stage ---
ROW_PATCHES.setdefault("realism.ecology.decomposition", {})["notes"] = ("Rex 2026-10-31 (confirmed owner, Life & Species): dead trees and animals and animal waste -> decomposers -> consumers up the chain -> waste -> "
    "soil nutrients (world.mineralisation_flux into realism.terrain.soils); organic matter that escapes decomposition and is buried passes to realism.terrain.burial_diagenesis")
ROW_PATCHES.setdefault("realism.ecology.food_web", {})["notes"] = "Rex 2026-10-31 (confirmed owner, Life & Species): energy and mass up the chain from decomposers and producers to consumers; waste returns to decomposition"
EXTRA_ROWS.append(_eco("realism.terrain.burial_diagenesis", "Organic burial and diagenesis", "A",
    "buried organic matter (from detritus escaping decomposition, in sediment) matures with burial depth, temperature and time: kerogen, then crude oil, gas or coal; runs in the once-run world-formation stage, and in the active world only as burial of new detritus; mineral_deposits reads it for fossil-fuel deposits",
    ["world.organic_burial"], ["world.detritus", "world.sediment_flux", "world.formation"], ["realism.terrain.mineral_deposits"], "2",
    "Physical Reality (Rex 2026-10-31): burial, diagenesis and deposits; Life & Species owns decomposition and the food web"))
EXTRA_QUANTITIES.append({"id": "world.organic_burial", "kind": "record", "unit": None, "scope": "world", "writer": "realism.terrain.burial_diagenesis",
    "description": "buried organic carbon by depth with maturity (kerogen, oil, gas, coal windows)", "status": "planned (Rex 2026-10-31, nutrient cycle and fossil fuels)"})
INTERFACES.append(("IF-28", "realism.ecology.decomposition", "realism.terrain.burial_diagenesis",
  "Life & Species to Physical Reality (Rex 2026-10-31): detritus that escapes decomposition and is buried in sediment becomes the input of diagenesis; mass conserved across the hand-off.", []))

# --- Rex 2026-10-31: Reality and Life are separate engines. build.py re-owns realism rows by domain tag (A -> reality, B -> life).
# Rows the tag cannot assign (infra, population F/D) stay 'realism' until the Reality keeper answers; overrides go here: id -> engine. ---
ENGINE_SPLIT_OVERRIDES = {}

# --- 2026-10-31: interfaces where Life reads Reality after the engine split (the only reality<->life depends_on edges in the graph) ---
INTERFACES += [
 ("IF-29", "realism.gas.room_box", "realism.gas.breathing_process",
  "Room air to breathing (engine split 2026-10-31): Reality owns the room's gas state; Life's breathing reads it and returns the body's gas exchange to the room through Reality's sources and sinks (mass conserved across the boundary).", []),
 ("IF-30", "realism.gas.altitude_inspired_po2", "realism.gas.alveolar_po2",
  "Inspired oxygen to the alveoli (engine split 2026-10-31): Reality supplies inspired PO2 by altitude; Life computes alveolar PO2 from it.", []),
]

# --- 2026-10-31: split owners for the 15 rows the tag could not assign (Reality keeper; realism/SPLIT.md, unit 2764 queued; all pending SPLIT open question A) ---
ENGINE_SPLIT_OVERRIDES.update({
 "realism.infra.component_registry": "reality", "realism.infra.connection_graph": "reality", "realism.infra.world_conservation": "reality",
 "realism.infra.trace": "reality", "realism.infra.scheduler": "reality", "realism.infra.still_scenario": "reality",
 "realism.infra.rng": "kernel", "realism.infra.library_loader": "shared",
 "realism.bio.library_text_parsing": "life", "realism.medicine.process": "life",
 "realism.population.cohort_tick": "life", "realism.population.epidemic": "life", "realism.population.famine": "life",
 "realism.population.labour": "life", "realism.population.migration": "life",
})
_SPLIT_Q = " Owner per realism/SPLIT.md (Reality keeper 2026-10-31; pending SPLIT open question A, where the substrate lives)."
for _k, _n in [("realism.infra.rng", "kernel owns the RNG; realism re-exports @rex/kernel since 2604, so the realism export is a read."),
               ("realism.infra.library_loader", "both engines through one shared loader: each package loads its own library files."),
               ("realism.population.labour", "life until Society exists; moves to Society under DUP-41."),
               ("realism.population.migration", "life until Society exists; moves to Society under DUP-41."),
               ("realism.population.cohort_tick", "life (organism demography) until Society exists."),
               ("realism.population.epidemic", "life (illness) until Society exists."),
               ("realism.population.famine", "life (organism demography) until Society exists.")]:
    ROW_PATCHES.setdefault(_k, {})
    _old = ROW_PATCHES[_k].get("notes")
    ROW_PATCHES[_k]["notes"] = ((_old + " ") if isinstance(_old, str) and _old else "") + _n + _SPLIT_Q
# Straddlers across the split: one owner each plus an interface (Reality keeper's list)
INTERFACES += [
 ("IF-31", "realism.gas.breathing_process", "realism.gas.room_box", "Body gas exchange to the room (return leg of IF-29): Life's physiology (bodyGasFlows) writes the body's O2 uptake and CO2 and water release; Reality's room box applies them (applyGasFlows); mass conserved.", []),
 ("IF-32", "realism.physiology.heat_balance", "realism.infra.energy_addheat", "Body heat exchange, both ways: Life's body heat (metabolic heat, sweat latent heat) enters Reality's room energy; Reality's air and wall temperatures (losses, walls, heatFlow) return to Life's heat balance; energy conserved.", []),
 ("IF-33", "realism.env.place_process", "realism.physiology.heat_balance", "Place conditions to the body: Reality's air temperature, humidity, WBGT, wind, sun and water temperature are read by Life's thermoregulation and hydration, and by medicine's exposure.", []),
 ("IF-34", "realism.physiology.sweat", "realism.gas.room_box", "Sweat and breath water to room humidity: Life writes the water released; Reality's room box adds it to water vapour through the substrate ledger.", []),
 ("IF-35", "realism.gas.room_box", "realism.medicine.air_conditions", "Gas exposure: Reality's room composition is read by Life's air conditions (accumulateExposure).", []),
 ("IF-36", "economy.inventory.holdings", "realism.nutrition.eat_meal", "Water and food mass into a body: the host or Economy hands over mass; Life ingests it (ingest, addBodyWater) through the substrate ledger; mass conserved.", []),
 ("IF-37", "realism.optics.light_visibility", "realism.perception.detectability", "Planned (phase 8): Reality's light and sound at the observer's position to Life's detectability (vision, group 4 / DUP-37).", ["DUP-37"]),
 ("IF-38", "realism.terrain.soils", "realism.plant.physiology", "Planned (phases 13-17): Reality's soil and weather to Life's plants.", []),
 ("IF-39", "realism.ecology.decomposition", "realism.terrain.soils", "Planned (phase 11): Life's decomposition returns nutrients to Reality's soil, air and water (mass conserved).", []),
]
# Contact -> wounds is already IF-3 (planned on the reality side). body.detectability split: Reality emits the signal at a point, Life computes detectability
EXTRA_ROWS += [
 {"id": "realism.signal.at_point", "name": "Signal at the observer's position (light and sound)", "engine": "realism", "home": "Toolchain/realism (planned; optics phase 8, acoustics)",
  "status": "planned", "domain": "A", "scope": "universal", "inputs": [], "outputs": [{"name": "world.signal_at_point", "unit": "record"}], "state": "planned",
  "formulation": "the signal emitted by a source and propagated to an observer's position (light by optics, sound by acoustics): intensity, spectrum, direction, occlusion", "dependencies": [],
  "timescale": "planned", "invariants": "physics only: never the observer's sensory capacity", "sources": "to research", "evidence": "1", "approximations": "planned", "tests": "none",
  "consumers": ["realism.perception.detectability"], "notes": "Reality keeper 2026-10-31: the reality half of body.detectability", "audit_batch": "reality-keeper-2026-10-31", "planned_writes": ["world.signal_at_point"]},
 {"id": "realism.perception.detectability", "name": "Detectability (signal against sensory capacity)", "engine": "realism", "home": "Toolchain/realism (planned; Life perception)",
  "status": "planned", "domain": "B", "scope": "universal", "inputs": [{"name": "world.signal_at_point", "unit": "record"}], "outputs": [{"name": "body.detectability", "unit": "1"}], "state": "planned",
  "formulation": "d' per observer, cue and channel: the signal at the observer's position against the observer's sensory capacity, counted once (DUP-37)", "dependencies": ["realism.signal.at_point"],
  "timescale": "planned", "invariants": "sensory capacity counted once; Cognition's perception reads d', never applies eyesight or hearing again", "sources": "to research", "evidence": "2",
  "approximations": "planned", "tests": "none", "consumers": ["cognition.perception.detect"], "notes": "Reality keeper 2026-10-31: the life half of body.detectability; host-written until built",
  "audit_batch": "reality-keeper-2026-10-31", "planned_writes": ["body.detectability"]},
]
EXTRA_QUANTITIES.append({"id": "world.signal_at_point", "kind": "record", "unit": None, "scope": "world", "writer": "realism.signal.at_point",
    "description": "light and sound at an observer's position (intensity, spectrum, direction, occlusion)", "status": "planned (Reality keeper 2026-10-31)"})
QUANTITY_PATCH.setdefault("body.detectability", {})["writer"] = "realism.perception.detectability"

# --- 2026-10-31: independent organisation review (controller's sub-agent) findings owned by the registry keeper ---
# (1) Overlap groups for organisations, households and transmission (proposed, batch 2b), with the planned rows ROADMAP P5, P6, P9 name
def _plan(k, eng, dom, name, form, home, notes=""):
    return {"id": k, "name": name, "engine": eng, "home": home, "status": "planned", "domain": dom, "scope": "universal",
            "inputs": [], "outputs": [], "state": "planned", "formulation": form, "dependencies": [], "timescale": "planned", "invariants": "",
            "sources": "to research; ROADMAP", "evidence": "?", "approximations": "planned", "tests": "none", "consumers": [], "notes": notes,
            "audit_batch": "registry-review-2026-10-31", "planned_writes": []}
EXTRA_ROWS += [
 _plan("society.organisation.actors", "society", "F", "Organisations as actors", "guilds, congregations, factions, companies as actors with members, resources and decisions (P6)", "ROADMAP P6 Society (planned)"),
 _plan("economy.household.budget", "economy", "D", "Household income, budget and consumption", "household income, budget and consumption (P5; CONTRACTS §12.4)", "ROADMAP P5 Grounded economy (planned)"),
 _plan("society.household.structure", "society", "F", "Households, marriage, kinship", "household formation, marriage, kinship and inheritance customs (P6)", "ROADMAP P6 Society (planned)"),
 _plan("knowledge.technology.diffusion", "knowledge", "G", "Diffusion of techniques", "diffusion of knowledge and techniques through trade, migration and writing (P9)", "ROADMAP P9 Knowledge & Technology (planned)"),
]
GROUPS += [
 ("DUP-58", "ownership", "Organisations: economy.org.organisation (built, domain F) and settlement businesses already act as organisations, while P6 plans 'organisations as actors' in Society (organisation review 2026-10-31)",
  ["society.organisation.actors", "economy.org.organisation", "settlement.business.open"],
  "Society owns the organisation as an actor (membership, decisions); Economy keeps its accounts and holdings, Settlement its legal records; economy.org.organisation becomes the economic view of the Society actor"),
 ("DUP-59", "ownership", "Households in two planned homes: P5 Economy (income, budget, consumption; CONTRACTS §12.4) and P6 Society (households, marriage, kinship) (organisation review 2026-10-31)",
  ["society.household.structure", "economy.household.budget"],
  "Society owns the household (who belongs, kinship); Economy owns its budget as a view keyed by the Society household id"),
 ("DUP-60", "shared-part", "Transmission in three planned homes: Society's cultural transmission and preference transmission (IF-12), Society's communication networks (IF-16), and Knowledge & Technology's diffusion (P9) (organisation review 2026-10-31)",
  ["society.network.communication", "society.transmission.preferences", "knowledge.technology.diffusion", "realism.communication.transmission"],
  "Society's network (society.network.communication) is the one transmission substrate; preferences, norms and techniques are content carried on it; Reality's transmission stays the physical channel"),
]
AUTH.update({"DUP-58": ("ownership-gap", "a built economic organisation with no Society actor yet"),
             "DUP-59": ("ownership-gap", "nothing built on either side"),
             "DUP-60": ("shared-part", "one substrate, several contents; nothing built")})
for _g in ("DUP-58", "DUP-59", "DUP-60"): BATCH[_g] = "2b"
# (2) V&V honesty: Cognition is wired to itself and host stubs; V1 is verification of form
_STUB = ("yes with stubs (kernel ports and the hungry-pair combined test, cognition 3a2bdcd; its body.* and mind.testimony inputs are host stubs: "
         "body.capacity_functional, body.detectability, body.hunger_signal, mind.testimony; no combined test with Life)")
for _k in [k for k in VV_OVERRIDES if k.startswith("cognition.")]:
    VV_OVERRIDES[_k]["integrated"] = _STUB if _k != "cognition.personality.eight_function" else "yes with stubs (hungry pair per personality version, cognition 3a2bdcd; host-stub inputs as the baseline)"
VV_OVERRIDES["cognition.memory.episodic"]["validated"] = ("no (V1 is verification: the power-law form follows from the model's own equation, so R2 0.99999983 is mathematical consistency, as V1-forgetting.md says; "
    "the model's long-delay exponent 1.25 is not compared with published human exponents (Wixted & Ebbesen 1991: 0.12-0.14); V2 failed (joint, default theta, C-V2))")
VV_OVERRIDES["cognition.memory.episodic"]["evidence"] = "re-audit 2026-10-31 (organisation review): V1 reclassified as verification of form; no independent validation yet"
# (3) shared holds contracts only; each mechanism gets its real owner
ENGINE_SPLIT_OVERRIDES["realism.infra.library_loader"] = "reality"
ROW_PATCHES.setdefault("realism.infra.library_loader", {})["notes"] = "owner reality (the substrate) since 2026-10-31, used by both engines (each package loads its own library files); 'shared' holds contracts only (organisation review)"
for _k, _eng, _n in [("economy.recipe.rates", "economy", "recipe rates are Economy's data and mechanism; the contract is CONTRACTS §16"),
                     ("shared.communication.medium", "reality", "medium properties are physical (range, speed, fidelity, detectability); Knowledge & Technology supplies which media exist (IF-15)"),
                     ("shared.presentation.set", "cognition", "presentation choice is Cognition's (DESIGN §13); goods are Economy's and meaning Society's")]:
    ROW_PATCHES.setdefault(_k, {}).update({"owning_engine": _eng})
    _o = ROW_PATCHES[_k].get("notes")
    ROW_PATCHES[_k]["notes"] = ((_o + " ") if isinstance(_o, str) and _o else "") + f"re-owned to {_eng} 2026-10-31 ('shared' holds contracts only): {_n}"

# --- 2026-10-31: clean ids for garbled realism seed quantities (Reality keeper; unit 2765 reads the new ids from aliases.json) ---
_RQ = "Reality keeper 2026-10-31 (unit 2765 splits realism/kernel.json per mechanism)"
QUANTITY_OPS += [
 ("rename", "air.outputs_o2_frac_co2_ppm_sao2_cohb_ventilation_l_", [("body.cohb", "1", "quantity", "carboxyhaemoglobin fraction"), ("body.ventilation_l_min", "L/min", "quantity", "minute ventilation")],
  _RQ + ": a bundle split; breathing writes body.cohb and body.ventilation_l_min; O2 and CO2 are reads of the room's air.ppm_gases / air.gas_masses (writer realism.gas.room_box); saturation is circulation's (DUP-11)"),
 ("rename", "body.bodyoutputs_medicine", [("body.medicine_outputs", None, "record", "medicine's per-body outputs")], _RQ),
 ("rename", "body.cascade_statement_kineticsseconds", [("body.organ_cascade_state", None, "record", "organ failure cascade state")], _RQ),
 ("rename", "body.compartments_resting_active_fatigued", [("body.muscle_compartments_3cc", "1", "quantity", "3CC muscle compartments: resting, active, fatigued fractions")], _RQ),
 ("rename", "body.organ_tissue_components_graph_edges", [("body.anatomy_graph", None, "record", "organ and tissue components and their graph edges")], _RQ),
 ("rename", "body.seconds", [("body.endurance_time_s", "s", "quantity", "endurance time at an effort")], _RQ),
 ("rename", "component.thickness_0_228_m_rho_1920_cp_790_u_2_11_h_10", [("component.wall_properties", None, "record", "wall thickness, density, heat capacity, U and h")], _RQ),
 ("rename", "place.props_outputs_by_id", [("place.outputs", None, "record", "place conditions by place id")], _RQ),
]
# The bundle stays live until realism unit 2765 commits its split kernel.json (the belt Gates' check reads realism HEAD; a split alias cannot resolve to one id)
QUANTITY_PATCH["air.outputs_o2_frac_co2_ppm_sao2_cohb_ventilation_l_"] = {"status": "superseded: split into body.cohb and body.ventilation_l_min; kept live until realism unit 2765 lands, then retired",
    "writer": "realism.gas.breathing_process"}

# --- 2026-10-31: provider calls as kernel.json ports on the caller (Kernel keeper; agreed by Settlement and Economy; kernel 2766/2767).
# One quantity per returned (in) or changed (call) value; writer = the serving mechanism; host-variable providers carry written_by host. ---
_PP = "provider-port vocabulary 2026-10-31 (Kernel keeper; Settlement and Economy agreed)"
_HOSTLAB = "host (pirate PortLabour / the caller's LabourSupply until Reality's population supply is wired, DUP-26)"
EXTRA_QUANTITIES += [
 {"id": "contract.labour_hours_left", "kind": "quantity", "unit": "person*h", "scope": "contract", "writer": "realism.population.labour", "written_by": _HOSTLAB,
  "description": "LabourSupply.hours: person-hours left after the day's grants (CONTRACTS s18)", "status": _PP},
 {"id": "contract.labour_hours_granted", "kind": "quantity", "unit": "person*h", "scope": "contract", "writer": "realism.population.labour", "written_by": _HOSTLAB,
  "description": "LabourSupply.draw return: hours granted", "status": _PP},
 {"id": "contract.labour_pool_grants", "kind": "record", "unit": None, "scope": "contract", "writer": "realism.population.labour", "written_by": _HOSTLAB,
  "description": "LabourSupply.draw call: the pool grants the draw changes", "status": _PP},
 {"id": "contract.utility_capacity", "kind": "quantity", "unit": "count/d", "scope": "contract", "writer": None, "written_by": "host (UtilityProvider; no Reality mechanism yet)",
  "description": "UtilityProvider.capacity: units per day", "status": _PP},
 {"id": "contract.transport_days", "kind": "quantity", "unit": "d", "scope": "contract", "writer": None, "written_by": "host (TransportProvider; transport over P2 geography is planned)",
  "description": "TransportProvider.days: travel days between two places", "status": _PP},
]
EXTRA_QUANTITIES.append({"id": "economy.units_taken", "kind": "quantity", "unit": "1", "scope": "economy", "writer": "economy.inventory.holdings",
    "description": "MaterialProvider.take return: units actually taken from one inventory (at most its stock)", "status": _PP + "; Economy keeper"})
QUANTITY_OPS += [
 ("writer", "contract.available_bool", "realism.population.labour", _PP + ": LabourSupply.available (person present)"),
 ("writer", "contract.productivity_factor", "realism.population.labour", _PP + ": LabourSupply.productivity"),
 ("writer", "contract.balance", "settlement.ledger.pay", _PP + ": LedgerProvider.balance"),
 ("writer", "contract.rows", "settlement.ledger.pay", _PP + ": LedgerProvider.rows"),
 ("writer", "contract.hasfixture", "settlement.query.fixtures", _PP + ": SettlementReader.hasFixture"),
 ("writer", "contract.posts", "settlement.business.staffing", _PP + ": SettlementReader.posts (serving mechanism to confirm by Settlement)"),
 ("writer", "contract.have", "economy.inventory.holdings", _PP + ": MaterialProvider.have, stock units (serving mechanism to confirm by Economy)"),
 ("retire", "contract.available", "economy.output_units", _PP + ": MaterialProvider.available is economy.material.available's output units"),
 ("retire", "contract.businesses", "settlement.business", _PP + ": SettlementReader.businesses"),
 ("retire", "contract.production", "settlement.production_record", _PP + ": SettlementReader.production"),
 ("retire", "contract.take", "economy.units_taken", _PP + ": MaterialProvider.take returns economy.units_taken and changes economy.stock_changes (the take command on the stock ledger, economy.inventory.holdings; corrected 2026-10-31 by the Economy keeper: economy.stock_taken is market consumption's write)"),
 ("retire", "contract.produce", ["economy.inputs_consumed", "economy.outputs_and_byproducts_added", "economy.market_producedtoday"], _PP + ": MaterialProvider.produce is a call on three economy quantities"),
 ("retire", "contract.rates", ["economy.unitsperfixtureday", "economy.labourhoursperunit"], _PP + ": MaterialProvider.rates"),
]
for _q in ("contract.available_bool", "contract.productivity_factor"):
    QUANTITY_PATCH.setdefault(_q, {})["written_by"] = _HOSTLAB
QUANTITY_PATCH.setdefault("population.labour.person_hours", {})["written_by"] = _HOSTLAB
QUANTITY_PATCH.setdefault("population.cohort_counts", {})["written_by"] = "host (PopulationProvider.headcount; Reality's cohort_tick when wired)"

# --- 2026-10-31: DUP-11 (batch 2 group 8) re-audit of realism 79d09da (2725) ---
QUANTITY_OPS.append(("rename", "air.sao2", [("body.sao2", "1", "quantity", "arterial haemoglobin oxygen saturation (fraction)")],
    "DUP-11: circulation owns the one saturation function (realism 79d09da, 2725); atmosphere supplies alveolar PO2 and calls it"))
QUANTITY_PATCH["body.sao2"] = {"writer": "realism.gas.hb_saturation", "writer_note": "the saturation row now lives in src/circulation.ts saturation() (79d09da); atmosphere re-exports it for compatibility"}
ROW_PATCHES.setdefault("realism.gas.hb_saturation", {})["home"] = "Toolchain/realism/src/circulation.ts saturation() (79d09da, 2725); atmosphere imports it plus a compatibility re-export"
DECISIONS["DUP-11"]["progress"] += [
 {"date": "2026-10-31", "step": "unit passed", "by": "Reality keeper", "commit": "realism 79d09da (2725)", "note": "belt review round aj: PASS-WITH-NOTES"},
 {"date": "2026-10-31", "step": "re-audit: not passed", "by": "registry keeper",
  "note": "implemented: one saturation function, src/circulation.ts:24 saturation(); atmosphere calls it (compatibility re-export); circulation.test covers it; gate passed; numbers unchanged (moved bit-identical). integrated: atmosphere and circulation run together in the human-week checkpoint chain. GAP: validation, part of the agreed acceptance test: the curve fails the cited +/-0.0055 accuracy at 100 mmHg (flags/circulation.md (2725), still labelled unvalidated; 27, 40, 60 mmHg and P50 pass). Owner: Reality keeper (the review fix relabels it as a validation failure; then fix the curve or record the reason). Alias air.sao2 -> body.sao2 recorded"},
]
DECISIONS["DUP-11"]["progress"].append({"date": "2026-10-31", "step": "units queued", "by": "Reality keeper",
    "note": "REAL-34: the 100 mmHg reference (96-97 %) is interpolated from rounded teaching tables (FPnotebook, LITFL), not measured; the model is Severinghaus 1979 (+/-0.0055), about 97.7 %. Realism 2770 (after 2765) writes '(2725) validation failed:' with the source disagreement and the experiment (Severinghaus 1966 standard ODC table, or co-oximetry at PO2 100 mmHg, pH 7.40, 37 C) and hardens the test; model unchanged. Registry closes DUP-11 on that record once 2770 lands and is re-audited"})

# --- 2026-10-31: units and kinds for quantities Settlement serves or writes (Settlement keeper; settlement 2771 copies them into kernel.json ports) ---
_SK = "Settlement keeper 2026-10-31"
for _id, _u in [("contract.balance", "money"), ("settlement.balance_changes", "money"), ("settlement.post_wage", "money/d")]:
    QUANTITY_PATCH.setdefault(_id, {}).update({"unit": _u, "kind": "quantity", "unit_status": "mapped", "unit_source": _SK})
for _id, _k in [("contract.rows", "record"), ("settlement.ledger_row", "record"), ("settlement.business", "record"), ("contract.posts", "record"),
                ("settlement.production_record", "record"), ("settlement.post_filledby", "categorical")]:
    QUANTITY_PATCH.setdefault(_id, {}).update({"unit": None, "kind": _k, "unit_status": "n/a (" + _k + ")", "unit_source": _SK})
QUANTITY_PATCH.setdefault("contract.posts", {})["writer_note"] = "settlement.business.staffing is the only tick writer on a post (sets filledBy daily); post records come from commands (addPost, hire, closeBusiness) as external writers (REG-21); the wage from settlement.wage.set_wage (Settlement keeper 2026-10-31)"

# --- 2026-10-31: units for Economy's provider-port quantities (Economy keeper accepted Settlement's corrections; economy 2773 copies them) ---
_EK = "Economy keeper 2026-10-31 (goods counted in each good's own unit, as unitsperfixtureday)"
QUANTITY_PATCH.setdefault("economy.labourhoursperunit", {}).update({"unit": "person*h/count", "unit_status": "mapped", "unit_source": _EK})
for _id in ("economy.output_units", "contract.have", "economy.units_taken", "economy.stock_taken", "economy.inputs_consumed",
            "economy.outputs_and_byproducts_added", "economy.market_producedtoday"):
    QUANTITY_PATCH.setdefault(_id, {}).update({"unit": "count", "kind": "quantity", "unit_status": "mapped", "unit_source": _EK})
QUANTITY_PATCH.setdefault("economy.stock_changes", {}).update({"unit": None, "kind": "record", "unit_status": "n/a (record)",
    "unit_source": _EK + ": one row per adjustment (inventory, good, delta in count, reason), the stockChanged event shape"})

# --- Rex 2026-10-31, ENGINES.md "History is the backend record; knowledge of history is Cognition's": planned ---
_HIST_HOME = "Toolchain/ENGINES.md 'History is the backend record; knowledge of history is Cognition's' (Rex 2026-10-31; planned, after the P7 baseline)"
_HIST_INV = ("no mechanism in any engine reads the History record; a mind knows the past only through memory, written records, inference from evidence "
             "and oral transmission, all fallible; those beliefs, never the record, drive choices through the ordinary decision mechanism; "
             "myth, propaganda, lost knowledge and archaeology arise from the gap between record and belief, never from scripts")
def _hist(k, name, form, writes, reads, consumers, notes, eng="cognition", dom="C"):
    return _sal(k, name, dom, form, writes, reads, consumers, notes, eng=eng, home=_HIST_HOME, inv=_HIST_INV, batch="rex-2026-10-31-history")
EXTRA_ROWS += [
 _hist("cognition.history.lived_memory", "Knowing the past: memory of lived events",
       "events a person lived through, known through attention, encoding, consolidation and retrieval (DESIGN §14, §16); a route over the existing memory rows, writes nothing of its own",
       [], ["mind.episode", "mind.recalled_body_state"], ["cognition.belief.update"], "reuses cognition.memory.episodic and its planned stages"),
 _hist("cognition.history.written_record", "Knowing the past: written records",
       "a record read through the communication subsystem: one knows only what the writer chose to record and how, and only if the medium persisted (persistence, fidelity, accessibility of shared.communication.medium); the reading is perception and comprehension of a persistent message; writes nothing of its own",
       [], ["world.message", "world.medium_properties", "mind.testimony"], ["cognition.belief.update"], "reuses cognition.communication.perceive and .comprehend"),
 _hist("cognition.history.inference", "Knowing the past: inference from remaining evidence",
       "hypotheses about past events inferred from evidence that remains (ruins, objects, scars, landscape), by perception plus belief update, each with a likelihood; may be wrong",
       ["mind.inferred_past"], ["mind.observation", "mind.belief"], ["cognition.belief.update", "cognition.decision.evaluate"], "archaeology arises here"),
 _hist("cognition.history.oral_transmission", "Knowing the past: oral transmission",
       "accounts of the past passed person to person through communication plus memory, with distortion at encoding, comprehension and retelling; writes nothing of its own",
       [], ["mind.testimony", "mind.episode"], ["cognition.belief.update"], "reuses the communication subsystem and memory across minds; Society's network carries it (DUP-60)"),
 _hist("history.record.backend", "The History record (backend only)",
       "the written record of what occurred in the simulation: events aggregated for validation against real history (Seshat as labelled data) and the evaluation harness; never read by any mechanism, never determines what happens",
       ["history.record"], [], [], "P10 History; the invariant is enforced by a check that no kernel.json process reads history.* (ROADMAP P10 test 2)", eng="history", dom="G"),
]
EXTRA_QUANTITIES += [
 {"id": "mind.inferred_past", "kind": "record", "unit": None, "scope": "mind", "writer": "cognition.history.inference",
  "description": "a mind's hypotheses about past events inferred from remaining evidence, with likelihoods", "status": "planned (Rex 2026-10-31)"},
 {"id": "history.record", "kind": "record", "unit": None, "scope": "history", "writer": "history.record.backend",
  "description": "the backend record of what occurred; read by no mechanism (validation and the harness only)", "status": "planned (Rex 2026-10-31)"},
]

# --- Rex 2026-10-31, ENGINES.md History paragraph: "three mechanisms with no owner yet" and "written and oral transmission are one kind of thing" ---
_ONE_FALL = (" Rex 2026-10-31: written and oral transmission are one kind of thing (data passed between minds) with one fallibility model; "
             "oral is worse because every hop re-encodes through a new mind, while a written record is re-encoded once by its writer and then only decays with its medium.")
for _k in ("cognition.history.written_record", "cognition.history.oral_transmission"):
    ROW_PATCHES.setdefault(_k, {})["notes"] = {"cognition.history.written_record": "reuses cognition.communication.perceive and .comprehend; the object is economy.goods.record_object (IF-40, IF-41).",
                                               "cognition.history.oral_transmission": "reuses the communication subsystem and memory across minds; Society's network carries it (DUP-60)."}[_k] + _ONE_FALL
ROW_PATCHES.setdefault("cognition.history.inference", {})["notes"] = "archaeology arises here. Flagged by Rex 2026-10-31 as a mechanism with no owner yet: planned under Cognition, **no design**."
EXTRA_ROWS += [
 {"id": "economy.goods.record_object", "name": "Records as physical objects", "engine": "economy", "home": _HIST_HOME, "status": "planned", "domain": "D", "scope": "universal",
  "inputs": [], "outputs": [{"name": "economy.record_object", "unit": "record"}], "state": "planned",
  "formulation": "a record is an Economy good made of a Reality material (paper, parchment, stone, wood) that decays by Reality's rules, carrying information with the medium's persistence and fidelity; it can be made, copied, traded, stored, lost or destroyed",
  "dependencies": [], "timescale": "planned", "invariants": "the object (Economy) and its content (Cognition's communication subsystem) have distinct owners; the content degrades only with the object or a re-copy",
  "sources": "to research", "evidence": "?", "approximations": "planned", "tests": "none", "consumers": ["cognition.history.written_record"],
  "notes": "flagged by Rex 2026-10-31 as a mechanism with no owner yet; proposed owner Economy for the object, Cognition's communication subsystem for the content (registry keeper's proposal, for the controller)",
  "audit_batch": "rex-2026-10-31-history", "planned_writes": ["economy.record_object"]},
 {"id": "knowledge.collective.stock", "name": "Collective knowledge stocks with loss", "engine": "knowledge", "home": _HIST_HOME, "status": "planned", "domain": "G", "scope": "universal",
  "inputs": [], "outputs": [{"name": "society.knowledge_stock", "unit": "record"}], "state": "planned",
  "formulation": "what a community knows, as an aggregate over its members' beliefs and its surviving records, with loss when holders die, records decay or transmission fails; the bridge between one mind's belief and 'what the town knows'",
  "dependencies": [], "timescale": "planned", "invariants": "an aggregate over minds and records, never a separate truth; Knowledge & Technology is recorded and transmitted knowledge with loss, never a tech tree (Rex)",
  "sources": "to research", "evidence": "?", "approximations": "planned", "tests": "none", "consumers": ["knowledge.technology.diffusion"],
  "notes": "flagged by Rex 2026-10-31 at the seam of Cognition, Society and Knowledge & Technology; Society's network is its transmission substrate (DUP-60); candidate overlap DUP-61",
  "audit_batch": "rex-2026-10-31-history", "planned_writes": ["society.knowledge_stock"]},
]
EXTRA_QUANTITIES += [
 {"id": "economy.record_object", "kind": "record", "unit": None, "scope": "economy", "writer": "economy.goods.record_object",
  "description": "a record as a good: material, condition, location, holder, and a reference to its content", "status": "planned (Rex 2026-10-31)"},
 {"id": "society.knowledge_stock", "kind": "record", "unit": None, "scope": "society", "writer": "knowledge.collective.stock",
  "description": "what a community knows, with who holds it and which records carry it; loses items as holders die and records decay", "status": "planned (Rex 2026-10-31)"},
]
INTERFACES += [
 ("IF-40", "cognition.communication.encode", "economy.goods.record_object",
  "Writing onto an object (Rex 2026-10-31): Cognition's encoding writes content onto a record object; Economy owns the object, Reality its material decay.", []),
 ("IF-41", "economy.goods.record_object", "cognition.history.written_record",
  "Reading a record (Rex 2026-10-31): a mind reads the surviving content of a record object through perception and comprehension; the medium's persistence and fidelity limit what remains.", []),
]
GROUPS.append(("DUP-61", "ownership", "Collective knowledge at the seam of three engines: Cognition's beliefs, Society's transmission network, Knowledge & Technology's diffusion, and the planned collective knowledge stock (Rex's history rule, 2026-10-31)",
  ["knowledge.collective.stock", "knowledge.technology.diffusion", "society.network.communication", "cognition.belief.update"],
  "Knowledge & Technology owns the collective stock as an aggregate over minds and records; Society's network is the substrate (DUP-60); Cognition owns each mind's belief; nobody else builds 'what the town knows'"))
AUTH["DUP-61"] = ("ownership-gap", "nothing built; flagged so it is built once")
BATCH["DUP-61"] = "2b"

# --- Rex 2026-10-31 (ENGINE_MAP.md top): living resources have three owners in sequence. Reality: soil, minerals, water, terrain, the material
# properties of wood. Life: the living tree, biomass, growth, mortality. Economy: harvested inventories. Felling, harvest, fishing and hunting
# are conservation-preserving transfers Life -> Economy: harvested mass = biomass removed. ---
ENGINE_SPLIT_OVERRIDES.update({"realism.terrain.soils": "reality", "realism.eco.soil_fertility": "reality"})
for _k in ("realism.terrain.soils", "realism.eco.soil_fertility"):
    ROW_PATCHES.setdefault(_k, {})
    _o = ROW_PATCHES[_k].get("notes")
    ROW_PATCHES[_k]["notes"] = ((_o + " ") if isinstance(_o, str) and _o else "") + "Owner reality (Rex 2026-10-31: soil is Reality's; the domain tag had placed it in Life)."
_HARVEST = " Invariant (Rex 2026-10-31): harvested mass = biomass removed; the transfer is Life -> Economy, conserving mass; Economy never creates the resource."
INTERFACES[:] = [(i[0], i[1], i[2], i[3] + (_HARVEST if i[0] == "IF-23" else ""), i[4]) for i in INTERFACES]
INTERFACES.append(("IF-42", "realism.terrain.vegetation_stocks", "economy.material.produce",
  "Felling and harvest (Rex 2026-10-31): Life owns the living plant (tree, crop) and its biomass; felling or harvest transfers the removed biomass into an Economy inventory; Reality owns the wood's material properties once it is a material." + _HARVEST, ["DUP-52", "DUP-53"]))
for _q in ("world.vegetation_stock", "world.wildlife_stock"):
    QUANTITY_PATCH.setdefault(_q, {})["external_writers"] = ["Economy extraction: removals only, through Life's stock; harvested mass = biomass removed (IF-23, IF-42; Rex 2026-10-31)"]

# --- Rex 2026-10-31, ENGINES.md "Institutions, government and religion emerge": planned for Government, Society and Cognition; none built.
# Checked first: society.organisation.actors (DUP-58), society.network.communication (DUP-60), settlement.authority.office_powers (built),
# cognition.belief.update (built), pirate alignment institutions (plugin content, CTRL-7; not universal mechanisms). ---
_INST_HOME = "Toolchain/ENGINES.md 'Institutions, government and religion emerge' (Rex 2026-10-31; planned)"
_INST_INV = ("no mechanism assigns a government type: the distribution of authority is computed, and monarchy, council, republic and the rest are "
             "classifications of the result (History or Catalogue may label them); a law can exist and not be obeyed, and enforcement can fail for want "
             "of resources, witnesses, cooperation or legitimacy; religious movements spread, fragment, merge, reform or vanish through these mechanisms, never a meter")
def _inst(k, name, eng, dom, form, writes, reads, consumers, notes=""):
    return _sal(k, name, dom, form, writes, reads, consumers, notes, eng=eng, home=_INST_HOME, inv=_INST_INV, batch="rex-2026-10-31-institutions")
EXTRA_ROWS += [
 _inst("government.authority.acquisition_delegation", "Authority acquisition and delegation", "government", "E",
       "how authority is gained (negotiation, conquest, inheritance, election, religious authority) and delegated to offices and agents; the computed distribution of authority over people, places and actions",
       ["government.authority_distribution"], ["society.organisation_event", "mind.intention", "mind.belief"], ["government.rule.creation_amendment", "government.compliance.enforcement"],
       "what an office may do is Government's; Settlement keeps who holds it and the permits issued (DUP-62)"),
 _inst("government.rule.creation_amendment", "Rule creation and amendment", "government", "E",
       "who may make or change a rule, by what procedure, and the resulting law records (government.law.schema); includes religious law and official recognition or restriction of religions",
       ["government.law"], ["government.authority_distribution", "government.jurisdiction"], ["government.compliance.enforcement", "cognition.decision.evaluate"]),
 _inst("government.law.schema", "Law as executable data", "government", "E",
       "the law record: jurisdiction, regulated action, condition, legal consequence, enforcing body, exceptions; executable data, never text or a modifier; evaluation chain: Cognition decides whether someone attempts the act, Reality and Life whether it succeeds, Settlement records the property interest, Government whether an enforceable violation occurred",
       [], [], ["government.rule.creation_amendment", "government.compliance.enforcement"], "the format of government.law; writes nothing of its own"),
 _inst("government.compliance.enforcement", "Institutional compliance and enforcement", "government", "E",
       "whether an attempted act violates a law in force in that jurisdiction, and whether enforcement happens: detection (witnesses, perception), the enforcing body's resources and cooperation, legitimacy; a rule's existence is not obedience",
       ["government.violation"], ["government.law", "mind.intention", "settlement.lease_record", "mind.observation"], ["cognition.learning.outcome", "society.organisation.actors"],
       "reads attempts (Cognition intentions), outcomes (Reality and Life), property interests (Settlement)"),
 _inst("government.succession.institutional", "Institutional succession", "government", "E",
       "how offices and authority pass on death, removal or term: rules, claimants, contests; the transfer of who holds an office is recorded by Settlement through a command",
       ["government.succession_event"], ["government.law", "government.authority_distribution", "body.crisis"], ["settlement.authority.office_powers"]),
 _inst("government.jurisdiction.competing", "Jurisdiction and competing authority", "government", "E",
       "which authority's rules apply to a person, place or act; overlapping and contested jurisdictions (crown and church, rival claimants, a town and a ship)",
       ["government.jurisdiction"], ["government.authority_distribution"], ["government.rule.creation_amendment", "government.compliance.enforcement"]),
 _inst("society.institution.formation_dissolution", "Institution formation and dissolution", "society", "F",
       "organisations become institutions (recognised offices, enforcement, succession, revenue) or dissolve, from coordination and conflict among individuals and households; acts on society.organisation.actors records, never a second organisation store",
       ["society.organisation_event"], ["mind.intention", "society.comm_network"], ["government.authority.acquisition_delegation", "society.organisation.actors"], "DUP-58 seam"),
 _inst("society.doctrine.transmission_divergence", "Doctrinal transmission and divergence", "society", "F",
       "shared doctrines carried on Society's one network as content (DUP-60) and diverging, fragmenting or merging through transmission error, reinterpretation and schism",
       ["society.doctrine"], ["society.comm_network", "mind.belief"], ["cognition.belief.system_formation", "society.religion.community_ritual"], "content on society.network.communication (DUP-60)"),
 _inst("society.religion.community_ritual", "Religious communities and ritual", "society", "F",
       "religious communities as organisations with membership, ritual practice and collective identity",
       ["society.religious_community"], ["society.doctrine", "mind.belief"], ["government.rule.creation_amendment", "cognition.belief.supernatural"], "a kind of society.organisation.actors (DUP-58)"),
 _inst("cognition.belief.system_formation", "Belief-system formation", "cognition", "C",
       "a mind forms a structured system of beliefs (explanations, values, a worldview) from experience, testimony and doctrine; through cognition.belief.update, writes nothing of its own",
       [], ["mind.belief", "mind.testimony", "society.doctrine"], ["cognition.belief.update"], "a configuration of the built belief update, never a second belief store"),
 _inst("cognition.belief.supernatural", "Individual supernatural belief, conviction and doubt", "cognition", "C",
       "individual supernatural belief, interpretation of events, spiritual experience, conviction and doubt, as beliefs with their confidence in mind.belief",
       [], ["mind.belief", "mind.appraisal", "society.religious_community"], ["cognition.belief.update", "cognition.decision.evaluate"], "writes through belief.update"),
]
_INST_Q = {"government.authority_distribution": ("government.authority.acquisition_delegation", "the computed distribution of authority over people, places and actions; a government type is a classification of it"),
           "government.law": ("government.rule.creation_amendment", "law records: jurisdiction, regulated action, condition, consequence, enforcing body, exceptions"),
           "government.violation": ("government.compliance.enforcement", "an enforceable violation and whether enforcement followed"),
           "government.succession_event": ("government.succession.institutional", "a succession: office, claimants, rule applied, outcome"),
           "government.jurisdiction": ("government.jurisdiction.competing", "which authority's rules apply where and to whom, including contested overlaps"),
           "society.organisation_event": ("society.institution.formation_dissolution", "an organisation becoming an institution, splitting, merging or dissolving"),
           "society.doctrine": ("society.doctrine.transmission_divergence", "doctrinal variants per community and their lineage"),
           "society.religious_community": ("society.religion.community_ritual", "a religious community: members, ritual, identity")}
for _id, (_w, _desc) in _INST_Q.items():
    EXTRA_QUANTITIES.append({"id": _id, "kind": "record", "unit": None, "scope": _id.split(".")[0], "writer": _w, "description": _desc,
                             "status": "planned (Rex 2026-10-31, institutions)"})
INTERFACES += [
 ("IF-43", "cognition.decision.select", "government.compliance.enforcement", "Attempt to violation (Rex 2026-10-31): Cognition decides whether someone attempts an act; Reality and Life whether it succeeds; Settlement records the property interest (IF-44); Government decides whether an enforceable violation occurred and whether enforcement follows.", []),
 ("IF-44", "settlement.property.lease", "government.compliance.enforcement", "Property interest to law (Rex 2026-10-31): Settlement titles and leases say whose property an act touched; Government reads them and never keeps a second property register.", ["DUP-62"]),
 ("IF-45", "society.network.communication", "society.doctrine.transmission_divergence", "Doctrine as content on the one network (DUP-60): Society's network carries doctrines as it carries preferences, norms and techniques.", ["DUP-60"]),
]
GROUPS.append(("DUP-62", "ownership", "Office powers: Settlement's built office and permit row records offices, permits and permissions, while ROADMAP P8 and Rex's institutions rule give what an office may do to Government (institutions registration 2026-10-31)",
  ["government.authority.acquisition_delegation", "settlement.authority.office_powers", "government.succession.institutional"],
  "Government owns what an office may do and how authority passes; Settlement keeps the record of who holds which office and the permits issued, written through commands"))
AUTH["DUP-62"] = ("ownership-gap", "Settlement's row is built; Government has no engine yet")
BATCH["DUP-62"] = "2b"

# --- Rex 2026-10-31 (via the controller): batch 2b approved, all five owners as proposed; DUP-61 collective knowledge under Knowledge & Technology ---
for _g in ("DUP-58", "DUP-59", "DUP-60", "DUP-61", "DUP-62"):
    DECISIONS[_g] = {"decision": "owner approved as proposed (Rex, 2026-10-31; OVERLAPS-BATCH-2B.md)" + (": the collective knowledge stock is Knowledge & Technology's" if _g == "DUP-61" else ""),
                     "state": "closing", "progress": [{"date": "2026-10-31", "step": "owner approved", "by": "Rex (via the controller)", "note": "batch 2b; closing on the named keepers' agreement of the acceptance test"}]}

# --- 2026-10-31: Society keeper's design proposals (Toolchain/society/DESIGN.md at society 1515974; proposed, NOT approved by Rex).
# Principle SOC-Q1: Society acts on what people do (intentions, acts, episodes), never on what they think. ---
_SOC_HOME = "Toolchain/society/DESIGN.md (society 1515974; proposed, awaiting Rex)"
_SOC_INV = ("Society acts on what people do (intentions, acts, episodes), never on what they think (SOC-Q1); every collective outcome traces to individual "
            "intentions; no meter (rebellion, legitimacy, class) is read by any mechanism")
def _soc(k, name, form, writes, reads, consumers, notes="", rl=None, fm=None, ev="?"):
    r = {"id": k, "name": name, "engine": "society", "home": _SOC_HOME, "status": "planned", "domain": "F", "scope": "universal",
         "inputs": [{"name": x, "unit": "see quantities.json"} for x in reads], "outputs": [{"name": x, "unit": "see quantities.json"} for x in writes],
         "state": "planned", "formulation": form, "dependencies": [], "timescale": "planned", "invariants": _SOC_INV,
         "sources": "Society DESIGN.md sources; evidence per unit", "evidence": ev, "approximations": "planned", "tests": "none", "consumers": consumers,
         "notes": "proposed by the Society keeper 2026-10-31, not yet approved by Rex. " + notes, "audit_batch": "society-keeper-2026-10-31", "planned_writes": writes}
    if rl: r["rate_limiter"] = rl
    if fm: r["failure_mode"] = fm
    return r
_D = " (Society DESIGN §{} at 1515974)"
EXTRA_ROWS += [
 _soc("society.organisation.collective_choice", "Collective choice inside an organisation",
      "an organisation's own rules (data) decide its acts from members' intentions: votes, quorum, office-holders' decisions; only members present vote where presence is required",
      [], ["mind.intention", "society.organisation"], ["society.organisation.actors", "society.collective.action"],
      "watched boundary with government.rule.creation_amendment (SOC-4, Rex's SOC-Q3; IF-47): an organisation's rules bind members who joined and may leave, law binds a territory and non-members",
      rl="meetings are contacts: only members present (attendance is each member's choice) vote where the rule requires presence" + _D.format("1.3"),
      fm="no quorum: no act, recorded; a tie under a rule with no tie-break: no act, recorded; never a random resolution unless the rule says lots" + _D.format("1.3")),
 _soc("society.collective.action", "Collective action",
      "a call to act travels the network contact by contact; people decide to join from their own states (P6 test 3); the act's effects are resolved by the engine that owns the target",
      ["society.collective_event"], ["mind.intention", "society.comm_network"], ["government.compliance.enforcement", "economy.consumption.demand"],
      rl="the speed of the network, physical presence (Reality, Settlement), time budgets" + _D.format("1.5"),
      fm="nobody else turns up: a single-person act, not a collective event; a call that reaches no one: no event, recorded" + _D.format("1.5")),
 _soc("society.population.demography", "Population and demography (accounting)",
      "counts by age, sex, household and place from Life's birth and death events and Society's migration; Life keeps every hazard",
      ["society.population"], ["body.conception", "body.crisis"], ["society.migration.flows", "economy.consumption.demand"],
      "the DUP-41 receiver once Life is ready; until then realism.population.* (life) stay as they are",
      rl="none of its own (it counts)" + _D.format("1.7"), fm="a birth or death without a Life event is a hard error" + _D.format("1.7")),
 _soc("society.migration.flows", "Migration",
      "people move when they believe a destination is better (wage, food, kin, safety); moves follow earlier migrants' ties; each move is an intention",
      [], ["mind.intention", "society.comm_network"], ["society.population.demography", "settlement.assign.workforce"],
      "proposed to replace realism.population.migration under DUP-41 (batch 5, not yet decided by Rex); writes moves through society.population",
      rl="travel (Reality, routes), cost (Economy), information (the network)" + _D.format("1.8"), fm="no believed destination: no move" + _D.format("1.8")),
 _soc("society.norm.sanction", "Norms and sanctions",
      "a norm is what people do and say and what organisation rules name, never a stored rule of the world; Society owns the sanction as an event (gossip as content, exclusion as an organisation act or a dropped tie, costly punishment as a mind's intention); a descriptive prevalence measure for observers and History that no mechanism reads",
      [], ["mind.intention", "society.comm_network"], ["cognition.belief.update"], "contract fields to be completed before its unit; cultural food norms (DUP-49) are norms of this kind"),
 _soc("society.class.structure", "Class (a measurement)",
      "class is a classification computed from holdings and income, occupation and posts, memberships and positions, marriage patterns and network position, for observers and History only; never stored on a person, never read by a mechanism",
      [], ["society.organisation", "society.household", "society.comm_network"], [], "SOC-Q5 open (Rex)", ev="3"),
]
_SQ = "proposed (Society keeper 2026-10-31, DESIGN at society 1515974; not approved)"
EXTRA_QUANTITIES += [
 {"id": "society.organisation", "kind": "record", "unit": None, "scope": "society", "writer": "society.organisation.actors",
  "description": "an organisation: id, founders, members, rules (data), positions, schedule, charter or doctrine reference, resources by Economy view", "status": _SQ},
 {"id": "society.membership", "kind": "record", "unit": None, "scope": "society", "writer": "society.organisation.actors",
  "description": "a person's memberships: organisation, role, joined_at, standing", "status": _SQ},
 {"id": "society.household", "kind": "record", "unit": None, "scope": "society", "writer": "society.household.structure",
  "description": "a household: id, members and relations, residence (Settlement parcel), formed_at; kin graph", "status": _SQ},
 {"id": "society.population", "kind": "quantity", "unit": "count", "scope": "society", "writer": "society.population.demography",
  "description": "counts by age, sex, household and place, with the population accounting record per step", "status": _SQ},
 {"id": "society.collective_event", "kind": "record", "unit": None, "scope": "society", "writer": "society.collective.action",
  "description": "a collective act: action, target, place, time, participants, organisers", "status": _SQ},
 {"id": "society.affordance", "kind": "record", "unit": None, "scope": "society", "writer": None,
  "description": "the social candidate actions open to a person now (join, leave, found, propose, support or oppose, pay, attend, participate, marry, move, seek or avoid contact) with their charter terms; Cognition evaluates them and returns mind.intention",
  "status": _SQ + "; writer row to be named by the Society keeper (affordances span organisations, households and migration)"},
]
# Contract fields for the adopted rows (Society DESIGN §1.1, §1.2, §1.6), and SOC-1
for _k, _sec, _rl, _fm in [
 ("society.network.communication", "1.1",
  "each person's waking hours: the contact durations offered cannot exceed the person's available hours (Cognition's time use, Life's capacity); a person in many organisations meets each less",
  "no exposure data (Settlement absent): only household and kin ties exist, flagged in the trace, never a random graph; a missing T_k: the run refuses to start, never a default"),
 ("society.organisation.actors", "1.2",
  "members' time and money: obligations compete for the same hours and the same household budget (Economy), so organisations compete for members as a consequence; admission rules limit entry",
  "an act no member funds does not happen (recorded); an organisation whose last member dies or leaves dissolves (event with cause); a rule set that cannot be evaluated blocks the founding, logged"),
 ("society.institution.formation_dissolution", "1.4",
  "founding costs the founders' time and money (meeting, fees, charter cost through Economy); every founder must be reachable by the others on the network",
  "founders who cannot meet cannot found; an incomplete founding is recorded with the missing intentions"),
 ("society.household.structure", "1.6",
  "housing (a residence must exist, Settlement) and the budget to run a household (Economy)",
  "no residence available: the union is recorded and the couple stays in an existing household, flagged; never a new parcel invented"),
]:
    ROW_PATCHES.setdefault(_k, {}).update({"rate_limiter": _rl + _D.format(_sec), "failure_mode": _fm + _D.format(_sec)})
ROW_PATCHES.setdefault("society.network.communication", {})["notes"] = "Society keeper 2026-10-31 (DESIGN §1.1): trust is not on the tie; it is Cognition's mind.source_credibility. The one transmission substrate (DUP-60)."
ROW_PATCHES.setdefault("society.organisation.actors", {}).update({"planned_writes": ["society.organisation", "society.membership"], "outputs": [{"name": "society.organisation", "unit": "record"}, {"name": "society.membership", "unit": "record"}]})
ROW_PATCHES.setdefault("society.household.structure", {}).update({"planned_writes": ["society.household"], "outputs": [{"name": "society.household", "unit": "record"}]})
ROW_PATCHES.setdefault("society.doctrine.transmission_divergence", {}).update({
    "inputs": [{"name": "society.comm_network", "unit": "see quantities.json"}],
    "notes": "content on society.network.communication (DUP-60). SOC-1 (Society keeper 2026-10-31): no mind.belief input; a doctrine is a record carried as content, and minds read it through communication"})
ROW_PATCHES.setdefault("society.religion.community_ritual", {}).update({
    "inputs": [{"name": "society.doctrine", "unit": "see quantities.json"}, {"name": "society.organisation", "unit": "see quantities.json"}],
    "planned_writes": [], "outputs": [],
    "notes": "SOC-1 (Society keeper 2026-10-31): a religious community is a view of society.organisation whose charter references a doctrine record, never a second store; no mind.belief input"})
QUANTITY_OPS.append(("retire", "society.religious_community", "society.organisation",
    "SOC-1 (Society keeper 2026-10-31): a religious community is a view of society.organisation (one store); planned, never built"))
ROW_PATCHES.setdefault("society.transmission.preferences", {})["notes"] = "DUP-60 (approved 2026-10-31): a content type on society.network.communication, never a network of its own (Society keeper agrees)"
INTERFACES += [
 ("IF-46", "society.organisation.actors", "cognition.decision.generate",
  "Affordances (Society keeper 2026-10-31, proposed): Society offers the social candidate actions open to a person with their charter terms (society.affordance); Cognition evaluates them with its own needs and returns mind.intention; norms reach minds only as observed acts and messages (closes C-Q6).", []),
 ("IF-47", "society.organisation.collective_choice", "government.rule.creation_amendment",
  "Watched boundary (SOC-4, Rex's SOC-Q3): an organisation's rules bind its members, who joined and may leave; law binds a territory and non-members. Neither engine makes the other's kind of rule.", []),
]
GROUPS[:] = [(g[0], g[1], g[2], g[3] + (["society.population.demography", "society.migration.flows"] if g[0] == "DUP-41" else []), g[4]) for g in GROUPS]
DECISIONS["DUP-61"]["progress"].append({"date": "2026-10-31", "step": "party agrees", "by": "Society keeper", "note": "K&T owns the collective stock; Society builds none"})
DECISIONS["DUP-60"]["progress"].append({"date": "2026-10-31", "step": "owner agrees", "by": "Society keeper", "note": "the network is the one substrate; society.transmission.preferences becomes a content type; trust stays Cognition's source_credibility (DESIGN §1.1); awaiting Cognition, K&T and Reality"})

# --- 2026-10-31: Economy keeper agrees DUP-58 and DUP-59 with amendments to the acceptance tests ---
DECISIONS["DUP-58"]["progress"].append({"date": "2026-10-31", "step": "party agrees (amended)", "by": "Economy keeper",
    "note": "(a) once Society's first unit lands, the economy view takes the Society actor id (mints none) and stores no name or kind; test (1) adds: economy state holds no organisation name, kind, member or leader field; "
            "(b) new test (4): the economy view refuses an organisation id Society's provider does not know (an in port on the actor id; stub until then); "
            "(c) holdings and accounts on merger or dissolution (who receives inventories; money stays in Settlement's ledger) are open for Rex and Society; Economy only applies the transfer Society issues. Awaiting Settlement"})
DECISIONS["DUP-59"]["progress"].append({"date": "2026-10-31", "step": "party agrees (amended)", "by": "Economy keeper",
    "note": "(a) the budget reads membership through a Society provider (in port); test (2) adds: economy state contains no member list (a state-shape test); "
            "(b) a membership change in Society changes the budget's member set the next day with no economy command; "
            "(c) this does not settle where household consumption comes from (CONTRACTS s12.4, ECON-8, open for Rex). Design until Society's first unit"})

# --- 2026-10-31: batch 2b agreements (Society, Economy, Settlement, Government, K&T, Cognition), Society's affordance writer,
# K&T reserved rows, and the Catalogue design (approved by Rex 2026-10-31). ---
def _agree(g, by, note, step="agreed"):
    DECISIONS[g]["progress"].append({"date": "2026-10-31", "step": step, "by": by, "note": note})
# DUP-58 organisations
_agree("DUP-58", "Society keeper", "tests (1)-(3) agreed; added (4) Society state holds no money: dues, relief and spending move only through the money ledger in one kernel transaction with the Society event; (5) no mechanism reads an organisation's kind label; a religious community is a view of society.organisation")
_agree("DUP-58", "Economy keeper", "correction to Society's (4): the economy has no ledger; money's one home is Settlement's ledger (CONTRACTS s3): dues and relief are transfers on settlement.ledger_row / settlement.balance_changes in one kernel transaction with the Society event; the economy's organisation account and household budget read those rows. D-SOC-1's labelled fixture budget lives in Society's demo only, never in economy state", step="party note")
_agree("DUP-58", "Settlement keeper", "agreed with amendments: (1) a business keeps its own id biz.<n> and gains a pointer to exactly one Society actor id; one actor may run several businesses: test (1) becomes 'every business carries one Society actor id and the economy's organisation is keyed by the same id'; (2) creating, merging and dissolving the actor only in Society; opening and closing a business stay Settlement commands for an existing actor; dissolution reaches Settlement as closeBusiness commands; (3) Business.operator and .manager stay Settlement records written only by commands Society's decisions issue. Also must agree the ledger part of Society's (4) (Economy's correction)")
DECISIONS["DUP-58"]["progress"].append({"date": "2026-10-31", "step": "agreed (amended)", "by": "Society, Economy, Settlement",
    "note": "all three parties agree; the acceptance test is batch 2b §1 with the amendments above (Economy (a)-(c), Settlement (1)-(3), Society (4)-(5) with money on Settlement's ledger); merger and dissolution transfers open for Rex and Society. Nothing changes until Society's first unit"})
# DUP-59 households
_agree("DUP-59", "Society keeper", "agreed; added (2): every person belongs to exactly one household at a time")
DECISIONS["DUP-59"]["progress"].append({"date": "2026-10-31", "step": "agreed (amended)", "by": "Society, Economy", "note": "batch 2b §2 with Economy (a)-(c) and Society's one-household rule; ECON-8 (consumption source) open for Rex"})
# DUP-60 transmission
_agree("DUP-60", "Society keeper", "tests (1)-(3) agreed; added (4) trust is not stored on a tie (Cognition's mind.source_credibility); (5) the network writes no content, belief or trust, offering contact opportunities only")
_agree("DUP-60", "Knowledge & Technology keeper", "agreed: diffusion becomes technique content on Society's network, no network of its own; channel content rules: migration and apprenticeship carry the whole method including the tacit share, talk and visits the principles plus what an artefact shows, records only the written part; test (3) clarified: a cut link stops new transmission, never erases a delivered record or held knowledge")
_agree("DUP-60", "Cognition keeper", "agreed: a network message reaches a mind only as a stimulus through perceive and comprehend; the three contents arrive by one path (mind.testimony) and diverge only in belief update weighted by credibility; no content type gets a second entry point; a cut link means no stimulus, so no belief moves. Amendment: Cognition's tests cover the per-mind side; the combined tests are integration tests (PLATFORM §11b) owned by whoever builds X1")
DECISIONS["DUP-60"]["progress"].append({"date": "2026-10-31", "step": "agreed except Reality", "by": "Society, K&T, Cognition", "note": "awaiting the Reality keeper (its transmission stays the physical channel)"})
# DUP-61 collective knowledge
_agree("DUP-61", "Knowledge & Technology keeper", "tests (1)-(3) agreed; amendments: (2a) last holder dead but a readable record survives: the technique stays known and drops out of invented (recoverable, not held); (2b) a record no living member can read does not count as known until a reader appears; (4) a settlement in summary: the summary stock's mean equals the full person-by-person run's mean within a tolerance stated before the run; (5) no mind reads the stock (a fence test: no Cognition process reads society.knowledge_stock). The stock reads mind.belief (truth attribute, theta_hold) through a host handle map (KNT-C1, agreed with Cognition)")
_agree("DUP-61", "Cognition keeper", "agreed: belief.update writes each mind's beliefs, nothing aggregate; no mind.* quantity holds a copy of the stock; no mind reads knowledge.* (as history.*, DESIGN §17); a dead holder's beliefs stop being counted, Cognition emits nothing on death")
DECISIONS["DUP-61"]["progress"].append({"date": "2026-10-31", "step": "agreed except History", "by": "K&T, Society, Cognition", "note": "awaiting the History keeper on test (3)"})
# DUP-62 office powers
_agree("DUP-62", "Government and Settlement keepers", "agreed with amendments (government DESIGN §2.3, GOV-8): (1) every office power check (settlement commands.ts permit L624/L637, public title L178, seize L212) goes through AuthorityProvider.may(office, power, subject, day); Settlement keeps no other power check; (2) succession changes the holder only through Settlement appoint / vacate / inherit commands Government issues; (3) the default provider reading Office.powers[] is host setup data serving the port, not a Settlement decision; Settlement keeps only the null-office and vacancy checks; (4) with Government absent, the default provider gives byte-identical thirty-day outputs and the settlement suite (U10 included) passes unchanged. Settlement doc unit 2781 queued")
DECISIONS["DUP-62"]["progress"].append({"date": "2026-10-31", "step": "units queued", "by": "Settlement keeper", "note": "settlement 2781 (Composer): PACKAGES.md and README.md mark office powers as Government's"})

# Society: the single writer of society.affordance (proposed, not approved)
EXTRA_ROWS.append(_soc("society.affordance.offer", "Affordances offered to a person",
    "the union of what each source permits one person at time t: organisation charters and terms, household union, fission and leave options, reachable migration destinations, contactable people, Government restrictions once they exist; decides nothing, scores nothing, filters by no belief",
    ["society.affordance"], ["society.organisation", "society.household", "society.comm_network"], ["cognition.decision.generate"],
    "the only writer of society.affordance; offering is not choosing (Cognition's, IF-46); its source rows stay providers. Evidence level 4, a simulation interface",
    rl="none of its own; each source's limits apply", fm="a missing source: its actions are absent and logged; nothing is invented", ev="4"))
QUANTITY_PATCH.setdefault("society.affordance", {}).update({"writer": "society.affordance.offer", "status": _SQ + "; writer society.affordance.offer"})

# Knowledge & Technology: reserved names (design awaiting Rex, KNT-Q1..Q4); contracts to follow
_KNT_HOME = "Toolchain/knowledge/DESIGN.md (proposed; awaiting Rex, KNT-Q1..Q4)"
for _k, _n, _f in [("knowledge.capability.state", "Capability state per society and technique", "the five states (possible, known, invented, adopted, deployed) per society and technique"),
                   ("knowledge.technique.requirements", "Technique requirements as data", "a technique's knowledge side as data: principles, minSkill, the unwritten (tacit) share, the recipes it enables, catalogueRef"),
                   ("knowledge.invention.hazard", "Invention hazard (summary resolution)", "invention at summary resolution only"),
                   ("knowledge.adoption.aggregate", "Adoption aggregate (Bass, summary resolution)", "Bass adoption at summary resolution only, aggregating Cognition's choices")]:
    _r = _plan(_k, "knowledge", "G", _n, _f, _KNT_HOME, "reserved by the K&T keeper 2026-10-31 so nobody else builds it; full contract after Rex approves the design")
    _r["audit_batch"] = "knowledge-keeper-2026-10-31"
    EXTRA_ROWS.append(_r)
ROW_PATCHES["knowledge.capability.state"] = {"planned_writes": ["society.capability_state"], "outputs": [{"name": "society.capability_state", "unit": "record"}]}
EXTRA_QUANTITIES.append({"id": "society.capability_state", "kind": "record", "unit": None, "scope": "society", "writer": "knowledge.capability.state",
    "description": "per society and technique: possible, known, invented, adopted or deployed", "status": "proposed (K&T keeper 2026-10-31; design awaiting Rex)"})

# Catalogue (design approved by Rex 2026-10-31; Toolchain/catalogue/DESIGN.md §1, §2.2, §5)
_CAT_HOME = "Toolchain/catalogue/DESIGN.md (approved by Rex 2026-10-31)"
_CAT_INV = ("tags, never unlocks (Rex): a date is reference information and nothing exists in the world because its year arrived; read-only at run time; "
            "a mechanism may read CatalogueReader.label only, while window and get are for configuration code (adapters, scenario builders, the History harness); "
            "each run records catalogue_hash")
def _cat(k, name, form, writes=None, notes=""):
    return {"id": k, "name": name, "engine": "catalogue", "home": _CAT_HOME + " §" + {"catalogue.record.schema": "1.1", "catalogue.provenance.classify": "1.2", "catalogue.date.normalise": "1.3",
            "catalogue.region.membership": "1.4", "catalogue.query.window": "1.5", "catalogue.ingest.fixture": "1.6", "catalogue.reference.ingest": "2.2"}[k],
            "status": "planned", "domain": "i", "scope": "universal", "inputs": [], "outputs": [{"name": x, "unit": "record"} for x in (writes or [])],
            "state": "planned", "formulation": form, "dependencies": [], "timescale": "load time" if k == "catalogue.reference.ingest" else "planned",
            "invariants": _CAT_INV, "sources": "per record (provenance class and confidence)", "evidence": "?", "approximations": "planned", "tests": "none",
            "consumers": [], "notes": "Catalogue keeper 2026-10-31; domain 'infra' (cross-cutting reference, registry keeper's choice). " + notes,
            "audit_batch": "catalogue-keeper-2026-10-31", "planned_writes": writes or []}
EXTRA_ROWS += [
 _cat("catalogue.record.schema", "The catalogue record", "stable id, names, classification, geographic origin and spread, culture, earliest evidence, dates of discovery, invention, identification and adoption, sources, confidence, provenance class"),
 _cat("catalogue.provenance.classify", "Provenance classes", "real, prehistoric, mythological, fantasy, science fiction, original fiction, per record"),
 _cat("catalogue.date.normalise", "Dates and calendars", "dates normalised across calendars (Julian to Gregorian with place), flagged"),
 _cat("catalogue.region.membership", "Regions and periods", "region and period membership for records and attestations"),
 _cat("catalogue.query.window", "The window query", "records present in a region and period, with attestations, labels, sources, known-elsewhere and coverage"),
 _cat("catalogue.ingest.fixture", "Fixture ingest", "ingests fixture files where they are (the pirate town files first), never moved"),
 _cat("catalogue.reference.ingest", "Catalogue reference ingest (load time)", "compiles data/ into the read-only index once before the run; the one writer of the catalogue quantities consumers read through CatalogueReader",
      ["catalogue.record", "catalogue.label", "catalogue.window_bundle", "catalogue.date"],
      "Toolchain/catalogue/kernel.json declares catalogue.load naming this mechanism; the check warns until this row is built"),
]
for _id, _d in [("catalogue.record", "one catalogue record (aliases resolved): CatalogueReader.get"),
                ("catalogue.label", "a record's label for a language, place and year: CatalogueReader.label (the only read a mechanism may declare)"),
                ("catalogue.window_bundle", "present, known-elsewhere and coverage for a region and period: CatalogueReader.window (configuration code only)"),
                ("catalogue.date", "a date converted to the proleptic Gregorian calendar with its place, flagged: CatalogueReader.date")]:
    EXTRA_QUANTITIES.append({"id": _id, "kind": "record", "unit": None, "scope": "catalogue", "writer": "catalogue.reference.ingest", "description": _d,
                             "status": "planned (Catalogue design approved by Rex 2026-10-31); consumers declare direction 'in' ports"})
GROUPS += [
 ("DUP-63", "duplicate", "Date-gated availability: the pirate tech availability table keys availability to invention dates (13 rows 'none (anomaly)'), while the Catalogue holds dated attestations as reference and K&T owns feasibility (Catalogue design §5, 2026-10-31)",
  ["catalogue.record.schema", "pirate.sci.tech_availability", "knowledge.capability.state"],
  "the dated availability becomes Catalogue attestations (presence, with sources); feasibility goes to Knowledge & Technology (P9); the game's anomaly plug stays the plugin's overlay"),
 ("DUP-64", "aggregation", "Provenance labels: the pirate journal anomaly label carries game-side provenance and anomaly labels; the Catalogue classifies provenance (Catalogue design §5)",
  ["catalogue.provenance.classify", "pirate.sci.journal_anomaly_label"],
  "the plugin's label reads the Catalogue's provenance; the plugin keeps its anomaly note"),
 ("DUP-65", "shared-part", "Goods and catalogue identity: economy.recipe.definition ('recipe and good catalogue') holds goods as economic records; the Catalogue holds the identity of the thing (Catalogue design §5)",
  ["catalogue.record.schema", "economy.recipe.definition"],
  "a good gains an optional ref to a catalogue id; nothing moves"),
]
AUTH.update({"DUP-63": ("duplicate-authority", "a date-gate is a §6 violation in spirit"), "DUP-64": ("aggregation", "the plugin label reads the Catalogue"), "DUP-65": ("shared-part", "a reference, no move")})
for _g in ("DUP-63", "DUP-64", "DUP-65"): BATCH[_g] = "2c"

# --- 2026-10-31: Cognition keeper agrees the Society affordance seam (IF-46) with two amendments ---
_IF46 = (" Cognition keeper 2026-10-31, agreed with amendments: (A) decision.generate filters candidates by the mind's believed preconditions (theta_pre), "
         "not by Society's truth; Society checks whether an action is actually open when the intention is attempted, and a refusal is an outcome the mind learns from; "
         "(B) charter terms enter the mind as observations or testimony (the §1 fence), so a mind can misread a charter; Society never writes mind.belief or the believed repertoire. "
         "C-Q6 answered by this seam (pending the controller confirming Rex's reading). Status need (SOC-5): a configuration need row with an appraisal source, added per scenario; the benchmark set stays Rex's C-Q5.")
INTERFACES[:] = [(i[0], i[1], i[2], i[3] + (_IF46 if i[0] == "IF-46" else ""), i[4]) for i in INTERFACES]
QUANTITY_PATCH.setdefault("mind.source_credibility", {})["writer_note"] = "the per-speaker reliability r_j of cognition DESIGN §2.3 (a Beta pseudo-count in the belief store); output of cognition.communication.credibility (confirmed with the Cognition keeper 2026-10-31)"

# --- 2026-10-31: remaining batch 2b agreements (Reality DUP-60, History DUP-61, Settlement DUP-58 (4)) and K&T's DUP-63 wording ---
DECISIONS["DUP-60"]["progress"] += [
 {"date": "2026-10-31", "step": "party agrees", "by": "Reality keeper", "note": "Reality's channel decides physical arrival only (whether, when, how degraded: attenuation and noise for sound and light; delay and loss for a carried letter); comprehension Cognition's, links Society's. Planned for phase 8 (optics, acoustics) writing realism.signal.at_point; a carried letter is an object moved by mechanics or transport. Test (3): a link cut by death is driven by Life's death ledger (crisis.ts declareDeath), read by Society's network; Reality writes nothing to the network"},
 {"date": "2026-10-31", "step": "agreed (amended)", "by": "Society, K&T, Cognition, Reality", "note": "all parties agree; nothing built on any side"}]
DECISIONS["DUP-61"]["progress"] += [
 {"date": "2026-10-31", "step": "party agrees", "by": "History keeper", "note": "(a) the mechanical form of test (3): History reads society.knowledge_stock as a declared read-only input in its record phase after every engine process (Kernel K-2), with no emit, no random draws, no transaction role; a run gives identical snapshot hashes with History attached or detached; the check rule K-4 (engine history) fails any History write outside history.*. (b) G-once: at t0 History only passes the Catalogue's starting bundle to Cognition's and Economy's own loaders; the stock is computed from those; History never writes the stock (history DESIGN §0, §4.4, §5)"},
 {"date": "2026-10-31", "step": "agreed (amended)", "by": "K&T, Society, Cognition, History", "note": "all parties agree"}]
DECISIONS["DUP-58"]["progress"].append({"date": "2026-10-31", "step": "party agrees", "by": "Settlement keeper",
    "note": "test (4) agreed: dues, relief and organisation spending are ledger rows moved through LedgerProvider (CONTRACTS s3), in one kernel transaction with the Society event. Notes: (a) Society, or Economy where it prices them, decides amounts and who pays; Settlement only moves money; (b) no rule for a payer who cannot cover a payment (Q19, open for Rex): balances may go negative today; whether dues can go unpaid is Society's or Rex's rule. Test of the one transaction: make the Society event throw after the ledger row; the ledger must equal its pre-step snapshot (kernel runner snapshot-and-restore over every runner a step touches, SET-15)"})
GROUPS[:] = [(g[0], g[1], g[2], g[3],
              "the dated availability becomes Catalogue attestations (presence, with sources); Knowledge & Technology owns availability (knowledge.capability.state), reading Reality's physical feasibility (knowledge.port.feasibility) and Economy's reach of inputs; the pirate table becomes an initial-stock seed from Catalogue tags plus the capability state, never a date gate (KNT-2); the game's anomaly plug stays the plugin's overlay"
              if g[0] == "DUP-63" else g[4]) for g in GROUPS]
ROW_PATCHES.setdefault("realism.communication.transmission", {})["notes"] = ("Reality-owned, planned for phase 8 (optics, acoustics), writing realism.signal.at_point for sound and light; a carried letter is an object moved by mechanics or transport. "
    "Decides physical arrival only; comprehension is Cognition's, links are Society's (DUP-60, Reality keeper 2026-10-31). IF-14: a received message is a Stimulus for Cognition's perception")

# --- 2026-10-31: Rex's semantic-systems model (cognition DESIGN §18, unit 2817; Cognition keeper's request). Planned ---
_SEM = "never a per-type rule; two minds with the same words and different exposure histories misread each other from the data alone; personality sets only the pool's parameters via the §9 hooks (Rex, cognition DESIGN §18)"
EXTRA_QUANTITIES += [
 {"id": "mind.meaning_pool", "kind": "record", "unit": None, "scope": "mind", "writer": "cognition.communication.comprehend",
  "description": "per mind and term: candidate meanings with likelihoods and the bubble each came from; selection updates likelihoods, reconstruction adds a candidate; read by cognition.communication.encode. " + _SEM,
  "status": "planned (Rex 2026-10-31, semantic systems)"},
 {"id": "mind.bubble_exposure", "kind": "record", "unit": None, "scope": "mind", "writer": None, "role": "derived",
  "derived_from": ["mind.episode (groups lived in, with duration and recency)", "society.membership"],
  "description": "per mind: the groups lived in, with duration and recency, built from history; derived from episodes and Society's membership records, so no second store of the past. " + _SEM,
  "status": "planned, derived (registry keeper 2026-10-31: no writer, because memory.episodic is built and its kernel.json declares only mind.episode and mind.retrieval_p; a dedicated row can be added if the cognition keeper wants one)"},
]
ROW_PATCHES.setdefault("cognition.communication.comprehend", {})["planned_writes"] = ["mind.testimony", "mind.meaning_pool"]
ROW_PATCHES["cognition.communication.comprehend"]["outputs"] = [{"name": "mind.testimony", "unit": "record"}, {"name": "mind.meaning_pool", "unit": "record"}]

# --- 2026-10-31: single writers for six multi-writer realism quantities (Reality keeper, for unit 2765's per-mechanism kernel.json; REG-16) ---
_RW = "Reality keeper 2026-10-31 (unit 2765); non-owner writes left in code are recorded as '(2765) multi-writer:' flags for the overlap work"
QUANTITY_OPS += [
 ("writer", "body.rmr", "realism.physiology.rmr", _RW + ": physiology owns RMR (DUP-24); anatomy.species_profile selects the formula and reads; nutri.rmr_mifflin is a restatement and reads"),
 ("writer", "air.pressure", "realism.atmos.barometric_pressure", _RW + ": gas.altitude_inspired_po2 reads it"),
 ("writer", "component.vessel_t", "realism.thermo.boiling", _RW + ": the vessel's energy balance; chem.reaction_extent reads the temperature and adds its reaction heat as heat"),
 ("writer", "body.blood_lost", "realism.circulation.blood_ledger", _RW + ": one ledger; circulation.bleed_rate supplies the bleed flux as an input"),
 ("writer", "body.blood_volume", "realism.circulation.blood_ledger", _RW + ": one ledger; circulation.volume_recovery supplies the refill flux as an input"),
 ("writer", "body.sweat", "realism.physiology.sweat", _RW + ": physiology.heat_balance reads it"),
]

# --- 2026-10-31: re-audit of settlement 47af0d5 (2771, provider ports) and 3069dda (2781, DUP-62 doc) ---
DECISIONS["DUP-62"]["progress"].append({"date": "2026-10-31", "step": "unit passed (doc part)", "by": "registry keeper", "commit": "settlement 3069dda (2781)",
    "note": "re-audited: PACKAGES.md and README.md mark office powers and succession as Government's; Office.powers[] and appoint / vacate / grantPermission are records only. The code part (AuthorityProvider.may, tests (1)-(4)) waits for Government; group stays closing"})

# --- 2026-10-31: the last four REG-16 multi-writer quantities (Reality keeper, for unit 2765) ---
QUANTITY_OPS += [
 ("rename", "air.pao2", [("body.pao2", "mmHg", "quantity", "alveolar and arterial oxygen partial pressure")],
  _RW + ": PO2 in the alveoli and blood belongs to the body (respiration after SPLIT step 2b); gas.altitude_inspired_po2 writes only the inspired air value"),
 ("writer", "body.crisis", "realism.infra.crisis_record", _RW + ": the crisis and cause-of-death ledger (2710; crisis.ts recordCrisis / trackCrisis); medicine, anatomy and the others open crises by calling the ledger, as callers not writers"),
 ("writer", "component.heat", "realism.infra.world_conservation", _RW + ": the substrate energy ledger (registry contents); every thermal process moves heat as a ledger transfer"),
 ("writer", "plugin.state", None, _RW + ": a host input, not a realism mechanism"),
]
QUANTITY_PATCH.setdefault("body.pao2", {}).update({"writer": "realism.gas.breathing_process"})
QUANTITY_PATCH.setdefault("plugin.state", {}).update({"written_by": "host (the pirate plugin's own state)"})

# --- Rex 2026-10-31 (via the controller): DUP-33 and DUP-32 acceptance texts amended ---
DECISIONS["DUP-33"]["progress"].append({"date": "2026-10-31", "step": "acceptance amended", "by": "Rex (via the controller)",
    "note": "the clause becomes: an engine may keep its own counter only if the kernel adapter asserts it equals floor(T/DAY) each tick"})
DECISIONS["DUP-32"]["progress"].append({"date": "2026-10-31", "step": "acceptance amended", "by": "Rex (via the controller)",
    "note": "the id clause becomes the <engine>/<local id> qualification scheme; kernel 2749 (aa8e64c, 'never collide' test in test/ids.test.ts, gate passed) is its test"})

# --- 2026-10-31: Government design approved by Rex (Toolchain/government/DESIGN.md; government 705ce83). GOV-Q3 rows, GOV-Q4 contract,
# and the agreed Government-Settlement contract quantity (GOVERNMENT-SETTLEMENT.md §2; government dd75837, settlement ac0a81d) ---
_GOV_HOME = "Toolchain/government/DESIGN.md (approved by Rex 2026-10-31) §"
_GOV_INV = _INST_INV + "; GOV-Q1 (Rex): authority is computed from mechanisms, never a stored score; GOV-Q2: the type label is the Catalogue's vocabulary, read by History; Government exposes only government.authority_distribution"
def _gov(k, sec, name, form, writes, reads, consumers, notes="", rl=None, fm=None, ev="?"):
    r = _sal(k, name, "E", form, writes, reads, consumers, "Government keeper 2026-10-31 (design approved). " + notes, eng="government", ev=ev,
             home=_GOV_HOME + sec, inv=_GOV_INV, batch="government-keeper-2026-10-31")
    if rl: r["rate_limiter"] = rl + " (government DESIGN §" + sec + ")"
    if fm: r["failure_mode"] = fm + " (government DESIGN §" + sec + ")"
    return r
EXTRA_ROWS += [
 _gov("government.legitimacy.aggregate", "1.8", "Legitimacy as an aggregate of beliefs",
      "an aggregate read of members' beliefs about an authority (mind.belief), for observers and History; writes no state, never a meter a mechanism reads",
      [], ["mind.belief"], [], "GOV-Q1: never a stored score"),
 _gov("government.fiscal.taxation", "1.9", "Taxation",
      "tax laws (data) on a base; collection runs in Government's own process phase, paying through Settlement's LedgerProvider; Settlement's publicWorks step stays a no-op",
      [], ["government.law", "contract.balance"], ["settlement.ledger.pay"], "closes DUP-42 with Settlement; money only through LedgerProvider",
      rl="the schedule and collectors' person-hours", fm="evasion (undetected breach), inability to pay (the base is not there), collector diversion"),
 _gov("government.fiscal.spending", "1.10", "Spending",
      "the treasury is a Settlement account; spending is a spending-power holder choosing (Cognition) or an appropriation rule (a require law on the treasury) within the balance; payments are Settlement pay rows; Government owns the appropriation rules and the record of promises and decides no expenditure itself",
      [], ["government.law", "contract.balance"], ["settlement.ledger.pay"],
      fm="an appropriation without funds is unpaid: a breach of the institution's own law, evidence for legitimacy beliefs"),
 _gov("government.property.regime", "1.11", "Property-rights regimes", "property-rights regimes as law data over Settlement's titles and leases (IF-44)", [], ["government.law", "settlement.lease_record"], ["settlement.property.lease"]),
 _gov("government.collective_choice.procedure", "1.12", "Collective choice procedures", "procedures by which a polity decides (councils, votes, assemblies) as law data over members' intentions", [], ["mind.intention", "government.law"], ["government.rule.creation_amendment"],
      "watched boundary with society.organisation.collective_choice (IF-47): law over a territory and non-members vs an organisation's own members"),
 _gov("government.military.organisation", "1.13", "Military organisation", "military organisation as an organisation record with command authority; on Society's organisation record", [], ["society.organisation", "government.authority_distribution"], [],
      "the DUP-58 seam: one organisation store (Society); GOV-Q7: battle-scale aggregation is a shared aggregation interface, Reality owns the physics, Government the decision"),
 _gov("government.polity.structure", "1.14", "Polity structure", "a read of the authority graph: which authorities form a polity, its territory and fragments; writes no state", [], ["government.authority_distribution", "government.jurisdiction"], [],
      "polity formation, expansion and fragmentation moved here from History (Rex 2026-10-31)"),
 _gov("government.diplomacy.relations", "1.14", "Diplomacy, war and relations", "relations between authorities (treaty, tribute, alliance, war) decided by office-holders (Cognition) under each authority's rules", [], ["government.authority_distribution", "mind.intention"], [],
      "war decisions moved here from History (Rex 2026-10-31)"),
]
EXTRA_ROWS.append({"id": "shared.action.kind", "name": "Action vocabulary (shared contract)", "engine": "shared", "home": _GOV_HOME + " GOV-Q4",
    "status": "planned", "domain": "i", "scope": "universal", "inputs": [], "outputs": [], "state": "planned",
    "formulation": "the vocabulary of actions that laws regulate: Cognition repertoire kinds, Settlement command types, Economy trade kinds; one id per action kind, owned by no engine",
    "dependencies": [], "timescale": "contract", "invariants": "a law's regulated action names a kind from this vocabulary; engines map their own actions to it; no engine owns it",
    "sources": "contract", "evidence": "?", "approximations": "contract", "tests": "none",
    "consumers": ["government.law.schema", "government.compliance.enforcement", "cognition.decision.generate"],
    "notes": "GOV-Q4 (Rex-approved Government design 2026-10-31); a contract row in 'shared', owned by no engine", "audit_batch": "government-keeper-2026-10-31", "planned_writes": []})
EXTRA_QUANTITIES.append({"id": "government.office_may", "kind": "quantity", "unit": "1", "scope": "government", "writer": "government.authority.acquisition_delegation",
    "written_by": "host (default provider: Settlement Office.powers[])",
    "description": "the answer to AuthorityProvider.may(office, power, subject, day), boolean (0/1); read by settlement.authority.office_powers as an in port at its four power checks",
    "status": "agreed contract (GOVERNMENT-SETTLEMENT.md §2; government dd75837, settlement ac0a81d)"})
GROUPS[:] = [(g[0], g[1], g[2], g[3] + (["government.fiscal.taxation"] if g[0] == "DUP-42" else []), g[4]) for g in GROUPS]
DECISIONS["DUP-62"]["progress"].append({"date": "2026-10-31", "step": "contract agreed", "by": "Government and Settlement keepers",
    "note": "GOVERNMENT-SETTLEMENT.md AGREED and byte-identical (settlement ac0a81d, government dd75837); quantity government.office_may registered for the AuthorityProvider.may port"})

# --- 2026-10-31: rate limiters and failure modes for six Government rows (Government keeper, DESIGN §1.8, §1.11-1.14) ---
for _k, _sec, _rl, _fm in [
 ("government.legitimacy.aggregate", "1.8", "none of its own; changes only as fast as Cognition's belief update changes each b_i",
  "no formed beliefs: R is null (flagged), never 0; aggregates only over persons with a belief"),
 ("government.property.regime", "1.11", "enactment events (rule.creation_amendment procedures)",
  "a title command contrary to the regime is void (Settlement refuses the transfer); rival regimes from rival jurisdictions coexist (§1.6)"),
 ("government.collective_choice.procedure", "1.12", "the body's meetings and its quorum",
  "no quorum: no decision; ties resolve by the procedure's own rule, or none: no decision"),
 ("government.military.organisation", "1.13", "recruitment and pay (Economy goods, Settlement ledger) and Life capacity",
  "unpaid or disloyal agents (low y_j) withdraw backing C; desertion is each agent's Cognition choice"),
 ("government.polity.structure", "1.14", "none of its own; a read of the authority graph, recomputed when authority inputs change",
  "fragmentation when the apex's A falls below a rival's over part of its territory, or the empower chains split"),
 ("government.diplomacy.relations", "1.14", "negotiation events (Cognition minds; IF-18 for executed agreements)",
  "no world enforcer: a treaty breach is enforced only by the parties' own capacity"),
]:
    ROW_PATCHES.setdefault(_k, {}).update({"rate_limiter": _rl + " (government DESIGN §" + _sec + ")", "failure_mode": _fm + " (government DESIGN §" + _sec + ")"})

# --- 2026-10-31: post-recovery harness rerun for DUP-32/33 (registry keeper, kernel 1e7f8bb) ---
_HR = ("harness rerun by the registry keeper at kernel 1e7f8bb (PLATFORM §11b: the recovery changed contract code): 13 of 15 pass; "
       "thirty-days 'P0 one clock' and replay 'canonical-equal snapshots' both TIMED OUT (600 s and 1200 s test timeouts; ran 1622 s and 2674 s), no assertion failed; unverified, not failed")
DECISIONS["DUP-32"]["progress"].append({"date": "2026-10-31", "step": "re-audit: not passed", "by": "registry keeper",
    "note": "amended id test passes (kernel 2749, aa8e64c). " + _HR + ". Closes when the replay test passes after the recovery (Kernel keeper: raise the timeout or find the slowdown). Economy's hand-minted txn ids are local ids qualified at the boundary, acceptable under the amended scheme"})
DECISIONS["DUP-33"]["progress"].append({"date": "2026-10-31", "step": "re-audit: not passed", "by": "registry keeper",
    "note": "under the amended clause, settlement and economy counters are asserted each tick (kernel harness/thirty-days.ts:59-68). GAP 1: Reality's own day counters (realism src/population.ts:221, ecology.ts:71, medicine.ts:448) are not asserted by any adapter: derive them from the clock or have the adapter assert them (Reality keeper). GAP 2: " + _HR})
DECISIONS["DUP-33"]["progress"].append({"date": "2026-10-31", "step": "units queued", "by": "Reality keeper",
    "note": "realism 2846 (after 2845): exports assertDayMatchesClock(day, tSeconds, origin?) (floor(t/86400) on the integer clock); realism calls it after each daily tick wherever it drives the clock; population, ecology and medicine ticks document that a host must call it; a test drives all three ticks for five days at 60 s and fails on a skipped or doubled day. Re-audit when it lands; the harness timeout (Kernel keeper) is the other open item. Note for the re-audit: the amended clause needs the kernel adapter to assert, so check the kernel harness adapter calls it where it drives realism"})
for _g in ("DUP-32", "DUP-33"):
    DECISIONS[_g]["progress"].append({"date": "2026-10-31", "step": "units queued", "by": "Kernel keeper",
        "note": "kernel 2886 raises the harness limits (thirty-days 3600 s, replay 7200 s; hang guards for periodic validation runs); kernel 2887 (gate-only) runs both once and prints their duration; its pass is the record. Machine at 100 % CPU tonight (69 Claude, 4 Codex) fits a 2.7x slowdown with no failed assertion"})
DECISIONS["DUP-62"]["progress"].append({"date": "2026-10-31", "step": "unit passed (Settlement code part)", "by": "registry keeper", "commit": "settlement e52afbd (2871)",
    "note": "re-audited: every office power check goes through officeHas -> AuthorityProvider.may (src/context.ts:78-82) at the four sites (commands.ts:178 public title, :212 seize, :624 and :637 permit); default provider officePowersAuthority reads Office.powers[]; kernel.json declares the in port on government.office_may; belt check exits 0; Settlement reports 72 tests and a byte-identical pirate golden (test (4)). Waits for Government's provider (government 2870) and test (2) through appoint / vacate / inherit"})

# --- 2026-10-31: re-audit of government 2863 (705ce83), 2864 (d04b4dc), 2867 (3f8fe4f); suite 286/286 at government 0ab1303 ---
_GC = "government 0ab1303 (suite 286/286, registry keeper rerun)"
for _k, _src, _t, _c, _n in [
 ("government.law.schema", "src/law/schema.ts, load.ts, predicate.ts", "test/law-schema.test.ts, law-load.test.ts, predicate.test.ts", "705ce83 (2863)", "the law record, predicate language and loader"),
 ("government.compliance.enforcement", "src/law/evaluate.ts, violation.ts", "test/evaluate.test.ts, violation.test.ts", "d04b4dc (2864)", "breach evaluation and violation stages"),
 ("government.jurisdiction.competing", "src/law/evaluate.ts (jurisdiction applicability), src/authority/distribution.ts", "test/evaluate.test.ts", "d04b4dc (2864)", "jurisdiction applicability in the evaluator"),
 ("government.authority.acquisition_delegation", "src/authority/distribution.ts, readers.ts", "test/authority.test.ts", "3f8fe4f (2867)", "authority distribution computed on read (provisionalF); keeper calls on supersession, dates and rivals in DESIGN §1.1-1.2 (0ab1303); the rival/place fix is unit 2890, so implemented, not final"),
]:
    ROW_PATCHES.setdefault(_k, {}).update({"status": "built", "home": "Toolchain/government/" + _src + " (" + _c + ")", "tests": "Toolchain/government " + _t + " (" + _GC + ")"})
    VV_OVERRIDES[_k] = {"validated": "no (no independent data yet; the law fixture 2866 failed review and is re-encoded in 2888)",
                        "integrated": "no (no combined test: the Settlement port provider is government 2870)",
                        "evidence": "re-audit 2026-10-31 of " + _c + ": " + _n}
DECISIONS["DUP-62"]["progress"].append({"date": "2026-10-31", "step": "units queued", "by": "Government keeper",
    "note": "the closing combined test is government 2892 (contract §7 tests 1-4 with both real packages), after government 2870 (the provider alone), settlement 2891 (subjects passed to may) and government 2888 (law fixture)"})

# --- Rex 2026-10-31, ENGINES.md "Developmental cognitive functions" (cognition DESIGN §19, unit 2896; Cognition keeper's request). Planned ---
_DEV_INV = ("all four stack functions exist from birth: no age unlocks or maturity thresholds; the hierarchy sets speed and focus, never existence; "
            "cognitive competence != domain knowledge != learned skill != intelligence (distinct from mind.skill and from K&T's holder port); the baseline B_f never changes")
EXTRA_ROWS.append(_sal("cognition.personality.function_development", "Developmental function experience and competence", "C",
    "accumulated function-relevant experience E_f(t+dt) = E_f(t) + A_f(t) R_f(t) dt per function; developed competence C_f = C_f,0 + k_f log(1 + E_f), provisional; competence feeds back into allocation as the L_f term",
    ["mind.function_experience", "mind.function_competence"], ["mind.function_allocation"], ["cognition.personality.function_allocation"],
    "a separate row so each quantity has one writer (allocation owns A_f); not built; does not interrupt the baseline or T-1/T-2; open: C-Q20 (sources for k_f, C_f,0, R_f), C-Q21 (how C_f enters L_f; decay of E_f)",
    ev="5", home="Toolchain/ENGINES.md 'Developmental cognitive functions' (Rex 2026-10-31; cognition DESIGN §19)", inv=_DEV_INV, batch="rex-2026-10-31-function-development"))
for _id, _d in [("mind.function_experience", "per mind, one value per function f: accumulated function-relevant experience E_f"),
                ("mind.function_competence", "per mind, one value per function f: developed competence C_f (provisional log form), read by function_allocation as L_f")]:
    EXTRA_QUANTITIES.append({"id": _id, "kind": "record", "unit": None, "scope": "mind", "writer": "cognition.personality.function_development",
                             "description": _d + ". " + _DEV_INV, "status": "planned (Rex 2026-10-31, cognition DESIGN §19)"})

# --- 2026-10-31: organism maturation and development (controller's overlap check for Rex). No authoritative row existed; registered planned.
# Existing: realism.development.trait_change (planned; adult trait change from genes, training, nutrition, hormones, recovery), realism.records.cellular_state
# (planned record 2: cellular and developmental state), realism.cellular.* (planned; ageing emergent), realism.genetics.* and realism.genes.ageing_capacity
# (planned); no endocrine or hormonal-development row; built age-keyed effects: the four frozen under DUP-17 plus realism.neurology.tone (an age scale). ---
_MAT_HOME = "Toolchain/realism (Life & Species; planned, P3 with the cellular layer; controller's overlap check for Rex 2026-10-31)"
EXTRA_ROWS.append({"id": "realism.development.maturation", "name": "Organism maturation and development (conception to adulthood)", "engine": "realism",
    "home": _MAT_HOME, "status": "planned", "domain": "B", "scope": "universal",
    "inputs": [{"name": x, "unit": "see quantities.json"} for x in ["realism.records.genetic_profile", "realism.nutrition.pools", "world.signal_at_point", "body.crisis"]],
    "outputs": [{"name": "body.developmental_state", "unit": "record"}, {"name": "body.neural_development", "unit": "record"}],
    "state": "the developmental part of record 2 (realism.records.cellular_state)",
    "formulation": "species-specific trajectories from conception through growth and puberty to adulthood: growth of bones, muscle, organs and nervous system; reproductive maturation; hormonal development; brain development as changing learning capacity, attention, memory and executive control; driven by genetics, nutrition, hormones and environment, with age an input and never the sole cause",
    "dependencies": ["realism.genetics.inheritance", "realism.cellular.population_state"], "timescale": "days to years",
    "invariants": "age is an input, never the sole cause; no age-keyed multiplier is added anywhere (DUP-17 freeze); adult decline is realism.cellular.ageing_emergent's, so this row ends where that one begins, over one continuous developmental state; Cognition never computes brain maturity itself",
    "sources": "to research per unit (developmental physiology, auxology, neurodevelopment)", "evidence": "?", "approximations": "planned", "tests": "none",
    "consumers": ["cognition.personality.function_development", "cognition.attention.allocate", "cognition.memory.episodic", "realism.development.trait_change", "realism.reproduction.fertility_conception"],
    "notes": "registered 2026-10-31 after the controller's overlap check for Rex: no authoritative maturation mechanism existed. Hormonal development has no endocrine row yet; this row owns it until one is registered. Writes the developmental part of record 2; trait_change stays adult trait change",
    "audit_batch": "registry-keeper-2026-10-31-maturation", "planned_writes": ["body.developmental_state", "body.neural_development"]})
EXTRA_QUANTITIES += [
 {"id": "body.developmental_state", "kind": "record", "unit": None, "scope": "body", "writer": "realism.development.maturation",
  "description": "per organism: growth (stature, bone, muscle, organ size), sexual and reproductive maturity, hormonal stage; the developmental part of record 2", "status": "planned (2026-10-31)"},
 {"id": "body.neural_development", "kind": "record", "unit": None, "scope": "body", "writer": "realism.development.maturation",
  "description": "per organism: neural development as limits on learning capacity, memory, attention and impulse regulation (executive control); read by Cognition, never computed there", "status": "planned (2026-10-31)"},
]
INTERFACES += [
 ("IF-48", "realism.development.maturation", "cognition.personality.function_development",
  "Neural development to Cognition (2026-10-31): Life's neurological development constrains learning capacity, memory, attention and impulse regulation (body.neural_development); Cognition reads the constraints and never computes brain maturity itself; function development operates within them; the same constraints reach attention.allocate and memory.", []),
 ("IF-49", "society.household.structure", "cognition.learning.outcome",
  "Social maturation (2026-10-31): language, norms and upbringing reach a growing mind as acquired experience (observed acts and messages from household, kin and community, IF-46), never as a maturity setting; Cognition learns from them as from any experience.", []),
]
GROUPS[:] = [(g[0], g[1], g[2], g[3] + (["realism.development.maturation", "realism.neurology.tone"] if g[0] == "DUP-17" else []), g[4]) for g in GROUPS]
DECISIONS["DUP-17"]["progress"].append({"date": "2026-10-31", "step": "members added", "by": "registry keeper",
    "note": "realism.development.maturation (planned) joins as the developmental side: it must add no age-keyed multiplier and ends where cellular ageing begins; realism.neurology.tone (built, an age scale in its formula) joins as a fifth age-keyed effect, frozen like the other four until the cellular layer"})
ROW_PATCHES["realism.development.maturation"] = {"notes": "registered 2026-10-31 after the controller's overlap check for Rex; adopted by the Life keeper (life DESIGN §1.9): shares the developmental-state record plants use (§1.2); full contract fields after the plant work; owns hormonal development until an endocrine row is proposed. Writes the developmental part of record 2; trait_change stays adult trait change"}

# --- 2026-10-31: DUP-32 closed (kernel 2887 at e2fca94: harness thirty-days and replay 15/15 after the recovery) ---
_H2887 = "kernel 2887 at e2fca94 (2886's raised limits): harness thirty-days and replay 15/15 pass (2,283 s under load; runner log)"
DECISIONS["DUP-32"]["progress"] += [
 {"date": "2026-10-31", "step": "re-audited (11a criteria)", "by": "registry keeper",
  "note": "implemented: kernel ids qualify as <engine>/<local id> (Rex's amended clause), test 'never collide' in test/ids.test.ts (2749, aa8e64c); settlement and economy import kernel ids, context and reduce; realism uses the kernel rng. integrated: " + _H2887 + " (replay 'canonical-equal kernel and all three engine snapshots'). validated: n/a (an identity and replay rule). Economy's locally minted txn ids are local ids qualified at the boundary"},
 {"date": "2026-10-31", "step": "closed", "by": "registry keeper"}]
DECISIONS["DUP-32"]["state"] = "closed"
DECISIONS["DUP-33"]["progress"].append({"date": "2026-10-31", "step": "harness passed", "by": "Kernel keeper", "note": _H2887 + "; DUP-33 now waits only on Reality's counter asserts (realism 2846)"})

# --- 2026-10-31: Life keeper, cellular architecture (Toolchain/life/DESIGN.md §1.10; design approved by Rex through the controller) ---
_CELL_HOME = "Toolchain/life/DESIGN.md §1.10 (cellular architecture; approved by Rex 2026-10-31)"
_CELL_INV = ("organ function is the combination of its cell-type populations; a regional subdivision sums to the aggregate (refinement B); "
             "one clearance number (hepatocyte capacity), never a second one in pharmacokinetics; reversal of remodelling only where sourced")
def _cell(k, name, form, writes, reads, consumers, notes, ev="?"):
    return _sal(k, name, "B", form, writes, reads, consumers, "Life keeper 2026-10-31. " + notes, eng="realism", ev=ev, home=_CELL_HOME, inv=_CELL_INV, batch="life-keeper-2026-10-31-cellular")
ROW_PATCHES.setdefault("realism.cellular.population_state", {}).update({
    "formulation": "the tissue-population state per cell type: viable mass, capacity, injury D, repair capacity, senescent fraction, turnover, fibrotic fraction, cell type, optional region; damage D(t+1) = D(t) + damage - repair; specialised cell-type populations per organ; organ function is the combination of its populations; optional regional subdivision where the sum of regions equals the aggregate (refinement B)",
    "notes": "adopted by the Life keeper (life DESIGN §1.10); first implementation src/tissue.ts in realism 2815 (plants first)"})
EXTRA_ROWS += [
 _cell("realism.cellular.cell_architecture", "Cell-type records (architecture)",
       "cell-type records as data: kingdom; wall (none, cellulose, chitin); plastids; vacuole; nutrition mode; division capacity; specialised function; the injury, repair and regeneration parameters it brings",
       [], [], ["realism.cellular.population_state", "realism.anatomy.species_profile"], "data, writes nothing at run time; evidence 1-2 for the cell-biology facts", ev="2"),
 _cell("realism.cellular.chemical_injury", "Chemical injury of tissue",
       "tissue exposure from realism.neurology.pk and medicine exposure gives an injury rate by sourced concentration-response and susceptibility; hepatocyte capacity sets the liver clearance that neurology.pk reads (no second clearance number)",
       [], ["body.medicine_outputs"], ["realism.cellular.population_state", "realism.neurology.pk"],
       "cell injury and loss; genomic damage stays realism.cellular.dna_damage_repair's (separate outputs; IF-50 boundary); writes injury into population_state's D through the population row"),
 _cell("realism.cellular.tissue_remodelling", "Tissue remodelling and fibrosis",
       "repeated injury activates the remodelling cell type (stellate cells, fibroblasts) and raises the fibrotic fraction, which lowers function; reversal only where sourced",
       [], [], ["realism.cellular.population_state", "realism.anatomy.organ_function"], "the fibrotic fraction is a field of population_state"),
]
INTERFACES += [
 ("IF-50", "realism.cellular.chemical_injury", "realism.cellular.dna_damage_repair",
  "Toxic exposure split (Life keeper 2026-10-31): chemical injury owns cell injury and loss from a toxic exposure; DNA damage and repair owns genomic damage from the same exposure; one exposure, two separate outputs, never the same damage counted twice.", []),
 ("IF-51", "realism.cellular.population_state", "realism.neurology.pk",
  "Hepatocyte capacity to clearance (Life keeper 2026-10-31): the liver's hepatocyte population capacity sets the clearance pharmacokinetics reads; pk keeps no clearance number of its own.", []),
]
GROUPS += [
 ("DUP-66", "aggregation", "Organ damage in two homes: anatomy's built damage accumulation and repair and organ function's damage term, vs the planned tissue-population state (Life cellular design, 2026-10-31)",
  ["realism.cellular.population_state", "realism.anatomy.damage_repair", "realism.anatomy.organ_function"],
  "population_state owns injury per cell-type population; the anatomy rows become the documented one-population aggregate; organs with populations read damage from them; anatomy restates; no numbers move until a unit does it"),
 ("DUP-67", "duplicate", "Connective tissue integrity: anatomy's built collagen integrity and the anatomy.tissues integrity table vs the planned tissue-population state (Life cellular design, 2026-10-31)",
  ["realism.cellular.population_state", "realism.anatomy.tissue_collagen"],
  "connective, bone and endothelial populations in population_state carry the same numbers; tissue_collagen becomes their read; the DUP-16 pathway (vitamin C to collagen to healing) runs through the population"),
]
AUTH.update({"DUP-66": ("aggregation", "the one-population organ aggregate is legitimate once it reads the populations"), "DUP-67": ("duplicate-authority", "")})
for _g in ("DUP-66", "DUP-67"): BATCH[_g] = "2c"

# --- 2026-10-31: LIFE-3 (species configuration record) and LIFE-2 (plant input quantities), Life keeper ---
ROW_PATCHES.setdefault("realism.anatomy.species_profile", {}).update({
    "name": "Species configuration record (every organism; animal anatomy is one part)",
    "home": "Toolchain/realism data/library/anatomy.json (animals) and data/library/plants.json (one table per species with a schema table; realism 2807, f2a9df5; scripts/check_plants.py); validation studies apart in validation.json plants_validation",
    "notes": "LIFE-3 (Life keeper 2026-10-31, life DESIGN §1.1): generalised from an animal anatomy profile to the species configuration record for every organism; one data record per species; every value labelled researched, estimate or fiction, or null with a flag; no behaviour rule; no species name in src/; cultivars and landraces are genetic profiles of one species. Consumers: every Life mechanism, the Catalogue, game adapters. Evidence per value. The animal part is built; the plant part is planned"})
_L2 = "planned (LIFE-2, Life keeper 2026-10-31): read by Life's plants; Reality writes it (phases 8, 13, 16) and registers the writer with its design"
for _id, _u, _d in [("place.par", "mol/m^2/d", "photosynthetically active radiation, mol photons per m2 per day"),
                    ("place.vpd", "kPa", "vapour pressure deficit"), ("place.rain", "mm/d", "rainfall"),
                    ("world.soil_water", "m^3/m^3", "root-zone volumetric soil water"), ("world.soil_salinity", "dS/m", "soil salinity (electrical conductivity)"),
                    ("world.water_depth", "m", "water depth"), ("world.water_kd", "1/m", "light attenuation coefficient in water"),
                    ("world.water_salinity", "1", "water salinity (PSU, practical salinity, dimensionless)"), ("world.water_t", "degC", "water temperature"),
                    ("world.inundation", "1", "fraction of time flooded"), ("world.sediment_porewater_nutrients", "mg/L", "sediment porewater N and P")]:
    EXTRA_QUANTITIES.append({"id": _id, "kind": "quantity", "unit": _u, "scope": _id.split(".")[0], "writer": None, "description": _d, "status": _L2})
QUANTITY_PATCH.setdefault("world.soil_nutrient_pool", {})["description"] = ("soil N, P and K pools per area, total and plant-available (Life keeper and Reality agreed 2026-10-31); written only by realism.terrain.soils; "
    "Life writes uptake (water, N, P, K) and litter fluxes back through the substrate ledger, never the stock")

# --- Rex 2026-10-31 (to the Life keeper, relayed): DUP-66 and DUP-67 approved as proposed, with a qualification ---
for _g in ("DUP-66", "DUP-67"):
    DECISIONS[_g] = {"decision": "owner approved as proposed (Rex 2026-10-31, to the Life keeper; relayed): tissue populations are the authoritative source of cellular injury, repair, viability and remodelling; anatomy's organ-damage and tissue-integrity quantities become derived summaries, never independent stores. Qualification: integrity is not cell survival alone; population_state gains a matrix integrity field (0-1) beside viable mass and fibrotic fraction, and the organ-integrity read combines all three; injury is counted once across chemical exposure, DNA damage and organ level (IF-50)" + (". DUP-67: collagen loss in scurvy is matrix integrity falling in the connective population, with the same numbers" if _g == "DUP-67" else ""),
                     "state": "closing", "progress": [{"date": "2026-10-31", "step": "owner approved", "by": "Rex (via the Life keeper)", "note": "life DESIGN §1.10; realism 2815 implements the matrix integrity field"}]}
ROW_PATCHES["realism.cellular.population_state"]["formulation"] = ("the tissue-population state per cell type: viable mass, capacity, injury D, repair capacity, senescent fraction, turnover, fibrotic fraction, matrix integrity (0-1; extracellular matrix and mechanical structure, Rex 2026-10-31), cell type, optional region; "
    "damage D(t+1) = D(t) + damage - repair; specialised cell-type populations per organ; organ function is the combination of its populations; the organ-integrity read combines viable mass, fibrotic fraction and matrix integrity; optional regional subdivision where the sum of regions equals the aggregate (refinement B)")

# --- Rex 2026-11-01 (Cognition keeper): Function Activation Ledger, diagnostic tooling, recorded as a note (the registry has no tooling kind) ---
_FAL = (" Diagnostic tooling (Rex 2026-11-01, not a mechanism): the Function Activation Ledger, id cognition.diagnostics.function_ledger, "
        "Toolchain/cognition/bench/diagnostics/DESIGN.md (units 2917 design, 2918 implementation, 2919 dashboard); writes no mind.* quantity and changes no decision; "
        "reads the existing processing trace (scenarios DESIGN §9) plus counterfactual ablation reruns; no second event or log system; F1-F13 unmodified during the initial experiments; the intended relevance map is never read by code.")
_o = ROW_PATCHES.get("cognition.personality.eight_function", {}).get("notes")
ROW_PATCHES.setdefault("cognition.personality.eight_function", {})["notes"] = ((_o or "Rex's theory as a hypothesis, one optional configuration of the slot (DESIGN.md §9); CTRL-7.") + _FAL)

# --- 2026-11-01: causal-chain completeness audit (Toolchain/CHAINS.md; Rex's direction via the controller). Gaps only; the registry decides nothing ---
for _id, _fr, _to, _gap in [
 ("CG-1", "reality", "life", "chain 1.1: place.par (mol/m^2/d) has no writer; LIFE-2 says Reality writes it (phases 8, 13, 16)"),
 ("CG-2", "reality", "life", "chain 1.2: place.rain, place.vpd and world.soil_water have no writer; hydrology writes only groundwater and drainage"),
 ("CG-3", "life", "reality", "chain 1.4: no plant uptake flux quantity (water, N, P, K) although realism.terrain.soils integrates uptake"),
 ("CG-4", "reality", "life", "chain 1.4: realism.plant.physiology inputs omit the LIFE-2 quantities (par, vpd, rain, soil_water, salinity, water)"),
 ("CG-5", "life", "reality", "chain 1.7: no Reality or Life row moves an organism between places (only the plugin pirate.align.step)"),
 ("CG-6", "life", "reality", "chain 1.8: no excreta mass or nutrient quantity for people or animals (body.urine is water only); DUP-45 undecided"),
 ("CG-7", "reality", "reality", "N balance: no nitrogen input quantities (deposition, biological fixation, manure as mass)"),
 ("CG-8", "reality", "reality", "N balance: no gaseous nitrogen losses (denitrification, volatilisation)"),
 ("CG-9", "reality", "life", "N balance: world.soil_nutrient_pool and the nutrient fluxes join N, P and K in one kg quantity described per area"),
 ("CG-10", "life", "life", "microbiology: no gut microbial digestion term (feed_gate, absorption, flux_digestion_atp)"),
 ("CG-11", "life", "economy", "X1 acceptance (1): mass leaving bodies as faeces has no destination row or declared boundary"),
 ("CG-12", "life", "life", "chain 2.2: the genetic profile (record 1) has no quantity id; maturation lists the row id as an input"),
 ("CG-13", "life", "life", "chain 2.4: realism.nutrition.energy_store reads 'intake'; whether energy enters as eaten or absorbed is unstated"),
 ("CG-14", "life", "life", "chain 2.4: expenditure has no growth, thermoregulation (shivering) or reproduction term"),
 ("CG-15", "life", "life", "chain 2.5: tissue populations have no dN/dt = B - D equation or quantities (population_state outputs empty)"),
 ("CG-16", "cognition", "reality / life", "chain 3.6: no row resolves an intention into a physical outcome (IF-43 names Reality and Life); body.capacity_functional has no writer (DUP-15)"),
 ("CG-17", "kernel", "all", "structures: the kernel ConservedQuantity / ResolutionService (kernel src/resolution.ts) has no registry row"),
 ("CG-18", "kernel", "all", "structures: KernelEvent payload is unknown; no list of event types with payload schema, producer and consumers"),
]:
    INTERFACE_GAPS.append({"interface": _id, "from": _fr, "to": _to, "state": "gap (CHAINS.md 2026-11-01)", "gap": _gap, "joins": "Toolchain/CHAINS.md"})

# --- 2026-11-01: Rex's addendum to CHAINS.md: each gap carries its failure type (missing mechanism / broken connection / invalid coupling); CG-19..25 added ---
for _id, _fr, _to, _gap in [
 ("CG-19", "economy", "life", "IF-36 and IF-42 require mass; economy.material.produce, inventory.holdings and consumption.demand count goods unitless; eat_meal takes kg and kcal; no row converts a good to mass or energy"),
 ("CG-20", "reality", "life", "one transfer calculated twice: built realism.eco.soil_fertility drains soil on harvest (f -= crop demand) apart from plant uptake (DUP-51, DUP-53)"),
 ("CG-21", "life", "life", "plant biomass in two quantities: world.plant_state (plant.physiology, fast) and world.vegetation_stock (vegetation_stocks, yearly), no aggregation (DUP-53)"),
 ("CG-22", "reality", "life", "realism.terrain.soils and hydrology timescale is once per world / yearly while the uptake and mineralisation fluxes they integrate run on the fast scheduler; no integration rule"),
 ("CG-23", "life", "life", "population consumption (world.trophic_flux kg/a) and individual consumption (body.kcal_in per meal) are not joined across resolutions"),
 ("CG-24", "life", "cognition", "body.hunger_signal's writer realism.nutrition.hunger_fullness is documented-only; Cognition reads a host stub"),
 ("CG-25", "life", "cognition", "body.detectability's writer realism.perception.detectability is planned; Cognition reads a host stub"),
]:
    INTERFACE_GAPS.append({"interface": _id, "from": _fr, "to": _to, "state": "gap (CHAINS.md 2026-11-01)", "gap": _gap, "joins": "Toolchain/CHAINS.md"})
_CG_TYPE = {"CG-1": "missing mechanism (no equation)", "CG-2": "missing mechanism (no equation)", "CG-3": "broken connection", "CG-4": "broken connection",
    "CG-5": "missing mechanism (no equation)", "CG-6": "missing mechanism (no equation)", "CG-7": "missing mechanism (no equation)", "CG-8": "missing mechanism (no equation)",
    "CG-9": "invalid coupling", "CG-10": "missing mechanism (no equation)", "CG-11": "missing mechanism (no equation)", "CG-12": "broken connection",
    "CG-13": "invalid coupling (to confirm by the owner)", "CG-14": "missing mechanism (no equation)", "CG-15": "missing mechanism (no equation)",
    "CG-16": "missing mechanism (no equation)", "CG-17": "broken connection", "CG-18": "missing mechanism (no equation)", "CG-19": "invalid coupling",
    "CG-20": "invalid coupling", "CG-21": "invalid coupling", "CG-22": "invalid coupling", "CG-23": "broken connection",
    "CG-24": "missing mechanism (not implemented)", "CG-25": "missing mechanism (not implemented)", "IF-26": "broken connection", "IF-27": "broken connection"}
for _g in INTERFACE_GAPS:
    if _g["interface"] in _CG_TYPE: _g["failure_type"] = _CG_TYPE[_g["interface"]]

# --- 2026-11-01: Rex approved CHAINS.md, integration first (PLATFORM §7a: one transfer per physical flow). Priority, owner and agreeing keepers per gap ---
_CG_ASSIGN = {
 "CG-20": (1, "reality", ["life"]), "CG-21": (1, "life", ["reality"]), "CG-19": (1, "economy", ["life"]), "CG-9": (1, "reality", ["life"]),
 "CG-22": (1, "reality", ["life", "kernel"]), "CG-13": (1, "life", []),
 "CG-16": (2, "cognition", ["reality", "life", "economy"]), "IF-26": (2, "cognition", ["economy"]), "IF-27": (2, "cognition", ["economy", "settlement"]),
 "CG-3": (2, "life", ["reality"]), "CG-4": (2, "life", ["reality"]), "CG-12": (2, "life", []), "CG-23": (2, "life", ["economy"]),
 "CG-17": (2, "kernel", ["registry keeper"]), "CG-18": (2, "kernel", ["controller", "all engines"]),
}
for _g in INTERFACE_GAPS:
    _id = _g["interface"]
    if _id in _CG_ASSIGN:
        _p, _o, _a = _CG_ASSIGN[_id]
        _g.update({"priority": _p, "owner": _o, "agreeing": _a, "approved": "Rex 2026-11-01 (integration first; PLATFORM §7a)"})
    elif _id.startswith("CG-"):
        _g.update({"priority": 3, "approved": "Rex 2026-11-01: research units now (web tools), implementation later"})

# --- 2026-11-01: CG-17 closed. Kernel keeper's proposal (shared note kernel-cg17-cg18-cg22.md); registry keeper re-audit at kernel 309a317
# (src/resolution.ts, src/transaction.ts and their tests unchanged since a3c4314): resolution.test.ts + transaction.test.ts 23/23 ---
_KH = "Kernel keeper 2026-11-01 (CG-17, CHAINS.md); the kernel owns no world quantity: quantities and tolerances are supplied by the owner at construction"
EXTRA_ROWS += [
 {"id": "kernel.resolution.handoff", "name": "Adaptive resolution hand-off", "engine": "kernel", "home": "Toolchain/kernel/src/resolution.ts (ResolutionService, ConservedQuantity, switchTo; kernel a3c4314)",
  "status": "built", "domain": "infra", "scope": "universal", "inputs": [], "outputs": [], "state": "the active representation, its RNG stream and enlisted participants",
  "formulation": "coarse to fine: I = refine(A, rng), accepted only if for every declared conserved quantity q (owner-declared unit, absolute tolerance tau_q) |Q_q(coarsen(I)) - Q_q(A)| <= tau_q; fine to coarse: A = coarsen(I) installed exactly; switch only at the current scheduler boundary T (the old process set closes T, the new set first runs after T with dt from T)",
  "dependencies": ["kernel.transaction"], "timescale": "per switch",
  "invariants": "conservation within tau per quantity on refine; exact aggregate on coarsen; a failed switch restores representation, RNG stream and participants; no switch inside an instant; a no-op switch never reconverts; duplicate conserved quantity rejected",
  "sources": "bookkeeping identity (PLATFORM §9: finer resolution refines the aggregate, never contradicts it)", "evidence": 1, "approximations": "none (accounting)",
  "tests": "Toolchain/kernel test/resolution.test.ts (R-refine, R-boundary, R-coarsen, R-loss, R-every-quantity, R-isolation, R-transaction, R-coarsen-rollback, R-outer-transaction, R-instant, R-time, R-noop; registry keeper rerun at kernel 309a317, with transaction.test.ts 23/23)",
  "consumers": [], "notes": _KH + "; no registered consumer yet (realism epidemic-vs-individuals uses its own)", "audit_batch": "kernel-keeper-2026-11-01-cg17"},
 {"id": "kernel.transaction", "name": "Atomic multi-participant boundary", "engine": "kernel", "home": "Toolchain/kernel/src/transaction.ts (transaction, Participant; kernel a3c4314)",
  "status": "built", "domain": "infra", "scope": "universal", "inputs": [], "outputs": [], "state": "participant snapshots for the duration of one call",
  "formulation": "snapshot every enlisted participant; run fn; on throw restore every participant (attempting all) and rethrow",
  "dependencies": [], "timescale": "per call",
  "invariants": "all-or-nothing state across enlisted participants; a restore failure never masks the original error; gives the atomicity PLATFORM §7a needs (delta source = -q and delta destination = +q commit together or not at all); it is not itself a transfer primitive (open with the controller)",
  "sources": "bookkeeping identity", "evidence": 1, "approximations": "none (accounting)",
  "tests": "Toolchain/kernel test/transaction.test.ts; test/resolution.test.ts R-transaction, R-outer-transaction (registry keeper rerun at kernel 309a317, 23/23)",
  "consumers": [], "notes": _KH, "audit_batch": "kernel-keeper-2026-11-01-cg17"},
]
ROW_PATCHES.setdefault("kernel.resolution.handoff", {}).update({"rate_limiter": "one switch per service per instant; tolerance is the owner's",
    "failure_mode": "throws 'does not conserve <q>' and rolls back; rejects past, future or invalid switch times"})
ROW_PATCHES.setdefault("kernel.transaction", {}).update({"rate_limiter": "none (synchronous call)",
    "failure_mode": "on throw every participant is restored and the original error rethrown"})
for _k in ("kernel.resolution.handoff", "kernel.transaction"):
    VV_OVERRIDES[_k] = {"validated": "n/a (accounting identity)", "integrated": "no (no registered consumer yet)",
                        "evidence": "re-audit 2026-11-01 at kernel 309a317 (code unchanged since a3c4314): 23/23"}
for _g in INTERFACE_GAPS:
    if _g["interface"] == "CG-17":
        _g.update({"state": "closed 2026-11-01: kernel.resolution.handoff and kernel.transaction registered (built; tests 23/23 at kernel 309a317)"})
    if _g["interface"] == "CG-22":
        _g["progress"] = ("Kernel keeper 2026-11-01: no kernel change; proposed rule: each fast flux applies its transfer to the stock at its own period "
                          "(one transaction with the source, §7a); the yearly mechanism runs only the stock's slow dynamics; a yearly buffer breaks §7a unless it is a declared conserved stock. Reality decides")
    if _g["interface"] == "CG-18":
        _g["progress"] = ("Kernel keeper 2026-11-01 proposes registry/events.json (registry keeper owns: type, producer, consumers, payload field schema, cause), "
                          "a checker in check-registry.ts and an opt-in bus contract hook; first unit an event inventory. Registry keeper agrees; waits on the controller")

# --- 2026-11-01: controller decisions on CG-18 and §7a; CG-19 progress (Economy keeper) ---
EXTRA_ROWS.append({"id": "kernel.transfer", "name": "Transfer service (one transfer per physical flow)", "engine": "kernel",
    "home": "Toolchain/kernel/src/transfer.ts (planned: kernel unit 3006-kernel-transfer-service; design §17 in 3008)", "status": "planned", "domain": "infra", "scope": "universal",
    "inputs": [], "outputs": [], "state": "TransferJournal entries per instant",
    "formulation": "transfer(source, destination, q) inside kernel.transaction: delta source = -q and delta destination = +q committed together; losses are ordinary transfers to a loss account in the same call; bookkeeping only: no formula, no knowledge of the quantity, no unit conversion (request and both ledgers in one unit); owners implement TransferLedger and decide their own refusals",
    "dependencies": ["kernel.transaction"], "timescale": "per call",
    "invariants": "PLATFORM §7a: per quantity per instant, debits equal credits; every engine's transfers (nutrients, water, mass, energy, money) go through it (controller 2026-11-01, recorded for Rex to overrule)",
    "sources": "bookkeeping identity", "evidence": 1, "approximations": "none (accounting)", "tests": "planned: test/transfer.test.ts (unit 3006)",
    "consumers": [], "notes": "controller decision 2026-11-01 (go): Economy and Settlement ledgers migrate in paired units after kernel v0.1.0; CHAINS CG-19/20/21 adopt it",
    "audit_batch": "controller-2026-11-01-transfer"})
EXTRA_QUANTITIES += [
 {"id": "economy.good_mass_per_unit", "kind": "quantity", "unit": "kg/count", "scope": "economy", "writer": "economy.recipe.definition",
  "description": "Good.weight: kg per unit of a good, owned once by the goods catalogue (CG-19)", "status": "planned (CG-19, Economy keeper 2026-11-01; unit 2999)"},
 {"id": "economy.mass_taken", "kind": "quantity", "unit": "kg", "scope": "economy", "writer": "economy.inventory.holdings",
  "description": "q of a mass transfer out of an inventory: units removed x good_mass_per_unit; the same q is added to the destination (a body through eat_meal, IF-36) in one transaction (CG-19, PLATFORM §7a)", "status": "planned (CG-19, Economy keeper 2026-11-01; unit 2999)"},
]
for _g in INTERFACE_GAPS:
    if _g["interface"] == "CG-19":
        _g["progress"] = ("Economy keeper 2026-11-01: unit 2999-economy-goods-mass-transfers (running). takeMass: delta inventory = -q, q = units x Good.weight (kg); "
            "eatMeal({food, kg: q}): delta body = +q in one kernel transaction; quantities economy.good_mass_per_unit (kg/count) and economy.mass_taken (kg) registered planned; "
            "energy: proposed amendment: goods carry no kcal, a good names its Life food id (Good.food) and Life's nutrition owns kcal per kg (Life to confirm); "
            "verification: economy test/mass.test.ts and goldens at 2999's commit, then Life's coupled test; adopts kernel.transfer (controller go)")
    if _g["interface"] == "CG-18":
        _g["progress"] = ("controller go 2026-11-01: registry/events.json (registry keeper owns; created empty) with type, producer, consumers, cause, payload schema; "
            "kernel 3007 adds checkEventContracts (warns until populated); the first unit is the event inventory")

# --- 2026-11-01: Life keeper's chain-gap decisions (Toolchain/life/DESIGN.md §2.4). CG-4 and CG-12 close with these registry edits; the rest are progress ---
_L2IN = ["place.par", "place.vpd", "place.rain", "world.soil_water", "world.soil_salinity", "world.water_depth", "world.water_kd",
         "world.water_salinity", "world.water_t", "world.inundation", "world.sediment_porewater_nutrients", "place.t", "air.ppm_gases"]
ROW_PATCHES.setdefault("realism.plant.physiology", {})["inputs"] = [{"name": x, "unit": "see quantities.json"} for x in _L2IN + ["world.soil", "world.soil_nutrient_pool", "world.soil_ph", "world.groundwater", "air.wind", "organism.genetic_profile"]]
EXTRA_QUANTITIES.append({"id": "organism.genetic_profile", "kind": "record", "unit": None, "scope": "organism", "writer": "realism.records.genetic_profile",
    "description": "record 1, kingdom-neutral: the organism's genome (chromosome segments with trait-associated variants), written once at conception or creation; read by maturation, phenotype and plant physiology (CG-12)",
    "status": "planned (CG-12, Life keeper 2026-11-01)"})
ROW_PATCHES.setdefault("realism.development.maturation", {})["inputs"] = [{"name": x, "unit": "see quantities.json"} for x in ["organism.genetic_profile", "realism.nutrition.pools", "world.signal_at_point", "body.crisis"]]
for _el, _d in [("water", "water"), ("n", "nitrogen"), ("p", "phosphorus"), ("k", "potassium")]:
    EXTRA_QUANTITIES.append({"id": "world.plant_uptake_" + _el, "kind": "quantity", "unit": "kg", "scope": "world", "writer": "realism.plant.physiology",
        "description": "plant uptake of " + _d + " per plant record per step, cell-scoped: one transfer, delta soil available = -q, delta plant = +q, one substrate transaction (PLATFORM §7a; CG-3); litter returns the same way",
        "status": "planned (CG-3, Life keeper 2026-11-01; built with unit {CG21} after realism 2815)"})
_LIFE_PROG = {
 "CG-4": "closed 2026-11-01 (registry edit): realism.plant.physiology inputs set to the eleven LIFE-2 ids + place.t + air.ppm_gases (Life keeper); verification: registry rebuild and belt check exit 0; 2815's env interface reads them",
 "CG-12": "closed 2026-11-01 (registry edit): organism.genetic_profile (record, scope organism, writer realism.records.genetic_profile) registered; maturation reads it; verification: registry rebuild and belt check exit 0",
}
for _g in INTERFACE_GAPS:
    _id = _g["interface"]
    if _id in _LIFE_PROG: _g["state"] = _LIFE_PROG[_id]
    elif _id == "CG-13": _g["progress"] = "Life keeper 2026-11-01: confirmed absorbed: kept = eaten x absorbedFraction('energy') to intake_kcal; eaten - kept is a traced food->waste transfer (J); no double count. Closes on unit {CG13}: realism test/nutrition.test.ts 'energy enters absorbed (CG-13)'. Unabsorbed energy has no quantity until CG-6"
    elif _id == "CG-21": _g["progress"] = "Life keeper 2026-11-01: world.plant_state is the only biomass store at every resolution; world.vegetation_stock becomes a derived read (sum over records in a region, never integrated); vegetation_stocks becomes the coarsen/refine interface (conserves to 1e-12, no transfer). Closes on unit {CG21} after 2815"
    elif _id == "CG-3": _g["progress"] = "Life keeper 2026-11-01: one transfer per element; world.plant_uptake_water/_n/_p/_k (kg) registered planned; harvest then removes nutrients from the plant only (Life's half of CG-20). Closes on unit {CG21} after 2815"
    elif _id == "CG-23": _g["progress"] = "Life keeper 2026-11-01: trophic_flux over a period = sum of kg eaten by individually resolved consumers + cohort consumption of population-resolved ones, never both for one consumer; E = m x e_food from Life's food table. Designed; built with phase 19"
    elif _id == "CG-19": _g["progress"] = _g.get("progress", "") + "; Life keeper 2026-11-01 confirms: goods carry no kcal, Life's food table owns kcal per kg; body-side test is unit {CG13}; the cross-engine test lives in the economy lane after 2999"
    elif _id == "CG-16": _g["progress"] = "Life keeper 2026-11-01: Life owns body.capacity_functional (DUP-15), designed with the human sections; lead Cognition"
    elif _id == "CG-20": _g["progress"] = "Life agrees 2026-11-01: soil loses nutrients only by uptake, leaching, runoff and erosion; the fertility drain becomes a read. Reality decides"
    elif _id == "CG-22": _g["progress"] = _g.get("progress", "") + "; Life 2026-11-01: immediate substrate transactions, not a pending sum"

# --- 2026-11-01: CG-19 wording amended (Economy and Life agreed); verification units 2999 + 3010 ---
for _g in INTERFACE_GAPS:
    if _g["interface"] == "CG-19":
        _g["progress"] = _g.get("progress", "") + "; amended 2026-11-01: goods carry mass (kg per unit, owned once by Economy) and name a Life food id; energy stays Life's (food.kcalPerKg, E = m x e_food); verification units 2999-economy-goods-mass-transfers and 3010-economy-coupled-food-to-body-test (one kernel transaction; Needs 2999)"

# --- 2026-11-01: CG-9 and CG-22 (Reality keeper; realism units 3000-3001 queued): N, P and K as separate per-cell quantities; one transfer per change ---
_CELL = "per soil cell (the cell record carries areaM2; kg/m^2 is a derived view)"
for _el, _nm in [("n", "nitrogen"), ("p", "phosphorus"), ("k", "potassium")]:
    EXTRA_QUANTITIES += [
     {"id": "world.soil_" + _el, "kind": "quantity", "unit": "kg", "scope": "world", "writer": "realism.terrain.soils",
      "description": "soil " + _nm + " pool, " + _CELL + "; changes only by transfer (transferNutrient / addNutrient, PLATFORM §7a); losses go to loss:<pathway> accounts (CG-9)",
      "status": "planned (CG-9, Reality keeper 2026-11-01; realism unit 3001)"},
     {"id": "world.mineralisation_flux_" + _el, "kind": "quantity", "unit": "kg/d", "scope": "world", "writer": "realism.ecology.decomposition",
      "description": _nm + " returned from detritus to the soil pool, " + _CELL + " (CG-9)", "status": "planned (CG-9, Reality keeper 2026-11-01)"},
     {"id": "world.nutrient_flux_" + _el, "kind": "quantity", "unit": "kg/d", "scope": "world", "writer": "realism.terrain.nutrient_transport",
      "description": _nm + " moved by runoff, leaching, erosion and deposition, " + _CELL + " (CG-9)", "status": "planned (CG-9, Reality keeper 2026-11-01)"},
    ]
_why9 = "split into separate N, P and K quantities per soil cell (CG-9, Reality keeper 2026-11-01; CHAINS.md priority 1)"
QUANTITY_OPS += [
 ("retire", "world.soil_nutrient_pool", ["world.soil_n", "world.soil_p", "world.soil_k"], _why9, "2026-11-01"),
 ("retire", "world.mineralisation_flux", ["world.mineralisation_flux_n", "world.mineralisation_flux_p", "world.mineralisation_flux_k"], _why9, "2026-11-01"),
 ("retire", "world.nutrient_flux", ["world.nutrient_flux_n", "world.nutrient_flux_p", "world.nutrient_flux_k"], _why9, "2026-11-01"),
]
_q = lambda xs: [{"name": x, "unit": "see quantities.json"} for x in xs]
_NPK = lambda p: [p + e for e in ("n", "p", "k")]
_TS = "pools change per transfer at the flux's step; formation once per world; pedogenesis per year (CG-22, Reality keeper 2026-11-01; realism gears/soil-integration.md, unit 3001)"
ROW_PATCHES.setdefault("realism.terrain.soils", {}).update({"timescale": _TS,
    "outputs": [{"name": "world.soil", "unit": "record"}, {"name": "world.soil_ph", "unit": "1"}] + [{"name": x, "unit": "kg"} for x in _NPK("world.soil_")],
    "planned_writes": ["world.soil", "world.soil_ph"] + _NPK("world.soil_")})
ROW_PATCHES.setdefault("realism.terrain.hydrology", {})["timescale"] = _TS
ROW_PATCHES.setdefault("realism.terrain.nutrient_transport", {}).update({"inputs": _q(["world.sediment_flux", "world.drainage"] + _NPK("world.soil_")),
    "outputs": [{"name": x, "unit": "kg/d"} for x in _NPK("world.nutrient_flux_")]})
ROW_PATCHES.setdefault("realism.ecology.decomposition", {})["outputs"] = [{"name": "world.detritus", "unit": "kg"}] + [{"name": x, "unit": "kg/d"} for x in _NPK("world.mineralisation_flux_")]
ROW_PATCHES["realism.plant.physiology"]["inputs"] = [i for i in ROW_PATCHES["realism.plant.physiology"]["inputs"] if i["name"] != "world.soil_nutrient_pool"] + _q(_NPK("world.soil_"))
QUANTITY_PATCH.setdefault("stock.f", {})["description"] = ("soil fertility index f (0-1): from realism unit 3001 a derived Liebig view of world.soil_n, world.soil_p and world.soil_k "
    "(level 4, gears doc), still written by realism.eco.soil_fertility as a view, never a second drain (CG-20)")
for _g in INTERFACE_GAPS:
    if _g["interface"] in ("CG-9", "CG-20", "CG-22"):
        _g["progress"] = _g.get("progress", "") + ("; Reality keeper 2026-11-01: realism units 3000 (sourced removal and manure N, P, K) and 3001 (src/soils.ts: SoilCell kg N, P, K with areaM2; "
            "transferNutrient the only decrease, pool -q / account +q, one trace record; losses to loss:<pathway>; no clamp; harvest one transfer of yield x removal, nothing from soil when uptakeByPlant; "
            "f a derived Liebig index; gears/soil-integration.md; tests 'one transfer', 'no clamp', 'integration rule' (daily vs hourly 1e-9), 'uptake once'); registry ids split 2026-11-01")

# --- 2026-11-01: Economy keeper's precision on the §7a migration (Economy owns the goods stock ledger; money is Settlement's ledger, CONTRACTS §3) ---
for _r in EXTRA_ROWS:
    if _r["id"] == "kernel.transfer":
        _r["notes"] = ("controller decision 2026-11-01 (go); after kernel v0.1.0 the ledgers migrate in paired units: Economy's goods stock ledger (adjust, economy.stock_changes; takeMass/addMass first) "
                       "and Settlement's money ledger (CONTRACTS §3; Economy has no money ledger); CHAINS CG-19/20/21 adopt it")

# --- 2026-11-01: Reality accepted the CG-22 rule (no buffer); 3001 needs kernel 3006 and uses transfer(); Life's chain units queued as realism 3014-3019 (3015 = CG-21 + CG-3) ---
for _g in INTERFACE_GAPS:
    if _g["interface"] == "CG-22": _g["progress"] += "; Reality accepted 2026-11-01 as worded, no buffer; realism 3001 needs kernel 3006 and uses transfer() for every soil transfer; tests 'integration rule (3001)', 'one transfer (3001)'"
    if _g["interface"] in ("CG-21", "CG-3"): _g["progress"] += "; queued as realism 3015 (needs 2815 and 3001)"

# --- 2026-11-01: CG-9 ports unit queued (Reality): realism 3021 (needs 3001), process realism.ecology.soils (terrain.soils + eco.soil_fertility) writes world.soil_{n,p,k} and stock.f; no existing process writes stock.f (checked realism kernel.json at HEAD) ---
for _g in INTERFACE_GAPS:
    if _g["interface"] == "CG-9": _g["progress"] += "; ports: realism 3021 (needs 3001), process realism.ecology.soils, gate check-registry on realism/kernel.json"

# --- 2026-11-01: CG-16 contract id accepted (Cognition keeper, lead): shared.action.resolution, registry-owned like shared.contract.labour_supply ---
EXTRA_ROWS.append({"id": "shared.action.resolution", "name": "Action resolution (shared contract)", "engine": "shared",
    "home": "Toolchain/cognition/DESIGN.md §2.4 (proposed by the Cognition keeper 2026-11-01 as CG-16 lead; success equations stay with the owning engines)",
    "status": "planned", "domain": "infra", "scope": "universal", "inputs": [], "outputs": [], "state": "none (a contract)",
    "formulation": "resolve(intention, truth) -> { status: completed | failed | impossible, stimuli, transfers }, implemented by the engine owning the action kind in shared.action.kind; one kernel.transaction per intention containing its kernel.transfer calls and the outcome event; the outcome event's cause is the intention event id",
    "dependencies": ["shared.action.kind", "kernel.transaction", "kernel.transfer"], "timescale": "per intention",
    "invariants": "Cognition decides only whether someone attempts an act; success is decided by Reality and Life (IF-43, CG-16), Economy (IF-26), Settlement and Economy (IF-27); outcome events are the resolving engine's own types with cause; no cognition.outcome event type; owned by no engine",
    "sources": "contract", "evidence": None, "approximations": "planned", "tests": "none",
    "consumers": ["cognition.learning.outcome"], "notes": "CG-16 (CHAINS.md priority 2); proposals with Reality, Life, Economy and Settlement", "audit_batch": "cognition-keeper-2026-11-01-cg16"})
for _g in INTERFACE_GAPS:
    if _g["interface"] in ("CG-16", "IF-26", "IF-27"):
        _g["progress"] = _g.get("progress", "") + "; Cognition keeper 2026-11-01: contract shared.action.resolution registered planned; proposals with Reality, Life, Economy, Settlement"
    if _g["interface"] == "CG-18":
        _g["progress"] += ("; Cognition keeper 2026-11-01: cognition.intention payload {id, mind, action, target?, t, expectedOutcomes: Categorical, status} (built, cognition 2106314), "
                           "producer cognition.decision.select, consumers the resolvers; proposed terms?: Record<string, number>; enters events.json with the 3011 inventory")

# --- 2026-11-01: CG-16 contract agreed by Reality, Life and Economy (Settlement's IF-27 answer pending); text in cognition DESIGN §2.4 via cognition 3043 ---
for _r in EXTRA_ROWS:
    if _r["id"] == "shared.action.resolution":
        _r["notes"] = ("CG-16 (CHAINS.md priority 2); agreed by Reality, Life and Economy 2026-11-01, Settlement's IF-27 answer pending. Implemented per action kind: Reality move/gather (after realism 3020); "
                       "Life eat and body.capacity_functional (after kernel 3006 + economy 2999); Economy buy/sell/consume (after cognition 3044); Settlement + Economy work; Society IF-46; Government IF-43. "
                       "Outcome event shared.action.outcome {cause: intention event id, status, stimuli, payload?} (CG-18), consumer cognition.learning.outcome via the host outcome command; "
                       "open: C-Q25 (refusal = failed? Rex), C-Q26 (who excludes simulated minds from the headcount, CG-23 never-both; controller)")
for _g in INTERFACE_GAPS:
    if _g["interface"] in ("CG-16", "IF-26"): _g["progress"] += "; agreed by Reality, Life, Economy 2026-11-01 (cognition DESIGN §2.4, unit 3043)"
    if _g["interface"] == "IF-27": _g["progress"] += "; Settlement's answer pending"
    if _g["interface"] == "CG-18": _g["progress"] += "; proposed event shared.action.outcome {cause, status, stimuli, payload?} (producer: the resolver), consumer cognition.learning.outcome; cognition.intention gains terms? (cognition 3044)"
    if _g["interface"] == "CG-23": _g["progress"] += "; open C-Q26 (controller): who excludes simulated minds from the population headcount"

# --- 2026-11-01: re-audit of kernel 3006 (a7459c8): src/transfer.ts; test/transfer.test.ts rerun by the registry keeper 20/20. kernel.transfer planned -> built ---
for _r in EXTRA_ROWS:
    if _r["id"] == "kernel.transfer":
        _r.update({"status": "built", "home": "Toolchain/kernel/src/transfer.ts (transfer, TransferLedger, TransferJournal; kernel a7459c8, unit 3006)",
                   "tests": "Toolchain/kernel test/transfer.test.ts (registry keeper rerun at kernel a7459c8, 20/20)"})
ROW_PATCHES.setdefault("kernel.transfer", {}).update({"rate_limiter": "none (synchronous call inside kernel.transaction)",
    "failure_mode": "a ledger refusal or unit mismatch throws inside the transaction, which restores every participant"})
VV_OVERRIDES["kernel.transfer"] = {"validated": "n/a (accounting identity)", "integrated": "no (no engine ledger migrated yet: realism 3001, economy, settlement follow)",
                                   "evidence": "re-audit 2026-11-01 at kernel a7459c8: transfer.test.ts 20/20"}
for _g in INTERFACE_GAPS:
    if _g["interface"] == "CG-18":
        _g["progress"] += "; registry/events.json populated 2026-11-01 with shared.action.outcome and settlement.post_filled (IF-27, Settlement keeper)"
    if _g["interface"] == "IF-27":
        _g["progress"] += "; agreed by Cognition, Economy, Settlement 2026-11-01; hire takes cause? and emits shared.action.outcome + settlement.post_filled (Settlement's next unit); CONTRACTS §19 optional reservationWage (economy da42670, settlement 87ff281)"

# --- 2026-11-01: IF-27 unit queued: settlement 3047 (hire.cause, postFilled, shared.action.outcome; test U24) ---
for _g in INTERFACE_GAPS:
    if _g["interface"] == "IF-27": _g["progress"] += "; settlement 3047 queued (Codex: hire.cause, postFilled, shared.action.outcome; test U24); money-ledger migration onto kernel.transfer after kernel v0.1.0"

# --- 2026-11-01: kernel 3007 (c171702) and 3008 (e1a35bb) landed; check-registry now reads registry/events.json: one warning (shared.action.outcome stimuli list has no 'of', documented); 3011 requeued on codex ---
for _g in INTERFACE_GAPS:
    if _g["interface"] == "CG-18":
        _g["progress"] += ("; kernel 3007 (c171702): checkEventContracts + opt-in EventBus hook, advisory; registry keeper ran the belt check with events.json: exit 0, one warning "
                           "(shared.action.outcome stimuli list has no 'of'; element schema open); kernel test suite 205/205; DESIGN §17 (e1a35bb); inventory 3011 requeued on codex")

# --- 2026-11-01: Cognition re-audit pointers: DESIGN §2.4 at cognition 1e229d1 (3043) and d6abcdc (3046); intention payload gains terms? at f53f16d (3044); C-Q25 decided (refusal = failed, controller); C-Q26 = Life ---
for _r in EXTRA_ROWS:
    if _r["id"] == "shared.action.resolution":
        _r["home"] = "Toolchain/cognition/DESIGN.md §2.4 (cognition 1e229d1, unit 3043; d6abcdc, unit 3046); success equations stay with the owning engines"
        _r["notes"] = _r["notes"].replace("open: C-Q25 (refusal = failed? Rex), C-Q26 (who excludes simulated minds from the headcount, CG-23 never-both; controller)",
                                          "C-Q25 decided by the controller (a refusal is failed, the reason among the stimuli); C-Q26 (headcount, CG-23) assigned to Life")
for _g in INTERFACE_GAPS:
    if _g["interface"] == "CG-18": _g["progress"] += "; cognition.intention payload now {id, mind, action, target?, t, expectedOutcomes, status, terms?} (cognition f53f16d, unit 3044)"
    if _g["interface"] == "CG-23": _g["progress"] += "; C-Q26 assigned to Life (controller)"

# --- 2026-11-01: re-audit of settlement 3047 (7e49d3c): U24 6/6 (registry keeper rerun). Settlement's resolver part of IF-27 verified; IF-27 stays open until an intention reaches it through the host (Cognition lead) ---
for _g in INTERFACE_GAPS:
    if _g["interface"] == "IF-27":
        _g["progress"] += ("; settlement 3047 landed 7e49d3c: hire takes cause?, emits settlement.post_filled then shared.action.outcome (completed, cause, wage) in one command; "
                           "unknown post throws with no event or state change; replay identical; test/engine.test.ts U24 6/6 (registry keeper rerun). Settlement's resolver part verified; "
                           "closes when an intention reaches hire through the host with a targeted test (Cognition lead)")

# --- 2026-11-01: IF-27 evidence (Cognition keeper): intention terms? at cognition f53f16d (unit 3044, test/intention-terms.test.ts 4/4, registry keeper rerun) ---
for _g in INTERFACE_GAPS:
    if _g["interface"] == "IF-27":
        _g["progress"] += ("; cognition 3044 f53f16d: intention terms? (test/intention-terms.test.ts 4/4, registry keeper rerun). Still missing: the LabourSupply provider that reads the latest "
                           "work/refuse_work intention and answers hours(person, role, day) with the intention event id as cause (owner not yet named: Reality's population provider or the host); "
                           "Economy's wage-quote floor (their wage rule, open for Rex). Units: person-hours per day (h); wage money per filled post-day")

# --- 2026-11-01: settlement.wage.pay rate_limiter (Settlement keeper's wording; code at settlement src/tick/wages.ts, ae07c4c, unchanged since). failure_mode left null: whether an account may go negative is open (Rex and Economy) ---
ROW_PATCHES.setdefault("settlement.wage.pay", {})["rate_limiter"] = (
    "once per tick (step 5 of 7), each filled post with wage > 0 pays its holder exactly post.wage from the business's account (the treasury for a public-works business): "
    "one ledger row and one wagePaid per post per day, so the daily outflow is the sum of wages over filled posts; pay checks no balance, so the payer's funds do not limit the rate "
    "(a statement of the current code, not a rule; settlement src/tick/wages.ts, ae07c4c)")

# --- 2026-11-01: IF-27 remaining pieces. Controller: the LabourSupply provider is Life's (population and labour supply sit on Life's side of SPLIT.md; Life owns C-Q26; a host-written provider would be a second labour authority).
# Settlement and Cognition point of fact: the provider answers pure queries (hours(person, role, day) §16/§17, reservationWage? §19), changes nothing and passes no cause;
# the cause reaches Settlement through the host's hire command {type: 'hire', post, holder, cause} via Settlement's apply. Population rows realism.population.* are already engine life ---
for _r in EXTRA_ROWS:
    pass
ROW_PATCHES.setdefault("shared.contract.labour_supply_provider", {})["notes"] = (
    "provider owner: Life (controller 2026-11-01, IF-27): the individual half of the one population count (C-Q26) feeding LabourSupply; reads each person's latest work/refuse_work intention; "
    "pure queries hours(person, role, day) (CONTRACTS §16/§17) and reservationWage? (§19); changes nothing, passes no cause; waits on kernel 3006 and the §19 ids")
for _g in INTERFACE_GAPS:
    if _g["interface"] == "IF-27":
        _g["progress"] += ("; remaining pieces (2026-11-01): (1) the LabourSupply provider, owner Life (controller): pure queries hours(person, role, day) and reservationWage?, no cause; "
                           "(2) the host's hire command {type: 'hire', post, holder, cause: intention event id} through Settlement's apply, owner the host adapter. Economy's wage-quote floor stays with Rex (ECON-24)")
        _g["owner_remaining"] = ["life (LabourSupply provider)", "host adapter (hire command with cause)"]

# --- 2026-11-01: controller: the host of IF-27's hire step is the kernel harness (code: Kernel keeper; specification: History keeper, as part of X1); in a game the game adapter plays the same role ---
EXTRA_ROWS.append({"id": "shared.host.work_resolution", "name": "Host role: resolving work intentions (shared contract)", "engine": "shared",
    "home": "contract (controller 2026-11-01); implemented in Toolchain/kernel/harness/ (Kernel keeper, after kernel v0.1.0), specified by the History keeper as part of X1; in a game the game adapter plays the same role",
    "status": "planned", "domain": "infra", "scope": "universal", "inputs": [], "outputs": [], "state": "none (a host role)",
    "formulation": "the host resolves a work intention by reading Life's LabourSupply provider answers (hours(person, role, day), reservationWage?) and issuing one {type: 'hire', post, holder, cause: intention event id} through Settlement's apply per accepted intention, inside one kernel.transaction",
    "dependencies": ["shared.action.resolution", "shared.contract.labour_supply_provider", "settlement.assign.workforce", "kernel.transaction"], "timescale": "per work intention",
    "invariants": "a host role, never a mechanism: no engine grows a staffing rule; the host never decides the wage (Economy's rule, ECON-24, Rex); one hire per accepted intention; cause = the intention event id",
    "sources": "contract", "evidence": None, "approximations": "planned", "tests": "none",
    "consumers": ["settlement.assign.workforce"], "notes": "IF-27 (CHAINS.md priority 2); the work resolver of the CG-16 contract for demonstration runs", "audit_batch": "controller-2026-11-01-if27-host"})
for _g in INTERFACE_GAPS:
    if _g["interface"] == "IF-27":
        _g["owner_remaining"] = ["life (LabourSupply provider)", "kernel harness (shared.host.work_resolution; Kernel keeper code after v0.1.0, History keeper specification in X1)"]
        _g["progress"] += "; controller 2026-11-01: the hire step is the kernel harness's (contract row shared.host.work_resolution); the game adapter plays the same role in a game"

# --- 2026-11-01: Kernel keeper: shared.host.work_resolution unit drafted after History's X1 spec defines an "accepted" work intention (hours > 0? available()? reservation wage vs posted wage?); Needs 2823 ---
for _r in EXTRA_ROWS:
    if _r["id"] == "shared.host.work_resolution":
        _r["notes"] += "; open (History keeper, X1 spec): what makes a work intention accepted (hours > 0, available(), or reservation wage vs posted wage); the kernel unit (Needs 2823) waits on it; the harness already reaches Settlement's apply and LabourSupply (settlement src/providers.ts)"

# --- 2026-11-01: History keeper: host work resolution specified in Toolchain/history DESIGN.md §3.8 (history 0c53036), carried by X1 seams S6 and S7; S6 Gate H1-H4.
# §3.8 does not define an accepted work intention or the host's phase (defers to the contract and kernel order.json); the Kernel keeper also waits on that: open, escalated to the controller ---
for _r in EXTRA_ROWS:
    if _r["id"] == "shared.host.work_resolution":
        _r["home"] += "; specification: Toolchain/history DESIGN.md §3.8 (history 0c53036), X1 seams S6 and S7"
        _r["tests"] = ("planned: X1 seam S6 Gate H1 (every post_filled traces through a hire to an accepted work intention; one hire per accepted intention), "
                       "H2 (a rejected hire leaves no partial state), H3 (the host writes no wage field), H4 (G-inert holds)")
        _r["notes"] += "; History §3.8 defers 'accepted' and the host's phase to the contract and kernel order.json, and the Kernel keeper defers it to History: escalated to the controller 2026-11-01"

# --- 2026-11-01: controller's ruling on an accepted work intention (recorded for Rex to overrule); owner: this host contract row, as a declared default (dispatch, not an engine formula) ---
for _r in EXTRA_ROWS:
    if _r["id"] == "shared.host.work_resolution":
        _r["formulation"] += ("; ACCEPTED (controller 2026-11-01, declared default, for Rex to overrule): a work intention is accepted when Life's provider answers hours(person, role, day) > 0 for the day "
            "(this already encodes availability; no separate available() test) AND a vacant post of the role named in the intention's terms exists in Settlement. Post mapping: the first vacant post of that role "
            "by stable id (deterministic under replay). No role in terms: not accepted (status failed, reason 'no role'). Wage: until Rex decides ECON-24 the host applies NO wage comparison "
            "(reservation wage vs posted wage is not tested), exactly as Economy applies no floor today. Not accepted resolves to shared.action.outcome status failed with the reason among the stimuli (C-Q25), so the mind learns")
        _r["notes"] = _r["notes"].replace("; History §3.8 defers 'accepted' and the host's phase to the contract and kernel order.json, and the Kernel keeper defers it to History: escalated to the controller 2026-11-01",
            "; 'accepted' ruled by the controller 2026-11-01 (see formulation); the host's phase follows kernel order.json")

# --- 2026-11-01: cognition.intention added to registry/events.json (fields from cognition src/types.ts at HEAD). Conflict found: the controller's 'accepted' ruling names the role in the intention's terms,
# but terms are numbers only (Readonly<Record<string, number>>); escalated to the controller ---
for _r in EXTRA_ROWS:
    if _r["id"] == "shared.host.work_resolution":
        _r["notes"] += "; OPEN 2026-11-01 (escalated): the ruling reads the role from the intention's terms, but terms are numbers only (cognition src/types.ts), so a role name cannot be a term; where the role comes from (target, a numeric role id, or a terms type change) is the controller's call"
for _g in INTERFACE_GAPS:
    if _g["interface"] == "CG-18": _g["progress"] += "; cognition.intention row added to events.json 2026-11-01 (expectedOutcomes and terms untyped: no map kind)"
    if _g["interface"] == "IF-27": _g["progress"] += "; Life's provider drafted (HQ/handoffs/life/drafts/life-20-labour-supply-from-intentions.md, LIFE-16): hours = terms.hours, reservationWage = terms.wage_min, reads cognition.intention from the EventBus, pure"

# --- 2026-11-01: History DESIGN §3.8 cites the contract and checks the ruling in H1 (history e1ff6ea); History also flags the role-in-terms conflict (already escalated) ---
for _r in EXTRA_ROWS:
    if _r["id"] == "shared.host.work_resolution":
        _r["home"] = _r["home"].replace("(history 0c53036)", "(history 0c53036; e1ff6ea cites this contract, H1 checks the accepted rule)")

# --- 2026-11-01: host work resolution queued as kernel 5006 (codex, after v0.1.0 / 2823), test harness/work-resolution.test.ts, built to history DESIGN §3.8 (037b87e) ---
for _r in EXTRA_ROWS:
    if _r["id"] == "shared.host.work_resolution":
        _r["tests"] = "planned: Toolchain/kernel harness/work-resolution.test.ts (kernel 5006, after v0.1.0 / 2823); X1 seam S6 Gate H1-H4 (history DESIGN §3.8)"

# --- 2026-11-01: controller's role ruling, option (a): the role or post travels in the intention's target; terms stay numbers only; no Cognition type change ---
for _r in EXTRA_ROWS:
    if _r["id"] == "shared.host.work_resolution":
        _r["formulation"] = _r["formulation"].replace(
            "AND a vacant post of the role named in the intention's terms exists in Settlement. Post mapping: the first vacant post of that role by stable id (deterministic under replay). No role in terms: not accepted (status failed, reason 'no role').",
            "AND a vacant post exists for the intention's target. ROLE SOURCE (controller 2026-11-01, option a): for a work intention, target = a Settlement role id or post id the mind knows through perception (its affordances, IF-46); "
            "a role id resolves to the first vacant post of that role by stable id (deterministic under replay), a post id directly; no target: not accepted (status failed, reason 'no target'); "
            "terms stay numbers only (cognition src/types.ts), no Cognition type change. Vacancy is acceptance until Society's organisations.")
        _r["notes"] = _r["notes"].replace("; OPEN 2026-11-01 (escalated): the ruling reads the role from the intention's terms, but terms are numbers only (cognition src/types.ts), so a role name cannot be a term; where the role comes from (target, a numeric role id, or a terms type change) is the controller's call",
                                          "; role source ruled 2026-11-01 (controller, option a): the intention's target")
        assert "option a" in _r["formulation"] and "option a" in _r["notes"]

# --- 2026-11-01: conflict: Cognition queued 5007/5008 adding role?: string to Candidate/Intention ('no role' failure), citing a controller amendment; the controller's ruling to the registry is option (a), target, no type change. Escalated; Cognition asked to hold ---
for _r in EXTRA_ROWS:
    if _r["id"] == "shared.host.work_resolution":
        _r["notes"] += "; OPEN 2026-11-01: Cognition queued 5007/5008 (role?: string on Intention) against ruling (a); controller asked which stands; Life's provider is unaffected (the host supplies roleOf(intention))"

# --- 2026-11-01: role source settled: controller confirms (a) stands (record: rs-platform 36ed07e); Cognition withdrew 5007/5008's type change (one-line DESIGN §2.4 note on the target convention instead); kernel 5006 and Life's roleOf(intention) read target ---
for _r in EXTRA_ROWS:
    if _r["id"] == "shared.host.work_resolution":
        _r["notes"] = _r["notes"].replace("; OPEN 2026-11-01: Cognition queued 5007/5008 (role?: string on Intention) against ruling (a); controller asked which stands; Life's provider is unaffected (the host supplies roleOf(intention))",
            "; (a) confirmed by the controller 2026-11-01: Cognition's role? type change withdrawn (a DESIGN §2.4 note on the target convention instead); kernel 5006 and Life's roleOf(intention) read target; the failure reason is 'no target'")
        assert "(a) confirmed" in _r["notes"]

# --- 2026-11-01: History DESIGN §3.8 at ab3274a: target carries the role, fixture interim dropped, reason 'no target' (registry keeper checked: 'no role' absent, 'no target' x2) ---
for _r in EXTRA_ROWS:
    if _r["id"] == "shared.host.work_resolution":
        _r["home"] = _r["home"].replace("e1ff6ea cites this contract, H1 checks the accepted rule)", "e1ff6ea cites this contract, H1 checks the accepted rule; ab3274a: target carries the role, reason 'no target')")

# --- 2026-11-01: CG-19 closed. Re-audit by the registry keeper at economy 4192e27 (contains da23966 2999, 2fef178 3010, 4192e27 3045):
# test/mass.test.ts M1-M9, test/food-to-body.test.ts F1-F5, test/intention.test.ts: 28/28. Ports (recipe.definition writes good_mass_per_unit,
# inventory.holdings writes mass_taken) are Composer unit 5049 (Economy keeper) ---
for _q in EXTRA_QUANTITIES:
    if _q["id"] in ("economy.good_mass_per_unit", "economy.mass_taken"):
        _q["status"] = "built (economy da23966, unit 2999; CG-19 re-audit 2026-11-01 at 4192e27, 28/28); port declaration pending economy 5049"
for _g in INTERFACE_GAPS:
    if _g["interface"] == "CG-19":
        _g.update({"state": "closed 2026-11-01: goods carry kg (Good.weight) and a Life food id; takeMass then eatMeal in one kernel transaction, "
                            "mass delta -q/+q exact, rollback of both engines on failure; re-audit at economy 4192e27: mass 9/9 + food-to-body 5/5 + intention, 28/28"})
