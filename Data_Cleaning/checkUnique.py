import pandas as pd

# Load the merged CSV file
try:
    merged_df = pd.read_csv('MergeData.csv')
except FileNotFoundError:
    print("Error: The MergeData.csv file does not exist. Please make sure it is in the same directory as this script.")
    exit()

# Remove duplicate rows and keep the first occurrence
unique_df = merged_df.drop_duplicates()

# Save the unique dataframe to a new CSV file
unique_df.to_csv('FinalData.csv', index=False)

# Print a success message
print("Duplicate rows have been removed, and the unique data has been saved to FinalData.csv")
