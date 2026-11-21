import os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

def create_sample_images(output_dir='e:/CSE471/Data/sample_images'):
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. Healthy Leaf
    img_h = Image.new('RGB', (300, 300), color=(240, 245, 235))
    draw_h = ImageDraw.Draw(img_h)
    # Leaf silhouette (ellipse + polygon)
    draw_h.polygon([(150, 30), (220, 110), (240, 180), (180, 260), (150, 280), (120, 260), (60, 180), (80, 110)], fill=(45, 140, 50))
    # Midrib vein
    draw_h.line([(150, 30), (150, 280)], fill=(80, 180, 70), width=4)
    # Side veins
    for y in range(70, 250, 30):
        draw_h.line([(150, y), (150 + int((250-y)*0.4), y - 15)], fill=(70, 160, 60), width=2)
        draw_h.line([(150, y), (150 - int((250-y)*0.4), y - 15)], fill=(70, 160, 60), width=2)
    img_h = img_h.filter(ImageFilter.SMOOTH_MORE)
    img_h.save(os.path.join(output_dir, 'tomato_healthy_sample.jpg'), quality=95)

    # 2. Tomato Early Blight (Target spots with concentric rings)
    img_eb = img_h.copy()
    draw_eb = ImageDraw.Draw(img_eb)
    spots = [(120, 130, 22), (180, 170, 18), (140, 210, 15), (100, 180, 12)]
    for cx, cy, r in spots:
        # Yellow chlorotic halo
        draw_eb.ellipse([cx - r - 6, cy - r - 6, cx + r + 6, cy + r + 6], fill=(190, 185, 45))
        # Outer brown ring
        draw_eb.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(92, 54, 25))
        # Concentric ring
        draw_eb.ellipse([cx - int(r*0.65), cy - int(r*0.65), cx + int(r*0.65), cy + int(r*0.65)], fill=(125, 75, 38))
        # Inner dark core
        draw_eb.ellipse([cx - int(r*0.3), cy - int(r*0.3), cx + int(r*0.3), cy + int(r*0.3)], fill=(50, 30, 15))
    img_eb = img_eb.filter(ImageFilter.SMOOTH)
    img_eb.save(os.path.join(output_dir, 'tomato_early_blight_sample.jpg'), quality=95)

    # 3. Potato Late Blight (Water-soaked dark purplish irregular lesions with pale margins)
    img_lb = img_h.copy()
    draw_lb = ImageDraw.Draw(img_lb)
    # Large water-soaked blights
    draw_lb.polygon([(90, 80), (160, 75), (150, 130), (80, 120)], fill=(65, 50, 50))
    draw_lb.polygon([(160, 150), (220, 160), (210, 230), (140, 200)], fill=(55, 40, 42))
    # Underside white downy mildew edge simulation
    draw_lb.line([(85, 122), (152, 132)], fill=(210, 215, 205), width=3)
    img_lb = img_lb.filter(ImageFilter.GaussianBlur(radius=1.2))
    img_lb.save(os.path.join(output_dir, 'potato_late_blight_sample.jpg'), quality=95)

    # 4. Apple Scab (Velvety olive-green to blackish scab patches)
    img_as = img_h.copy()
    draw_as = ImageDraw.Draw(img_as)
    scabs = [(110, 100), (135, 115), (160, 95), (130, 160), (175, 190), (120, 220)]
    for cx, cy in scabs:
        draw_as.ellipse([cx - 10, cy - 8, cx + 10, cy + 8], fill=(42, 58, 30))
        draw_as.ellipse([cx - 5, cy - 4, cx + 5, cy + 4], fill=(30, 38, 22))
    img_as = img_as.filter(ImageFilter.SMOOTH)
    img_as.save(os.path.join(output_dir, 'apple_scab_sample.jpg'), quality=95)

    # 5. Pest Infestation (Fall Armyworm leaf feeding damage & holes)
    img_pest = img_h.copy()
    draw_pest = ImageDraw.Draw(img_pest)
    # Chewed holes showing background
    draw_pest.ellipse([110, 120, 145, 155], fill=(240, 245, 235))
    draw_pest.ellipse([160, 160, 185, 195], fill=(240, 245, 235))
    # Frass (caterpillar droppings)
    for fx, fy in [(150, 140), (155, 145), (148, 150), (170, 205), (165, 210)]:
        draw_pest.ellipse([fx-2, fy-2, fx+2, fy+2], fill=(60, 45, 20))
    img_pest = img_pest.filter(ImageFilter.SMOOTH)
    img_pest.save(os.path.join(output_dir, 'pest_infestation_sample.jpg'), quality=95)

    print(f"Generated 5 representative test images in {output_dir}")

if __name__ == '__main__':
    create_sample_images()

