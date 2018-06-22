
from flask import Flask, request, redirect, url_for, send_from_directory, render_template
from config import Config
import pytesseract
import Image

import os
import logging
from logging.handlers import RotatingFileHandler
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = '/home/ec2-user/environment/photos'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config.from_object(Config)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

handler = RotatingFileHandler(app.config['LOG_FILE'], maxBytes=10000, backupCount=1)
log = logging.getLogger('werkzeug')
log.setLevel(logging.INFO)
log.addHandler(handler)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path=os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            return pytesseract.image_to_string(Image.open(file_path));
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new pic</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''
    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=Config.RUN_PORT)    