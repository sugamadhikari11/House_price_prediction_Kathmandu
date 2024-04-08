import pandas as pd
import re

# Assuming the data is in a file named 'roadUpdate.csv'
# Load the dataset from the CSV file
df = pd.read_csv('roadUpdate.csv', skipinitialspace=True)

# Define a function to remove 'Feet' and convert to int
def convert_road_distance(value):
    # Remove 'Feet' and any other non-numeric characters
    clean_value = re.sub(r'[^0-9]+', '', value)
    # Convert to int if the cleaned value is not empty
    return int(clean_value) if clean_value else None

# Apply the conversion function to the 'Road Distance' column
df['Road Distance'] = df['Road Distance'].apply(convert_road_distance)

# Save the updated dataframe to a new CSV file called roaddistanceupdate.csv
df.to_csv('roaddistanceupdate.csv', index=False)

# Print a success message
print("The 'Road Distance' column has been updated and saved to roaddistanceupdate.csv")
