import os
import glob
import jiwer
from jiwer import cer, wer
import matplotlib.pyplot as plt
from scipy.stats import wilcoxon

# folders = ["baseline_large", "baseline_medium", "baseline_small", "baseline_base", "ground_truth"]
# original_directory = os.getcwd()
# for folder in folders:
#     os.chdir(folder)
#     txt_files_in_folder = glob.glob("*.txt")
#     print(f"TXT files in {folder}: {len(txt_files_in_folder)}")
#
#     with open(f"{folder}.txt", "a", encoding="utf-8") as outfile:
#         for file in txt_files_in_folder:
#             with open(file, "r", encoding="utf-8") as infile:
#                 content = infile.read().replace('\n', ' ')  # Replace newlines with spaces to keep content on one line
#                 outfile.write(content + "\n")  # Add a newline after each file's content
#
#     os.chdir(original_directory)  # Change back to the original directory

# Compute CER of each set relative to ground_truth.txt
print("Current working directory:", os.getcwd())
with open("ground_truth.txt", "r", encoding="utf-8") as f0:
    ground_truth = f0.readlines()
with open("baseline_base.txt", "r", encoding="utf-8") as f1:
    baseline_base = f1.readlines()
with open("baseline_small.txt", "r", encoding="utf-8") as f2:
    baseline_small = f2.readlines()
with open("baseline_medium.txt", "r", encoding="utf-8") as f3:
    baseline_medium = f3.readlines()
with open("baseline_large.txt", "r", encoding="utf-8") as f4:
    baseline_large = f4.readlines()
#
# print(f"baseline_base length and type: {len(baseline_base)}; {type(baseline_base)}; first element: {baseline_base[3]}")
# print(f"baseline_small length and type: {len(baseline_small)}; {type(baseline_small)}")
# print(f"baseline_medium length and type: {len(baseline_medium)}; {type(baseline_medium)}")
# print(f"baseline_large length and type: {len(baseline_large)}; {type(baseline_large)}")

data = [baseline_base, baseline_small, baseline_medium, baseline_large]
iteration = 0
for m in data:
    line_no = 0
    cer_scores = []
    wer_scores = []
    for line in m:
        reference = ground_truth[line_no]
        hypothesis = line
        char_error = cer(reference, hypothesis)
        word_error = wer(reference, hypothesis)
        cer_scores.append(char_error)
        wer_scores.append(word_error)
        line_no += 1
    iteration += 1
    if iteration == 1:
        model_name = "baseline_base"
    elif iteration == 2:
        model_name = "baseline_small"
    elif iteration == 3:
        model_name = "baseline_medium"
    elif iteration == 4:
        model_name = "baseline_large"
    print(f"The CERs for {model_name} are: {cer_scores}; average: {sum(cer_scores)/len(cer_scores)}.\n")
    print(f"The WERs for {model_name} are {wer_scores}; average: {sum(cer_scores)/len(cer_scores)}.\n\n")