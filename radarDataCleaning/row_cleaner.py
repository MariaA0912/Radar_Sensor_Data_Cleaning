import csv
from collections import defaultdict

# Function to restructure CSV into Unix Time-based columns
def restructure_csv(input_file, output_file):
    # Read the CSV data
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        rows = list(reader)
    
    # Dictionary to store the grouped data by Unix time
    unix_data = defaultdict(lambda: {'id': None, 'position': None, 'x': None, 'y': None})
    
    # Loop through the rows and organize them by Unix time
    for row in rows:
        if row and len(row) >= 3:
            unix_time = row[0].strip()  # Get the Unix timestamp from the first column
            key = row[1].strip()  # Get the label ('id', 'position', 'x', 'y')
            value = row[2].strip()  # Get the value from the second column

            # Store the value based on the label (id, position, x, y)
            if key in unix_data[unix_time]:
                unix_data[unix_time][key] = value

    # Prepare the output CSV data with header
    header = ['Unix Time', 'id', 'position', 'x', 'y']
    
    # Open the output CSV file and write the grouped data
    with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(header)  # Write the header row
        
        # Write the grouped data for each Unix time
        for unix_time in sorted(unix_data.keys()):
            row = [unix_time]
            row.extend([unix_data[unix_time]['id'], unix_data[unix_time]['position'], 
                        unix_data[unix_time]['x'], unix_data[unix_time]['y']])
            writer.writerow(row)

# Example usage
restructure_csv('clean_data.csv', 'row_cleaner.csv')

