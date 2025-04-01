import csv

# Input and output file names
input_file = "cData.csv"
output_file = "cData_clean.csv"

# Column index to check (0-based index)
column_index = 0  # Change this if the number is in a different column

# Open the input file and process
with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8", newline="") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    for row in reader:
        if len(row) > column_index:  # Ensure column exists
            value = row[column_index].strip()
            if value.isdigit() and not value.startswith("171114"):
                continue  # Skip this row
        
        writer.writerow(row)  # Write the row if it doesn't match the condition

print(f"Filtered file saved as '{output_file}'")