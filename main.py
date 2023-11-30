from src.image_recognizer import ImageRecognizer
from src.nutritionist import Nutritionist
from src.telegram_bot import TelegramBot


def main():
    last_update = 0
    while True:
        bot = TelegramBot()
        telegram_output = bot.paying_attention_to_chatgroup(last_update_in_unix=last_update)
        if telegram_output != False:        
            last_updates, info, types = telegram_output
            bot.send_message(f"🔍 Let me analyze the {types[0] + 's' if len(types) > 1 else types[0]}...")
            bot.send_message("📌 Remember that I tag them based on this sorted scale: \n 1⃣ Excellent \n 2⃣ Good Choice \n 3⃣ Moderate \n 4⃣ Deficient \n 5⃣ Unhealthy")
            
            if types[0] == 'photo':
                text_detector = ImageRecognizer()
                info = text_detector.extract_data_from_image()
            elif types[0] == 'text':
                info = info[0]

            nutritionist = Nutritionist()
            output = nutritionist.new_chat(info)

            output_txt =f"Review: \n\n {output}" 

            bot.send_message(output_txt)
            
            last_update = last_updates[-1]

if __name__ == '__main__':
    main()