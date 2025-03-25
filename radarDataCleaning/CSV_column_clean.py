import pandas as pd

def filter_time_and_objects(input_csv, output_csv):
    
    # Load the CSV file into a DataFrame
    df = pd.read_csv(input_csv)

    # Extract 'Time' and 'object' columns
    time_column = df['Time']
    #making sure to ignore 'header.frame_id' column and only grab objects
    object_column = df.select_dtypes(include=['object']).drop(columns=['header.frame_id'], errors='ignore')


    
    # Concatenate object columns on the right and time column on the left
    filtered_df = pd.concat([ time_column, object_column], axis=1)
    
    # Save the filtered dataframe to a new CSV file
    filtered_df.to_csv(output_csv, index=False)
    
    print(f"Filtered file saved as: {output_csv}")

# Example usage
input_file = "radar_fc-objects.csv"  # Change this to your actual file
output_file = "column_cleaned.csv"
filter_time_and_objects(input_file, output_file)
