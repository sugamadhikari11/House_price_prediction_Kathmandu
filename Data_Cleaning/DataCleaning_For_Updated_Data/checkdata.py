import pandas as pd

# Assuming the data is in a file named 'roadUpdate.csv'
# Load the dataset from the CSV file
df = pd.read_csv('roadUpdate.csv', skipinitialspace=True)

# Define a function to check if the unit is not 'Feet'
def check_road_distance_unit(value):
    if 'Feet' not in value:
        return True
    return False

# Apply the function to the 'Road Distance' column and get the index of rows with units other than 'Feet'
invalid_road_distance_indices = df[df['Road Distance'].apply(check_road_distance_unit)].index.tolist()

# Print the indices and values of rows with invalid 'Road Distance' units
for index in invalid_road_distance_indices:
    print(f"Index: {index}, Road Distance: {df.at[index, 'Road Distance']}")