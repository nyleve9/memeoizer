import base64
import logging
import os
import subprocess as sp

from flask import render_template
from flask import request
from app import app

@app.route('/')
@app.route('/index')
def index():
    title = "Index"
    return render_template('index.html', title=title)


@app.route('/upload', methods=['GET', 'POST'])
def upload_page():
    if request.method == 'GET':
        title = 'Upload'
        return render_template('upload.html', title=title)

    if request.method == 'POST':
        title = 'Image Text'
        # Load data in payload
        data = request.data

        # Checks on user input
        # is not image
            # render not_an_image.html
        # is image
            # decode first 8 bytes of b64 string
            # confirm against list of mimetype strings
            # decode whole file
            # check mimetype of whole file
            # check last 8 bytes make sure file ends where it says it ends
            
        # Store image as file
        with open('tmp_img_file', 'w') as f:
            f.write(data)
            f.close()
        
        # Synchronous, blocking, call OCR program on saved file
        sp.call(['tesseract', 'tmp_img_file', 'tmp_text_file'])
        
        # Read text from output file
        with open('tmp_text_file.txt', 'r') as f:
            image_text = f.read()
        
        # Render text to user
        return render_template('text.html', text=image_text)

