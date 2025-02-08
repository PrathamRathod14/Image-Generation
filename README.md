# AI-Powered Image Generator

## Overview
It is an AI-powered **Image Generator** that allows users to generate images from text prompts using **NiceGUI** and **Stable Diffusion 2** from Hugging Face. The application provides a simple web interface for inputting prompts and retrieving AI-generated images.

## Features
- **User-Friendly Interface:** Built with **NiceGUI** for seamless interaction.
- **Stable Diffusion Model:** Uses **Stable Diffusion 2** for high-quality AI-generated images.
- **Real-Time Image Generation:** Fetches and displays images instantly.
- **Local Storage:** Saves generated images for easy access.

## Requirements
Ensure you have the following dependencies installed:

```sh
pip install nicegui requests pillow starlette
```

## Setup and Usage
1. **Clone the Repository**
   ```sh
   git clone https://github.com/yourusername/image-generator.git
   cd image-generator
   ```
2. **Replace API Key**
   - Open `image_generator.py`
   - Replace `HUGGING_FACE_API_KEY` with your actual Hugging Face API key.

3. **Run the Application**
   ```sh
   python image_generator.py
   ```

4. **Open the Web Interface**
   - Visit `http://localhost:8080` in your browser.

## Directory Structure
```
image-generator/
│── generated_images/  # Folder to store generated images
│── image_generator.py  # Main application file
│── README.md  # Documentation
```

## API Used
This project uses the **Stable Diffusion 2** model from Hugging Face:
- API Endpoint: `https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2`
  

## License
This project is licensed under the **MIT License**.

