import pandas as pd
import re

# Define a function to check for Nepali words
def contains_nepali_words(text):
    # Define a regex pattern for Nepali words (assuming Nepali words are non-ASCII characters)
    pattern = re.compile(r'[\u0900-\u097F]+')
    # Search for the pattern in the text
    if pattern.search(text):
        return True
    return False

# Load the dataset from the CSV file
df = pd.read_csv('HouseData.csv', skipinitialspace=True)

# Iterate over each row and column to check for Nepali words
for index, row in df.iterrows():
    for column in df.columns:
        # Check if the cell is a string and contains Nepali words
        if isinstance(row[column], str) and contains_nepali_words(row[column]):
            print(f"Nepali words found in row {index+1}, column '{column}': {row[column]}")

