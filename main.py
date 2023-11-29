from src.image_recognizer import ImageRecognizer
from src.nutritionist import Nutritionist
from src.telegram_bot import TelegramBot


def main():
    # choice = input("Choose one option: \n 1) Import an image of the product. \n 2) Put details of the product in text \n Enter your answer here: ")
    # if choice == '1':
    #     text_detector = ImageRecognizer()
    #     info = text_detector.extract_data_from_image()
    # else:
    #     info = input('Put the ingredients and nutritional information:')

    bot = TelegramBot()
    telegram_output = bot.paying_attention_to_chatgroup(last_update_in_min=5)
    if telegram_output != False:
        last_update, info, type = telegram_output
        if type == 'photo':
            text_detector = ImageRecognizer()
            info = text_detector.extract_data_from_image()

        nutritionist = Nutritionist()
        output = nutritionist.new_chat(info)

        output_txt =f"Review about your product: \n\n {output} \n\n Remember that the nutritionist tags the product based on this sorted scale: \n 1) Excellent \n 2) Good Choice \n 3) Moderate \n 4) Deficient \n 5) Unhealthy" 

        bot.send_message(output_txt)

if __name__ == '__main__':
    main()