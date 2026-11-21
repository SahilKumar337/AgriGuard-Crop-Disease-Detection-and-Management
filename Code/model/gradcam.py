"""
AgriGuard Interpretability Engine: Grad-CAM (Gradient-Weighted Class Activation Mapping)
Course: CSE471 | Deep Learning for Computer Vision (Unit VI & Practical 10)

Implements:
1. Grad-CAM for convolutional feature maps (MobileNetV3 / ResNet).
2. Saliency heatmap generation and blending with original leaf imagery.
3. Comparative visualization of correctly classified lesions vs healthy foliage.
"""

import os
import sys

# Ensure project root is in sys.path
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

import cv2
import torch
import torch.nn.functional as F
import numpy as np
from PIL import Image
import torchvision.transforms as transforms

try:
    from Code.model.architecture import build_model
except ImportError:
    from architecture import build_model

class GradCAM:
    """
    Computes Gradient-weighted Class Activation Mapping (Grad-CAM)
    for deep convolutional neural networks.
    
    Formula:
        alpha_k^c = (1 / Z) * sum_i sum_j (d y^c / d A_ij^k)
        L_GradCAM^c = ReLU( sum_k alpha_k^c * A^k )
    """
    def __init__(self, model, target_layer):
        self.model = model
        self.target_layer = target_layer
        self.gradients = None
        self.activations = None
        
        # Register hooks
        self._register_hooks()
        
    def _register_hooks(self):
        def forward_hook(module, input, output):
            self.activations = output.detach()
            
        def backward_hook(module, grad_in, grad_out):
            self.gradients = grad_out[0].detach()
            
        self.target_layer.register_forward_hook(forward_hook)
        self.target_layer.register_full_backward_hook(backward_hook)
        
    def generate_heatmap(self, input_tensor, target_class=None):
        """
        Generates Grad-CAM heatmap for a given input tensor and target class.
        """
        self.model.eval()
        self.model.zero_grad()
        
        # Forward pass
        logits, severity = self.model(input_tensor)
        
        if target_class is None:
            target_class = torch.argmax(logits, dim=1).item()
            
        # Backward pass on target class score
        score = logits[0, target_class]
        score.backward(retain_graph=True)
        
        # Global Average Pooling on gradients -> channel weights alpha_k
        weights = torch.mean(self.gradients, dim=(2, 3), keepdim=True)
        
        # Weighted combination of forward activation maps
        cam = torch.sum(weights * self.activations, dim=1, keepdim=True)
        
        # Apply ReLU to retain features that have positive influence on target class
        cam = F.relu(cam)
        
        # Normalize between 0 and 1
        cam = cam.squeeze().cpu().numpy()
        if np.max(cam) != 0:
            cam = cam / np.max(cam)
        else:
            cam = np.zeros_like(cam)
            
        return cam, target_class, float(severity.squeeze().item())

    @staticmethod
    def overlay_heatmap(image_np, heatmap, alpha=0.5, colormap=cv2.COLORMAP_JET):
        """
        Resizes heatmap to match image dimensions and overlays JET colormap.
        """
        h, w = image_np.shape[:2]
        heatmap_resized = cv2.resize(heatmap, (w, h))
        heatmap_uint8 = np.uint8(255 * heatmap_resized)
        color_heatmap = cv2.applyColorMap(heatmap_uint8, colormap)
        
        # If original image is RGB, convert heatmap to RGB
        color_heatmap = cv2.cvtColor(color_heatmap, cv2.COLOR_BGR2RGB)
        
        # Overlay
        blended = np.float32(color_heatmap) * alpha + np.float32(image_np) * (1 - alpha)
        blended = np.clip(blended, 0, 255).astype(np.uint8)
        return blended, heatmap_resized

def explain_leaf_sample(image_path, model_weights_path="Code/model/weights/agriguard_mobilenetv3.pth", output_path="Data/sample_images/gradcam_explanation.png"):
    """
    Runs Grad-CAM on a leaf image and saves the diagnostic visual explanation.
    """
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = build_model(num_classes=10, pretrained=False)
    
    if os.path.exists(model_weights_path):
        model.load_state_dict(torch.load(model_weights_path, map_location=device))
        print(f"[Grad-CAM] Loaded weights from {model_weights_path}")
    else:
        print("[Grad-CAM] Running in demonstration mode with initialized weights.")
        
    model.to(device)
    model.eval()
    
    # Target layer: last convolutional block of MobileNetV3 features
    target_layer = model.features[-1]
    grad_cam = GradCAM(model, target_layer)
    
    # Load and preprocess image (Unit I: Preprocessing & Normalization)
    orig_img = Image.open(image_path).convert('RGB')
    orig_np = np.array(orig_img)
    
    preprocess = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    
    input_tensor = preprocess(orig_img).unsqueeze(0).to(device)
    
    # Compute CAM
    cam, pred_class, severity = grad_cam.generate_heatmap(input_tensor)
    
    # Overlay on original image
    blended, _ = GradCAM.overlay_heatmap(orig_np, cam)
    
    # Class dictionary
    class_names = [
        "Apple Scab", "Corn Fall Armyworm", "Grape Black Rot", 
        "Healthy Crop", "Potato Early Blight", "Potato Late Blight", 
        "Rice Brown Spot", "Tomato Early Blight", "Tomato Late Blight", 
        "Wheat Leaf Rust"
    ]
    pred_label = class_names[pred_class] if pred_class < len(class_names) else f"Class_{pred_class}"
    
    # Save combined comparison image
    comparison = np.hstack([orig_np, blended])
    
    # Add textual annotation
    annotated = comparison.copy()
    cv2.putText(annotated, f"Input Leaf | Pred: {pred_label} (Severity: {severity*100:.1f}%)", 
                (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(annotated, "Grad-CAM Saliency Heatmap (Red = Necrotic Lesion Focus)", 
                (orig_np.shape[1] + 10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.48, (255, 255, 0), 1, cv2.LINE_AA)
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    Image.fromarray(annotated).save(output_path)
    print(f"[Grad-CAM] Visual explanation saved to: {output_path}")
    return output_path, pred_label, severity

if __name__ == '__main__':
    test_img = "Data/sample_images/tomato_early_blight_sample.jpg"
    if os.path.exists(test_img):
        explain_leaf_sample(test_img)
    else:
        print(f"Sample image {test_img} not found.")
