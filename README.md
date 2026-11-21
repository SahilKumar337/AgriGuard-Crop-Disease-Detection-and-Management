# 🌿 AgriGuard: Edge-Optimized YOLO Crop Disease Detection & Multimodal IPM Platform

[![Course](https://img.shields.io/badge/Course-CSE471%20Deep%20Learning%20for%20Computer%20Vision-blue.svg)](https://github.com/Devanshu-Dhyanu/AgriGuard-Crop-Disease-Detection-and-Management)
[![Model](https://img.shields.io/badge/YOLOv8n-Anchor--Free%20Detector-brightgreen.svg)](https://github.com/ultralytics/ultralytics)
[![XAI](https://img.shields.io/badge/Explainable%20AI-Grad--CAM%20Heatmaps-orange.svg)](https://github.com/Devanshu-Dhyanu/AgriGuard-Crop-Disease-Detection-and-Management)
[![Edge](https://img.shields.io/badge/Edge%20Runtime-ONNX%20Mobile%20%7C%20FastAPI-blueviolet.svg)](https://github.com/Devanshu-Dhyanu/AgriGuard-Crop-Disease-Detection-and-Management)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **Author:** Devanshu Kumar  
> **Roll No.:** 9 | **Registration No.:** 12404673  
> **Institution:** Department of Computer Science and Engineering, Lovely Professional University  
> **Course:** CSE471 (Deep Learning for Computer Vision) | Capstone Project

---

## 📌 Executive Summary

Agricultural crop diseases and pest infestations cause 20% to 40% of global yield reductions annually ($220B+ economic burden, FAO). Traditional CNN classifiers trained on laboratory datasets (such as PlantVillage) suffer an accuracy collapse exceeding **31%** when deployed in real fields due to soil clutter, weed foliage, canopy shadows, and variable natural illumination. Furthermore, single-label classifiers fail to isolate multiple co-occurring lesions on a single leaf blade and offer zero quantitative severity metrics.

**AgriGuard** resolves this laboratory-to-field domain shift by combining:
1. **Anchor-Free YOLOv8n Object Detector**: Localizes millimeter-scale pathological lesions with individual bounding boxes across 27 disease categories and 13 economic crops.
2. **Botanical Architecture Verification Gate**: Uses HSV foliage segmentation and active contour aspect-ratio analysis ($AR < 3.5$ for broadleaf dicots vs. $AR \ge 4.5$ for monocot grasses) to eliminate cross-phylogenetic false positives (e.g., preventing cereal rust predictions on broadleaf rose/apple foliage).
3. **Quantitative Severity Index (QSI)**: Measures cumulative necrotic lesion area relative to green leaf area to assign objective clinical infection stages (Stage 0: Healthy, Stage 1: Mild, Stage 2: Moderate, Stage 3: Severe).
4. **Explainable AI (Grad-CAM)**: Generates class-discriminative convolutional attention heatmaps to verify that neural predictions attend to true pathology rather than background artifacts.
5. **Multimodal Integrated Pest Management (IPM)**: Translates diagnostic telemetry and microclimate sensor readings ($T, RH$) into actionable cultural sanitation, biological treatments, and exact chemical dosages (g/L) with Pre-Harvest Interval (PHI) safety countdowns.
6. **Edge & Mobile Deployment**: Deployed across an asynchronous FastAPI REST backend, a Progressive Web Application (PWA) with offline caching, a desktop Streamlit telemetry dashboard, and quantized ONNX edge models achieving **14.8 ms GPU latency** and **42.1 ms mobile CPU latency**.

---

## 📄 Key Project Deliverables

- **IEEE Technical Research Paper (10 Pages, 2-Column):** [`IEEE_AgriGuard_Project_Documentation.pdf`](IEEE_AgriGuard_Project_Documentation.pdf)
- **IEEE Paper (Microsoft Word):** [`IEEE_AgriGuard_Project_Documentation.docx`](IEEE_AgriGuard_Project_Documentation.docx)
- **IEEE Paper (Markdown Source):** [`IEEE_AgriGuard_Project_Documentation.md`](IEEE_AgriGuard_Project_Documentation.md)
- **University Capstone Report:** [`RollNo_CropDiseaseDetection_Report.pdf`](RollNo_CropDiseaseDetection_Report.pdf)
- **Presentation Slides:** [`RollNo_CropDiseaseDetection_PPT.pptx`](RollNo_CropDiseaseDetection_PPT.pptx)
- **Deployment Manifest:** [`Deployment_Link.txt`](Deployment_Link.txt)

---

## 🔬 Benchmark Results on In-Situ PlantDoc Dataset

| Metric | Baseline ResNet-50 | Faster R-CNN | YOLOv8n (No Botanical Gate) | **AgriGuard Full Pipeline** |
| :--- | :---: | :---: | :---: | :---: |
| **mAP@0.5** | 0.642 | 0.784 | 0.778 | **0.812 (81.2%)** |
| **mAP@[0.5:0.95]** | 0.418 | 0.512 | 0.521 | **0.548 (54.8%)** |
| **Mean Precision** | 68.4% | 80.2% | 79.5% | **83.4%** |
| **Mean Recall** | 62.1% | 75.8% | 76.1% | **78.6%** |
| **Mean F1-Score** | 65.1% | 77.9% | 77.8% | **80.9%** |
| **Severity MAE** | N/A | 4.82% | 3.45% | **3.18%** |
| **Inference Latency (RTX 4060)** | 11.2 ms | 84.5 ms | 14.6 ms | **14.8 ms** |
| **Mobile CPU Latency (ONNX)** | 35.0 ms | 280.0 ms | 41.5 ms | **42.1 ms** |

---

## 🏛️ System Architecture

```
[Smartphone Camera / File Upload]
             │
             ▼
[Foliage Preprocessing & HSV Segmentation] ──► [Active Contour Aspect-Ratio Gate]
             │                                              │
             ▼                                              ▼
[Anchor-Free YOLOv8n Object Detection] ───────► [Botanical Phylogenetic Override]
             │                                              │
             ▼                                              ▼
[Quantitative Lesion Severity Staging]        [Grad-CAM Saliency Attention Maps]
             │                                              │
             └──────────────────────┬───────────────────────┘
                                    │
                                    ▼
                 [Multimodal IPM Agronomic Reasoner]
                 (Microclimate T & RH Risk Analysis)
                                    │
                                    ▼
       [Structured Diagnostic Telemetry & Extension Dashboard]
```

---

## 🚀 Quickstart & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Devanshu-Dhyanu/AgriGuard-Crop-Disease-Detection-and-Management.git
cd AgriGuard-Crop-Disease-Detection-and-Management
```

### 2. Set Up Virtual Environment & Dependencies
```bash
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

pip install -r Code/requirements.txt
```

### 3. Run FastAPI Backend & PWA Service
```bash
uvicorn Code.app.main:app --host 0.0.0.0 --port 8000 --reload
```
- Open browser at `http://localhost:8000` for the mobile PWA interface.
- Open Swagger API documentation at `http://localhost:8000/docs`.

### 4. Run Streamlit Telemetry Dashboard
```bash
streamlit run Code/app/streamlit_app.py
```
- Open browser at `http://localhost:8501` for the desktop telemetry and model inspection dashboard.

---

## 📱 Mobile PWA & Offline Edge Support

- **Progressive Web App (PWA):** Installs directly to smartphone home screen (`manifest.json` and `sw.js`).
- **Autofocus Capture:** Uses HTML5 media stream with rear camera autofocus (`capture="environment"`).
- **ONNX Mobile Export:** Quantized model weights (`Code/model/weights/best.onnx`) enable sub-50 ms edge inference on resource-constrained Android devices.

---

## 📚 References & Academic Citations

1. **Singh et al. (2020)** — *PlantDoc: A Dataset for Visual Plant Disease Detection*, ACM IKDD CoDS-COMAD.
2. **Barbedo, J. G. A. (2019)** — *Plant disease identification from individual lesions and spots using deep learning*, Biosystems Engineering.
3. **Fuentes et al. (2017)** — *A Robust Deep-Learning-Based Detector for Real-Time Tomato Plant Diseases and Pests Recognition*, Sensors.
4. **Hughes & Salathé (2015)** — *An open access repository of images on plant health to enable mobile diagnostics*, arXiv:1511.08060.
5. **Mohanty, Hughes, & Salathé (2016)** — *Using Deep Learning for Image-Based Plant Disease Detection*, Frontiers in Plant Science.
6. **Selvaraj et al. (2019)** — *Detection of banana diseases and pest damage using deep learning and handheld smartphones*, Plant Methods.
7. **Selvaraju et al. (2017)** — *Grad-CAM: Visual Explanations from Deep Networks via Gradient-Based Localization*, IEEE ICCV.
8. **Jocher et al. (2023)** — *Ultralytics YOLOv8*, Version 8.0.0.
9. **FAO (2022)** — *The State of Food and Agriculture 2022: Leveraging automation in agriculture for transforming agrifood systems*.
10. **Ferentinos, K. P. (2018)** — *Deep learning models for plant disease detection and diagnosis*, Computers and Electronics in Agriculture.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
