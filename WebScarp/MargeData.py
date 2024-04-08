import pandas as pd

# Define the file names
files = ['FinalData1.csv', 'FinalData2.csv', 'FinalData3.csv']

# Initialize an empty list to store dataframes
dataframes = []

# Loop through the file names
for file in files:
    # Read each CSV file into a dataframe and append to the list
    df = pd.read_csv(file)
    dataframes.append(df)

# Concatenate all dataframes into one
merged_df = pd.concat(dataframes, ignore_index=True)

# Save the merged dataframe to a new CSV file
merged_df.to_csv('AllHouseData.csv', index=False)

# Print a success message
print("All CSV files have been successfully merged into HouseData.csv")