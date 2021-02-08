from OCR import process_image
from flask import  Flask,render_template,request,jsonify
from OCR import process_image
import logging
import os

app = Flask(__name__)

@app.route('/ocr',methods=['POST'])
def ocr():
    try:
        url = request.json['image_url']
        if 'jpg' or 'JPG'in url:
            output = process_image(url)
            return jsonify({'output':output})
        else:
            return jsonify({'error':'only.jpg files,please'})
    except :
        return jsonify(
            {'error':'Did you mean to send: {"image_url":"some_jpeg_url"}'}
        )
if __name__== '__main__':
    app.run(debug=True)