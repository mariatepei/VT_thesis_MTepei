with open("CSS10_Dutch/transcript.txt", "r") as f:
    lines = f.readlines()

labs = []
for line in lines:
    file_name, text, preprocessed_text, duration = line.split("|")
    file_name = file_name.split("/")[-1]
    print(file_name, preprocessed_text)
    lab_file = file_name.replace(".wav", ".lab")
    with open("CSS10_Dutch/labs/" + lab_file, "w") as f:
        f.write(preprocessed_text)
