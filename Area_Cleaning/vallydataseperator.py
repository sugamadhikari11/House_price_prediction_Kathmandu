import pandas as pd

# Load the dataset
df = pd.read_csv('FinalData.csv') 

# Function to check if the district is 'kathmandu' or 'lalitpur'
def is_valley_district(district):
    return district.lower() in ['kathmandu', 'lalitpur','bhaktapur']

# Separate the dataframe based on the district
valley_df = df[df['District'].apply(is_valley_district)]
out_of_valley_df = df[~df['District'].apply(is_valley_district)]

# Save the separated dataframes to their respective CSV files
valley_df.to_csv('vallydata.csv', index=False)
out_of_valley_df.to_csv('outofvallydata.csv', index=False)

print("The data has been separated into 'vallydata.csv' and 'outofvallydata.csv' based on the 'District' column.")
