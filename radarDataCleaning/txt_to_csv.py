# importing pandas library 
import pandas as pd 

input_text_file = "test_text_deleter.txt"
output_csv_file = "clean_data.csv"
  
# reading the given csv file  
# and creating dataframe 
account = pd.read_csv(input_text_file, 
                      delimiter = ':') 
  
# store dataframe into csv file 
account.to_csv( output_csv_file, 
               index = None) 