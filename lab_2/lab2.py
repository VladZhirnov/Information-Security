import argparse
import json
import math


def frequency_bit_test(bits_row):
    x = None
    s = 0
    for bit in bits_row:
        if bit == "1":
            x = 1
        else:
            x = -1
        s += (1 / pow(128, 0.5)) * x
    p = math.erfc(s / pow(2, 0.5))
    print(f"P = {p}")
        

def identical_bits_test(bits_row):
    z = 0
    for bit in bits_row:
        z  += (1 / 128) * int(bit)
    if abs(z - 1/2) < (2 / pow(128, 0.5)):
        v = sum(bits_row[i] == bits_row[i + 1] for i in range(len(bits_row) - 1))
        p = math.erfc((abs(v - 2 * 128 * z * (1 - z))) / (2 * pow(2 * 128, 0.5) * z * (1 - z)))
    else:
        p = 0
    print(f"P = {p}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=" ")
    parser.add_argument("random_bits_json_file", help="Path to the input file")
    args = parser.parse_args()
    try:
        with open(args.random_bits_json_file, "r", encoding="utf-8") as f:
            bits_row = json.load(f)
    except Exception as e:
         print(f"Error with {args.random_bits_json_file} file: {str(e)}")
    cpp_row = bits_row["c++"]
    java_row = bits_row["java"]
    frequency_bit_test(cpp_row)
    identical_bits_test(cpp_row)
    frequency_bit_test(java_row)
    identical_bits_test(java_row)
