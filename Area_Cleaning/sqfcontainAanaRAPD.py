import pandas as pd
import re

# Load the dataset
df = pd.read_csv('RAPDformat.csv')

# Define the conversion factors for each number in the format '0-4-1-2 Aana'
conversion_factors = [5476, 342.25, 85.56, 21.39]

# Function to convert 'Area Covered' values to float
def convert_area_covered(area_covered):
    if pd.isna(area_covered):
        return None
    # Extract the numbers from the string
    numbers = re.findall(r'\d+', area_covered)
    # Convert each number to float and multiply by the corresponding conversion factor
    converted_numbers = [float(num) * factor for num, factor in zip(numbers, conversion_factors)]
    # Sum the converted numbers
    return sum(converted_numbers)

# Apply the conversion to the 'Area Covered' column
df['Area Covered'] = df['Area Covered'].apply(convert_area_covered)

# Save the updated dataframe to a new CSV file
df.to_csv('finaldata1.csv', index=False)

print("The 'Area Covered' column has been updated and the new file 'finaldata1.csv' has been saved.")
