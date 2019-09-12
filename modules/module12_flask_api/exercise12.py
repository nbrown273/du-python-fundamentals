from flask import request
from flask_api import FlaskAPI
from random import choice, random


# Initialize the Flask App
app = FlaskAPI(__name__)


reminders = {
    0: "Wake up"
}


# Set up what to do at 'root' endpoint
@app.route("/", methods=["GET"])
def home():
    return {
        "routes": {
            "/": "Root, shows list of available routes",
            "/color": "Color, returns a random color",
            "/number": "Number, returns a random number",
            "/reminder": "Reminder, returns list of added reminders"
        }
    }


# Set up what to do at 'color' endpoint
@app.route("/color", methods=["GET"])
def color():
    """
    Return a randomly choosen color from a set list
    """
    colors = ["red", "yellow", "blue", "purple", "green", "orange"]
    return {"color": choice(colors)}


# Set up what to do at 'color' endpoint
@app.route("/number", methods=["GET"])
def number():
    """
    Returns a random number, [0, 100]
    """
    n = int(random() * 100)
    return {"number": n}


# Set up what to do at 'reminder' endpoint
@app.route("/reminder", methods=["GET", "POST"])
def reminder():
    """
    Add passed in reminder to a list
    """
    if(request.method == "POST"):
        reminder = request.data.get("reminder")
        i = max(reminders.keys()) + 1
        reminders[i] = reminder
    return reminders


# Set up what to do at 'reminder detail' endpoint
@app.route("/reminder/<int:key>", methods=["GET"])
def reminderDetails(key):
    """
    Return details for a specific reminder by key
    """
    if(reminders.get(key)):
        return {key: reminders[key]}
    else:
        return {"error": f"Key '{key}' not found"}


"""
# TODO: Write a route that removes a key/value from reminders
    The route will be used to update the 'reminders' dictionary,
    removing a specified key/value pair based on a passed in
    key value
        * If method is 'GET':
            * Route should return the 'reminders' dict
        * If method is 'POST':
            * Route should parse key from route
            * If key is in 'reminders' dict:
                * Key should be removed from 'reminders'
                * Updated 'reminders' should be returned
            * If key is not in 'reminders' dict:
                * Dict with error message should be returned
"""


if __name__ == "__main__":
    app.run()