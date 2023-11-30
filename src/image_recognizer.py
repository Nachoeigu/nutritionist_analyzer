import os
import requests
from .functions import customizing_request, extracting_info, load_images, printing_token_usage, drop_images
from dotenv import load_dotenv

class InvalidPetition(Exception):
    pass

class ImageRecognizer:

    def __init__(self, model = 'gpt-4-vision-preview'):
        load_dotenv()
        self.openai_token =os.getenv('openai_token')
        self.model = model

    def extract_data_from_image(self):
        pic_url = load_images()

        headers, payload = customizing_request(self.openai_token, 
                            model = self.model,
                            img_path = pic_url)
        
        drop_images(pic_url)
        
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

        if response.status_code != 200:
            raise InvalidPetition("Your request wasn´t proccessed correctly...")
        else:
            print("Token usage for petition in Image Recognizition:")
            printing_token_usage(response.content)
            return extracting_info(response)
