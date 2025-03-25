import pandas as pd

def csv_to_document(csv_file, output_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)
    
    # Open the output file in write mode
    with open(output_file, 'w') as file:
        # Iterate over each row in the DataFrame
        for index, row in df.iterrows():
            # Extract the Time column and Objects column, and write them to the document
            file.write(f"{row['Time']}: {row['objects']}\n")

    print(f"Document created: {output_file}")

# Example usage:
csv_to_document('column_cleaned.csv', 'output.txt')
