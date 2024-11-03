from flask import Flask, request
from flask_cors import CORS
from flasgger import Swagger

import data

app = Flask(__name__)
Swagger(app)
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route("/")
def index():
    return "<!DOCTYPE html><html><head><title>fabula-db</title></head><body>boo</body></html>"

@app.route("/api/class/", methods=['GET'])
def api_get_classes():
    """
    Returns player classes, filtered by the query parameters.
    ---
    parameters:
      - name: name
        in: query
        type: string
        required: false
        description: Text to filter the class name by
    responses:
      200:
        description: dictionary of filtered player classes
    """
    filter_name = request.args.get("name", "").lower()
    if filter_name == "":
        return data.get_classes()

    # identify valid objects by the name
    valid = {}
    for class_id, player_class in data.get_classes().items():
        if filter_name in player_class["name"].lower():
            valid[class_id] = player_class
    return valid

@app.route("/api/class/<class_name>", methods=['GET'])
def api_get_class(class_name: str):
    classes = data.get_classes()
    player_class = classes.get(class_name.lower())
    if player_class is None:
        return {"error": "no such class found"}, 404
    return player_class

@app.route("/api/skill/", methods=['GET'])
def api_get_skills():
    """
    Returns skills, filtered by the query parameters.
    ---
    parameters:
      - name: name
        in: query
        type: string
        required: false
        description: Text to filter the skill name by
      - name: requirements
        in: query
        type: string
        required: false
        description: Comma-separated string of requirements for the skill to filter by
      - name: description
        in: query
        type: string
        required: false
        description: Text to find in the descriptions
    responses:
      200:
        description: dictionary of filtered player classes
    """
    filter_name = request.args.get("name", "").lower()
    filter_req = request.args.get("requirements", "").lower()
    filter_desc = request.args.get("description", "").lower()

    # identify valid objects by the name
    valid = {}
    for skill_id, skill in data.get_skills().items():
        if filter_name != "":
            if filter_name not in skill["name"].lower():
                continue

        if filter_req != "":
            # Split filter reqs
            filter_req_ls = [req.strip() for req in filter_req.split(",")]

            # Split this skill's requirements
            req_ls = [req.strip() for req in skill["requirements"].lower().split(",")]

            print(filter_req_ls, req_ls, end="")

            # Check if ALL filter requirements exist in req_ls
            filter_reqs_satisfied = True
            for filter_req in filter_req_ls:
                if filter_req not in req_ls:
                    filter_reqs_satisfied = False
                    break
            if not filter_reqs_satisfied:
                continue

        if filter_desc != "":
            if filter_desc not in skill["description"].lower():
                continue

        valid[skill_id] = skill
        
    return valid

@app.route("/api/skill/<skill_name>", methods=['GET'])
def api_get_skill(skill_name: str):
    skills = data.get_skills()
    skill = skills.get(skill_name.lower())
    if skill is None:
        return {"error": "no such skill found"}, 404
    return skill

@app.route("/class/")
def get_class_home():
    return ""
