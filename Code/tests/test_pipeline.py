"""
AgriGuard Test Suite: End-to-End Pipeline & YOLO Verification
Course: CSE471 | AIML Engineering Pipeline
"""

import os
import sys
import unittest
import numpy as np
import torch
from PIL import Image

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if base_dir not in sys.path:
    sys.path.append(base_dir)

from model.yolo_detector import YOLOCropDetector, YOLO_CLASS_NAMES
from model.chat_agent import AgriGuardChatAgent
from model.ipm_engine import DISEASE_KNOWLEDGE_BASE, get_ipm_advisory
from model.gradcam import explain_leaf_sample

class TestAgriGuardYOLOPipeline(unittest.TestCase):

    def setUp(self):
        self.sample_img_path = os.path.join(base_dir, "..", "Data", "sample_images", "tomato_early_blight_sample.jpg")
        self.detector = YOLOCropDetector()
        self.agent = AgriGuardChatAgent()

    def test_yolo_weights_loaded(self):
        """Verify that trained YOLO weights exist and are loaded."""
        weights_path = os.path.join(base_dir, "model", "weights", "best.pt")
        self.assertTrue(os.path.exists(weights_path), "Trained best.pt model missing!")
        self.assertIsNotNone(self.detector.yolo_model)

    def test_yolo_lesion_detection(self):
        """Verify YOLO detects bounding boxes and computes severity."""
        if os.path.exists(self.sample_img_path):
            res = self.detector.detect_lesions(self.sample_img_path)
            self.assertIn("detections", res)
            self.assertIn("lesion_count", res)
            self.assertIn("severity_percentage", res)
            self.assertIn("annotated_image_b64", res)
            self.assertGreater(len(res["detections"]), 0)
            self.assertGreater(res["severity_percentage"], 0.0)

    def test_conversational_chat_agent(self):
        """Verify multimodal ChatGPT-style agent processes image and returns markdown advice."""
        if os.path.exists(self.sample_img_path):
            reply = self.agent.process_consultation("Diagnose my crop leaf", image_input=self.sample_img_path)
            self.assertIn("response_text", reply)
            self.assertIn("annotated_image_b64", reply)
            self.assertIn("Integrated Pest Management", reply["response_text"])
            self.assertIn("Pre-Harvest Interval", reply["response_text"])

    def test_conversational_text_qa(self):
        """Verify text-only consultation (knapsack dosage calculation)."""
        reply = self.agent.process_consultation("How do I calculate chemical dosage for a 15-liter backpack sprayer?")
        self.assertIn("response_text", reply)
        self.assertIn("Knapsack Sprayer", reply["response_text"])
        self.assertIn("Mancozeb", reply["response_text"])

    def test_ipm_completeness(self):
        """Verify all 10 YOLO classes have verified IPM treatments."""
        for cid, cname in YOLO_CLASS_NAMES.items():
            self.assertIn(cname, DISEASE_KNOWLEDGE_BASE)
            adv = get_ipm_advisory(cname, 0.12)
            self.assertIn("organic_biocontrol", adv)
            self.assertIn("chemical_control", adv)
            self.assertIn("dosage", adv)
            self.assertIn("pre_harvest_interval_days", adv)

    def test_gradcam_interpretability(self):
        """Verify Grad-CAM saliency map generation for Unit VI & Practical 10."""
        if os.path.exists(self.sample_img_path):
            out_img = os.path.join(base_dir, "..", "Data", "sample_images", "test_gradcam_out.png")
            saved_path, pred_label, severity = explain_leaf_sample(self.sample_img_path, output_path=out_img)
            self.assertTrue(os.path.exists(saved_path), "Grad-CAM output image was not saved!")
            self.assertIsNotNone(pred_label)
            self.assertGreaterEqual(severity, 0.0)
            if os.path.exists(out_img):
                os.remove(out_img)

if __name__ == '__main__':
    unittest.main()
