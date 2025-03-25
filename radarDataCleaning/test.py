import csv

# Function to parse the text file and extract specific fields (id, position, x, y)
def parse_text_to_table(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Initialize a list to hold the rows for the table
    table = []
    
    # Initialize variables to hold values for id, position, x, y
    current_row = {}

    # Iterate through each line of the text file
    for line in lines:
        line = line.strip()
        
        # Check if the line contains one of the required keys (id, position, x, y)
        if 'id:' in line or 'position:' in line or 'x:' in line or 'y:' in line:
            # Split the line into key-value pair
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()

            # Add the key-value pair to the current row if it's part of the required keys
            if key in ['id', 'position', 'x', 'y']:
                current_row[key] = value
        
        # When all required keys are collected (id, position, x, y), save this row and reset for the next one
        if 'id' in current_row and 'position' in current_row and 'x' in current_row and 'y' in current_row:
            table.append(current_row)
            current_row = {}  # Reset the current_row for the next block

    # Write the table to a CSV file
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['id', 'position', 'x', 'y']  # Define the table headers
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()  # Write the header row
        for row in table:
            writer.writerow(row)  # Write each row of data

# Example usage
parse_text_to_table('test_text_deleter.txt', 'output.csv')
