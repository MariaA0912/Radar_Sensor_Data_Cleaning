import pandas as pd
import re

# Load CSV file
df = pd.read_csv("radar_fc-objects.csv")

# Function to extract all instances of id and detection_level from the objects column
def extract_info(text):
    # Regular expressions to find id and detection_level
    id_matches = re.findall(r'id:\s*(\d+)', text)
    detection_matches = re.findall(r'detection_level:\s*(\d+)', text)
    # Combine results as tuples (handling multiple objects per row)
    extracted_data = list(zip(id_matches, detection_matches))

    return extracted_data if extracted_data else None

# Apply the function to extract data from the 'objects' column
df['extracted_data'] = df['objects'].apply(lambda x: extract_info(str(x)))

# Expand extracted data into separate rows, keeping the associated Time column
df_exploded = df.explode('extracted_data')

# Split extracted data into separate 'id' and 'detection_level' columns
df_exploded[['id', 'detection_level']] = pd.DataFrame(df_exploded['extracted_data'].tolist(), index=df_exploded.index)

# Keep only necessary columns
df_exploded = df_exploded[['Time', 'id', 'detection_level']]

# Display the cleaned DataFrame
print(df_exploded)

# Save to a new CSV (optional)
df_exploded.to_csv("cleaned_output_check.csv", index=False)
