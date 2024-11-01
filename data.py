"""
Provides functions to load local data
"""
from typing import Dict, Any, List

import json
from flask import g
from pathlib import Path

CLASSES_JSON = Path("data/classes.json")

def get_classes() -> List[Dict[str, Any]]:
    """ Returns player classes """
    if "data_classes" not in g:
        if not CLASSES_JSON.is_file():
            raise ValueError(f"{str(CLASSES_JSON)} does not exist.")
        class_ls = json.loads(CLASSES_JSON.read_text())
        g.data_classes = {}
        for playerclass in class_ls:
            g.data_classes[playerclass["name"].lower()] = playerclass
    return g.data_classes
