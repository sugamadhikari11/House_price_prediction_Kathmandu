import pandas as pd

# Load the dataset from the CSV file
df = pd.read_csv('HouseData.csv', skipinitialspace=True)

# Define a function to extract district and location from the address
def extract_district_location(address):
    # Split the address using ',' as the separator
    parts = address.split(',')
    # The last part is the district and the second last part is the location
    district = parts[-1].strip()
    location = parts[-2].strip()
    return district, location

# Apply the function to the 'Address' column and create new columns 'District' and 'Location'
df['District'], df['Location'] = zip(*df['Address'].apply(extract_district_location))

# Drop the original 'Address' column
df.drop('Address', axis=1, inplace=True)

# Save the updated dataframe to a new CSV file
df.to_csv('UpdatedHouseData.csv', index=False)

# Print a success message
print("The Address column has been separated into District and Location columns and saved to UpdatedHouseData.csv")
