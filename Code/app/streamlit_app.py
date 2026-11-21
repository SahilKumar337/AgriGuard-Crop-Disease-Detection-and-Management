"""
AgriGuard: ChatGPT-Style Multimodal Conversational Web Application
Course: CSE471 | AIML Engineering Pipeline
"""

import os
import sys
import io
import base64
from PIL import Image
import streamlit as st

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from model.chat_agent import AgriGuardChatAgent
from model.yolo_detector import YOLO_CLASS_NAMES

def main():
    st.set_page_config(
        page_title="AgriGuard | YOLO AI Agronomist",
        page_icon="🌱",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Initialize chat agent
    if "agent" not in st.session_state:
        st.session_state.agent = AgriGuardChatAgent()

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": """### Welcome to AgriGuard AI Agronomist! 🌱

I am your multimodal AI crop protection assistant powered by **YOLO Object Detection** and Integrated Pest Management (IPM) science.

- 📷 **Snap or upload a leaf photo** to detect disease lesions with bounding boxes.
- 📊 View quantitative **severity staging** and pathogen etiology.
- 🧪 Receive exact **prescribed chemical and organic dosages** with safety waiting intervals.
- 💬 **Ask follow-up questions** anytime (e.g. knapsack tank mixing, weather advisories)!""",
                "image": None
            }
        ]

    # Sidebar
    with st.sidebar:
        st.image("https://img.icons8.com/color/96/organic-food.png", width=64)
        st.title("AgriGuard AI")
        st.caption("YOLO Multimodal Crop Protection | CSE471")
        st.markdown("---")

        st.subheader("⛅ Microclimate Sensors")
        temp_c = st.slider("Ambient Temperature (°C)", 10.0, 45.0, 26.5, 0.5)
        humidity_pct = st.slider("Relative Humidity (%)", 20.0, 100.0, 82.0, 1.0)
        st.markdown("---")

        st.subheader("📷 Attach Leaf Image")
        camera_img = st.camera_input("Take photo with camera:")
        upload_img = st.file_uploader("Or select from gallery:", type=["jpg", "jpeg", "png"])

        st.markdown("---")
        st.subheader("🧪 Quick Test Samples")
        sample_choice = st.selectbox(
            "Load benchmark field sample:",
            ["None", "Tomato Early Blight", "Potato Late Blight", "Apple Scab", "Fall Armyworm Pest", "Healthy Crop Leaf"]
        )

        sample_path_map = {
            "Tomato Early Blight": os.path.join(parent_dir, "..", "Data", "sample_images", "tomato_early_blight_sample.jpg"),
            "Potato Late Blight": os.path.join(parent_dir, "..", "Data", "sample_images", "potato_late_blight_sample.jpg"),
            "Apple Scab": os.path.join(parent_dir, "..", "Data", "sample_images", "apple_scab_sample.jpg"),
            "Fall Armyworm Pest": os.path.join(parent_dir, "..", "Data", "sample_images", "pest_infestation_sample.jpg"),
            "Healthy Crop Leaf": os.path.join(parent_dir, "..", "Data", "sample_images", "tomato_healthy_sample.jpg")
        }

        if st.button("🗑️ Clear Consultation History"):
            st.session_state.messages = []
            st.rerun()

    # Determine attached image
    attached_image = None
    if camera_img is not None:
        attached_image = Image.open(camera_img)
    elif upload_img is not None:
        attached_image = Image.open(upload_img)
    elif sample_choice != "None":
        p = sample_path_map.get(sample_choice)
        if p and os.path.exists(p):
            attached_image = Image.open(p)

    # Main Chat View
    st.markdown("### 💬 Conversational Agronomist & YOLO Lesion Inspector")

    # Render conversation history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"], avatar="🌱" if msg["role"] == "assistant" else "👤"):
            if msg.get("image") is not None:
                st.image(msg["image"], caption=msg.get("image_caption", "Leaf Inspection"), use_container_width=True)
            st.markdown(msg["content"])

    # Chat Input Box
    user_prompt = st.chat_input("Ask AgriGuard anything about crop diseases, chemical dosages, or weather risk...")

    if user_prompt or (attached_image is not None and "last_processed_img" not in st.session_state):
        # Handle message submission
        query = user_prompt if user_prompt else "Please analyze this leaf photo for diseases and recommend treatment."
        
        # Add user message
        st.session_state.messages.append({
            "role": "user",
            "content": query,
            "image": attached_image,
            "image_caption": "Uploaded Field Leaf"
        })

        with st.chat_message("assistant", avatar="🌱"):
            with st.spinner("Analyzing with YOLO Object Detection & IPM Engine..."):
                res = st.session_state.agent.process_consultation(
                    message=query,
                    image_input=attached_image,
                    temp_c=temp_c,
                    humidity_pct=humidity_pct
                )

            # Check if annotated image returned
            annotated_pil = None
            if res["annotated_image_b64"]:
                # Convert b64 back to PIL for Streamlit display
                b64_data = res["annotated_image_b64"].split(",")[1]
                img_bytes = base64.b64decode(b64_data)
                annotated_pil = Image.open(io.BytesIO(img_bytes))
                st.image(annotated_pil, caption=f"🎯 YOLO Lesions Detected: {res['detection_meta']['lesion_count']} | Severity: {res['detection_meta']['severity_pct']}%", use_container_width=True)

            st.markdown(res["response_text"])

        # Record assistant reply
        st.session_state.messages.append({
            "role": "assistant",
            "content": res["response_text"],
            "image": annotated_pil,
            "image_caption": "YOLO Annotated Bounding Boxes" if annotated_pil else None
        })

        if attached_image is not None:
            st.session_state["last_processed_img"] = True

if __name__ == '__main__':
    main()
