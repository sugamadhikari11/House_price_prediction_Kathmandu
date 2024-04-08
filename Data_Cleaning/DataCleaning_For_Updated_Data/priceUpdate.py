import pandas as pd
import re

# Load the dataset from the CSV file
df = pd.read_csv('Landdataremove.csv', skipinitialspace=True)

# Define a function to convert the price to an integer value
def convert_price_to_int(price_str):
    # Remove all characters except digits
    clean_price = re.sub(r'[^0-9]+', '', price_str)
    # Convert to integer if the cleaned price is not empty
    return int(clean_price) if clean_price else None

# Apply the conversion function to the 'Price' column
df['Price'] = df['Price'].apply(convert_price_to_int)

# Save the updated dataframe to a new CSV file called updateprice.csv
df.to_csv('updateprice.csv', index=False)

# Print a success message
print("The Price column has been cleaned and converted to integer values and saved to updateprice.csv")
