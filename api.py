from flask import Flask , request, jsonify
import datetime

app = Flask(__name__)

timestamp = None
text = None

@app.route('/')
def hello_world():
    return 'Hello from Flask! it is hosted in pythonanywhere'

@app.route("/get_timestamp" , methods=["GET"])
def get_timestamp():
    global timestamp , text
    return jsonify({"timestamp": timestamp , "text": text})



@app.route("/add_data", methods=["POST"])
def add_data():
    global timestamp , text
    timestamp = datetime.datetime.now()
    text = str(request.args.get('input'))  # request like this zzz.com/add_data?input=
    return jsonify({"success": True})



@app.route("/add_data_get" , methods=["GET"])
def add_data_get():
    global timestamp
    timestamp = datetime.datetime.now()
    return jsonify({"timestamp": timestamp , "text": text})
