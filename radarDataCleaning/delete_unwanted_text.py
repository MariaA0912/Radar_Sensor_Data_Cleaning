import re
#Define patterns of lines to remove
patterns_to_remove = [r"\[header:", r"seq:0", r"stamp:", r"secs:0", r"nsecs:0", r"frame_id:\"radar_fc\"", r"detection_level:1"
                        , r"object_classified:False", r"pose:", r"orientation:", r"x:0.0\n", r"y:0.0\n", r"z:0.0\n", r"w:1.0", r"covariance:"
                        , r"\[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0\]"
                        , r"polygon:", r"points:\[\]", r"shape:", r"type:0", r"dimensions:\[\]", r"\[\]", r"classification:0", r"classification_certainty:10"
                        , r"classification_age:0", r"header:", r"twist:", r"angular:", r"accel:", r",", r"linear:", r"\]", r"y:-0.0\n", r"x:-0.0\n", r"x:0\n", r"y:0\n", r"x:\-?0\.00",r"x:\-?0\.0", r"y:\-?0\.00", r"x:0.00", r"y:0.00"]  # Modify as needed

 # Read the text file
with open("no_spaces_output.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()


# Modify lines instead of removing them entirely
cleaned_lines = [re.sub("|".join(patterns_to_remove), "", line) for line in lines]

# Write the cleaned content back to the file
with open("test_text_deleter.txt", "w", encoding="utf-8") as file:
    file.writelines(cleaned_lines)

print("Filtered file saved as 'test_text_deleter.txt'")