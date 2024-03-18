import argparse
import json
import math
import re
import scipy


pi = [0.2148, 0.3672, 0.2305, 0.1875]


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
    return p
        

def identical_bits_test(bits_row):
    z = 0
    for bit in bits_row:
        z  += (1 / 128) * int(bit)
    if abs(z - 1/2) < (2 / pow(128, 0.5)):
        v = sum(bits_row[i] == bits_row[i + 1] for i in range(len(bits_row) - 1))
        p = math.erfc((abs(v - 2 * 128 * z * (1 - z))) / (2 * pow(2 * 128, 0.5) * z * (1 - z)))
    else:
        p = 0
    return p


def sequence_of_units_test(bits_row):
    v1 = v2 = v3 = v4 = 0
    divided_bits = re.findall(r'.{%s}' % 8, bits_row)
    for row in divided_bits:
        k = 0
        max_k = 0
        for bit in row:
            if bit == "1":
                k += 1
            if k > max_k:
                max_k = k
            if bit == "0":
                k = 0
        if max_k == 1 or max_k < 1:
            v1 += 1
        elif max_k == 2:
            v2 += 1
        elif max_k == 3:
            v3 += 1
        else:
            v4 += 1
    v = [v1, v2, v3, v4]
    x_square = 0
    for i in range(4):
        x_square += (pow(v[i] - 16 * pi[i], 2)) / (16 * pi[i])
    p = scipy.special.gammainc(3 / 2,  x_square / 2)
    return p


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
    with open(bits_row["path"], mode = "w", encoding = "utf-8") as results:
        results.write("NIST TEST RESULTS:\n")
        results.write("C++:\n")
        results.write(f"1) Frequency bit test: P = {frequency_bit_test(cpp_row)}\n")
        results.write(f"2) Identical bits test: P = {identical_bits_test(cpp_row)}\n")
        results.write(f"3) Sequence of units test: P = {sequence_of_units_test(cpp_row)}\n")

        results.write("Java:\n")
        results.write(f"1) Frequency bit test: P = {frequency_bit_test(java_row)}\n")
        results.write(f"2) Identical bits test: P = {identical_bits_test(java_row)}\n")
        results.write(f"3) Sequence of units test: P = {sequence_of_units_test(java_row)}\n")
