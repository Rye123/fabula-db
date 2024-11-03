"""
Provides functions to load local data
"""
from typing import Dict, Any, List

import json
import markdown
import bleach
import urllib.parse
from flask import g
from pathlib import Path

DATA_CLASSES = Path("data/classes.json")
DATA_SKILLS  = Path("data/skills.json")

ACCEPTED_CHARS = ['_', '-']

#TODO: might need to allow links if we link to external stuff, which also means attribs needs to enable href
ALLOWED_TAGS = [
    "strong", "b",
    "em", "i",
    "br"
]
ALLOWED_ATTRIBS = {}

def urlsafe_name(name: str) -> str:
    # Only accept alphanumeric characters, brackets and replace spaces with underscores, raises an error if the name contains invalid characters
    result = ""
    for c in name.lower():
        if c == '(' or c == ')' or c.isalnum():
            result += c
        elif c == ' ':
            result += '_'
        elif c in ACCEPTED_CHARS:
            result += c
        else:
            raise ValueError(f"Invalid character detected in name {name}: '{c}'")
    return result

def load_data_file(f: str) -> Dict[str, Dict[str, Any]]:
    if not f.is_file():
        raise ValueError(f"{str(f)} does not exist.")

    ls = None
    try:
        ls = json.loads(f.read_text())
    except json.JSONDecodeError as e:
        raise ValueError(f"{str(f)} contains invalid JSON: {e}")

    data_dict = {}
    for elem in ls:
        if "name" not in elem:
            raise ValueError(f"{str(f)} contains an invalid element that does not have the \"name\" attribute. element: {repr(elem)}")
            

        # Convert the markdown description to HTML and sanitise
        final_desc = ""
        paragraphs = elem["description"].splitlines()
        for paragraph in paragraphs:
            desc = markdown.markdown(paragraph)
            desc = bleach.clean(
                desc,
                tags=ALLOWED_TAGS,
                attributes=ALLOWED_ATTRIBS,
                strip=True
            )
            desc = "<div>" + desc + "</div>"
            final_desc += desc
        elem["description"] = final_desc
        
        
        data_dict[urlsafe_name(elem["name"])] = elem
        
        
    return data_dict

def get_classes() -> Dict[str, Dict[str, Any]]:
    """ Returns player classes """
    if "data_classes" not in g:
        g.data_classes = load_data_file(DATA_CLASSES)
    
    return g.data_classes

def get_skills() -> Dict[str, Dict[str, Any]]:
    """ Returns skills """
    if "data_skills" not in g:
        g.data_skills = load_data_file(DATA_SKILLS)

    return g.data_skills
