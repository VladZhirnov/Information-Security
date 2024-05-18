import json

def read_json(path):
    with open(path, "r") as json_file:
        json_data = json.load(json_file)
    return json_data

def write_key_to_file(path, key):
    with open(path, "wb") as file:
        file.write(key)

def read_file(path):
    with open(path, "rb") as file:
        data = file.read()
    return data

def write_text_to_file(path, text):
    with open(path, "wb") as file:
        file.write(text)