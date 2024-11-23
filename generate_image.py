import requests
import os

# Hugging Face API token
HUGGINGFACE_API_TOKEN = "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"

def generate_image_huggingface(prompt):
    """
    Generate an image using Hugging Face's Stable Diffusion API.
    """
    api_url = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}

    payload = {"inputs": prompt}
    response = requests.post(api_url, headers=headers, json=payload)

    if response.status_code == 200:
        output_path = "static/generated_images/output_image_1.png"
        os.makedirs(os.path.dirname(output_path), exist_ok=True)  # Ensure directory exists
        with open(output_path, "wb") as img_file:
            img_file.write(response.content)
        return output_path
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")


def generate_image(prompt, method="huggingface"):
    """
    Wrapper function to generate an image.
    Only Hugging Face is supported in this version.
    """
    if method == "huggingface":
        return generate_image_huggingface(prompt)
    else:
        raise ValueError(f"Unsupported method: {method}")
