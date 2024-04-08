import csv
import pandas as pd

# Read the dataset using pandas
df = pd.read_csv('UpdatedHouseData.csv')

# Define the patterns to look for in the 'Price' column
patterns = ['per aana', 'per ana']

# Remove rows where 'Price' column contains any of the patterns (case-insensitive)
df = df[~df['Price'].str.lower().str.contains('|'.join(patterns))]

# Write the updated data to a new CSV file
df.to_csv('Landdataremove.csv', index=False)

# Print a success message
print("Rows with 'per Aana' or 'Per Ana' in the 'Price' column have been removed and saved to Landdataremove.csv.")