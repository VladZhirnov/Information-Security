import json
import argparse
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encryption_or_decryption_by_substitution(encryption_key1_file, input_file, mode):
    try:
        with open(encryption_key1_file) as f:
            templates = json.load(f)
    except FileNotFoundError:
        print(f"Error: File {encryption_key1_file} not found!")
        return
    for section, commands in templates.items():
        step = int(('\n'.join(commands)))
    try:
        with open(input_file) as file:
            data = file.read().upper()
    except FileNotFoundError:
        print(f"Error: {input_file} File not found!")
        return
    output = ""
    for i in data:
        place = ALPHABET.find(i)
        new_place = None
        match mode:
            case 'encryption':
                new_place = place + step
            case 'decryption':
                new_place = place - step
        if i in ALPHABET:
            output += ALPHABET[new_place] 
        else:
            output += i
    print(output)

def check_character_frequency(original_cod9_file):
    try:
        with open(original_cod9_file) as file:
            original = file.read().upper()
    except FileNotFoundError:
        print(f"Error: File {original_cod9_file} not found!")
        return
    count = len(original)
    arr_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-/;<=>?@[\]^_`"
    for i in arr_letters:
        if i in original:
            count_symbol = original.count(i)
            print(f"{i}({count_symbol}) : {count_symbol / count}")

def decryption_by_frequency_analysis(filename, replacements_file):
    try:
        with open(replacements_file, "r", encoding="utf-8") as json_file:
            replacements = json.load(json_file)
    except FileNotFoundError:
        print(f"Error: File {replacements_file} not found!")
        return
    try:
        with open(filename, "r", encoding="utf-8") as file:
            encoded_text = file.read().upper()
    except FileNotFoundError:
        print(f"Error: File {filename} not found!")
        return
    decoded_text = ""
    for char in encoded_text:
        decoded_char = replacements.get(char, char)
        decoded_text += decoded_char
    print(decoded_text)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Substitution encryption/decryption")
    parser.add_argument("encryption_key1_file", help="Path to the encryption key file")
    parser.add_argument("input_file", help="Path to the input file")
    parser.add_argument("mode", choices=['encryption', 'decryption'], help="Mode of operation: encryption or decryption")
    parser.add_argument("original_cod9_file", help="Path to the original cod9 file")
    parser.add_argument("replacements_file", help="Path to the replacements file")
    args = parser.parse_args()

    encryption_or_decryption_by_substitution(args.encryption_key1_file, args.input_file, args.mode)
    check_character_frequency(args.original_cod9_file)
    decryption_by_frequency_analysis(args.original_cod9_file, args.replacements_file)
    