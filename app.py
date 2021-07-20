from flask import Flask, render_template, Response, request, session, redirect, url_for, send_from_directory, flash
from werkzeug.utils import secure_filename

from PIL import Image
import os
import sys
from app_helper import *

app = Flask(__name__)
UPLOAD_FILE = 'input.jpg'

app.config['UPLOAD_FILE'] = UPLOAD_FILE

@app.route("/")
def index():
	return render_template('main.html')

@app.route("/upload", methods = ["GET", "POST"])
def upload_file():
	if request.method == "POST":
		f = request.files['file']
		f.save(app.config['UPLOAD_FILE'])
		#info = get_image(app.config['UPLOAD_FILE'])
		info = ''
		return render_template('upload.html', info = info)

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host = '0.0.0.0',port=port,debug = True)