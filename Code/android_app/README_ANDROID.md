# AgriGuard Android Application Deployment Guide
**Course:** CSE471 | **Project:** Early Detection & Management of Crop Diseases and Pest Infestations

This directory provides the production-grade Android application infrastructure for **AgriGuard**, supporting both:
1. **Direct Native Android Studio APK Project** (`MainActivity.java`, `AndroidManifest.xml`, `build.gradle`)
2. **Instant Progressive Web App (PWA) 1-Tap Android Installation** (Runs offline, full-screen standalone with camera access)

---

## Method 1: Instant 1-Tap Android Installation (PWA / Recommended for Evaluation)
No heavy Android Studio download or compilation needed on the user's phone.

1. Start the AgriGuard backend server:
   ```bash
   cd Code/app
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```
2. Connect your Android smartphone to the same Wi-Fi network as your computer, or access the deployed cloud URL (e.g. via Render or ngrok).
3. Open **Google Chrome** on your Android smartphone and navigate to:
   ```
   http://<YOUR_COMPUTER_IP>:8000
   ```
4. Tap the **Three Dots Menu (⋮)** at the top right of Chrome, and select **"Add to Home screen"** or **"Install AgriGuard"**.
5. The AgriGuard icon will appear directly in your **Android App Drawer** as a standalone application.
6. **Features Active on Android:**
   - Native Camera trigger with autofocus (`capture="environment"`).
   - Offline caching via Service Worker (`sw.js`).
   - Fullscreen immersive UI with status bar tinting (#059669).

---

## Method 2: Native Android Studio Build (APK Generation)
For evaluation through Android Studio or physical device debugging:

1. Open **Android Studio** (Hedgehog / Iguana or later).
2. Click **File -> Open** and navigate to `Code/android_app`.
3. In `MainActivity.java`, if testing with the Android Emulator, the target URL is already preset to:
   ```java
   mWebView.loadUrl("http://10.0.2.2:8000/"); // 10.0.2.2 maps to host PC localhost
   ```
   If testing on a physical phone connected via USB, replace `10.0.2.2` with your host PC's LAN IP (e.g. `http://192.168.1.100:8000/`).
4. Click **Build -> Build Bundle(s) / APK(s) -> Build APK(s)**.
5. Transfer the generated `app-debug.apk` to your phone and install it.
6. Grant camera and storage permissions when prompted.

---

## Hardware Permissions Configured
- `android.permission.CAMERA`: Live leaf inspection in fields.
- `android.permission.READ_MEDIA_IMAGES` / `READ_EXTERNAL_STORAGE`: Load previously taken field photographs from gallery.
- `android.permission.INTERNET`: Real-time IPM advisory fetch & cloud model synchronization.

