import pandas as pd
import re

# Load the dataset
df = pd.read_csv('AanaNotRAPDformat.csv')

# Define a regular expression pattern to match the 'Aana' format
aana_pattern = re.compile(r'^\d+(\.\d+)?\sAana$')

# Create two separate DataFrames based on the pattern
df_aana_format = df[df['Area Covered'].str.match(aana_pattern, na=False)]
df_other_format = df[~df['Area Covered'].str.match(aana_pattern, na=False)]

# Save the separated data into two different CSV files
df_aana_format.to_csv('Aana_Format.csv', index=False)
df_other_format.to_csv('Other_Format.csv', index=False)

# Print success messages
print(f"Data with 'Aana' format saved to Aana_Format.csv")
print(f"Data with other formats saved to Other_Format.csv")
