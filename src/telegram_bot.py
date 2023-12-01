import os
import requests
from dotenv import load_dotenv
import logging
import time
import random

logger = logging.getLogger(__name__)


class TelegramBot:

    def __init__(self):
        load_dotenv()
        logger.info("Setting the Telegram Bot")
        self.token = os.getenv('telegram_bot')
        self.chat_id = os.getenv('chat_id')
        self.params = {
            "chat_id": self.chat_id,
            "text": '',
            "parse_mode": "Markdown" 
        }

        self.url = "https://api.telegram.org/bot"+ self.token + "/sendMessage"

    def send_message(self, text):
        self.params['text'] = text
        response = requests.get(self.url, params = self.params)        
        if response.status_code != 200:
            logger.info('We received an error while sending the msg to Telegram')
            logger.info(f'Response: {str(response.content)}')

    def __downloading_pic_from_telegram(self, file_id):
        url = f"https://api.telegram.org/bot{self.token}/getFile"
        params = {"file_id": file_id}
        response = requests.get(url, params=params)
        data = response.json()
        if data["ok"]:
            file_path = data["result"]["file_path"]
            download_url = f"https://api.telegram.org/file/bot{self.token}/{file_path}"
            response = requests.get(download_url)

            with open(f'./input_images/output_{str(random.randint(100, 900))}.jpg', 'wb') as file:
                file.write(response.content)

            return True

        return None

    def paying_attention_to_chatgroup(self, offset=None, last_update_in_min=2, last_date_executed=None):
        time.sleep(2)
        url = f"https://api.telegram.org/bot{self.token}/getUpdates"
        params = {"offset": offset, 'chat_id': self.chat_id}
        response = requests.get(url, params=params)
        data = response.json()['result']
        if data == []:
            return False
        
        if last_date_executed is None:
            last_minutes = time.time() - (last_update_in_min * 60)
        else:
            last_minutes = last_date_executed

        #This is for avoid old messages
        if data[-1]['message']['date'] <= last_minutes:
            return False
        
        last_updates = []
        msgs = []
        output_types = []
        for block_of_msg in data:
            if block_of_msg['message']['date'] <= last_minutes:
                continue
            try:
                msg = block_of_msg['message']['text']
                output_type = 'text'
            except:
                file_id = block_of_msg['message']['photo'][-1]['file_id']
                msg = self.__downloading_pic_from_telegram(file_id = file_id)
                output_type = 'photo'
            last_updates.append(block_of_msg['message']['date'])
            msgs.append(msg)
            output_types.append(output_type)


        return last_updates, msgs, output_types

    
