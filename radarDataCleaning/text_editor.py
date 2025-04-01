import re

# Define the pattern for numbers starting with "12345"
pattern = r"\b171114\d*\b"  # \b ensures it's a standalone word, \d* allows variations

# Read the file
with open("test_text_deleter.txt", "r") as file:
    lines = file.readlines()

# Process the lines while inserting "Word" before matching numbers
modified_lines = []
for i, line in enumerate(lines):
    if re.search(pattern, line):  # If the pattern is found
        if i == 0:  # If it's the first line, insert at the start
            modified_lines.append("Time:\n")
        else:
            modified_lines.append("Time:\n")  # Insert "Word" before the match
    
    modified_lines.append(line)  # Always add the current line

# Write to a new file
with open("flagged.txt", "w") as file:
    file.writelines(modified_lines)

print("Modification complete. Check flagged.txt!")
