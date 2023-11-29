from src.image_recognizer import ImageRecognizer
from src.nutritionist import Nutritionist

def main():
    choice = input("Choose one option: \n 1) Import an image of the product. \n 2) Put details of the product in text \n Enter your answer here: ")
    if choice == '1':
        text_detector = ImageRecognizer()
        info = text_detector.extract_data_from_image()
    else:
        info = input('Put the ingredients and nutritional information:')

    nutritionist = Nutritionist()
    output = nutritionist.new_chat(info)

    print("Review about your product: ")
    print(output)
    print("Remember that the nutritionist tags the product based on this sorted scale: \n 1) Excellent \n 2) Healthy \n 3) Moderate \n 4) Subpar \n 5) Unhealthy")

if __name__ == '__main__':
    main()