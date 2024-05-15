import json

def read_json(path):
    with open(path) as json_file:
        json_data = json.load(json_file)
    return json_data