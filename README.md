# 🖼️ AI Image Generator with Gradio (Realistic Vision v5.1)

This is a **prompt-based AI image generator** powered by the **Realistic Vision v5.1** model (a variant of Stable Diffusion). It runs entirely offline using Python and Gradio, and lets users generate stunning photorealistic images from simple text prompts.

---

## 🚀 Features

* 🧐 Text-to-image generation using Stable Diffusion
* 🔥 Realistic Vision v5.1 model support (ultra-realistic outputs)
* 🎨 Gradio interface with real-time generation
* ⚡ GPU acceleration supported
* 🛠️ Local execution, no LLMs or API keys required
* 📦 Expandable with future features like image-to-image, styles, etc.

---

## 📁 Project Structure

```
image_generator/
│
├── app.py                 # Main Gradio app
├── launch_app.bat         # Batch file to auto-launch with venv
├── requirements.txt       # Python dependencies
├── .gitignore             # Exclude virtual env, cache, etc.
└── README.md              # You're reading it!
```

---

## ⚙️ Installation Instructions

### 🐍 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/image-generator-gradio.git
cd image-generator-gradio
```

### 🧱 2. Create & Activate a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
```

### 📦 3. Install Required Packages

```bash
pip install -r requirements.txt
```

> If `requirements.txt` not present, install manually:

```bash
pip install torch torchvision diffusers transformers accelerate gradio
```

### 🚀 4. Run the App

```bash
python app.py
```

Or just double-click:

```
launch_app.bat
```

---

## 🔍 Example Prompts to Try

* `A footballer eating a burger, cinematic lighting, ultra-realistic`
* `Tokyo street at night with neon lights and reflections, photorealistic`
* `Close-up of a smiling woman, freckles, cinematic portrait`
* `A dog wearing sunglasses on the beach, DSLR look, hyperreal`

---

## 🔧 Model Used

* **Model**: [Realistic Vision v5.1](https://civitai.com/models/4201/realistic-vision-v51)
* **Format**: Diffusers (you can also use `.safetensors` in A1111 or convert for use here)
* **Alternative HF Repo**: `"SG161222/Realistic_Vision_V5.1_noVAE"`

---

## 🖼️ Screenshots

> (Paste screenshots of your app interface and a few output samples here)

---

## 📦 Example `requirements.txt`

```
torch
torchvision
diffusers
transformers
gradio
accelerate
pillow
```

---

## 📖 Sample `.gitignore`

```
venv/
__pycache__/
*.safetensors
*.pt
*.png
*.jpg
*.log
.idea/
.DS_Store
```

---

## 🤛🏼‍♂️ Author

Built by **\[Your Name]**
GitHub: [@YourUsername](https://github.com/YourUsername)

---

## 📄 License

This project is open-source under the **MIT License**.

---

## 🌟 Star this project if you found it helpful!
