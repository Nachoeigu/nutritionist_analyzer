from flask import Flask, render_template, request
import base64
from PIL import Image
from io import BytesIO
from nutritionist import Nutritionist
from image_recognizer import ImageRecognizer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if 'text' in request.form:
        processed_data = process_text(request.form['text'])
    elif 'image' in request.form:
        processed_data = process_image(request.form['image'])
    else:
        processed_data = "Invalid request."

    return render_template('result.html', result=processed_data)

def process_text(text):
    nutritionist = Nutritionist()
    output = nutritionist.new_chat(text)

    return output

def process_image(encoded_image):
    # Decode base64 image
    image_data = base64.b64decode(encoded_image.split(',')[1])
    img = Image.open(BytesIO(image_data))
    img.save('./input_images/output.jpg')
    text_detector = ImageRecognizer()
    info = text_detector.extract_data_from_image(['output.jpg'])
    nutritionist = Nutritionist()
    output = nutritionist.new_chat(info)

    return output

if __name__ == '__main__':
    app.run()
