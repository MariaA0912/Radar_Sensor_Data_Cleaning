def remove_spaces_and_write(input_file_path, output_file_path):
   
    try:
        with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
            for line in infile:
                # Remove spaces from each line
                modified_line = line.replace(" ", "")
                # Write the modified line to the output file
                outfile.write(modified_line)
    except FileNotFoundError:
        print(f"Error: Input file not found at {input_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
input_file = "output.txt"  # Replace with your input file path
output_file = "no_spaces_output.txt"  # Replace with your desired output file path
remove_spaces_and_write(input_file, output_file)