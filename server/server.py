from flask import Flask, request
from flask_cors import CORS
from photo import Photo


app = Flask(__name__)
CORS(app)



@app.route("/rotate_cw")
def rotate_clockwise():
    path = request.args.get("path", type=str, default="")
    filename = request.args.get("filename", type=str, default="")

    if(path!="" and filename!=""):
        photo =  Photo(path, filename)
        photo.rotate()
        print(path, filename)
        return "Rotate clockwise"
    else:
        print( "missing args")
        return "false"


@app.route("/rotate_cc")
def rotate_counterClock():
    return"Rotate counter clockwise"


if __name__ == "__main__":
    app.run(debug=True)