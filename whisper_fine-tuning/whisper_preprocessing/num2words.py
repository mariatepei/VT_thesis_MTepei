import os
import re

# Define units, teens, tens, and thousands in Dutch
units = ["", "een", "twee", "drie", "vier", "vijf", "zes", "zeven", "acht", "negen"]
teens = ["tien", "elf", "twaalf", "dertien", "veertien", "vijftien", "zestien", "zeventien", "achttien", "negentien"]
tens = ["", "", "twintig", "dertig", "veertig", "vijftig", "zestig", "zeventig", "tachtig", "negentig"]
thousands = ["", "duizend"]


def number_to_dutch(n):
    if n == 0:
        return "nul"
    elif n < 10:
        return units[n]
    elif 10 <= n < 20:
        return teens[n - 10]
    elif 20 <= n < 100:
        if n % 10 == 0:
            return tens[n // 10]
        else:
            return units[n % 10] + "en" + tens[n // 10]
    elif 100 <= n < 1000:
        if n % 100 == 0:
            return units[n // 100] + "honderd"
        else:
            return units[n // 100] + "honderd" + number_to_dutch(n % 100)
    elif 1000 <= n < 10000:
        if n % 1000 == 0:
            return units[n // 1000] + "duizend"
        else:
            return units[n // 1000] + "duizend" + number_to_dutch(n % 1000)


def convert_numbers_to_words(text):
    """
    Convert all numbers in the given text to Dutch words.
    """

    def replace_number(match):
        number = int(match.group(0))
        return number_to_dutch(number)

    # Regular expression to find numbers in the text
    number_pattern = re.compile(r'\b\d+\b')
    return number_pattern.sub(replace_number, text)


def process_file(file_path):
    """
    Read a file, convert numbers to words, and save the changes to the same file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    updated_lines = [convert_numbers_to_words(line) for line in lines]

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(updated_lines)


files = ["baseline_base.txt",
         "baseline_n_base.txt",
         "baseline_small.txt",
         "baseline_n_small.txt",
         "baseline_medium.txt",
         "baseline_n_medium.txt",
         "baseline_large.txt",
         "baseline_n_large.txt",
         "ground_truth.txt",
         "ground_truth_n.txt"
         ]
for filename in files:
    process_file(filename)
    print(f"Processed {filename}")
