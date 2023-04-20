import pandas as pd
import os

# Define the folder path where your files are stored
folder_path = "/Users/ben/Documents/CU/DTSA5506"

# Create an empty list to store your data frames
df_list = []

# Loop through each file in the folder
for file_name in os.listdir(folder_path):
    # Check if the file is an Excel file
    if file_name.endswith("Leg.xlsx"):
        # Read the Excel file into a data frame
        df = pd.read_excel(os.path.join(folder_path, file_name))
        # add a new column with the file name
        df['ElectionYear'] = file_name[0:4]
        # Append the data frame to your list
        df_list.append(df)

# Concatenate all data frames into one
combined_df = pd.concat(df_list)

# save dataframe to an excel file
combined_df.to_excel('output.xlsx', index=False)