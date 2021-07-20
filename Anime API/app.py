from flask import Flask, render_template, Response, request, session, redirect, url_for, send_from_directory, flash
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename

from PIL import Image
import os
import sys
import cv2
from app_helper import *
filepath = r"C:\Users\Acer\Downloads\input.jpg"
filename = "output.jpg"
app = Flask(__name__)
UPLOAD_FOLDER = r'C:\Users\Acer\source\repos\Drag and upload\static\upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/upload", methods = ["GET", "POST"])
def upload_file():
	if request.method == "POST":


		
		info, img_path = get_image(filepath, filename)
		return {'info':info,'filename':img_path}

if __name__ == '__main__':
   app.run(host = '0.0.0.0',port=5000, debug=True)