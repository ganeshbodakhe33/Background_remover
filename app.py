from flask import Flask, request, render_template
from rembg import remove
from PIL import Image
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return 'No file part'

    file = request.files['image']

    if file.filename == '':
        return 'No selected file'

    if file:
        # Save the uploaded image
        input_path = 'uploads/' + file.filename
        file.save(input_path)

        # Remove background
        input_image = Image.open(input_path)
        output_image = remove(input_image)

        # Save the result
        output_path = 'static/' + os.path.splitext(file.filename)[0] + '_removed.png'
        output_image.save(output_path)

        return f'<img src="{output_path}" alt="Removed Background">'

if __name__ == '__main__':
    app.run(debug=True)
