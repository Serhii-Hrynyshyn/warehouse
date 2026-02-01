import json


def open_json(filename):
    try:
        with open(filename, "r", encoding="utf8") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("Error: The file 'data.json' was not found.")
