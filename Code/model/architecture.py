"""
AgriGuardNet: Dual-Head Lightweight Edge Architecture
Course: CSE471 | Early Detection & Management of Crop Diseases and Pest Infestations
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.models as models

class SqueezeExcitation(nn.Module):
    """
    Squeeze-and-Excitation channel attention block.
    Recalibrates channel-wise feature responses to emphasize subtle micro-lesion cues.
    """
    def __init__(self, in_channels, reduction=16):
        super(SqueezeExcitation, self).__init__()
        reduced_channels = max(in_channels // reduction, 8)
        self.fc1 = nn.Linear(in_channels, reduced_channels, bias=False)
        self.relu = nn.ReLU(inplace=True)
        self.fc2 = nn.Linear(reduced_channels, in_channels, bias=False)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        b, c, _, _ = x.size()
        y = x.view(b, c, -1).mean(dim=2)  # Global Average Pooling
        y = self.fc1(y)
        y = self.relu(y)
        y = self.fc2(y)
        y = self.sigmoid(y).view(b, c, 1, 1)
        return x * y

class AgriGuardNet(nn.Module):
    """
    Edge-Optimized Dual-Head Neural Network:
    - Backbone: MobileNetV3-Large with SE Attention for edge/mobile efficiency.
    - Head 1 (Disease Diagnosis): Predicts disease/pest category.
    - Head 2 (Severity Quantification): Predicts affected leaf percentage (0.0 to 1.0)
      to distinguish Early (Stage 1) from Moderate/Severe infections.
    """
    def __init__(self, num_classes=10, pretrained=True):
        super(AgriGuardNet, self).__init__()
        
        # Load lightweight MobileNetV3 backbone
        weights = models.MobileNet_V3_Large_Weights.DEFAULT if pretrained else None
        base = models.mobilenet_v3_large(weights=weights)
        self.features = base.features
        
        # Channel attention enhancement
        in_features = 960  # MobileNetV3-Large output channels
        self.se_attention = SqueezeExcitation(in_features, reduction=16)
        self.avgpool = nn.AdaptiveAvgPool2d((1, 1))
        
        # Head 1: Disease Classification Head
        self.classifier_head = nn.Sequential(
            nn.Linear(in_features, 256),
            nn.Hardswish(inplace=True),
            nn.Dropout(p=0.3),
            nn.Linear(256, num_classes)
        )
        
        # Head 2: Severity Quantification Head (Percentage of leaf affected)
        self.severity_head = nn.Sequential(
            nn.Linear(in_features, 128),
            nn.Hardswish(inplace=True),
            nn.Dropout(p=0.2),
            nn.Linear(128, 1),
            nn.Sigmoid()  # Constrains predicted ratio between 0.0 and 1.0 (0% - 100%)
        )

    def forward(self, x):
        feat = self.features(x)
        feat = self.se_attention(feat)
        feat = self.avgpool(feat)
        feat = torch.flatten(feat, 1)
        
        disease_logits = self.classifier_head(feat)
        severity_score = self.severity_head(feat)
        
        return disease_logits, severity_score

def build_model(num_classes=10, pretrained=True):
    return AgriGuardNet(num_classes=num_classes, pretrained=pretrained)

if __name__ == '__main__':
    model = build_model(num_classes=10, pretrained=False)
    dummy_input = torch.randn(2, 3, 224, 224)
    logits, severity = model(dummy_input)
    print("AgriGuardNet Architecture Instantiated Successfully:")
    print(f" - Input shape: {dummy_input.shape}")
    print(f" - Disease Logits shape: {logits.shape}")
    print(f" - Severity Output shape: {severity.shape}")

