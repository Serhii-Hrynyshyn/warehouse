import json


def open_json(filename) -> dict:
    with open(filename, "r") as file:
        return json.load(file)
