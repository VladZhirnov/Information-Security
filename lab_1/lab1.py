import json

def encryption_by_substitution():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    with open('Information-Security/lab_1/encryption_key1.json') as f:
        templates = json.load(f)
    for section, commands in templates.items():
        step = int(('\n'.join(commands)))
    with open("Information-Security/lab_1/original1.txt") as file:
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
    with open('Information-Security/lab_1/encryption_key1.json') as f:
        templates = json.load(f)
    for section, commands in templates.items():
        step = int(('\n'.join(commands)))
    with open("Information-Security/lab_1/result1.txt") as file:
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

def check_character_frequency():
    with open("Information-Security/lab_1/original_cod9.txt") as file:
        original = file.read().upper()
    count = len(original) - 10
    arr_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-/;<=>?@[\]^_`"
    for i in arr_letters:
        if i in original:
            count_symbol = original.count(i)
            print(f"{i}({count_symbol}) : {count_symbol / count}")

def decryption_by_frequency_analysis(filename, replacements_file):
    with open(replacements_file, "r", encoding="utf-8") as json_file:
        replacements = json.load(json_file)
    with open(filename, "r", encoding="utf-8") as file:
        encoded_text = file.read().upper()
    decoded_text = ""
    for char in encoded_text:
        decoded_char = replacements.get(char, char)
        decoded_text += decoded_char
    print(decoded_text)

if __name__ == "__main__":
    decryption_by_substitution()
    encryption_by_substitution()
    check_character_frequency()
    decryption_by_frequency_analysis("Information-Security/lab_1/original_cod9.txt", "Information-Security/lab_1/replacements.json")
    