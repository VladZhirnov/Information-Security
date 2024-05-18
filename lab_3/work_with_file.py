import json

def read_json(path):
    with open(path) as json_file:
        json_data = json.load(json_file)
    return json_data

def write_key_to_file(path, key):
    with open(path, "wb") as file:
        file.write(key)