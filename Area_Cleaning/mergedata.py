import pandas as pd

# Load the datasets
df1 = pd.read_csv('finaldata1.csv')
df2 = pd.read_csv('finaldata2.csv')

# Merge the two datasets
final_df = pd.concat([df1, df2], ignore_index=True)

# Save the merged dataset to a new CSV file
final_df.to_csv('FinalData.csv', index=False)

print("The datasets finaldata1 and finaldata2 have been successfully merged into FinalData.csv.")
