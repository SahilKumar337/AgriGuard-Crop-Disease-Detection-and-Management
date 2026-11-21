# AgriGuard: Multimodal YOLOv8/v11 Crop Disease Detection & Conversational ChatGPT-Style Agronomist

**Course:** CSE471 | Artificial Intelligence & Machine Learning  
**Target Platform:** Android (Native APK & PWA) + Cloud (FastAPI & Streamlit)  
**Security Notice:** All sensitive API keys and personal credentials have been removed.

---

## 1. Google Scholar Literature Survey & Identified Research Gaps

Recent research in computer vision phytopathology (*Computers and Electronics in Agriculture*, *Frontiers in Plant Science*, ACM CoDS-COMAD) highlights four critical research gaps:

1. **The Laboratory vs. In-The-Wild Domain Shift (Singh et al., PlantDoc 2020):**
   Standard models trained on pristine laboratory leaves (e.g. PlantVillage) fail when deployed in actual fields due to soil noise, weeds, and varying sunlight. AgriGuard utilizes **YOLO object detection** trained on PlantDoc-formatted bounding-box annotations to isolate lesion patches from background clutter.
2. **Small Lesion Feature Degradation:**
   Early Stage 1 infections present tiny micro-lesions (<16x16 pixels). Deeper CNN feature strides lose fine spatial details. AgriGuard incorporates multi-scale feature pyramids (PANet) and cross-stage partial connections (C2f) to preserve high-resolution P3 spatial representations.
3. **The 'Silent AI' Detection Void:**
   Existing models output raw bounding boxes or abstract labels without explaining treatments to farmers. AgriGuard introduces a **ChatGPT-style Conversational Agronomist Agent** that interprets bounding boxes into stage-graded Integrated Pest Management (IPM) advisories.
4. **Edge Device Latency & Quantization Constraints:**
   Heavy two-stage detectors (Faster R-CNN) throttle mobile processors. AgriGuard delivers a quantized **YOLOv8n model** (6.2 MB, 21.8 ms edge latency) capable of offline execution on Android smartphones.

---

## 2. Directory Structure

```
Code/
├── app/
│   ├── main.py              # FastAPI REST service & PWA static server
│   ├── streamlit_app.py     # ChatGPT-style Streamlit web dashboard
│   └── static/              # Conversational Android PWA client (HTML/CSS/JS, icons, Service Worker)
├── android_app/
│   ├── AndroidManifest.xml  # Native Android camera & storage permissions
│   ├── MainActivity.java    # Android WebView with camera file chooser hooks
│   ├── build.gradle         # Gradle build script for APK generation
│   └── README_ANDROID.md    # Step-by-step Android installation guide
├── model/
│   ├── train_yolo.py        # YOLOv8n model training on PlantDoc dataset
│   ├── yolo_detector.py     # YOLO lesion detection & severity quantification
│   ├── chat_agent.py        # Multimodal ChatGPT-style conversational agent
│   ├── ipm_engine.py        # Agronomic IPM knowledge base & weather risk
│   └── weights/             # Trained best.pt (6.17 MB) & yolo_crop_disease.onnx (12.57 MB)
├── tests/
│   └── test_pipeline.py     # Automated unit & integration tests
├── requirements.txt         # Production dependencies
└── README.md                # System documentation
```

---

## 3. Quickstart & Local Execution

### Prerequisites
- Python 3.9+ with PyTorch
- Camera or sample image files

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run Automated Tests
```bash
python tests/test_pipeline.py
```

### Step 3: Launch FastAPI & Android PWA Server
```bash
cd app
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
Open your browser at `http://localhost:8000` to interact with the ChatGPT-style interface, or visit `http://localhost:8000/docs` for the interactive Swagger API documentation.

### Step 4: Launch Streamlit Cloud Dashboard (Alternative)
```bash
cd app
streamlit run streamlit_app.py
```

---

## 4. Android App Execution (Two Production Modes)

### Mode A: 1-Tap Progressive Web App (PWA) on Android (Instant)
1. Ensure your Android phone and PC are on the same Wi-Fi network.
2. Open **Google Chrome** on your phone and navigate to `http://<YOUR_PC_IP>:8000`.
3. Tap Chrome's menu (`⋮`) -> **"Add to Home Screen"** or **"Install AgriGuard"**.
4. The application installs into your Android app drawer with full-screen standalone execution, native camera shutter access (`capture="environment"`), and offline caching via `sw.js`.

### Mode B: Native Android Studio APK Build
1. Open **Android Studio** and load `Code/android_app/`.
2. Target URL in `MainActivity.java` is preset to `http://10.0.2.2:8000/` (for emulator) or your local network IP.
3. Click **Build -> Build Bundle(s) / APK(s) -> Build APK(s)** to generate `app-debug.apk`.

---

## 5. Experimental Benchmark Results

| Metric | YOLOv8n (Ours) | YOLOv8s | SSD-MobileNet | Faster R-CNN |
| :--- | :--- | :--- | :--- | :--- |
| **mAP@50 (%)** | **75.3%** | 78.4% | 62.1% | 74.8% |
| **Overall Recall (%)** | **96.6%** | 94.1% | 81.4% | 88.2% |
| **Model Size** | **6.2 MB** | 22.5 MB | 18.4 MB | 168.0 MB |
| **Edge CPU Latency** | **21.8 ms** | 48.2 ms | 34.5 ms | 142.0 ms |
| **GPU Latency (RTX 4060)** | **5.4 ms** | 12.1 ms | 9.8 ms | 46.0 ms |
| **Edge Feasibility** | **Native Android Optimal** | Moderate | Low Accuracy | Unusable on Edge |
