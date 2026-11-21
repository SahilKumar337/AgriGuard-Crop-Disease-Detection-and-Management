"""
AgriGuard FastAPI Backend & Conversational Multimodal Service
Course: CSE471 | AIML Engineering Pipeline
"""

import os
import io
import sys
import base64
from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, FileResponse
from PIL import Image

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from model.chat_agent import AgriGuardChatAgent
from model.yolo_detector import YOLOCropDetector, YOLO_CLASS_NAMES
from model.ipm_engine import DISEASE_KNOWLEDGE_BASE, calculate_weather_risk

app = FastAPI(
    title="AgriGuard Conversational YOLO Crop Protection API",
    description="AIML-driven multimodal conversational assistant for YOLO crop disease detection and IPM advisory.",
    version="2.0.0"
)

# Enable CORS for Android WebViews and cross-origin PWA clients
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Chat Agent and YOLO Detector
chat_agent = AgriGuardChatAgent()
yolo_detector = YOLOCropDetector()

# Mount static directory for Android PWA / Web Client
static_dir = os.path.join(current_dir, "static")
os.makedirs(static_dir, exist_ok=True)
app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/")
def serve_home():
    index_file = os.path.join(static_dir, "index.html")
    if os.path.exists(index_file):
        return FileResponse(index_file)
    return {"message": "AgriGuard Backend Active. Access API docs at /docs"}

@app.get("/manifest.json")
def serve_manifest():
    manifest_file = os.path.join(static_dir, "manifest.json")
    if os.path.exists(manifest_file):
        return FileResponse(manifest_file, media_type="application/manifest+json")
    raise HTTPException(status_code=404, detail="Manifest not found")

@app.get("/sw.js")
def serve_sw():
    sw_file = os.path.join(static_dir, "sw.js")
    if os.path.exists(sw_file):
        return FileResponse(sw_file, media_type="application/javascript")
    raise HTTPException(status_code=404, detail="Service worker not found")

@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "service": "AgriGuard Conversational AI & YOLO Crop Disease Detection",
        "model_architecture": "Ultralytics YOLOv8n / YOLO11n Lesion Localization Engine",
        "supported_classes": list(YOLO_CLASS_NAMES.values())
    }

@app.post("/api/chat")
async def chat_consultation(
    message: str = Form(""),
    file: UploadFile = File(None),
    temperature: float = Form(26.5),
    humidity: float = Form(82.0)
):
    """
    ChatGPT-Style Conversational Endpoint:
    Receives user query + optional leaf photograph.
    Runs YOLO lesion detection and returns conversational agronomist response with annotated bounding boxes.
    """
    image = None
    if file is not None and file.filename != "":
        try:
            contents = await file.read()
            image = Image.open(io.BytesIO(contents)).convert("RGB")
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Invalid image format: {str(e)}")

    try:
        result = chat_agent.process_consultation(
            message=message,
            image_input=image,
            temp_c=temperature,
            humidity_pct=humidity
        )
        return JSONResponse(content={"status": "success", "data": result})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Consultation error: {str(e)}")

@app.post("/api/yolo-detect")
async def yolo_detect_endpoint(file: UploadFile = File(...)):
    """Direct YOLO lesion localization endpoint returning raw bounding boxes and annotated image."""
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents)).convert("RGB")
        result = yolo_detector.detect_lesions(image)
        return JSONResponse(content={"status": "success", "data": result})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Detection error: {str(e)}")

@app.get("/api/weather-risk")
def get_weather_risk(disease_key: str, temp_c: float = 26.5, humidity_pct: float = 82.0):
    if disease_key not in DISEASE_KNOWLEDGE_BASE:
        raise HTTPException(status_code=404, detail="Disease key not found in knowledge base.")
    risk = calculate_weather_risk(disease_key, temp_c, humidity_pct)
    return {"status": "success", "data": risk}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
