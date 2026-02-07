import json


def open_json(filename):
    try:
        with open(filename, "r", encoding="utf8") as file:
            data = json.load(file)
            file.close()
        return data
    except FileNotFoundError:
        print(FileNotFoundError)
