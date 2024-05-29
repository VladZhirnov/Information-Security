import json


def read_json(path: str) -> dict:
    """
    Read JSON data from a file.

    Args:
        path (str): The file path to the JSON file.

    Returns:
        dict: The JSON data parsed into a dictionary.
    """
    try:
        with open(path, "r") as json_file:
            json_data = json.load(json_file)
        return json_data
    except FileNotFoundError:
        print("The file was not found!")
    except Exception as e:
        print(f"Error reading json file: {str(e)}")


def write_key_to_file(path: str, key: bytes) -> None:
    """
    Write a key to a file.

    Args:
        path (str): The file path where the key will be written.
        key (bytes): The key to be written to the file.
    """
    try:
        with open(path, "wb") as file:
            file.write(key)
    except FileNotFoundError:
        print("The file was not found!")
    except Exception as e:
        print(f"Error writing key to file: {str(e)}")


def read_file(path: str) -> bytes:
    """
    Read data from a file.

    Args:
        path (str): The file path to read data from.

    Returns:
        bytes: The data read from the file.
    """
    try:
        with open(path, "rb") as file:
            data = file.read()
        return data
    except FileNotFoundError:
        print("The file was not found!")
    except Exception as e:
        print(f"File reading error: {str(e)}")


def write_text_to_file(path: str, text: str) -> None:
    """
    Write text to a file.

    Args:
        path (str): The file path where the text will be written.
        text (str): The text to be written to the file.
    """
    try:
        if type(text) is bytes:
            with open(path, "wb") as file:
                file.write(text)
        else:
            with open(path, "w") as file:
                file.write(text)
    except FileNotFoundError:
        print("The file was not found!")
    except Exception as e:
        print(f"Error writing text to file: {str(e)}")