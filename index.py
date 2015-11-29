import os
import json
from os import listdir
from os.path import isfile, join
from flask import redirect, url_for
from werkzeug import secure_filename
from flask import Flask, Response
from flask import render_template
from flask import Flask, request, send_from_directory
from flask import jsonify
from middleware import plagiot, pattern_check
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

@app.route('/getfiles',methods=['GET'])
def get_files():
    files = os.listdir(UPLOAD_FOLDER)
    print files
    dat = json.dumps(files)
    resp = Response(response=dat,status=200, mimetype="application/json")
    return resp

@app.route('/plagcheck',methods=['POST'])
def plag_check():
    if request.method == 'POST':
        post_obj = request.form.keys()[0]
        post_obj = json.loads(post_obj)
        print post_obj
        o_obj = plagiot(post_obj)
        print o_obj
        return json.dumps(o_obj)

@app.route('/patterncheck',methods=['POST'])
def patterncheck():
    if request.method == 'POST':
        post_obj = request.form.keys()[0]
        post_obj = json.loads(post_obj)
        print post_obj
        o_obj = pattern_check(post_obj)
        return json.dumps(o_obj)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
