from flask import Flask
import data

app = Flask(__name__)

@app.route("/")
def index():
    return "<!DOCTYPE html><html><head><title>fabula-db</title></head><body>boo</body></html>"

@app.route("/api/class/")
def get_classes():
    return data.get_classes()

@app.route("/api/class/<class_name>")
def get_class(class_name: str):
    classes = data.get_classes()
    player_class = classes.get(class_name.lower())
    if player_class is None:
        return {"error": "no such class found"}, 404
    return player_class