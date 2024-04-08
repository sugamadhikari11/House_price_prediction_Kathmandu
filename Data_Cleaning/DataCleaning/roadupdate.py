import pandas as pd

# Load the dataset from the CSV file
df = pd.read_csv('updateprice.csv', skipinitialspace=True)

# Split the 'Road Access' column into 'Road Distance' and 'Type of Road'
df[['Road Distance', 'Type of Road']] = df['Road Access'].str.split(' / ', expand=True)

# Drop the original 'Road Access' column
df.drop('Road Access', axis=1, inplace=True)

# Save the updated dataframe to a new CSV file called roadUpdate.csv
df.to_csv('roadUpdate.csv', index=False)

# Print a success message
print("The 'Road Access' column has been split into 'Road Distance' and 'Type of Road' and saved to roadUpdate.csv")
