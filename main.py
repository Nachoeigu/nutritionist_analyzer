from image_recognizer import ImageRecognizer
from nutritionist import Nutritionist

choice = input("Choose one option: \n 1) Import an image of the product. \n 2) Put details of the product in text \n Enter your answer here: ")
if choice == '1':
    text_detector = ImageRecognizer()
    info = text_detector.extract_data_from_image(['example.png','example_2.png'])
else:
    info = input('Put the ingredients and nutritional information:')

nutritionist = Nutritionist()
output = nutritionist.new_chat(info)

print("Review about your product: ")
print(output)