import os

def merge_files(input_dir, output_file):
    # Open the output file in write mode
    with open(output_file, 'w', encoding="utf8") as outfile:
        # Loop through all files in the input directory
        for filename in os.listdir(input_dir):
            # Construct the full file path
            file_path = os.path.join(input_dir, filename)
            # Check if it's a file (and not a directory)
            if os.path.isfile(file_path):
                # Open the current file in read mode
                with open(file_path, 'r', encoding="utf8") as infile:
                    # Read the content of the file (assumes it's one line)
                    content = infile.readline().strip()
                    # Write the content to the output file followed by a newline
                    outfile.write(content + '\n')

# Specify the input directory and the output file
input_directory = 'ft_large_on_native'
output_file_path = 'data/ft_large_on_native.txt'

# Call the function to merge files
merge_files(input_directory, output_file_path)
