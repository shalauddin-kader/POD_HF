import time
import requests
import os

# Hugging Face API token
HUGGINGFACE_API_TOKEN = "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"

def generate_image_huggingface(prompt):
    """
    Generate an image using Hugging Face's Stable Diffusion API with retry logic.
    """
    api_url = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}

    payload = {"inputs": prompt}
    retries = 5  # Number of retries
    wait_time = 60  # Time to wait (in seconds) between retries

    for attempt in range(retries):
        response = requests.post(api_url, headers=headers, json=payload)

        if response.status_code == 200:
            # Save the generated image
            output_path = "static/generated_images/output_image_1.png"
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            with open(output_path, "wb") as img_file:
                img_file.write(response.content)
            return output_path
        elif response.status_code == 503:
            print(f"Model is loading. Retrying in {wait_time} seconds...")
            time.sleep(wait_time)  # Wait before retrying
        else:
            raise Exception(f"Error: {response.status_code}, {response.text}")

    # If retries are exhausted
    raise Exception("Model is still loading after maximum retries.")


def generate_image(prompt, method="huggingface"):
    """
    Wrapper function to generate an image using Hugging Face's API.
    Currently supports only the 'huggingface' method.
    """
    if method == "huggingface":
        return generate_image_huggingface(prompt)
    else:
        raise ValueError(f"Unsupported method: {method}")
