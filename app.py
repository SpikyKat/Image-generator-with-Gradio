from diffusers import StableDiffusionPipeline
import torch
import gradio as gr

# Load Realistic Vision
pipe = StableDiffusionPipeline.from_pretrained(
    "SG161222/Realistic_Vision_V5.1_noVAE",  # Hugging Face model
    torch_dtype=torch.float16,
    safety_checker=None
)
pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")

def generate_image(prompt):
    image = pipe(prompt).images[0]
    return image

gr.Interface(
    fn=generate_image,
    inputs=gr.Textbox(label="Enter prompt"),
    outputs=gr.Image(label="Generated Image"),
    title="🔍 Realistic Vision Image Generator",
    description="Enter a prompt for realistic image generation using Realistic Vision v5.1"
).launch()
