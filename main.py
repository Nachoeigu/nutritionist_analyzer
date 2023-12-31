from src.image_recognizer import ImageRecognizer
from src.nutritionist import Nutritionist
from src.telegram_bot import TelegramBot


def main():
    last_update = None
    bot = TelegramBot()
    while True:
        telegram_output = bot.paying_attention_to_chatgroup(last_date_executed=last_update)
        if telegram_output != False:        
            last_updates, info, types = telegram_output
            bot.send_message(f"🔍 Let me analyze the {types[0] + 's' if len(types) > 1 else types[0]}...")
            bot.send_message("📌 Remember, I tag them based on this sorted scale: \n 1⃣ Excellent \n 2⃣ Good Choice \n 3⃣ Moderate \n 4⃣ Deficient \n 5⃣ Unhealthy")
            
            if types[0] == 'photo':
                text_detector = ImageRecognizer()
                info = text_detector.extract_data_from_image()
            elif types[0] == 'text':
                info = info[0]

            nutritionist = Nutritionist()
            output = f"🥗 Analysis: \n\n👉{nutritionist.new_chat(info)}"

            bot.send_message(output)
            
            last_update = last_updates[-1]

if __name__ == '__main__':
    main()