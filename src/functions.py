import base64
import copy
from .constants import HEADERS_IMG_RECOGNIZER_STRUCTURE, PAYLOAD_IMG_RECOGNIZER_STRUCTURE, IMAGE_EXTENSIONS
import json
import os

def load_images():
    images = []
    for root, dirs, files in os.walk('./input_images'):
        for file in files:
            if file.lower().endswith(tuple(IMAGE_EXTENSIONS)):
                images.append(os.path.join(root, file))

    return images

def encoding_img(img_name):
    with open(img_name, 'rb') as image_file: 
        encoded_string = base64.b64encode(image_file.read()) 
        return encoded_string.decode('utf-8')


def customizing_request(openai_token, model, img_path):
    custom_header = copy.copy(HEADERS_IMG_RECOGNIZER_STRUCTURE)
    custom_header['Authorization'] = 'Bearer ' + openai_token
    custom_payload = copy.copy(PAYLOAD_IMG_RECOGNIZER_STRUCTURE)
    custom_payload['model'] = model
    for n_image, image in enumerate(img_path):
        custom_payload['messages'][1]['content'].append({
            "type": "image_url",
            "image_url": {
                "url": 'data:image/jpeg;base64,' + encoding_img(image)
            }
        })

    return (custom_header, custom_payload)

def printing_token_usage(content):
    data = json.loads(content)
    input_tokens = data['usage']['prompt_tokens']
    output_tokens = data['usage']['completion_tokens']
    total_tokens = data['usage']['total_tokens']

    print(f"Prompt tokens usage: {input_tokens}")
    print(f"Output tokens usage: {output_tokens}")
    print(f"Total tokens usage: {total_tokens}")

def extracting_info(response):
    return json.loads(response.content)['choices'][0]['message']['content']
