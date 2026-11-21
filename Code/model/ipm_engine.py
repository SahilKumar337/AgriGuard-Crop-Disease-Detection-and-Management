"""
Integrated Pest Management (IPM) & Diagnostic Knowledge Engine
Course: CSE471 | AgriGuard Platform
"""

from typing import Dict, Any, Optional

DISEASE_KNOWLEDGE_BASE = {
    "Tomato_Early_Blight": {
        "crop": "Tomato",
        "disease_name": "Early Blight",
        "scientific_name": "Alternaria solani",
        "pathogen_class": "Fungal",
        "description": "Fungal disease causing brown circular spots with characteristic concentric target rings, surrounded by yellow chlorotic halo. Originates on older foliage.",
        "early_symptoms": "Pinpoint dark brown spots with concentric ring pattern on lower leaves.",
        "weather_risk_profile": {
            "optimal_temp_range": (24, 29),
            "humidity_threshold": 80.0
        },
        "stage_treatments": {
            "Stage 1 (Early < 15%)": {
                "severity_label": "Early Infection",
                "organic_biocontrol": "Apply Trichoderma viride (2.5 kg/ha) foliar spray combined with cold-pressed Neem oil (1500 ppm at 3 ml/L). Remove lower infected leaflets.",
                "chemical_control": "Preventive spray with Chlorothalonil 75% WP at 600 g/acre in 200 L water.",
                "active_ingredient": "Chlorothalonil",
                "dosage": "3 g/L of water",
                "phi_days": 7,
                "cultural_practice": "Apply straw mulch to prevent soil-to-leaf rain splash; ensure drip irrigation to keep canopy dry."
            },
            "Stage 2 (Moderate 15-40%)": {
                "severity_label": "Moderate Infection",
                "organic_biocontrol": "Bacillus amyloliquefaciens bio-formulation combined with copper soap.",
                "chemical_control": "Mancozeb 75% WP (800 g/acre) or Azoxystrobin 18.2% + Difenoconazole 11.4% SC (200 ml/acre).",
                "active_ingredient": "Azoxystrobin + Difenoconazole",
                "dosage": "1 ml/L of water",
                "phi_days": 10,
                "cultural_practice": "Prune lower 30 cm canopy foliage to maximize airflow; dispose of infected clippings away from field."
            },
            "Stage 3 (Severe > 40%)": {
                "severity_label": "Severe Infection",
                "organic_biocontrol": "Bio-control alone is insufficient at severe stage; integrate with urgent curative measures.",
                "chemical_control": "Curative systemic treatment: Tebuconazole 25.9% EC (250 ml/acre in 200 L water) or Pyraclostrobin 20% WG.",
                "active_ingredient": "Tebuconazole",
                "dosage": "1.25 ml/L of water",
                "phi_days": 14,
                "cultural_practice": "Quarantine severely diseased rows; immediately burn infected haulms post-harvest; rotate with maize or beans for 3 seasons."
            }
        }
    },
    "Tomato_Late_Blight": {
        "crop": "Tomato",
        "disease_name": "Late Blight",
        "scientific_name": "Phytophthora infestans",
        "pathogen_class": "Oomycete",
        "description": "Devastating water-mold infection causing water-soaked purplish-black lesions with white sporulation on leaf undersides during cool, humid conditions.",
        "early_symptoms": "Irregular pale green to brown water-soaked lesions near leaf tips and margins.",
        "weather_risk_profile": {
            "optimal_temp_range": (15, 22),
            "humidity_threshold": 88.0
        },
        "stage_treatments": {
            "Stage 1 (Early < 15%)": {
                "severity_label": "Early Warning",
                "organic_biocontrol": "Bordeaux Mixture (1% concentration) or Copper Hydroxide 53.8% DF.",
                "chemical_control": "Cymoxanil 8% + Mancozeb 64% WP at 1000 g/acre in 200 L water.",
                "active_ingredient": "Cymoxanil-Mancozeb",
                "dosage": "5 g/L of water",
                "phi_days": 10,
                "cultural_practice": "Eradicate cull piles and volunteer tomato/potato shoots; stop all overhead sprinkler irrigation."
            },
            "Stage 2 (Moderate 15-40%)": {
                "severity_label": "Moderate Outbreak",
                "organic_biocontrol": "Copper octanoate spray coupled with systemic induced resistance elicitors (chitosan).",
                "chemical_control": "Metalaxyl-M 4% + Mancozeb 64% WP (1200 g/acre) or Dimethomorph 50% WP (400 g/acre).",
                "active_ingredient": "Metalaxyl-M + Mancozeb",
                "dosage": "2.5 g/L of water",
                "phi_days": 14,
                "cultural_practice": "Improve field drainage; avoid planting solanaceous crops downwind from infected fields."
            },
            "Stage 3 (Severe > 40%)": {
                "severity_label": "Critical Epidemic",
                "organic_biocontrol": "Critical stage: Chemical intervention mandatory to preserve remaining yield.",
                "chemical_control": "Fluopicolide 4.44% + Fosetyl-Al 66.67% WG (1000 g/acre in 250 L water).",
                "active_ingredient": "Fluopicolide + Fosetyl-Al",
                "dosage": "4 g/L of water",
                "phi_days": 14,
                "cultural_practice": "Destructive sanitation of heavily blighted plots to stop airborne sporangia dispersal."
            }
        }
    },
    "Potato_Early_Blight": {
        "crop": "Potato",
        "disease_name": "Early Blight",
        "scientific_name": "Alternaria solani",
        "pathogen_class": "Fungal",
        "description": "Foliar pathogen producing target-board lesions, leading to premature leaf defoliation and tuber quality loss.",
        "early_symptoms": "Dark angular spots restricted by leaf veins on senescing bottom leaves.",
        "weather_risk_profile": {
            "optimal_temp_range": (22, 28),
            "humidity_threshold": 75.0
        },
        "stage_treatments": {
            "Stage 1 (Early < 15%)": {
                "severity_label": "Early Stage",
                "organic_biocontrol": "Pseudomonas fluorescens bio-agent (1 kg/acre) + Potassium silicate foliar spray.",
                "chemical_control": "Mancozeb 75% WP at 800 g/acre in 200 L water.",
                "active_ingredient": "Mancozeb",
                "dosage": "4 g/L of water",
                "phi_days": 14,
                "cultural_practice": "Maintain optimal nitrogen-potassium balance; avoid plant drought stress."
            },
            "Stage 2 (Moderate 15-40%)": {
                "severity_label": "Moderate Stage",
                "organic_biocontrol": "Bacillus subtilis + bio-sulfur wettable powder.",
                "chemical_control": "Difenoconazole 25% EC (150 ml/acre) or Metiram 70% WG (1000 g/acre).",
                "active_ingredient": "Difenoconazole",
                "dosage": "0.75 ml/L of water",
                "phi_days": 14,
                "cultural_practice": "Kill potato vines 10 to 14 days before harvest to thicken tuber skins and avoid spore wash-down."
            },
            "Stage 3 (Severe > 40%)": {
                "severity_label": "Severe Stage",
                "organic_biocontrol": "Emergency curative chemical management required.",
                "chemical_control": "Boscalid 25.2% + Pyraclostrobin 12.8% WG at 250 g/acre.",
                "active_ingredient": "Boscalid-Pyraclostrobin",
                "dosage": "1.25 g/L of water",
                "phi_days": 21,
                "cultural_practice": "Disinfect harvesting machinery; discard any skin-blemished tubers before cold storage."
            }
        }
    },
    "Potato_Late_Blight": {
        "crop": "Potato",
        "disease_name": "Late Blight",
        "scientific_name": "Phytophthora infestans",
        "pathogen_class": "Oomycete",
        "description": "The causal agent of the Irish Potato Famine; causes rapid leaf destruction and dry tuber rot.",
        "early_symptoms": "Water-soaked lesions on leaf tips, rapidly wilting into purplish blotches.",
        "weather_risk_profile": {
            "optimal_temp_range": (14, 20),
            "humidity_threshold": 90.0
        },
        "stage_treatments": {
            "Stage 1 (Early < 15%)": {
                "severity_label": "Early Alert",
                "organic_biocontrol": "Preventive Bordeaux mixture (1:1:100) or Copper oxychloride 50% WP.",
                "chemical_control": "Cymoxanil 8% + Mancozeb 64% WP at 1200 g/acre.",
                "active_ingredient": "Cymoxanil-Mancozeb",
                "dosage": "5 g/L of water",
                "phi_days": 10,
                "cultural_practice": "Hill up soil ridges generously to form a physical barrier preventing zoospore wash into tubers."
            },
            "Stage 2 (Moderate 15-40%)": {
                "severity_label": "Active Epidemic",
                "organic_biocontrol": "Phosphorous acid bio-stimulant foliar spray to activate systemic acquired resistance (SAR).",
                "chemical_control": "Mandipropamid 23.4% SC (200 ml/acre) or Metalaxyl 8% + Mancozeb 64% WP.",
                "active_ingredient": "Mandipropamid",
                "dosage": "1 ml/L of water",
                "phi_days": 14,
                "cultural_practice": "Scout low-lying depression areas of the field daily; burn heavily infected spots immediately."
            },
            "Stage 3 (Severe > 40%)": {
                "severity_label": "Severe Outbreak",
                "organic_biocontrol": "Curative synthetic treatment mandatory.",
                "chemical_control": "Cyazofamid 34.5% SC (80 ml/acre) or Fenamidone 10% + Mancozeb 50% WG.",
                "active_ingredient": "Cyazofamid",
                "dosage": "0.4 ml/L of water",
                "phi_days": 14,
                "cultural_practice": "Defoliate vines chemically or mechanically; delay digging tubers for 14 days after haulm death."
            }
        }
    },
    "Apple_Scab": {
        "crop": "Apple",
        "disease_name": "Apple Scab",
        "scientific_name": "Venturia inaequalis",
        "pathogen_class": "Fungal",
        "description": "Fungal pathogen causing velvety olive-green to black crusty lesions on leaves and corky cracks on fruit.",
        "early_symptoms": "Olive-drab velvety spots on leaves expanding during green-tip and pink-bud stages.",
        "weather_risk_profile": {
            "optimal_temp_range": (15, 22),
            "humidity_threshold": 85.0
        },
        "stage_treatments": {
            "Stage 1 (Early < 15%)": {
                "severity_label": "Early Scab Detection",
                "organic_biocontrol": "Wettable Sulfur 80% WDG (bio-compatible) + Horticultural dormant oil spray.",
                "chemical_control": "Difenoconazole 25% EC at 150 ml/acre in 200 L water.",
                "active_ingredient": "Difenoconazole",
                "dosage": "0.75 ml/L of water",
                "phi_days": 14,
                "cultural_practice": "Flail-mow or shred autumn leaf litter and spray 5% urea solution to accelerate decomposition."
            },
            "Stage 2 (Moderate 15-40%)": {
                "severity_label": "Moderate Scab",
                "organic_biocontrol": "Potassium bicarbonate (Armicarb) foliar wash.",
                "chemical_control": "Captan 50% WP (1000 g/acre) or Kresoxim-methyl 44.3% SC (200 ml/acre).",
                "active_ingredient": "Kresoxim-methyl",
                "dosage": "1 ml/L of water",
                "phi_days": 21,
                "cultural_practice": "Prune dense canopy tree branches to facilitate sun penetration and rapid leaf drying."
            },
            "Stage 3 (Severe > 40%)": {
                "severity_label": "Severe Scab & Fruit Cracking",
                "organic_biocontrol": "Immediate systemic chemical fungicide program necessary.",
                "chemical_control": "Trifloxystrobin 25% + Tebuconazole 50% WG at 160 g/acre.",
                "active_ingredient": "Trifloxystrobin-Tebuconazole",
                "dosage": "0.8 g/L of water",
                "phi_days": 28,
                "cultural_practice": "Remove culled infected fruits; plan full dormant copper sanitation wash before next spring."
            }
        }
    },
    "Corn_Fall_Armyworm": {
        "crop": "Corn (Maize)",
        "disease_name": "Fall Armyworm Infestation",
        "scientific_name": "Spodoptera frugiperda",
        "pathogen_class": "Insect Pest",
        "description": "Invasive moth pest whose nocturnal larvae feed voraciously inside maize whorls, creating skeletonized leaves and sawdust-like frass.",
        "early_symptoms": "Pinholes and small 'window-pane' translucent scrapes on tender inner whorl leaves.",
        "weather_risk_profile": {
            "optimal_temp_range": (25, 32),
            "humidity_threshold": 65.0
        },
        "stage_treatments": {
            "Stage 1 (Early < 15%)": {
                "severity_label": "Early Larval Emergence",
                "organic_biocontrol": "Apply Bacillus thuringiensis kurstaki (Bt 2 g/L) or Nomuraea rileyi bio-fungus directly into central whorls; release egg parasitoid Trichogramma.",
                "chemical_control": "Emamectin Benzoate 5% SG at 80 g/acre in 200 L water.",
                "active_ingredient": "Emamectin Benzoate",
                "dosage": "0.4 g/L of water",
                "phi_days": 14,
                "cultural_practice": "Install 5 sex pheromone funnel traps per acre; drop a pinch of sand/sawdust into whorls."
            },
            "Stage 2 (Moderate 15-40%)": {
                "severity_label": "Active Leaf Windowing",
                "organic_biocontrol": "Neem seed kernel extract (NSKE 5%) foliar spray + Beauveria bassiana.",
                "chemical_control": "Spinetoram 11.7% SC (170 ml/acre) or Chlorantraniliprole 18.5% SC (80 ml/acre).",
                "active_ingredient": "Chlorantraniliprole",
                "dosage": "0.4 ml/L of water",
                "phi_days": 14,
                "cultural_practice": "Practice Push-Pull intercropping: plant Desmodium between maize rows and Napier grass on perimeter."
            },
            "Stage 3 (Severe > 40%)": {
                "severity_label": "Severe Cob Borer Stage",
                "organic_biocontrol": "Chemical eradication required to prevent cob tunneling and total crop loss.",
                "chemical_control": "Spinetoram 11.7% SC (200 ml/acre) directed into reproductive silk tassels.",
                "active_ingredient": "Spinetoram",
                "dosage": "1 ml/L of water",
                "phi_days": 14,
                "cultural_practice": "Deep winter plowing to expose pupae to predatory birds; destroy stubble."
            }
        }
    },
    "Rice_Brown_Spot": {
        "crop": "Rice",
        "disease_name": "Brown Spot",
        "scientific_name": "Bipolaris oryzae",
        "pathogen_class": "Fungal",
        "description": "Fungal disease linked to poor soil nutrition; produces oval dark-brown spots with gray centers on leaf blades and glumes.",
        "early_symptoms": "Minute brown specks on leaf surfaces of nutrient-stressed tillers.",
        "weather_risk_profile": {
            "optimal_temp_range": (25, 30),
            "humidity_threshold": 85.0
        },
        "stage_treatments": {
            "Stage 1 (Early < 15%)": {
                "severity_label": "Early Spotting",
                "organic_biocontrol": "Pseudomonas fluorescens (10 g/kg seed treatment) + foliar spray with fermented cow urine solution (10%).",
                "chemical_control": "Carbendazim 12% + Mancozeb 63% WP at 500 g/acre in 200 L water.",
                "active_ingredient": "Carbendazim-Mancozeb",
                "dosage": "2.5 g/L of water",
                "phi_days": 21,
                "cultural_practice": "Apply balanced soil fertilizers (correct potash and zinc deficiencies); avoid dry drought spells in paddy."
            },
            "Stage 2 (Moderate 15-40%)": {
                "severity_label": "Moderate Foliar Blight",
                "organic_biocontrol": "Trichoderma harzianum soil and foliar enrichment.",
                "chemical_control": "Propiconazole 25% EC (200 ml/acre) or Edifenphos 50% EC (200 ml/acre).",
                "active_ingredient": "Propiconazole",
                "dosage": "1 ml/L of water",
                "phi_days": 30,
                "cultural_practice": "Maintain steady shallow flood water layer (3-5 cm); eliminate grassy weeds along bunds."
            },
            "Stage 3 (Severe > 40%)": {
                "severity_label": "Severe Panicle Infection",
                "organic_biocontrol": "Immediate systemic chemical intervention.",
                "chemical_control": "Azoxystrobin 18.2% + Difenoconazole 11.4% SC at 200 ml/acre.",
                "active_ingredient": "Azoxystrobin-Difenoconazole",
                "dosage": "1 ml/L of water",
                "phi_days": 21,
                "cultural_practice": "Ensure certified seed for next cycle; treat seed with hot water (52-54 C for 10 minutes)."
            }
        }
    },
    "Wheat_Leaf_Rust": {
        "crop": "Wheat",
        "disease_name": "Leaf Rust (Brown Rust)",
        "scientific_name": "Puccinia triticina",
        "pathogen_class": "Fungal",
        "description": "Airborne basidiomycete fungus forming circular orange-brown powdery pustules scattered across the upper leaf surface.",
        "early_symptoms": "Randomly scattered minute orange-brown powdery urediniospores on upper leaves.",
        "weather_risk_profile": {
            "optimal_temp_range": (15, 22),
            "humidity_threshold": 75.0
        },
        "stage_treatments": {
            "Stage 1 (Early < 15%)": {
                "severity_label": "Early Rust Pustules",
                "organic_biocontrol": "Trichoderma viride + Kaolin particle film barrier spray to block spore germination.",
                "chemical_control": "Tebuconazole 25.9% EC at 250 ml/acre in 200 L water.",
                "active_ingredient": "Tebuconazole",
                "dosage": "1.25 ml/L of water",
                "phi_days": 21,
                "cultural_practice": "Sow rust-resistant recommended wheat cultivars; destroy self-sown wild grass weeds."
            },
            "Stage 2 (Moderate 15-40%)": {
                "severity_label": "Active Rust Proliferation",
                "organic_biocontrol": "Potassium silicate foliar spray combined with bio-fungicide Bacillus pumilus.",
                "chemical_control": "Propiconazole 25% EC at 200 ml/acre in 200 L water.",
                "active_ingredient": "Propiconazole",
                "dosage": "1 ml/L of water",
                "phi_days": 28,
                "cultural_practice": "Monitor flag leaf health meticulously; do not delay spray once pustules reach middle canopy."
            },
            "Stage 3 (Severe > 40%)": {
                "severity_label": "Severe Foliar Desiccation",
                "organic_biocontrol": "Systemic triazole chemical application required.",
                "chemical_control": "Picoxystrobin 7.05% + Propiconazole 11.71% SC at 300 ml/acre.",
                "active_ingredient": "Picoxystrobin-Propiconazole",
                "dosage": "1.5 ml/L of water",
                "phi_days": 30,
                "cultural_practice": "Harvest early if grain fill is complete; avoid planting susceptible legacy seeds in rust-prone zones."
            }
        }
    },
    "Grape_Black_Rot": {
        "crop": "Grape",
        "disease_name": "Black Rot",
        "scientific_name": "Guignardia bidwellii",
        "pathogen_class": "Fungal",
        "description": "Fungal disease producing small brown circular leaf lesions ringed with tiny black fruiting bodies, later shriveling fruit into hard black mummies.",
        "early_symptoms": "Small reddish-brown circular spots on expanding leaves with a dark raised border.",
        "weather_risk_profile": {
            "optimal_temp_range": (21, 29),
            "humidity_threshold": 80.0
        },
        "stage_treatments": {
            "Stage 1 (Early < 15%)": {
                "severity_label": "Early Leaf Lesions",
                "organic_biocontrol": "Equisetum arvense (Horsetail) tea + Copper soap bio-formulation.",
                "chemical_control": "Kresoxim-methyl 44.3% SC at 200 ml/acre in 200 L water.",
                "active_ingredient": "Kresoxim-methyl",
                "dosage": "1 ml/L of water",
                "phi_days": 21,
                "cultural_practice": "Inspect vineyard trellis and remove overwintered mummified berries before spring bud break."
            },
            "Stage 2 (Moderate 15-40%)": {
                "severity_label": "Moderate Cane & Leaf Spread",
                "organic_biocontrol": "Serenade ASO (Bacillus amyloliquefaciens) bio-spray.",
                "chemical_control": "Myclobutanil 10% WP (250 g/acre) or Mancozeb 75% WP (800 g/acre).",
                "active_ingredient": "Myclobutanil",
                "dosage": "1.25 g/L of water",
                "phi_days": 21,
                "cultural_practice": "Perform shoot thinning and leaf pulling around fruit cluster zones to accelerate cluster drying."
            },
            "Stage 3 (Severe > 40%)": {
                "severity_label": "Severe Cluster Mummification",
                "organic_biocontrol": "Systemic chemical control necessary.",
                "chemical_control": "Pyraclostrobin 20% WG at 150 g/acre in 200 L water.",
                "active_ingredient": "Pyraclostrobin",
                "dosage": "0.75 g/L of water",
                "phi_days": 28,
                "cultural_practice": "Destroy severely mummified grape clusters; apply dormant lime-sulfur spray before winter dormancy."
            }
        }
    },
    "Healthy_Crop": {
        "crop": "General Crop",
        "disease_name": "Healthy Foliage",
        "scientific_name": "Plantae",
        "pathogen_class": "None",
        "description": "Turgid, uniformly pigmented vegetative foliage displaying robust vascular structure and zero observable lesioning or pest invasion.",
        "early_symptoms": "No visible pathological symptoms. Vibrant chlorophyllic balance.",
        "weather_risk_profile": {
            "optimal_temp_range": (18, 28),
            "humidity_threshold": 65.0
        },
        "stage_treatments": {
            "Stage 0 (Healthy 0%)": {
                "severity_label": "Healthy - Disease Free",
                "organic_biocontrol": "Apply foliar bio-stimulants (Seaweed extract 2 ml/L or Vermiwash) to maintain plant vigor.",
                "chemical_control": "No synthetic chemical intervention required.",
                "active_ingredient": "None",
                "dosage": "0",
                "phi_days": 0,
                "cultural_practice": "Maintain scheduled soil fertility testing; practice regular drip fertigation and proactive weekly field scouting."
            }
        }
    }
}

CLASS_NAME_MAP = {
    0: "Tomato_Early_Blight",
    1: "Tomato_Late_Blight",
    2: "Potato_Early_Blight",
    3: "Potato_Late_Blight",
    4: "Apple_Scab",
    5: "Corn_Fall_Armyworm",
    6: "Rice_Brown_Spot",
    7: "Wheat_Leaf_Rust",
    8: "Grape_Black_Rot",
    9: "Healthy_Crop"
}

def determine_severity_stage(ratio: float) -> str:
    """Classifies numerical lesion area ratio into standardized IPM stage."""
    if ratio < 0.03:
        return "Stage 0 (Healthy 0%)"
    elif ratio < 0.15:
        return "Stage 1 (Early < 15%)"
    elif ratio <= 0.40:
        return "Stage 2 (Moderate 15-40%)"
    else:
        return "Stage 3 (Severe > 40%)"

def calculate_weather_risk(disease_key: str, temp_c: float, humidity_pct: float) -> Dict[str, Any]:
    """
    Multimodal Environmental Disease Risk Engine:
    Evaluates ambient temperature and relative humidity against the pathogen's optimal incubation thresholds.
    """
    kb = DISEASE_KNOWLEDGE_BASE.get(disease_key, DISEASE_KNOWLEDGE_BASE["Healthy_Crop"])
    if disease_key == "Healthy_Crop":
        return {
            "risk_score": 10,
            "risk_level": "LOW",
            "explanation": "Plant foliage is healthy and environmental conditions pose no immediate threat."
        }
        
    prof = kb["weather_risk_profile"]
    t_min, t_max = prof["optimal_temp_range"]
    h_thresh = prof["humidity_threshold"]
    
    score = 0
    factors = []
    
    # Temperature check
    if t_min <= temp_c <= t_max:
        score += 50
        factors.append(f"Ambient temperature ({temp_c:.1f}°C) is in pathogen optimum range ({t_min}-{t_max}°C).")
    elif abs(temp_c - t_min) <= 4 or abs(temp_c - t_max) <= 4:
        score += 25
        factors.append(f"Ambient temperature ({temp_c:.1f}°C) is moderately favorable for pathogen development.")
    else:
        factors.append(f"Ambient temperature ({temp_c:.1f}°C) is outside peak pathogen incubation zone.")
        
    # Humidity check
    if humidity_pct >= h_thresh:
        score += 50
        factors.append(f"Relative humidity ({humidity_pct:.1f}%) exceeds infection threshold ({h_thresh}%).")
    elif humidity_pct >= (h_thresh - 15):
        score += 25
        factors.append(f"Relative humidity ({humidity_pct:.1f}%) is nearing critical spore germination threshold.")
    else:
        factors.append(f"Relative humidity ({humidity_pct:.1f}%) is low, inhibiting foliar spore germination.")
        
    if score >= 75:
        risk_level = "CRITICAL HIGH"
    elif score >= 50:
        risk_level = "MODERATE"
    else:
        risk_level = "LOW"
        
    return {
        "risk_score": score,
        "risk_level": risk_level,
        "explanation": " ".join(factors)
    }

def get_ipm_advisory(
    disease_key: str,
    severity_ratio: float,
    temp_c: Optional[float] = 26.0,
    humidity_pct: Optional[float] = 85.0
) -> Dict[str, Any]:
    """
    Generates a full agronomic advisory combining detection, severity stage,
    and environmental weather risk.
    """
    kb = DISEASE_KNOWLEDGE_BASE.get(disease_key, DISEASE_KNOWLEDGE_BASE["Healthy_Crop"])
    stage = determine_severity_stage(severity_ratio)
    
    # Fallback to nearest stage if exact key not in dictionary
    treatments = kb.get("stage_treatments", {})
    if stage in treatments:
        rec = treatments[stage]
    else:
        # Default to first available treatment
        rec = list(treatments.values())[0]
        
    weather_risk = calculate_weather_risk(disease_key, temp_c, humidity_pct)
    
    return {
        "crop": kb["crop"],
        "disease_name": kb["disease_name"],
        "scientific_name": kb["scientific_name"],
        "pathogen_class": kb["pathogen_class"],
        "description": kb["description"],
        "early_symptoms": kb["early_symptoms"],
        "severity_percentage": round(severity_ratio * 100, 1),
        "severity_stage": stage,
        "severity_label": rec.get("severity_label", stage),
        "organic_biocontrol": rec.get("organic_biocontrol", "Maintain routine organic care."),
        "chemical_control": rec.get("chemical_control", "None"),
        "active_ingredient": rec.get("active_ingredient", "None"),
        "dosage": rec.get("dosage", "N/A"),
        "pre_harvest_interval_days": rec.get("phi_days", 0),
        "cultural_practice": rec.get("cultural_practice", "Standard field maintenance."),
        "environmental_risk": weather_risk
    }

if __name__ == '__main__':
    advisory = get_ipm_advisory("Tomato_Early_Blight", severity_ratio=0.12, temp_c=26.5, humidity_pct=86.0)
    print("IPM Advisory Test Passed:")
    for k, v in advisory.items():
        print(f"  {k}: {v}")

