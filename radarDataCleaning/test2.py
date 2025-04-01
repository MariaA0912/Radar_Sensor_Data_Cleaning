import csv
import re

# Function to parse the text file and extract specific fields (Time, id, position, x, y)
def parse_text_to_table(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Initialize a list to hold the rows for the table
    table = []
    
    # Initialize variables to hold values for time, id, position, x, y
    current_row = {}
    current_time = None

    # Define a regex to match numbers starting with '171114'
    time_pattern = re.compile(r"^171114")

    # Iterate through each line of the text file
    for line in lines:
        line = line.strip()

        # Check for Time and update the current_time if the line matches the pattern
        if line.startswith("Time:") and time_pattern.match(line.split(":")[1].strip()):
            current_time = line.split(":", 1)[1].strip()

        # Check for time in unix (lines that start with '171114')
        if time_pattern.match(line):
            current_time = line.strip()

        # Check for id, position, x, y
        if 'id:' in line or 'position:' in line or 'x:' in line or 'y:' in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()

            if key == 'id':
                current_row['id'] = value
            elif key == 'position':
                current_row['position'] = value
            elif key == 'x':
                current_row['x'] = value
            elif key == 'y':
                current_row['y'] = value
        
        # When all required keys are collected (id, position, x, y) for a specific Time, save this row and reset for the next one
        if 'id' in current_row and 'position' in current_row and 'x' in current_row and 'y' in current_row and current_time:
            # Add the current time to the row
            current_row['Time'] = current_time
            table.append(current_row)
            current_row = {}  # Reset the current_row for the next block

    # Write the table to a CSV file
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['Time', 'id', 'position', 'x', 'y']  # Define the table headers
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()  # Write the header row
        for row in table:
            writer.writerow(row)  # Write each row of data

# Example usage
parse_text_to_table('flagged.txt', 'output.csv')
