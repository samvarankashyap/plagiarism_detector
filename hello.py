import os
from os import listdir
from os.path import isfile, join
from flask import redirect, url_for
from werkzeug import secure_filename
from flask import Flask
from flask import render_template
from flask import Flask, request, send_from_directory


UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['txt'])

app = Flask(__name__,static_url_path='/static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('./static/js', path)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        try:
            for filename in request.files:
                file = request.files[filename]
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return "upload sucessfull"
        except Exception,e:
            return str(e)
    else:
        return render_template('index.html')

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('./static/css', path)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
