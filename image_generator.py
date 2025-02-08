import os
import io
import time
import requests
from PIL import Image
from nicegui import ui, app
from starlette.staticfiles import StaticFiles


class ImageGenerator:
    # Hugging Face API Details
    HUGGING_FACE_API_KEY = "YOUR_API_KEY"  # Replace with your Hugging Face API key
    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"
    HEADERS = {"Authorization": f"Bearer {HUGGING_FACE_API_KEY}"}

    # Directory for storing generated images
    IMAGE_DIR = "generated_images"
    os.makedirs(IMAGE_DIR, exist_ok=True)

    # Mount static files for accessing generated images
    app.mount("/generated_images", StaticFiles(directory=IMAGE_DIR), name="generated_images")

    def generate_image(self, dialog, img, prompt_input):
        """Generate an image from the prompt text and update the UI."""
        prompt_text = prompt_input.value.strip()
        if not prompt_text:
            ui.notify("Please enter a prompt!", color="red")
            return

        ui.notify("Generating image, please wait...", color="blue")

        payload = {"inputs": prompt_text}

        try:
            response = requests.post(self.API_URL, headers=self.HEADERS, json=payload)
            
            if response.status_code == 200 and response.content:
                # Save the image
                timestamp = int(time.time())
                image_filename = f"generated_image_{timestamp}.png"
                image_path = os.path.join(self.IMAGE_DIR, image_filename)

                image = Image.open(io.BytesIO(response.content))
                image.save(image_path)

                # Update the dialog with the generated image
                img.set_source(f"/generated_images/{image_filename}")

                ui.notify("Image generated successfully!", color="green")
            else:
                error_message = response.json().get("error", "Unknown error")
                ui.notify(f"API Error: {error_message}", color="red")

        except requests.exceptions.RequestException as e:
            ui.notify(f"API Request failed: {str(e)}", color="red")

    def open_image_generation_dialog(self):
        """Open the dialog for image generation."""
        with ui.dialog() as dialog:
            dialog.classes("w-[90vw] h-[90vh]")
            
            with ui.card().classes("w-full h-full overflow-auto"):
                ui.label("Image Generation").classes("text-2xl font-bold mb-6 text-center")

                prompt_input = ui.input(label="Enter Prompt", placeholder="Describe your image...").classes("w-full mb-6")

                img_placeholder = ui.image("https://via.placeholder.com/600").classes("w-full h-100 rounded-lg shadow-md object-cover")

                ui.button(
                    "Generate Image",
                    on_click=lambda: self.generate_image(dialog, img_placeholder, prompt_input)
                ).classes("bg-blue-500 text-white px-6 py-3 rounded-lg mb-6 w-full")

        return dialog


def main():
    generator = ImageGenerator()
    ui.button("Open Image Generator", on_click=generator.open_image_generation_dialog).classes("bg-green-500 text-white px-6 py-3 rounded-lg")
    ui.run()



main()
