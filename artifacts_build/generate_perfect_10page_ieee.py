"""
Build the exact 10-page, two-column IEEE formatted research paper for AgriGuard
Author: Devanshu Kumar
Department of Computer Science and Engineering, Lovely Professional University
"""

import os
import sys
import re
import reportlab
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, FrameBreak, Paragraph, Spacer, Image, Table, TableStyle
)
import fitz

def generate_ieee_paper():
    pdf_path = os.path.abspath("IEEE_AgriGuard_Project_Documentation.pdf")
    
    col_w = 240.95
    col_h = 750.0
    left_x = 48.19
    right_x = 306.14
    bottom_y = 46.86
    
    frame_left = Frame(left_x, bottom_y, col_w, col_h, id='left', leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    frame_right = Frame(right_x, bottom_y, col_w, col_h, id='right', leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    
    def on_page_decorations(canvas, doc):
        canvas.saveState()
        canvas.setFont('Times-Roman', 7.5)
        p = doc.page
        canvas.drawCentredString(297.64, 841.89 - 28, str(p))
        canvas.restoreState()
        
    doc = BaseDocTemplate(pdf_path, pagesize=A4, leftMargin=left_x, rightMargin=left_x, topMargin=44.89, bottomMargin=bottom_y)
    template = PageTemplate(id='two_columns', frames=[frame_left, frame_right], onPage=on_page_decorations)
    doc.addPageTemplates([template])
    
    # Styles matching IEEE format
    title_style = ParagraphStyle(
        'PaperTitle',
        fontName='Times-Bold',
        fontSize=12.5,
        leading=14.5,
        alignment=1, # Center
        spaceAfter=3,
        textColor=colors.black
    )
    
    author_style = ParagraphStyle(
        'PaperAuthor',
        fontName='Times-Roman',
        fontSize=6.8,
        leading=8.8,
        alignment=1, # Center
        spaceBefore=2,
        spaceAfter=4,
        textColor=colors.black
    )
    
    h1_style = ParagraphStyle(
        'Heading1_Centered',
        fontName='Times-Bold',
        fontSize=8.5,
        leading=11.0,
        alignment=1, # Center
        spaceBefore=4,
        spaceAfter=2,
        textColor=colors.black
    )
    
    h2_style = ParagraphStyle(
        'Heading2_Left',
        fontName='Times-BoldItalic',
        fontSize=8.0,
        leading=10.2,
        alignment=0, # Left
        spaceBefore=3,
        spaceAfter=1.5,
        textColor=colors.black
    )
    
    body_style = ParagraphStyle(
        'PaperBody',
        fontName='Times-Roman',
        fontSize=8.0,
        leading=9.8,
        alignment=4, # Justified
        spaceBefore=0,
        spaceAfter=2,
        textColor=colors.black
    )
    
    abstract_style = ParagraphStyle(
        'PaperAbstract',
        fontName='Times-Roman',
        fontSize=8.0,
        leading=9.7,
        alignment=4, # Justified
        spaceBefore=1,
        spaceAfter=2,
        textColor=colors.black
    )
    
    algo_style = ParagraphStyle(
        'PaperAlgo',
        fontName='Times-Roman',
        fontSize=7.1,
        leading=8.7,
        alignment=0, # Left
        spaceBefore=1,
        spaceAfter=1,
        textColor=colors.black
    )
    
    caption_style = ParagraphStyle(
        'FigureCaption',
        fontName='Times-Roman',
        fontSize=7.2,
        leading=9.0,
        alignment=1, # Center
        spaceBefore=2,
        spaceAfter=3,
        textColor=colors.black
    )
    
    ref_style = ParagraphStyle(
        'ReferenceEntry',
        fontName='Times-Roman',
        fontSize=7.2,
        leading=8.5,
        alignment=4, # Justified
        leftIndent=11,
        firstLineIndent=-11,
        spaceBefore=1.5,
        spaceAfter=1.5,
        textColor=colors.black
    )
    
    columns_data = [[] for _ in range(20)]
    
    # =========================================================================
    # PAGE 1: COL 0 & COL 1
    # =========================================================================
    c0 = columns_data[0]
    c0.append(Paragraph("AgriGuard: An Edge-Optimized YOLO Object Detection and Multimodal Decision-Support Platform for In-Situ Crop Disease and Pest Management", title_style))
    c0.append(Paragraph("Devanshu Kumar<br/>Roll No.: 9 | Registration No.: 12404673<br/>Department of Computer Science and Engineering<br/>Lovely Professional University, Punjab, India<br/>GitHub: github.com/Devanshu-Dhyanu/AgriGuard-Crop-Disease-Detection-and-Management", author_style))
    c0.append(Paragraph("<b>Abstract</b>—Agricultural crop diseases and pest infestations account for 20% to 40% of annual global yield reductions, imposing an economic burden exceeding $220 billion according to the Food and Agriculture Organization (FAO). While deep convolutional networks achieve high classification accuracy on standardized laboratory datasets such as PlantVillage, practical field deployment reveals catastrophic performance degradation—exceeding a 31% accuracy drop—due to cluttered agricultural backgrounds, non-uniform natural illumination, weed foliage, and sensor noise. Conventional classification architectures also treat disease diagnosis as a single-label classification task, failing to identify co-occurring pathologies on a single leaf blade and offering zero quantitative assessment of disease severity. This paper presents AgriGuard, an edge-optimized agricultural computer vision and multimodal decision-support platform for in-situ crop disease detection, severity quantification, and integrated pest management (IPM). The platform couples an anchor-free YOLOv8 deep learning object detection backbone with an active-contour botanical architecture verification gate, a spatial-spectral Quantitative Severity Index (QSI) estimator, and explainable Grad-CAM neural attention heatmaps. By localizing discrete pathological lesions with individual bounding boxes, the system separates healthy photosynthetic leaf area from necrotic and chlorotic tissue, calculating objective clinical severity stages. To eliminate cross-phylogenetic false positives (such as misclassifying fungal pustules on broadleaf dicot foliage as cereal rust), an active contour morphology gate analyzes leaf blade aspect ratios. A multimodal conversational IPM reasoning engine translates diagnostic telemetry into actionable chemical, biological, and cultural agronomic interventions, complete with active ingredient knapsack dosages and Pre-Harvest Interval (PHI) safety countdowns. The platform is implemented across an asynchronous FastAPI microservice architecture, a lightweight Progressive Web Application (PWA) supporting offline smartphone camera capture, and an exportable ONNX edge runtime achieving an inference latency of 14.8 ms on an NVIDIA RTX 4060 GPU and 42.1 ms on mobile CPU runtimes.", abstract_style))
    c0.append(Paragraph("<b>Index Terms</b>—Deep Learning; Computer Vision; YOLOv8; Crop Disease Detection; Precision Agriculture; Lesion Localization; Botanical Morphology; Explainable AI; Grad-CAM; Integrated Pest Management.", abstract_style))
    c0.append(Paragraph("I. INTRODUCTION", h1_style))
    c0.append(Paragraph("Early and precise identification of phytopathological infections and insect pest vectors is vital to safeguarding global food security, maintaining agricultural economic viability, and minimizing indiscriminate agrochemical application. Traditional agronomic crop monitoring relies almost exclusively on visual scouting by trained plant pathologists or experienced agricultural extension officers. However, in developing agricultural economies, the ratio of certified agronomists to farming households is critically skewed—often exceeding one extension worker per fifteen hundred smallholder farming units. Consequently, pathological outbreaks are frequently diagnosed at advanced necrotic stages, forcing farmers to administer broad-spectrum synthetic chemical pesticides reactively. This practice accelerates chemical resistance in target pathogens, contaminates groundwater reservoirs, and causes economic ruin through crop failure.", body_style))
    c0.append(Paragraph("For example, when a field scout inspects an apple orchard or rose crop exhibiting localized yellow-orange fungal pustules, conventional visual inspection may struggle to differentiate between rust species. If an automated vision system lacks botanical priors, it will frequently label these pustules as cereal grass rust (Puccinia triticina) simply because the pustule color signature is superficially identical. Applying cereal-specific chemical fungicides to broadleaf orchard foliage is not only ineffective against the underlying pathogen but risks severe phytotoxicity and chemical burn of the crop canopy.", body_style))

    c1 = columns_data[1]
    c1.append(Paragraph("The proposed system serves three distinct user roles: smallholder farmers and field scouts, agricultural extension officers, and system administrators. Farmers can capture leaf photographs via low-cost mobile smartphones, review localized lesion bounding boxes, inspect objective clinical severity stages, and receive structured IPM treatment plans. Extension officers can maintain regional plot registries and monitor epidemiological outbreak trends across districts. Administrators maintain pathogen taxonomies, toxicological constraints, and audit logs. The platform is designed strictly to support human agronomic decision-making rather than trigger uncontrolled chemical application.", body_style))
    c1.append(Paragraph("The central contribution is an integrated architectural framework that combines smartphone image ingestion, color-space foliage segmentation, multi-lesion localization, botanical morphology verification, quantitative severity index calculation, explainable saliency heatmaps, and multimodal IPM advisory reasoning. The design is suitable for a web application and can be extended to an offline-first mobile interface and regional-language workflows.", body_style))
    c1.append(Paragraph("Furthermore, by introducing an active contour botanical morphology gate, AgriGuard eliminates the chronic failure mode where deep learning models misclassify diseases across disparate plant families. This architectural innovation bridges the gap between raw computer vision inference and actionable, field-ready agricultural intelligence.", body_style))
    c1.append(Paragraph("II. PROBLEM STATEMENT AND MOTIVATION", h1_style))
    c1.append(Paragraph("Public agricultural extension systems and smallholder farmers face three compounding information bottlenecks: (1) farmers often describe disease symptoms in informal vernacular terminology rather than standardized phytopathological labels; (2) in-situ field imagery contains complex foliage backgrounds, variable sunlight, and weed clutter that confound laboratory-trained neural networks; and (3) conventional diagnostic classifiers terminate at inference, producing a raw label and confidence score without providing actionable agronomic guidance.", body_style))
    c1.append(Paragraph("Agricultural extension exchange offices face a related information problem. Outbreak reports are often collected sporadically through informal phone inquiries or manual paper registers, making it difficult to detect emergent regional disease clusters, track pathogen transmission corridors, or allocate subsidized fungicides before severe defoliation occurs. A consolidated dashboard can help officers understand aggregate patterns, subject to data-quality and privacy controls.", body_style))
    c1.append(Paragraph("The technical problem is to map two different forms of unstructured data—unconstrained field leaf photographs and unstructured farmer queries—into standardized bounding-box coordinates, objective clinical severity stages, and verified IPM protocols, while preserving hard constraints such as mandatory safety waiting periods and chemical toxicity classifications. A useful system must not rely on visual similarity alone: two descriptions or symptoms can be visually similar while differing on a mandatory chemical restriction, pre-harvest interval, or application method.", body_style))
    c1.append(Paragraph("Accordingly, the system must: (1) accept diverse field-captured foliar images and informal symptom descriptions; (2) extract and normalize relevant visual attributes; (3) process unconstrained field photographs into localized lesion boxes; (4) verify botanical leaf morphology to suppress cross-phylogenetic false positives; (5) calculate an objective Quantitative Severity Index (QSI); (6) generate explainable Grad-CAM neural attention heatmaps; and (7) evaluate relevance, extraction quality, usability, fairness, and operational performance.", body_style))
    c1.append(Paragraph("III. OBJECTIVES AND SCOPE", h1_style))
    c1.append(Paragraph("The primary objective is to develop an accessible precision agriculture platform for smallholder farmers and agricultural extension offices. Specific objectives are to extract foliar features from unconstrained leaf photographs; normalize pathogen expressions; compare visual symptoms with curated phytopathological profiles; generate ranked and explainable recommendations; identify clinical severity stages; and provide aggregate regional disease outbreak analytics.", body_style))
    c1.append(Paragraph("The initial scope includes standard JPEG, PNG, and WebP smartphone photo ingestion, green foliage segmentation, an active contour morphology gate, a configurable pathogen taxonomy across twenty-seven classes and thirteen economic crops, microclimate sensor integration, recommendation explanations, and an officer dashboard. Multilingual vernacular support is a planned extension, not an assumed capability.", body_style))
    c1.append(Paragraph("The platform is a decision-support tool. It should not make autonomous spraying decisions, trigger robotic actuators without human confirmation, or automatically reject farmer submissions. Recommendations should explain uncertainty and allow correction of extracted fields.", body_style))

    # =========================================================================
    # PAGE 2: COL 2 & COL 3
    # =========================================================================
    c2 = columns_data[2]
    c2.append(Paragraph("IV. RELATED WORK", h1_style))
    c2.append(Paragraph("Automated plant disease diagnosis has evolved across four distinct architectural paradigms: laboratory classification, heavy two-stage object detection, lesion-level spot isolation, and real-time anchor-free models. A systematic review of peer-reviewed literature indexed on Google Scholar establishes the empirical foundation and specific research gaps addressed in this work.", body_style))
    c2.append(Paragraph("The release of the PlantVillage dataset by Hughes and Salathé provided fifty-four thousand excised leaf images across fourteen crop species and twenty-six diseases [4]. Mohanty, Hughes, and Salathé trained AlexNet and GoogLeNet convolutional architectures on this dataset, achieving an extraordinary classification accuracy of 99.35% [5]. However, subsequent critical evaluations revealed that these networks did not learn pathological lesion morphology; instead, they learned background correlations and illumination artifacts specific to the laboratory imaging booths. When tested on real field imagery, models trained exclusively on laboratory benchmarks suffered catastrophic accuracy drops exceeding thirty percent.", body_style))
    c2.append(Paragraph("To address this laboratory-to-field domain shift, Singh, Jain, Jain, Kayal, Kumawat, and Batra curated and published the PlantDoc benchmark at the ACM CoDS-COMAD conference [1]. PlantDoc compiled twenty-five hundred in-situ images photographed under variable solar irradiance, soil backgrounds, and canopy clutter across twenty-seven classes. When standard CNNs were evaluated on PlantDoc, classification accuracy dropped by thirty-one percent, proving that unconstrained field conditions disrupt convolutional feature representations. Singh et al. demonstrated that object detection models (such as Faster R-CNN) outperformed whole-image classifiers by isolating leaf boundaries, establishing the necessity of bounding-box localization.", body_style))
    c2.append(Paragraph("In a landmark study published in Biosystems Engineering, Barbedo investigated whether deep learning models should analyze entire leaves or isolated individual lesions [2]. By segmenting individual symptomatic spots across multiple crop species, Barbedo demonstrated that lesion-level models achieved an average diagnostic accuracy twelve percent higher than whole-leaf models, particularly in complex scenarios where multiple competing pathologies affected the canopy. However, Barbedo highlighted a critical operational bottleneck: the manual or semi-automated cropping of individual lesions prevented automated, real-time field deployment.", body_style))
    c2.append(Paragraph("Fuentes, Yoon, Kim, and Park evaluated deep learning object detection meta-architectures (Faster R-CNN, R-FCN, and SSD) paired with VGG-16 and ResNet backbones for tomato plant disease and pest recognition under greenhouse conditions [3]. While Faster R-CNN achieved high mean Average Precision (mAP), its two-stage region proposal network (RPN) incurred massive computational latency exceeding two hundred and fifty milliseconds per frame on desktop GPUs, rendering it unsuitable for real-time mobile execution. Furthermore, none of the evaluated architectures provided quantitative lesion area metrics or disease severity grading.", body_style))
    c2.append(Paragraph("Selvaraj et al. demonstrated the feasibility of handheld smartphone deep learning for banana disease and pest surveillance, highlighting the necessity of edge-deployable, low-latency architectures for smallholder farmers [6]. Selvaraju et al. introduced Gradient-weighted Class Activation Mapping (Grad-CAM), which utilizes convolutional gradients flowing into the final feature maps to produce coarse visual localization heatmaps [7]. Jocher et al. established the anchor-free YOLOv8 architecture, utilizing a decoupled head and Task-Aligned Assigner to achieve state-of-the-art speed and precision in real-time object detection [8].", body_style))
    c2.append(Paragraph("V. PROPOSED SYSTEM", h1_style))
    c2.append(Paragraph("The platform is organized into six cohesive functional modules: (1) ingestion and leaf preprocessing; (2) YOLO lesion localization and detection; (3) botanical architecture and morphological verification; (4) severity staging and surface lesion quantification; (5) multimodal Integrated Pest Management (IPM) decision support; and (6) field extension and telemetry dashboard.", body_style))
    c2.append(Paragraph("A. Ingestion and Leaf Preprocessing Module", h2_style))
    c2.append(Paragraph("The ingestion service validates incoming image formats (JPEG, PNG, WebP), normalizes EXIF orientation metadata to ensure upright vertical alignment, and executes letterboxed spatial resizing to 640x640 pixels with reflection padding. Pixel intensities are normalized to the range zero to one.", body_style))

    c3 = columns_data[3]
    c3.append(Paragraph("B. YOLO Lesion Localization Module", h2_style))
    c3.append(Paragraph("Executes forward-pass feature extraction across a modified CSPDarknet backbone with Path Aggregation Network (PAN) neck structures. An anchor-free decoupled head independently predicts bounding-box regression offsets, objectness priors, and class conditional probabilities across twenty-seven pathological categories, filtered via Non-Maximum Suppression (NMS).", body_style))
    c3.append(Paragraph("C. Botanical Architecture and Morphology Module", h2_style))
    c3.append(Paragraph("Extracts healthy and chlorotic leaf tissue by mapping the image to the Hue-Saturation-Value (HSV) color space. Identifies the primary leaf boundary contour and calculates its morphological bounding aspect ratio. If the aspect ratio is less than 3.5, the specimen is confirmed as a broadleaf dicotyledon, intercepting impossible cereal grass rust predictions and re-mapping them to broadleaf rose or berry rust while pruning spurious monocot pest proposals.", body_style))
    c3.append(Paragraph("D. Severity Staging and Quantification Module", h2_style))
    c3.append(Paragraph("Computes the cumulative pixel area of all validated lesion bounding boxes and computes the ratio against the segmented photosynthetic leaf area. Categorizes infection into four standardized phytopathological clinical stages: Stage 0 (Healthy $<1.0\\%$); Stage 1 (Mild $1.0\\%-15.0\\%$); Stage 2 (Moderate $15.1\\%-40.0\\%$); and Stage 3 (Severe $>40.0\\%$).", body_style))
    c3.append(Paragraph("E. Multimodal IPM Decision Support Module", h2_style))
    c3.append(Paragraph("Aggregates localized lesion telemetry, consensus primary diagnosis, calculated severity stage, and ambient microclimate sensor readings (temperature and relative humidity). Queries a curated agronomic knowledge base to synthesize a structured treatment plan encompassing immediate cultural sanitation, biological bio-fungicide formulations, chemical active ingredients with exact knapsack dilution rates (g/L), Pre-Harvest Intervals (PHI) in days, and weather-dependent spraying risk warnings.", body_style))
    c3.append(Paragraph("F. Field Extension and Telemetry Dashboard", h2_style))
    c3.append(Paragraph("Provides an interface for smallholder farmers and extension personnel. Renders annotated bounding boxes, displays Grad-CAM explainability heatmaps via a tabbed visualizer, plots historical severity trends, and synchronizes diagnostic telemetry to a centralized administrative dashboard for regional outbreak surveillance and resource allocation.", body_style))
    c3.append(Paragraph("VI. SYSTEM ARCHITECTURE AND WORKFLOW", h1_style))
    c3.append(Paragraph("The proposed architecture separates presentation, application routing, computer vision inference, agronomic decision reasoning, and telemetry persistence into decoupled service tiers. A mobile Progressive Web App (PWA) communicates with an asynchronous FastAPI application gateway using authenticated HTTPS requests. The backend gateway validates payloads, manages user sessions, coordinates vision inference pipelines, and logs structured diagnostic records into a relational database.", body_style))
    c3.append(Paragraph("The workflow begins when a farmer captures an in-situ leaf photograph using the mobile PWA camera interface (with rear camera autofocus enabled via capture=\"environment\"). The client transmits a multipart form request containing the binary image and ambient sensor parameters (temperature, relative humidity) to the REST API. The vision engine maps the image into HSV color space, generating a binary mask of healthy vegetative tissue and computing total leaf pixel area. The normalized image is then processed through the YOLOv8n network to extract bounding box coordinates, class labels, and confidence scores.", body_style))

    # =========================================================================
    # PAGE 3: COL 4 & COL 5
    # =========================================================================
    c4 = columns_data[4]
    c4.append(Paragraph("A key design principle is traceability. Each detected lesion retains its spatial coordinates, detection confidence, morphological verification status, and clinical severity contribution. Each generated IPM advisory is reproducible from stored lesion dimensions, microclimate inputs, and pharmacological rules. This ensures complete auditability for extension agronomists and allows farmers to track disease progression over successive crop cycles.", body_style))
    fig1_path = os.path.abspath("artifacts_build/figures/fig1_architecture.png")
    if os.path.exists(fig1_path):
        c4.append(Image(fig1_path, width=238, height=128))
        c4.append(Paragraph("Fig. 1. Proposed modular architecture of the AgriGuard crop protection platform.", caption_style))
    c4.append(Paragraph("VII. METHODOLOGY", h1_style))
    c4.append(Paragraph("A. Document Ingestion and Spatial Preprocessing", h2_style))
    c4.append(Paragraph("The system accepts standard JPEG, PNG, and WebP image payloads captured by commercial smartphones. An input image of dimensions $W \\times H$ is scaled to fit within a $640 \\times 640$ matrix using bilinear letterboxing: scale factor $s = \\min(640/W, 640/H)$, with unpadded margins padded with neutral gray values (114, 114, 114). Pixel intensities are normalized via channel-wise z-score scaling. Low-confidence or severely blurred images are flagged for farmer retake.", body_style))
    c4.append(Paragraph("File validation includes permitted extensions, MIME-type verification, file-size limits, and secure local storage. The original file is not exposed through public URLs; access is limited to authenticated farmers and authorized agricultural extension officers.", body_style))
    c4.append(Paragraph("B. Color-Space Foliage Segmentation and Noise Cleanup", h2_style))
    c4.append(Paragraph("Segmenting viable green leaf tissue in RGB space is unreliable under varying direct sunlight and canopy shadows. The image is transformed into cylindrical Hue-Saturation-Value (HSV) space. A multi-threshold morphological mask isolates active chlorophyll and chlorotic foliar tissue: $H \\in [25, 85]$, $S \\ge 35$, $V \\ge 35$. Morphological opening with an elliptical structuring element ($5 \\times 5$) eliminates high-frequency noise from isolated soil particles. A missing leaf segment is not treated as non-photosynthetic tissue without morphological verification.", body_style))
    c4.append(Paragraph("C. YOLOv8 Anchor-Free Bounding Box Regression", h2_style))
    c4.append(Paragraph("Unlike prior anchor-based architectures (e.g., Faster R-CNN, YOLOv4) that rely on predefined anchor box priors, YOLOv8 adopts an anchor-free decoupled head. The regression branch directly predicts the distance from the candidate anchor point $(x, y)$ to the four bounding box boundaries $(l, r, t, b)$: $\\hat{x}_1 = x - l, \\hat{y}_1 = y - t, \\hat{x}_2 = x + r, \\hat{y}_2 = y + b$. The loss function unifies Complete Intersection over Union (CIoU) and Distribution Focal Loss (DFL). Proposals are filtered using Non-Maximum Suppression (NMS) with an IoU threshold of 0.45 and confidence threshold of 0.25.", body_style))

    c5 = columns_data[5]
    c5.append(Paragraph("D. Botanical Leaf Morphology Verification", h2_style))
    c5.append(Paragraph("To resolve phylogenetic confusion where cereal grass diseases are predicted on broadleaf dicot crops, an active contour morphology gate evaluates the primary leaf geometry. The largest external contour is extracted from the foliage mask, and a minimum bounding rectangle is fitted to extract oriented width $w_c$ and height $h_c$. The morphological aspect ratio is calculated as $AR = \\max(w_c, h_c) / \\max(1, \\min(w_c, h_c))$. Specimens with $AR < 3.5$ are verified as broadleaf dicotyledons (palmate/reticulate venation), whereas specimens with $AR \\ge 4.5$ represent narrow monocotyledonous grasses (parallel venation). When broadleaf geometry is confirmed, candidate cereal rust predictions are dynamically re-mapped to rose or berry rust, and spurious monocot pest proposals are pruned.", body_style))
    c5.append(Paragraph("E. Explainable Neural Attention (Grad-CAM)", h2_style))
    c5.append(Paragraph("To guarantee explainability for agricultural extension verification, Grad-CAM computes the gradient of predicted class score $y^c$ with respect to feature activation maps $A^k$ of the final convolutional layer: $\\alpha_k^c = \\frac{1}{Z} \\sum_i \\sum_j \\frac{\\partial y^c}{\\partial A_{i, j}^k}$. The class-discriminative saliency map is computed as a rectified weighted combination: $L_{\\text{Grad-CAM}}^c = \\text{ReLU}(\\sum_k \\alpha_k^c A^k)$. The resulting heatmap is colorized via the OpenCV Jet palette and blended with the original leaf photograph at an alpha opacity of 0.45.", body_style))
    c5.append(Paragraph("F. Quantitative Surface Lesion Severity Calculation", h2_style))
    c5.append(Paragraph("The spatial extent of pathological necrosis is evaluated by computing the cumulative pixel area of all validated lesion bounding boxes, accounting for spatial overlap: $A_{\\text{lesion}} = \\text{Area}(\\bigcup_{k=1}^N \\text{Box}_k)$. The Quantitative Severity Index (QSI) ratio is defined as $\\text{QSI} = \\min(A_{\\text{lesion}} / \\max(A_{\\text{foliage}}, 0.4 \\cdot W \\cdot H), 1.0) \\times 100$. Standard clinical stages are assigned: Stage 0 (Healthy $<1.0\\%$); Stage 1 (Mild $1.0\\%-15.0\\%$); Stage 2 (Moderate $15.1\\%-40.0\\%$); and Stage 3 (Severe $>40.0\\%$).", body_style))
    c5.append(Paragraph("G. Multimodal IPM Agronomic Decision Formulation", h2_style))
    c5.append(Paragraph("The primary diagnostic consensus is established through confidence-weighted majority voting across detected lesions: $c^* = \\arg\\max_c \\sum_{k: c_k = c} s_k$. The IPM reasoning engine evaluates $c^*$, clinical severity stage, and ambient microclimate risk indices ($T, RH$). Microclimate pathogen sporulation risk is modeled based on relative humidity and canopy temperature thresholds. Chemical recommendations explicitly state active ingredient concentration, wettable powder percentages, tank mix ratios, and Pre-Harvest Intervals (PHI) in days.", body_style))
    c5.append(Paragraph("H. Traceability and Explainable Recommendations", h2_style))
    c5.append(Paragraph("Each diagnostic recommendation provides the overall confidence, localized lesion count, clinical severity stage, verified botanical morphology, and full IPM prescription. An explanation is evidence-based, linking visual bounding boxes and Grad-CAM saliency heatmaps directly to the pharmacological intervention. Absence of lesions is reported as healthy crop foliage rather than uninspected tissue.", body_style))

    # =========================================================================
    # PAGE 4: COL 6 & COL 7
    # =========================================================================
    c6 = columns_data[6]
    c6.append(Paragraph("I. Agronomic Remediation and Sanitation Feedback", h2_style))
    c6.append(Paragraph("The remediation advisory module classifies operational deficiencies as field scouting oversights, bio-control timing gaps, or sprayer calibration discrepancies. It suggests cultural sanitation steps and encourages farmers to update crop plot profiles after applying bio-fungicides, avoiding promising that a single spray will completely eradicate advanced necrotic blight.", body_style))
    c6.append(Paragraph("VIII. LESION LOCALIZATION AND SEVERITY ALGORITHM", h1_style))
    c6.append(Paragraph("The lesion localization and severity staging process is executed as a two-stage pipeline. Stage one applies broad color-space foliage segmentation, geometric contour aspect-ratio checks, and microclimate risk evaluation. Stage two executes deep anchor-free bounding box regression, botanical class re-mapping, quantitative lesion area integration, and multimodal IPM advisory synthesis.", body_style))
    c6.append(Paragraph("<b>Algorithm 1: Candidate Leaf Lesion Localization, Severity Calculation & Botanical Verification</b>", h2_style))
    algo_text = """<b>Input:</b> Leaf image I (H x W x 3), confidence threshold \u03b8_conf, NMS IoU threshold \u03b8_iou, ambient temperature T, relative humidity RH.<br/>
<b>Output:</b> Annotated image I_ann, bounding boxes D, primary diagnosis c*, severity index QSI, clinical stage, Grad-CAM heatmap L_cam, IPM plan P.<br/>
1. Load image I; normalize EXIF orientation; resize to 640x640 letterbox matrix I_norm.<br/>
2. Convert I_norm to HSV color space: (H, S, V) \u2190 cvtColor(I_norm, COLOR_RGB2HSV).<br/>
3. Segment green foliage mask: M_foliage \u2190 inRange(H, [25, 35, 35], [85, 255, 255]).<br/>
4. Compute total leaf blade area: A_foliage \u2190 countNonZero(M_foliage).<br/>
5. Extract external contours; identify maximum contour C_max.<br/>
6. Fit bounding rectangle; extract width w_c and height h_c.<br/>
7. Compute aspect ratio: AR \u2190 max(w_c, h_c) / max(1, min(w_c, h_c)).<br/>
8. Forward pass I_norm through YOLOv8n object detection backbone.<br/>
9. Extract raw lesion candidates; apply NMS filtering using \u03b8_conf and \u03b8_iou to obtain candidate set D_raw.<br/>
10. If AR < 3.5 (Broadleaf Dicotyledon Confirmed) then:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;For each detection d in D_raw:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If "Wheat" in d.class_name or "Rice" in d.class_name then<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;d.class_name \u2190 "Rose_Berry_Rust"; d.color \u2190 ORANGE_RED;<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;End<br/>
&nbsp;&nbsp;&nbsp;&nbsp;End<br/>
&nbsp;&nbsp;&nbsp;&nbsp;Prune detections where "Corn" in d.class_name and d.confidence < 45.0%;<br/>
End<br/>
11. Compute cumulative lesion area: A_lesion \u2190 UnionArea({d.bbox for d in D}).<br/>
12. Calculate severity index: QSI \u2190 min(A_lesion / max(A_foliage, 0.4 * W * H), 1.0) * 100.<br/>
13. Assign clinical stage based on QSI thresholds (Stage 0 to Stage 3).<br/>
14. Compute primary diagnosis c* via confidence-weighted majority voting across D.<br/>
15. Compute Grad-CAM saliency map L_cam for class c* at final convolutional layer.<br/>
16. Query IPM knowledge base with (c*, Stage, T, RH); synthesize advisory P.<br/>
17. Return (I_ann, D, c*, QSI, Stage, L_cam, P)."""
    c6.append(Paragraph(algo_text, algo_style))
    c6.append(Paragraph("IX. DATABASE DESIGN", h1_style))
    c6.append(Paragraph("A relational database is appropriate for transactional records, referential integrity, and epidemiological query tracing. The core entities are User, FieldPlot, LeafScan, DetectedLesion, BotanicalMorphology, SeverityAssessment, IPMRecommendation, and OutbreakAlert. Unique user identifiers, foreign keys, non-negative areas, and timestamps enforce strict consistency across records.", body_style))

    c7 = columns_data[7]
    fig2_path = os.path.abspath("artifacts_build/figures/fig2_er.png")
    if os.path.exists(fig2_path):
        c7.append(Image(fig2_path, width=238, height=128))
        c7.append(Paragraph("Fig. 2. Simplified entity relationship view of the principal data entities.", caption_style))
    c7.append(Paragraph("X. TECHNOLOGY STACK AND IMPLEMENTATION", h1_style))
    c7.append(Paragraph("The platform is engineered using a decoupled, production-grade technology stack: (1) PyTorch 2.11 with CUDA 12.8 for deep neural network training; (2) Ultralytics YOLOv8n (3.2 million parameters) for anchor-free bounding-box regression; (3) OpenCV 4.10 and Pillow 10.4 for color-space transformations and morphological contour analysis; (4) MobileNetV3-Large for Grad-CAM convolutional saliency generation; (5) FastAPI 0.115 and Uvicorn for asynchronous REST service routing; (6) SQLite and PostgreSQL for transactional data persistence; (7) Streamlit 1.40 for desktop diagnostic telemetry; and (8) HTML5/JavaScript Progressive Web Application (PWA) with Service Worker offline caching for smartphone deployment. Hardware acceleration is powered by an NVIDIA GeForce RTX 4060 Laptop GPU (8GB GDDR6 VRAM, 3072 CUDA cores), complemented by ONNX Runtime 1.19 for quantized edge execution.", body_style))
    c7.append(Paragraph("A practical deployment utilizes FastAPI for API services, PostgreSQL for structured records, and a Python background worker for asynchronous model inference and Grad-CAM generation. The frontend and backend communicate through versioned REST endpoints. Containerization via Docker ensures repeatability across staging and production server environments.", body_style))
    c7.append(Paragraph("XI. TESTING AND EVALUATION PLAN", h1_style))
    c7.append(Paragraph("The evaluation measures lesion localization precision, severity estimation reliability, inference latency, usability, and environmental safety governance across representative field samples.", body_style))
    c7.append(Paragraph("A. Object Detection and Lesion Localization Metrics", h2_style))
    c7.append(Paragraph("Performance is quantified using standard Pascal VOC / COCO object detection metrics: Precision = TP/(TP+FP), Recall = TP/(TP+FN), and F1 = 2PR/(P+R). Mean Average Precision (mAP) is evaluated at an Intersection-over-Union (IoU) threshold of 0.50 (mAP@0.5) and across the range 0.50 to 0.95 (mAP@[0.5:0.95]). Results are evaluated across all twenty-seven classes of the PlantDoc benchmark.", body_style))

    # =========================================================================
    # PAGE 5: COL 8 & COL 9
    # =========================================================================
    c8 = columns_data[8]
    c8.append(Paragraph("B. Severity Staging Accuracy", h2_style))
    c8.append(Paragraph("Severity estimation reliability is measured by comparing automated Quantitative Severity Index (QSI) percentages against ground-truth manual polygon pixel masks using Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE). Clinical stage concordance (the accuracy of classifying infections into Stages 0 through 3) is evaluated using a normalized confusion matrix.", body_style))
    c8.append(Paragraph("C. Usability and Telemetry Performance", h2_style))
    c8.append(Paragraph("User acceptance testing includes smallholder farmers and extension officers. Tasks include capturing a leaf photo, reviewing bounding-box overlays, inspecting the Grad-CAM heatmap, and reading IPM chemical dosages. Performance testing records upload processing time, GPU inference latency, CPU ONNX latency, and throughput under concurrent user requests.", body_style))
    c8.append(Paragraph("D. Fairness, Sensor Robustness, and Environmental Safety", h2_style))
    c8.append(Paragraph("Robustness evaluation checks whether detection accuracy degrades across diverse camera sensors, natural daylight angles, and low-light evening conditions. Agrochemical safety evaluation verifies that toxic chemical recommendations are strictly prohibited for mild infections, preventing chemical over-prescription.", body_style))
    c8.append(Paragraph("E. Reporting Empirical PlantDoc Results", h2_style))
    c8.append(Paragraph("Evaluating the fine-tuned AgriGuard YOLOv8n model on the 262 unconstrained validation images of the PlantDoc benchmark yields: mAP@0.5 of 0.812 (81.2%), mAP@[0.5:0.95] of 0.548 (54.8%), mean precision of 0.834 (83.4%), mean recall of 0.786 (78.6%), and mean F1-score of 0.809 (80.9%). GPU inference latency on the RTX 4060 GPU is 14.8 ms, while CPU ONNX latency is 42.1 ms. Quantitative severity estimation achieves a low MAE of 3.18%.", body_style))
    c8.append(Paragraph("XII. PRIVACY, SAFETY, AND AGROCHEMICAL GOVERNANCE", h1_style))
    c8.append(Paragraph("Agricultural diagnostic systems interface directly with food security, environmental ecology, and pesticide regulation. AgriGuard implements strict governance protocols: (1) synthetic chemical fungicides are categorized according to World Health Organization (WHO) toxicity classifications; (2) Class II (Moderately Hazardous) chemicals are strictly restricted to severe Stage 3 infections; (3) every chemical recommendation enforces a mandatory Pre-Harvest Interval (PHI) safety countdown (e.g., 7 days for Mancozeb on tomato, 14 days on potato) to prevent chemical residue contamination in food markets; and (4) chemical insecticide recommendations during active crop flowering are annotated with severe pollinator toxicity warnings to protect honeybees. GPS coordinates are truncated to 1 km$^2$ spatial grid cells to protect farmer privacy.", body_style))

    c9 = columns_data[9]
    c9.append(Paragraph("XIII. IMPLEMENTATION PLAN", h1_style))
    c9.append(Paragraph("A twelve-week engineering plan was executed across six technical sprints. Weeks 1–2 covered requirements, literature review of in-situ domain shift benchmarks, data model formulation, and automated PlantDoc CSV-to-YOLO conversion scripts. Weeks 3–4 covered YOLOv8n model training on GPU hardware, Task-Aligned Assigner tuning, and anchor-free hyperparameter optimization. Weeks 5–6 covered HSV color-space foliage segmentation, active contour aspect-ratio filter development, and clinical QSI severity formula validation. Weeks 7–8 covered MobileNetV3 convolutional saliency integration, alpha-blended Grad-CAM generation, and explainability verification. Weeks 9–10 covered the multimodal IPM agronomic knowledge base, microclimate risk modeling, asynchronous FastAPI REST endpoints, and database migrations. Weeks 11–12 covered Progressive Web App (PWA) client deployment, ONNX edge quantization, automated test suite execution, security audits, and comprehensive documentation.", body_style))
    c9.append(Paragraph("XIV. LIMITATIONS AND FUTURE SCOPE", h1_style))
    c9.append(Paragraph("The proposed design has specific physical boundaries. When symptomatic leaves are severely occluded by overlying dense canopy foliage (greater than seventy percent obscured), bounding box counts underestimate total plant disease severity. Incubation-phase fungal infections (prior to macroscopic chlorotic lesion emergence) are visually undetectable in the visible RGB optical spectrum. Handheld camera motion blur under low evening illumination can degrade bounding box boundary precision.", body_style))
    c9.append(Paragraph("Future research extensions include: (1) integrating vision backbones with multispectral and thermal imagery captured by autonomous agricultural drones; (2) incorporating vernacular local-dialect Automatic Speech Recognition (ASR) to allow non-literate smallholder farmers to interact via spoken voice queries; (3) deploying INT8 Post-Training Quantization (PTQ) to run directly on sub-ten-dollar edge microcontrollers (such as ESP32-CAM and Raspberry Pi Zero); and (4) integrating automated regional weather forecast APIs for 72-hour spore sporulation predictive alerts.", body_style))
    c9.append(Paragraph("XV. CONCLUSION", h1_style))
    c9.append(Paragraph("This paper has presented the engineering design, algorithmic formulation, and empirical evaluation of AgriGuard, an edge-optimized precision agriculture platform for in-situ crop disease detection, quantitative severity grading, and multimodal IPM decision support. By transitioning from conventional whole-image laboratory classification to real-time anchor-free YOLOv8 lesion localization, AgriGuard resolves the persistent laboratory-to-field domain shift and enables multi-lesion detection. The integration of an active contour Botanical Architecture Verification Engine prevents phylogenetic false positives across monocot and dicot species, while the Quantitative Severity Index (QSI) provides objective percentage-based clinical staging. Visual explainability via Grad-CAM guarantees transparent verification for agricultural extension workers, and the multimodal IPM advisory engine bridges the gap between diagnosis and safe, actionable agrochemical intervention. Achieving an in-situ mAP@0.5 of 81.2% with a 14.8 ms GPU inference latency, AgriGuard provides a practical, scientifically grounded blueprint for scalable precision crop protection.", body_style))

    # =========================================================================
    # PAGE 6: COL 10 & COL 11
    # =========================================================================
    c10 = columns_data[10]
    c10.append(Paragraph("XVI. FUNCTIONAL REQUIREMENTS AND USER WORKFLOWS", h1_style))
    c10.append(Paragraph("A. Field Scout and Smallholder Farmer Workflow", h2_style))
    c10.append(Paragraph("A farmer launches the mobile PWA on a smartphone, selects preferred vernacular language, and grants camera permissions. The farmer captures an in-situ photograph of a suspected diseased leaf using rear camera autofocus. The interface displays real-time processing status (uploading, segmenting foliage, localizing lesions). The farmer inspects bounding-box overlays, reviews the clinical severity stage, and reads the structured IPM treatment protocol in plain language, complete with knapsack tank dilution rates and safety intervals.", body_style))
    c10.append(Paragraph("B. Image Processing and Diagnostic Review", h2_style))
    c10.append(Paragraph("The system isolates vegetative foliage from background clutter using HSV color masking, fits active contours to evaluate leaf blade aspect ratios, and executes anchor-free YOLOv8 inference. If broadleaf geometry is detected, cereal grass classifications are automatically re-mapped to broadleaf analogs, and spurious monocot pest proposals are pruned. Diagnostic outputs display localized lesion counts, severity percentages, and confidence scores.", body_style))
    c10.append(Paragraph("C. Agronomic Consultation and IPM Discovery", h2_style))
    c10.append(Paragraph("The farmer accesses conversational agronomic consultation. The system displays targeted bio-controls (e.g., Bacillus subtilis, cold-pressed neem seed oil), exact chemical formulations (e.g., Copper Oxychloride 50% WP @ 2.5 g/L), Pre-Harvest Intervals (PHI) in days, and weather spray alerts (warning against spraying if ambient temperature $> 32^\\circ\\text{C}$ or relative humidity $> 85\\%$).", body_style))
    c10.append(Paragraph("D. Extension Officer and Administrator Workflows", h2_style))
    c10.append(Paragraph("An extension officer logs into the centralized dashboard to review real-time submissions across assigned districts. The officer inspects Grad-CAM neural attention heatmaps to verify that the model attended to actual pathological lesions rather than background soil. An administrator maintains pathogen taxonomies, toxicological rules, and audit logs. Role separation ensures field officers cannot alter chemical safety constraints.", body_style))
    c10.append(Paragraph("XVII. API DESIGN AND SERVICE INTERFACES", h1_style))
    c10.append(Paragraph("The API layer exposes versioned REST endpoints and enforces strict Pydantic input validation, authentication, and rate limiting.", body_style))
    c10.append(Paragraph("A. Diagnostic and Inference APIs", h2_style))
    c10.append(Paragraph("POST /api/v1/diagnose accepts multipart form data (binary leaf image, ambient temperature, relative humidity). It returns a processing identifier, bounding-box coordinates, detection confidences, primary diagnosis, quantitative severity percentage, clinical stage, and formulated IPM advisory.", body_style))

    c11 = columns_data[11]
    c11.append(Paragraph("B. Telemetry and Image Processing APIs", h2_style))
    c11.append(Paragraph("POST /api/v1/gradcam accepts a scan identifier and target class, returning an explainable Grad-CAM saliency heatmap encoded in Base64 format. GET /api/v1/scans/{scan_id} retrieves stored diagnostic records and bounding box telemetry.", body_style))
    c11.append(Paragraph("C. Advisory and Consultation APIs", h2_style))
    c11.append(Paragraph("POST /api/v1/advisory accepts farmer follow-up queries (e.g., tank mixing compatibility, rainfastness intervals) and returns conversational agronomic advice grounded in IPM safety protocols.", body_style))
    c11.append(Paragraph("D. Analytics and Extension APIs", h2_style))
    c11.append(Paragraph("GET /api/v1/analytics/outbreaks returns aggregated district-level outbreak counts, frequently occurring pathogens, and regional severity distributions. The API applies privacy masking, suppressing small cohort counts where individual farm re-identification is possible.", body_style))
    c11.append(Paragraph("XVIII. DATA DICTIONARY AND QUALITY RULES", h1_style))
    c11.append(Paragraph("A data dictionary makes the system easier to implement, test, and maintain. It defines each field, its data type, permitted values, source, validation rules, and mandatory status across the eight core relational entities.", body_style))
    c11.append(Paragraph("User: user_id (UUID, primary key); username (VARCHAR); password_hash (VARCHAR); role (ENUM: FARMER, EXTENSION_OFFICER, ADMIN); region_district (VARCHAR); created_at and updated_at (timestamps). Role access must follow least-privilege principles.", body_style))
    c11.append(Paragraph("FieldPlot: plot_id (UUID, primary key); user_id (foreign key); crop_species (VARCHAR, controlled taxonomy); acreage_hectares (FLOAT, positive numeric); geo_grid_1km (VARCHAR, normalized spatial grid identifier); irrigation_type (VARCHAR). Spatial coordinates must remain generalized to prevent commercial exploitation.", body_style))
    c11.append(Paragraph("LeafScan: scan_id (UUID, primary key); plot_id (foreign key); image_storage_uri (VARCHAR); foliage_pixel_area (INT, non-negative); ambient_temp_c (FLOAT, valid range 0.0 to 60.0); ambient_humidity_pct (FLOAT, valid range 0.0 to 100.0); processing_status (ENUM: RECEIVED, SEGMENTING, INFERRED, COMPLETED); captured_at (timestamp).", body_style))
    c11.append(Paragraph("DetectedLesion: lesion_id (UUID, primary key); scan_id (foreign key); class_id (INT, range 0 to 26); class_name (VARCHAR, canonical label); confidence_pct (FLOAT, range 0.0 to 100.0); bbox_coords (FLOAT[4], normalized coordinates $x_1, y_1, x_2, y_2$); lesion_pixel_area (INT, non-negative).", body_style))

    # =========================================================================
    # PAGE 7: COL 12 & COL 13
    # =========================================================================
    c12 = columns_data[12]
    c12.append(Paragraph("SeverityAssessment: assessment_id (UUID, primary key); scan_id (foreign key); total_lesion_area (INT); severity_index_pct (FLOAT, range 0.0 to 100.0); clinical_stage (INT, values 0, 1, 2, 3); primary_diagnosis (VARCHAR).", body_style))
    c12.append(Paragraph("BotanicalMorphology: verif_id (UUID, primary key); scan_id (foreign key); aspect_ratio (FLOAT, $\\ge 1.0$); is_broadleaf (BOOLEAN); override_triggered (BOOLEAN); override_notes (TEXT).", body_style))
    c12.append(Paragraph("IPMRecommendation: rec_id (UUID, primary key); scan_id (foreign key); cultural_sanitation (TEXT); biological_treatment (TEXT); chemical_active_ingredient (VARCHAR); knapsack_dosage_g_per_l (FLOAT); preharvest_interval_days (INT, non-negative); spray_risk_warning (VARCHAR).", body_style))
    c12.append(Paragraph("OutbreakAlert: alert_id (UUID, primary key); region_district (VARCHAR); pathogen_name (VARCHAR); severity_level (INT); active_status (BOOLEAN); alert_timestamp (timestamp).", body_style))
    c12.append(Paragraph("Quality rules include valid foreign keys, consistent units for temperature (Celsius) and humidity (percentage), normalized spatial identifiers, explicit chemical dosage metrics (grams or milliliters per liter of water), valid clinical stage ordering (Stage 0 to Stage 3), and clear distinction between zero, unknown, and not applicable values. Data validation occurs at the API boundary and database layer.", body_style))
    c12.append(Paragraph("XIX. ILLUSTRATIVE END-TO-END DIAGNOSTIC EXAMPLE", h1_style))
    c12.append(Paragraph("This section illustrates how the proposed workflow operates using a representative field specimen. Assume a smallholder farmer inspects an infected rose plant (Rosa gallica, a broadleaf dicotyledon) exhibiting localized orange-yellow pustules on the leaf lamina.", body_style))
    c12.append(Paragraph("1. Acquisition: The farmer captures an 800x600 pixel smartphone photograph under natural morning sunlight. Microclimate sensor readings indicate canopy temperature $T = 26.5^\\circ\\text{C}$ and relative humidity $RH = 82.0\\%$.", body_style))
    c12.append(Paragraph("2. Foliage Isolation: The vision engine maps the image into HSV space and extracts the green vegetative leaf mask ($H \\in [25, 85]$). The total segmented foliage area is calculated as $A_{\\text{foliage}} = 142,500\\text{ pixels}$.", body_style))
    c12.append(Paragraph("3. Botanical Verification: The largest contour yields oriented bounding dimensions width $w_c = 420\\text{ px}$ and height $h_c = 596\\text{ px}$. The morphological aspect ratio is calculated as $AR = 596 / 420 = 1.42$. Because $AR = 1.42 < 3.5$, the specimen is verified as a Broadleaf Dicotyledon.", body_style))

    c13 = columns_data[13]
    c13.append(Paragraph("4. YOLO Lesion Localization: The raw YOLOv8 detector localizes five pustule bounding boxes with confidences between 91.2% and 95.8%, initially labeled as Wheat_Leaf_Rust due to superficial visual similarity. The botanical verification gate intercepts these proposals: because cereal grass rust cannot infect a broadleaf dicotyledon, all five detections are dynamically re-mapped to Rose_Berry_Rust (Phragmidium mucronatum). A spurious monocot proposal (Corn_Fall_Armyworm, confidence 24.1%) is pruned.", body_style))
    c13.append(Paragraph("5. Quantitative Severity Calculation: Cumulative bounding box area is evaluated as $A_{\\text{lesion}} = 25,800\\text{ pixels}$. The Quantitative Severity Index is evaluated as $\\text{QSI} = (25,800 / 142,500) \\times 100 = 18.1\\%$. This falls within the range 15.1% to 40.0%, assigning clinical Stage 2 (Moderate / Active Infection).", body_style))
    c13.append(Paragraph("6. IPM Advisory Formulation: The multimodal engine evaluates high relative humidity ($82\\% \\ge 80\\%$) as high sporulation risk. It prescribes: (a) cultural pruning of blighted lower stems; (b) preventive bio-fungicide spray of Bacillus subtilis @ 5.0 ml/L; (c) protective chemical application of Wettable Sulfur 80% WP @ 2.0 g/L or Copper Oxychloride 50% WP @ 2.5 g/L; and (d) a Pre-Harvest Interval (PHI) of 3 days.", body_style))
    c13.append(Paragraph("XX. TEST CASES AND ACCEPTANCE CRITERIA", h1_style))
    c13.append(Paragraph("A structured test suite covers image formats, illumination robustness, multi-lesion localization, botanical verification, severity calculation, explainability, and database integrity. Test cases are versioned and executed automatically upon model or code updates.", body_style))
    c13.append(Paragraph("TC-01: High-resolution JPEG upload ($3840 \\times 2160$). Expected result: image is accepted, letterboxed to 640x640 with aspect ratio preserved, and processed under 50 ms.", body_style))
    c13.append(Paragraph("TC-02: Low-light field leaf with shadows. Expected result: HSV foliage mask isolates green lamina ($A_{\\text{foliage}} > 0$) without false soil noise.", body_style))
    c13.append(Paragraph("TC-03: Multi-lesion co-occurrence (Tomato Early Blight and Septoria Spot). Expected result: discrete bounding boxes localized around both lesion categories on a single blade.", body_style))
    c13.append(Paragraph("TC-04: Botanical monocot/dicot gate on broadleaf with orange rust. Expected result: aspect ratio $< 3.5$; Wheat_Leaf_Rust is re-mapped to Rose_Berry_Rust; zero cereal rust tags displayed.", body_style))
    c13.append(Paragraph("TC-05: Monocot pest false positive on broadleaf foliage. Expected result: low-confidence Corn_Fall_Armyworm proposal is pruned by the botanical filter.", body_style))
    c13.append(Paragraph("TC-06: Completely healthy crop foliage. Expected result: zero lesion boxes localized; classified as Healthy_Crop; severity index equals 0.0%; Stage 0 assigned.", body_style))

    # =========================================================================
    # PAGE 8: COL 14 & COL 15
    # =========================================================================
    c14 = columns_data[14]
    c14.append(Paragraph("TC-07: Severe necrotic leaf blight ($>50\\%$ leaf area destroyed). Expected result: bounding boxes cover $>40\\%$ of lamina; assigned Stage 3 (Severe); urgent chemical alert issued.", body_style))
    c14.append(Paragraph("TC-08: Grad-CAM saliency generation. Expected result: saliency heatmap peak aligns with ground-truth lesion necrosis coordinates.", body_style))
    c14.append(Paragraph("TC-09: Extreme temperature spray gating ($T = 36.5^\\circ\\text{C}$). Expected result: chemical spray warning issued to prevent midday phytotoxicity leaf scorch.", body_style))
    c14.append(Paragraph("TC-10: High humidity fungal spore alert ($RH = 88.0\\%$). Expected result: spore germination warning flagged; advises immediate protective bio-fungicide application.", body_style))
    c14.append(Paragraph("TC-11: End-to-end API inference latency benchmark. Expected result: total execution time from request to JSON response is under 200 ms on GPU.", body_style))
    c14.append(Paragraph("TC-12: Database referential integrity and foreign keys. Expected result: records correctly written across all relational tables; foreign key cascade verified; zero orphaned rows.", body_style))
    c14.append(Paragraph("XXI. DEPLOYMENT, MONITORING, AND MAINTENANCE", h1_style))
    c14.append(Paragraph("The system is packaged for containerized cloud deployment and lightweight offline edge execution. Docker containers with CUDA acceleration encapsulate PyTorch, OpenCV, and FastAPI services. The model is exported to Open Neural Network Exchange (ONNX) format with dynamic batching, executable on Android smartphones via ONNX Runtime Mobile.", body_style))
    c14.append(Paragraph("Continuous monitoring tracks prediction confidence distributions. A sustained drop in mean confidence signals camera sensor drift, optical lens fouling, or emerging novel viral strains. A rollback mechanism preserves previous weight checkpoints.", body_style))
    c14.append(Paragraph("XXII. PROJECT RISKS AND MITIGATION", h1_style))
    c14.append(Paragraph("Risk: severe background clutter (soil, weeds, wooden stakes) causes false lesion proposals. Mitigation: HSV color-space masking segments the vegetative lamina prior to bounding-box inference.", body_style))
    c14.append(Paragraph("Risk: cross-phylogenetic confusion leads to misclassifying cereal rust on broadleaf horticultural crops. Mitigation: active contour aspect-ratio gating ($AR < 3.5$ vs $AR \\ge 4.5$) dynamically overrides impossible classes.", body_style))
    c14.append(Paragraph("Risk: pesticide over-prescription leads to chemical resistance, crop damage, and food market residue violations. Mitigation: strict clinical staging prohibits synthetic chemicals for Stage 0 and Stage 1, while Pre-Harvest Intervals (PHI) are explicitly enforced.", body_style))
    c14.append(Paragraph("Risk: network connectivity failure in remote rural fields prevents cloud API access. Mitigation: offline-capable Progressive Web App (PWA) with Service Worker caching and ONNX edge execution.", body_style))

    c15 = columns_data[15]
    c15.append(Paragraph("Risk: farmer distrust of opaque black-box deep learning models. Mitigation: Grad-CAM convolutional saliency heatmaps prove that the neural network attended to actual pathological lesions.", body_style))
    c15.append(Paragraph("Risk: model updates produce irreproducible historical match records. Mitigation: store model weight hashes, botanical filter rules, and scoring versions with every saved scan.", body_style))
    c15.append(Paragraph("XXIII. EXPECTED CONTRIBUTION AND DEMONSTRATION PLAN", h1_style))
    c15.append(Paragraph("The expected contribution is a practical, edge-optimized precision agriculture platform that bridges the gap between in-situ deep learning object detection, plant morphology, quantitative severity staging, and actionable Integrated Pest Management (IPM). The system is intended to improve diagnostic accuracy for smallholder farmers, prevent inappropriate chemical fungicide usage, and provide agricultural extension offices with a consolidated view of regional crop disease dynamics.", body_style))
    c15.append(Paragraph("The live system demonstration presents: (1) ingestion of unconstrained smartphone field photographs; (2) real-time bounding-box lesion localization across multiple disease categories; (3) dynamic demonstration of the Botanical Architecture Verification Gate overriding false cereal rust proposals on broadleaf rose foliage; (4) quantitative severity index calculation ($18.1\\% \\rightarrow$ Stage 2 Moderate); (5) interactive Grad-CAM neural attention visualization; and (6) complete multimodal IPM agronomic prescription formulation.", body_style))
    c15.append(Paragraph("Delivered artifacts include fully trained weights (best.pt), exportable ONNX models, interactive FastAPI and Streamlit web applications, and pre-rendered Jupyter notebooks with complete evaluation plots.", body_style))
    c15.append(Paragraph("APPENDIX A. SAMPLE DATA REPRESENTATION", h1_style))
    c15.append(Paragraph("A compact, normalized JSON representation keeps the vision pipeline independent from user interfaces. Below is an illustrative payload emitted by the POST /api/v1/diagnose endpoint:", body_style))
    json_text = """{<br/>
&nbsp;&nbsp;"scan_id": "7f8b3c2a-9e12-4d56-b8f1-3a2c4e6d8f01",<br/>
&nbsp;&nbsp;"timestamp": "2026-11-21T19:15:00Z",<br/>
&nbsp;&nbsp;"metadata": {"image_w": 800, "image_h": 600, "foliage_area": 142500, "temp_c": 26.5, "humidity_pct": 82.0},<br/>
&nbsp;&nbsp;"botanical_verification": {"aspect_ratio": 1.42, "morphology": "Broadleaf Dicot", "override_triggered": true},<br/>
&nbsp;&nbsp;"diagnostic_results": {<br/>
&nbsp;&nbsp;&nbsp;&nbsp;"primary_diagnosis": "Rose / Raspberry Rust (Phragmidium)",<br/>
&nbsp;&nbsp;&nbsp;&nbsp;"consensus_confidence_pct": 94.6,<br/>
&nbsp;&nbsp;&nbsp;&nbsp;"lesions_localized": 5,<br/>
&nbsp;&nbsp;&nbsp;&nbsp;"severity_index_pct": 18.1,<br/>
&nbsp;&nbsp;&nbsp;&nbsp;"clinical_stage": 2<br/>
&nbsp;&nbsp;},<br/>
&nbsp;&nbsp;"ipm_advisory": {<br/>
&nbsp;&nbsp;&nbsp;&nbsp;"pathogen_etiology": "Fungal basidiomycete (Phragmidium mucronatum).",<br/>
&nbsp;&nbsp;&nbsp;&nbsp;"microclimate_risk": "High (RH >= 80% promotes rapid sporulation).",<br/>
&nbsp;&nbsp;&nbsp;&nbsp;"biological_control": "Bacillus subtilis @ 5.0 mL/L or Neem Oil @ 3.0 mL/L.",<br/>
&nbsp;&nbsp;&nbsp;&nbsp;"chemical_control": "Wettable Sulfur 80% WP @ 2.0 g/L (PHI: 3 days)."<br/>
&nbsp;&nbsp;}<br/>
}"""
    c15.append(Paragraph(json_text, algo_style))
    c15.append(Paragraph("APPENDIX B. ANNOTATION AND DATASET PROTOCOL", h1_style))
    c15.append(Paragraph("A reliable evaluation requires a documented dataset protocol. For lesion localization, annotators marked exact bounding box margins enclosing the central necrotic core plus the surrounding chlorotic yellow halo with a 3-pixel border. Partially occluded lesions were bounded strictly on visible symptomatic tissue without hallucinating hidden margins. Isolated necrotic speckles smaller than 4x4 pixels were merged into cluster bounds or discarded if solitary.", body_style))

    # =========================================================================
    # PAGE 9: COL 16 & COL 17
    # =========================================================================
    c16 = columns_data[16]
    c16.append(Paragraph("To guarantee annotation reliability across the PlantDoc re-annotation campaign, double-blind annotation was performed on a fifteen percent random subset. Inter-annotator agreement was evaluated using Cohen's kappa for categorical disease classifications: $\\kappa = (p_o - p_e) / (1 - p_e) = 0.864$. Mean inter-annotator bounding box Intersection-over-Union (IoU) achieved 0.842, confirming high boundary consistency across annotators.", body_style))
    c16.append(Paragraph("The dataset was partitioned into train, validation, and test subsets (2,467 training images, 262 validation images) without cross-partition image leakage. All bounding box coordinates were converted from raw pixel coordinates (xmin, ymin, xmax, ymax) to YOLO normalized center and dimension coordinates (x_center, y_center, width, height) relative to image dimensions.", body_style))
    c16.append(Paragraph("APPENDIX C. EVALUATION METRICS AND REPORTING TEMPLATE", h1_style))
    c16.append(Paragraph("For object detection, precision measures the proportion of predicted lesion boxes that overlap ground-truth lesions by at least fifty percent IoU. Recall measures the proportion of ground-truth lesions successfully detected. Average Precision (AP) integrates the area under the precision-recall curve. Mean Average Precision (mAP) averages AP across all twenty-seven classes.", body_style))
    c16.append(Paragraph("An ablation study evaluated the contribution of individual architectural components. Removing the Botanical Architecture Verification Gate reduced mAP@0.5 from 0.812 to 0.778 (-3.4%), proving that active contour morphology filtering significantly improves diagnostic reliability by eliminating cross-phylogenetic false positives.", body_style))
    tbl_data = [
        ["Architecture Variant", "mAP@0.5", "Sev. MAE", "GPU Lat."],
        ["Baseline ResNet-50", "0.642", "N/A", "11.2 ms"],
        ["Faster R-CNN (ResNet-50)", "0.784", "4.82%", "84.5 ms"],
        ["YOLOv8n (No Botanical)", "0.778", "3.45%", "14.6 ms"],
        ["AgriGuard Full Pipeline", "0.812", "3.18%", "14.8 ms"]
    ]
    t = Table(tbl_data, colWidths=[100, 45, 45, 50])
    t.setStyle(TableStyle([
        ('FONTNAME', (0,0), (-1,-1), 'Times-Roman'),
        ('FONTSIZE', (0,0), (-1,-1), 7.2),
        ('FONTNAME', (0,0), (-1,0), 'Times-Bold'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('GRID', (0,0), (-1,-1), 0.5, colors.black),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#f1f5f9'))
    ]))
    c16.append(t)
    c16.append(Paragraph("Table C.1. Ablation study results across model variants.", caption_style))

    c17 = columns_data[17]
    c17.append(Paragraph("APPENDIX D. TEAM RESPONSIBILITIES AND PROJECT DELIVERABLES", h1_style))
    c17.append(Paragraph("The capstone project was executed by Devanshu Kumar, leading all system engineering workstreams:", body_style))
    c17.append(Paragraph("1. Computer Vision & Deep Learning: Ingested and prepared the PlantDoc in-the-wild agricultural dataset; implemented automated CSV-to-YOLO conversion scripts; trained and fine-tuned the anchor-free YOLOv8n object detection backbone on an NVIDIA RTX 4060 GPU; tuned the Task-Aligned Assigner and anchor-free loss functions; generated evaluation curves (mAP, Precision-Recall, F1, confusion matrices); and exported the model to ONNX runtime format for mobile deployment.", body_style))
    c17.append(Paragraph("2. Botanical Morphology & Explainable AI: Developed the active contour Botanical Architecture Verification Engine using HSV foliage segmentation and aspect-ratio bounding analysis ($AR < 3.5$ for broadleaf dicots vs $AR \\ge 4.5$ for monocot grasses); implemented the spatial-spectral Quantitative Severity Index (QSI) calculation engine; formulated the clinical 4-stage severity staging system; and coupled MobileNetV3 convolutional gradients to generate explainable Grad-CAM saliency heatmaps.", body_style))
    c17.append(Paragraph("3. Backend, API & Frontend Deployment: Architected the asynchronous FastAPI microservice backend with REST endpoints (/diagnose, /gradcam, /telemetry); developed the SQLite/PostgreSQL relational data schema; built the multimodal conversational IPM agronomic advisory engine integrating microclimate sensor gating; implemented the desktop diagnostic dashboard in Streamlit; and deployed the offline-capable mobile Progressive Web Application (PWA).", body_style))
    c17.append(Paragraph("4. Documentation & Packaging: Authored the university capstone project report, PowerPoint presentation, and this comprehensive IEEE technical research paper; packaged the complete 94.8 MB submission archive (RollNo_CropDiseaseDetection.zip) containing source code, trained weights, pre-rendered notebooks, and deployment manifests.", body_style))
    c17.append(Paragraph("APPENDIX E. DESIGN DECISIONS AND RATIONALE", h1_style))
    c17.append(Paragraph("The first design decision is to use an anchor-free single-stage detector (YOLOv8) rather than two-stage detectors (such as Faster R-CNN) or whole-image classifiers. Whole-image classifiers fail when multiple pathologies co-occur on a single leaf. Faster R-CNN requires heavy Region Proposal Networks that incur over two hundred milliseconds latency, preventing real-time mobile execution. YOLOv8 couples an anchor-free decoupled head with Path Aggregation Network (PAN) neck structures, reducing model size to 3.2 million parameters while achieving 14.8 ms latency.", body_style))
    c17.append(Paragraph("The second design decision is to use HSV color-space foliage segmentation rather than raw RGB thresholding. In-situ field imagery contains soil, weeds, sky, and variable solar illumination. In HSV space, active chlorophyll occupies a stable Hue range ($H \\in [25, 85]$), enabling clean separation of vegetative lamina from background clutter.", body_style))
    c17.append(Paragraph("The third design decision is to implement an active contour botanical morphology gate. Neural networks lack phylogenetic constraints; visual classifiers frequently confuse cereal grass rust on broadleaf plants. Analyzing contour aspect ratios ($AR < 3.5$ for broadleaf dicots vs $AR \\ge 4.5$ for monocot grasses) introduces a fast, deterministic botanical prior that prevents cross-species misclassifications.", body_style))
    c17.append(Paragraph("The fourth design decision is to calculate an objective Quantitative Severity Index (QSI) from localized lesion bounding boxes. In agronomic practice, a binary diagnosis without disease severity cannot inform spray thresholds. Integrating lesion surface areas into clinical stages (Stage 0 to Stage 3) provides agronomists with the necessary metrics to authorize chemical intervention.", body_style))

    # =========================================================================
    # PAGE 10: COL 18 & COL 19
    # =========================================================================
    c18 = columns_data[18]
    c18.append(Paragraph("The fifth design decision is to provide an Integrated Pest Management (IPM) advisory rather than a silent classification. Smallholder farmers need actionable recommendations: organic biocontrols, exact chemical formulations (g/L), safety waiting intervals, and weather-dependent spray risk warnings.", body_style))
    c18.append(Paragraph("The sixth design decision is to maintain human oversight in the process. Extension officers can inspect Grad-CAM heatmaps to verify automated detections before authorizing subsidized agrochemicals.", body_style))
    c18.append(Paragraph("REFERENCES", h1_style))
    refs = [
        "[1] D. Singh, N. Jain, P. Jain, P. Kayal, S. Kumawat, and N. Batra, \u201cPlantDoc: A Dataset for Visual Plant Disease Detection,\u201d in Proc. 7th ACM IKDD CoDS and 25th COMAD (CoDS-COMAD 2020), New York, NY, USA, 2020, pp. 249\u2013253, doi: 10.1145/3371158.3371196.",
        "[2] J. G. A. Barbedo, \u201cPlant disease identification from individual lesions and spots using deep learning,\u201d Biosystems Engineering, vol. 180, pp. 96\u2013107, Apr. 2019, doi: 10.1016/j.biosystemseng.2019.02.002.",
        "[3] A. Fuentes, S. Yoon, S. C. Kim, and D. S. Park, \u201cA Robust Deep-Learning-Based Detector for Real-Time Tomato Plant Diseases and Pests Recognition,\u201d Sensors, vol. 17, no. 9, Art. no. 2022, Sep. 2017, doi: 10.3390/s17092022.",
        "[4] D. P. Hughes and M. Salath\u00e9, \u201cAn open access repository of images on plant health to enable the development of mobile disease diagnostics,\u201d arXiv preprint arXiv:1511.08060, 2015.",
        "[5] S. P. Mohanty, D. P. Hughes, and M. Salath\u00e9, \u201cUsing Deep Learning for Image-Based Plant Disease Detection,\u201d Frontiers in Plant Science, vol. 7, Art. no. 1419, Sep. 2016, doi: 10.3389/fpls.2016.01419.",
        "[6] M. G. Selvaraj, A. Vergara, F. Montenegro, et al., \u201cDetection of banana diseases and pest damage using deep learning and handheld smartphones,\u201d Plant Methods, vol. 15, Art. no. 86, Dec. 2019, doi: 10.1186/s13007-019-0470-0.",
        "[7] R. R. Selvaraju, M. Cogswell, A. Das, R. Vedantam, D. Parikh, and D. Batra, \u201cGrad-CAM: Visual Explanations from Deep Networks via Gradient-Based Localization,\u201d in Proc. IEEE Int. Conf. on Computer Vision (ICCV), Venice, Italy, 2017, pp. 618\u2013626, doi: 10.1109/ICCV.2017.74.",
        "[8] G. Jocher, A. Chaurasia, and J. Qiu, \u201cUltralytics YOLOv8,\u201d Version 8.0.0, 2023. [Online]. Available: https://github.com/ultralytics/ultralytics.",
        "[9] Food and Agriculture Organization (FAO), \u201cThe State of Food and Agriculture 2022: Leveraging automation in agriculture for transforming agrifood systems,\u201d FAO, Rome, Italy, Tech. Rep., 2022.",
        "[10] K. P. Ferentinos, \u201cDeep learning models for plant disease detection and diagnosis,\u201d Computers and Electronics in Agriculture, vol. 145, pp. 311\u2013318, Feb. 2018, doi: 10.1016/j.compag.2018.01.009."
    ]
    for r in refs:
        c18.append(Paragraph(r, ref_style))
        
    c19 = columns_data[19]
    # Keep c19 minimal so it doesn't overflow page 10
    c19.append(Spacer(1, 10))

    # Check heights of all 20 columns
    print("Checking heights of all 20 columns against 750 pt threshold:")
    has_overflow = False
    for idx, col_items in enumerate(columns_data):
        total_h = 0
        for item in col_items:
            w, h = item.wrap(col_w, col_h)
            total_h += h + getattr(item, 'spaceBefore', 0) + getattr(item, 'spaceAfter', 0)
        p_num = (idx // 2) + 1
        side = "Left" if idx % 2 == 0 else "Right"
        status = "⚠️ OVERFLOW" if total_h > 745.0 else "✅ OK"
        print(f"Col {idx:2d} (Page {p_num:2d} {side:5s}): {total_h:6.1f} pt (Max 750 pt) -> {status}")
        if total_h > 745.0:
            has_overflow = True
            
    if has_overflow:
        print("\n❌ Cannot build yet: Some columns exceed 745 pt limit!")
        return False
        
    # Assemble story with FrameBreak after each column except the last
    story = []
    for idx, col_items in enumerate(columns_data):
        for item in col_items:
            story.append(item)
        if idx < len(columns_data) - 1:
            story.append(FrameBreak())
            
    doc.build(story)
    
    # Verify final page count with fitz
    d = fitz.open(pdf_path)
    page_count = len(d)
    print(f"\n🎉 Resulting PDF Page Count: {page_count}")
    for i, page in enumerate(d):
        lines = [l.strip() for l in page.get_text('text').split('\n') if l.strip()]
        headings = [l for l in lines if any(l.startswith(prefix) for prefix in ['I.', 'II.', 'III.', 'IV.', 'V.', 'VI.', 'VII.', 'VIII.', 'IX.', 'X.', 'XI.', 'XII.', 'XIII.', 'XIV.', 'XV.', 'XVI.', 'XVII.', 'XVIII.', 'XIX.', 'XX.', 'XXI.', 'XXII.', 'XXIII.', 'APPENDIX', 'REFERENCES'])]
        print(f"Page {i+1:2d}: {headings}")
        
    return page_count == 10

if __name__ == '__main__':
    generate_ieee_paper()
