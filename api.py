from flask import Flask , request, jsonify
import datetime
import git  # GitPython library

app = Flask(__name__)

# Global variables
timestamp = None
text = None

@app.route('/git_update', methods=['POST'])
def git_update():
    """
    Update the git repository with the latest changes from the remote and switch to the main branch.
    
    Parameters:
        None
    
    Returns:
        tuple: A tuple in the format (None, 200) indicating a successful update.
    """
    repo = git.Repo('./cr_alarm_custom_api_server')
    origin = repo.remotes.origin
    # repo.create_head('main', origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
    origin.pull()
    return '', 200



@app.route('/')
def hello_world():
    return 'Hello from Flask! it is hosted in pythonanywhere'

@app.route("/get_timestamp", methods=["GET"])
def get_timestamp():
    """
    Get the timestamp and text that is stored in the previous POST request.

    Parameters:
        None

    Returns:
        dict: A dictionary containing the timestamp and text.
            - timestamp (int): The timestamp.
            - text (str): The text.
    """
    global timestamp, text
    return jsonify({
        "timestamp": timestamp,
        "text": text
    })



@app.route("/add_data", methods=["POST"])
def add_data():
    """
    Handles the route "/add_data" for the POST method.

    This function is responsible for adding data to the system. It retrieves the input value
    from the request parameters and stores it in the 'text' variable. It also updates the
    'timestamp' variable with the current date and time when post request is made. Finally,
    it returns a JSON response indicating the success of the operation.

    Parameters:
        key = input, value=<your input value>

    Returns:
        A JSON response with the key "success" set to True.
    """
    global timestamp , text
    timestamp = datetime.datetime.now()
    text = str(request.args.get('input'))
    return jsonify({"success": True})



@app.route("/add_data_get" , methods=["GET"])
def add_data_get():
    """
    Handle GET requests to the /add_data_get endpoint.

    It updates the 'timestamp' variable with the current date and time when post request is made.
    Finally, it returns a JSON response indicating the success of the operation.

    Returns:
        A JSON response containing the current timestamp and text.
    """
    global timestamp
    timestamp = datetime.datetime.now()
    return jsonify({"timestamp": timestamp , "text": text})
