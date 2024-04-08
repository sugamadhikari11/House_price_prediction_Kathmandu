import pandas as pd

# Load the dataset
df = pd.read_csv('NotRAPDformat.csv')

# Define a function to check if the 'Area Covered' column contains 'aana' or 'ana' (case-insensitive)
def contains_aana_or_ana(area_covered):
    area_covered_lower = str(area_covered).lower()  # Convert to lowercase
    return 'aana' in area_covered_lower or 'ana' in area_covered_lower

# Separate rows based on whether 'Area Covered' contains 'aana' or 'ana'
contains_aana = df[df['Area Covered'].apply(contains_aana_or_ana)]
not_contains_aana = df[~df['Area Covered'].apply(contains_aana_or_ana)]

# Save each separated dataframe to a separate CSV file
contains_aana.to_csv('AanaNotRAPDformat.csv', index=False)
not_contains_aana.to_csv('NotAanaNotRAPDformat.csv', index=False)

print("Data separated and saved into two different files.")
