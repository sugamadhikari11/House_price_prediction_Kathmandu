import pandas as pd

# Load the dataset
data = pd.read_csv('byu_vallyData.csv')

# Function to convert Posted Date to months
def convert_to_months(posted_date):
    if 'day' in posted_date or 'week' in posted_date:
        return 1
    elif 'month' in posted_date:
        return int(posted_date.split()[0])
    elif 'year' in posted_date:
        return int(posted_date.split()[0]) * 12
    else:
        return 0

# Apply the function to the Posted Date column
data['Posted Date'] = data['Posted Date'].apply(convert_to_months)

# Save the updated dataset to a new CSV file
data.to_csv('FinalData.csv', index=False)

print("The 'Posted Date' values have been updated to months. The updated dataset is saved as 'FinalData.csv'.")