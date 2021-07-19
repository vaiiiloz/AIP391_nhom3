from flask import Flask, render_template, Response, request, session, redirect, url_for, send_from_directory, flash
from werkzeug.utils import secure_filename

from PIL import Image
import os
import sys
import cv2
from app_helper import *

app = Flask(__name__)
UPLOAD_FOLDER = r'C:\Users\Acer\source\repos\Drag and upload\static\upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def index():
	return render_template('main.html')

@app.route("/upload", methods = ["GET", "POST"])
def upload_file():
	if request.method == "POST":
		f = request.files['file']
		filename = secure_filename(f.filename)
		filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
		f.save(filepath)
		info = get_image(filepath, filename)
		return render_template('upload.html', display_detection = filename, fname = filename, info = info)

if __name__ == '__main__':
   app.run(port=1002, debug=True)