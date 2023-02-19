from flask import Flask, request
from flask_cors import CORS
from photo import Photo


app = Flask(__name__)
CORS(app)


@app.route("/sharpen")
def sharpen():
    path = request.args.get("path", type=str, default="")
    filename = request.args.get("filename", type=str, default="")

    if(path!="" and filename!=""):
        photo =  Photo(path, filename)
        photo.sharpen()
        print(path, filename)
        return "Photo sharpen"
    else:
        print( "missing args")
        return "false"



@app.route("/rotate_cw")
def rotate_clockwise():
    path = request.args.get("path", type=str, default="")
    filename = request.args.get("filename", type=str, default="")

    if(path!="" and filename!=""):
        photo =  Photo(path, filename)
        photo.rotate_cw()
        print(path, filename)
        return "Rotate clockwise"
    else:
        print( "missing args")
        return "false"


@app.route("/rotate_cc")
def rotate_counterClock():
    path = request.args.get("path", type=str, default="")
    filename = request.args.get("filename", type=str, default="")

    if(path!="" and filename!=""):
        photo =  Photo(path, filename)
        photo.rotate_cc()
        print(path, filename)
        return "Rotate counter clockwise"
    else:
        print( "missing args")
        return "false"

    return"Rotate counter clockwise"

@app.route("/greyscale")
def invert():
    path = request.args.get("path", type=str, default="")
    filename = request.args.get("filename", type=str, default="")

    if(path!="" and filename!=""):
        photo =  Photo(path, filename)
        photo.greyscale()
        print(path, filename)
        return "GreyScale"
    else:
        print( "missing args")
        return "false"

    return"Rotate counter clockwise"

@app.route("/mirror")
def flip_lr():
    path = request.args.get("path", type=str, default="")
    filename = request.args.get("filename", type=str, default="")

    if(path!="" and filename!=""):
        photo = Photo(path, filename)
        photo.mirror()
        print(path, filename)
        return "Mirror"
    else:
        print( "missing args")
        return "false"

    return"Rotate counter clockwise"


if __name__ == "__main__":
    app.run(debug=True)