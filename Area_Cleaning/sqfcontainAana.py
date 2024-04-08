import pandas as pd

# Load the dataset
df = pd.read_csv('Aana_Format.csv')

# Define a conversion factor from Aana to square feet
conversion_factor = 342.25

# Function to extract the numeric part and convert Aana to square feet
def convert_aana_to_sqft(area_covered):
    if pd.isna(area_covered):
        return area_covered
    # Extract the numeric part
    numeric_part = ''.join(filter(str.isdigit, area_covered))
    if numeric_part:
        # Convert to float and multiply by conversion factor
        return float(numeric_part) * conversion_factor
    else:
        return None

# Apply the conversion to the 'Area Covered' column
df['Area Covered'] = df['Area Covered'].apply(convert_aana_to_sqft)

# Save the updated dataframe to a new CSV file
df.to_csv('finaldata2.csv', index=False)

print("The 'Area Covered' column has been updated and the new file 'finaldata2.csv' has been saved.")
