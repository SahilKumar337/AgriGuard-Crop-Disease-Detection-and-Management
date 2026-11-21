# Data Dictionary: Crop Disease & Pest Infestation Dataset
**Course:** CSE471 | **Project:** AgriGuard - Early Detection & Management of Crop Diseases and Pest Infestations

---

### 1. Dataset Overview
This dataset provides a comprehensive, field-validated agricultural record repository designed for training, validating, and testing early-stage crop disease detection models, severity quantification engines, and Integrated Pest Management (IPM) decision support systems.

The dataset includes **35 diverse agricultural conditions** spanning 10 economically vital crops: Tomato, Potato, Apple, Corn (Maize), Rice, Wheat, Grape, Cotton, Bell Pepper, and Citrus.

---

### 2. Attribute Specifications

| Field Name | Data Type | Nullable | Example Values | Description |
| :--- | :--- | :--- | :--- | :--- |
| `record_id` | String (Alpha-numeric) | No | `REC-001`, `REC-015` | Unique identifier assigned to each crop disease/pest sample. |
| `crop_name` | String | No | `Tomato`, `Potato`, `Apple`, `Rice` | Name of the cultivated host agricultural crop. |
| `disease_or_pest_name` | String | No | `Early Blight`, `Late Blight`, `Fall Armyworm` | Clinical or common diagnostic name of the pathological disease or entomological pest. |
| `scientific_name` | String (Italicized taxonomy) | No | *Alternaria solani*, *Phytophthora infestans* | Binomial nomenclature of the causative pathogen (fungus, bacterium, virus, insect). |
| `pathogen_class` | Categorical | No | `Fungal`, `Bacterial`, `Viral`, `Insect Pest`, `Oomycete` | Biological classification category of the disease-causing agent. |
| `primary_early_symptom` | Text | No | `Pinpoint chlorotic spots with concentric rings` | Initial physical symptom observed during Stage 1 infection before large necrosis occurs. |
| `severity_stage` | Categorical | No | `Stage 1 (Early < 15%)`, `Stage 2 (Moderate 15-40%)`, `Stage 3 (Severe > 40%)` | Severity classification grade based on affected leaf surface area percentage. |
| `optimal_temp_c` | String (Range) | No | `24 - 29 °C`, `15 - 20 °C` | Ambient atmospheric temperature range where spore germination / pest reproduction peaks. |
| `optimal_humidity_pct` | String (Range) | No | `80 - 95%`, `> 90%` | Relative humidity (RH%) threshold accelerating pathogen incubation. |
| `favorable_weather_condition` | Text | No | `Intermittent rains followed by warm dry spells` | Climatic conditions triggering rapid disease outbreak and spore dispersion. |
| `organic_biocontrol_recommendation` | Text | No | `Neem oil (Azadirachtin 0.03% EC), Trichoderma viride` | Environmentally benign, bio-fungicidal or botanic IPM intervention. |
| `chemical_control_treatment` | Text | No | `Chlorothalonil 75% WP, Mancozeb 75% WP` | Recommended synthetic chemical fungicide/insecticide for urgent containment. |
| `active_ingredient` | Text | No | `Chlorothalonil`, `Mancozeb`, `Copper Oxychloride` | Active pharmaceutical chemical molecule responsible for fungicidal or pesticidal action. |
| `dosage_per_acre` | String | No | `600 - 800 g dissolved in 200 L water/acre` | Prescribed application concentration to prevent crop toxicity and chemical run-off. |
| `pre_harvest_interval_days` | Integer | No | `3`, `7`, `14` | Minimum safe waiting period (in days) between spraying and crop harvesting for consumption. |
| `preventive_cultural_measures` | Text | No | `Drip irrigation, rogue out volunteer solanaceous weeds` | Agronomic practices to mitigate spore recurrence, vector harbor, and moisture accumulation. |

---

### 3. Severity Quantification Matrix

| Severity Level | Leaf Area Affected (%) | Chlorosis/Necrosis Diameter | Propagation Risk | Action Required |
| :--- | :--- | :--- | :--- | :--- |
| **Stage 1 (Early)** | < 15% | Micro-lesions (< 2 mm) | Low - Contained | Organic biocontrol, cultural pruning, avoid foliar spray |
| **Stage 2 (Moderate)** | 15% – 40% | Expanding lesions (2 - 8 mm) | Medium - Spreading | Targeted fungicide/insecticide application at standard dosage |
| **Stage 3 (Severe)** | > 40% | Coalescing blight (> 8 mm), defoliation | Critical - Outbreak | Emergency systemic chemical eradication, quarantine affected rows |

---

### 4. Ethical & Data Usage Notice
- Chemical dosages follow standardized guidelines from the Central Insecticides Board & Registration Committee (CIB&RC) and FAO Plant Protection recommendations.
- Always observe Pre-Harvest Interval (PHI) limits to prevent chemical residues on consumable agricultural produce.

