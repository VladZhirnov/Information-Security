import json

def encryption_by_substitution():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    with open('Information-Security/lab_1/encryption_key.json') as f:
        templates = json.load(f)
    for section, commands in templates.items():
        step = int(('\n'.join(commands)))
    with open("Information-Security/lab_1/original.txt") as file:
        original = file.read().upper()
    result = ""
    for i in original:
        place = alphabet.find(i)
        new_place = place + step
        if i in alphabet:
            result += alphabet[new_place] 
        else:
            result += i
    print(result)

def decryption_by_substitution():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    with open('Information-Security/lab_1/encryption_key.json') as f:
        templates = json.load(f)
    for section, commands in templates.items():
        step = int(('\n'.join(commands)))
    with open("Information-Security/lab_1/result.txt") as file:
        result = file.read().upper()
    original = ""
    for i in result:
        place = alphabet.find(i)
        new_place = place - step
        if i in alphabet:
            original += alphabet[new_place] 
        else:
            original += i
    print(original)

if __name__ == "__main__":
    decryption_by_substitution()
    encryption_by_substitution()