from flask import Flask, flash, jsonify, request, redirect, url_for
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_cors import CORS
import urllib.request
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


app = Flask(__name__)
app.secret_key = "1234"
UPLOAD_FOLDER = 'frontend/src/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', ])
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['POST'])
def upload_file():
    # check if the post request has the file part
    if 'files[]' not in request.files:
        resp = jsonify({'message': 'No file part in the request'})
        resp.status_code = 400
        return resp

    files = request.files.getlist('files[]')

    errors = {}
    success = False

    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            success = True
        else:
            errors[file.filename] = 'File type is not allowed'

    if success and errors:
        errors['message'] = 'File(s) successfully uploaded'
        resp = jsonify(errors)
        resp.status_code = 500
        return resp
    if success:
        resp = jsonify({'message': 'Files successfully uploaded'})
        resp.status_code = 201
        return resp
    else:
        resp = jsonify(errors)
        resp.status_code = 500
        return resp


@app.route("/sharpen")
def sharpen():
    path = request.args.get("path", type=str, default="")
    filename = request.args.get("filename", type=str, default="")

    if (path != "" and filename != ""):
        photo = Photo(path, filename)
        photo.sharpen()
        print(path, filename)
        return "Photo sharpen"
    else:
        print("missing args")
        return "false"


@app.route("/rotate_cw")
def rotate_clockwise():
    path = request.args.get("path", type=str, default="")
    filename = request.args.get("filename", type=str, default="")

    if (path != "" and filename != ""):
        photo = Photo(path, filename)
        photo.rotate_cw()
        print(path, filename)
        return "Rotate clockwise"
    else:
        print("missing args")
        return "false"


@app.route("/rotate_cc")
def rotate_counterClock():
    path = request.args.get("path", type=str, default="")
    filename = request.args.get("filename", type=str, default="")

    if (path != "" and filename != ""):
        photo = Photo(path, filename)
        photo.rotate_cc()
        print(path, filename)
        return "Rotate counter clockwise"
    else:
        print("missing args")
        return "false"

    return "Rotate counter clockwise"


@app.route("/greyscale")
def invert():
    path = request.args.get("path", type=str, default="")
    filename = request.args.get("filename", type=str, default="")

    if (path != "" and filename != ""):
        photo = Photo(path, filename)
        photo.greyscale()
        print(path, filename)
        return "GreyScale"
    else:
        print("missing args")
        return "false"

    return "Rotate counter clockwise"


@app.route("/mirror")
def flip_lr():
    path = request.args.get("path", type=str, default="")
    filename = request.args.get("filename", type=str, default="")

    if (path != "" and filename != ""):
        photo = Photo(path, filename)
        photo.mirror()
        print(path, filename)
        return "Mirror"
    else:
        print("missing args")
        return "false"

    return "Rotate counter clockwise"


if __name__ == "__main__":
    app.run(debug=True)
