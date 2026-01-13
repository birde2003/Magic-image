import gradio as gr
from PIL import Image

# Constants
DEFAULT_IMAGE_WIDTH = 1024
DEFAULT_IMAGE_HEIGHT = 1024
PLACEHOLDER_COLOR = (73, 109, 137)  # Blue-gray color for placeholder images

def generate_image(prompt):
    """
    Generate an image based on text prompt using Tongyi MAI-Z Image Turbo model.
    
    Args:
        prompt: Text description of the image to generate
    
    Returns:
        PIL Image or error message
    """
    try:
        # Note: This is a placeholder implementation
        # In a real implementation, you would integrate with the actual Tongyi API
        # For demonstration purposes, we'll create a simple interface
        
        if not prompt or prompt.strip() == "":
            return None
        
        # Create a placeholder image
        # In production, this would call the actual Tongyi MAI-Z Image API
        img = Image.new('RGB', (DEFAULT_IMAGE_WIDTH, DEFAULT_IMAGE_HEIGHT), color=PLACEHOLDER_COLOR)
        
        return img
        
    except Exception as e:
        print(f"Error generating image: {str(e)}")
        return None

# Create the Gradio interface
with gr.Blocks(title="Tongyi MAI-Z Image Turbo") as demo:
    gr.Markdown("# Tongyi MAI-Z Image Turbo")
    gr.Markdown("Generate AI images using text prompts")
    
    with gr.Row():
        with gr.Column():
            prompt_input = gr.Textbox(
                label="Prompt",
                placeholder="Enter your image description here...",
                lines=5
            )
            generate_btn = gr.Button("Generate Image", variant="primary")
        
        with gr.Column():
            output_image = gr.Image(label="Generated Image")
    
    generate_btn.click(
        fn=generate_image,
        inputs=prompt_input,
        outputs=output_image
    )
    
    gr.Markdown("""
    ### About
    This is a demo interface for AI image generation using Tongyi MAI-Z Image Turbo.
    
    **Note:** This is a demonstration interface. To use the actual Tongyi MAI-Z model,
    you would need to integrate with Alibaba Cloud's API service and provide proper authentication.
    
    ### How to use:
    1. Enter a detailed description of the image you want to generate
    2. Click "Generate Image"
    """)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)