import pandas as pd
import re

# Load the dataset
df = pd.read_csv('CleanedData.csv')

# Define a function to check if the 'Area Covered' column contains the specified format
def contains_RAPD_format(area_covered):
    pattern = r'\d{1,2}-\d{1,2}-\d{1,2}-\d{1,2}'  # Define the regex pattern for the format
    return bool(re.search(pattern, str(area_covered)))  # Check if the pattern exists in the string

# Separate rows based on whether 'Area Covered' contains the RAPD format or not
contains_custom = df[df['Area Covered'].apply(contains_RAPD_format)]
not_contains_custom = df[~df['Area Covered'].apply(contains_RAPD_format)]

# Save each separated dataframe to a separate CSV file
contains_custom.to_csv('RAPDformat.csv', index=False)
not_contains_custom.to_csv('NotRAPDformat.csv', index=False)

print("Data separated and saved into two different files.")
