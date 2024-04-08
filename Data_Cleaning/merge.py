import pandas as pd

# Load the two CSV files
df1 = pd.read_csv('roaddistanceupdate1.csv')
df2 = pd.read_csv('roaddistanceupdate2.csv')

# Merge the two dataframes
merged_df = pd.concat([df1, df2])

# Save the merged dataframe to a new CSV file
merged_df.to_csv('MergeData.csv', index=False)

# Print a success message
print("The two CSV files have been successfully merged into MergeData.csv")
