import csv

def filter_and_remove_duplicates(csv_filename, output_filename):
    with open(csv_filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        filtered_data = set()  # Use a set to store unique and filtered values

        for row in reader:
            if row:  # Check if the row is not empty
                url = row[0]
                # Check if 'house-for-sale' is in the URL
                if 'house-for-sale' in url:
                    filtered_data.add(url)  # Add the URL if it matches the criteria

    with open(output_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for item in filtered_data:
            writer.writerow([item])  # Write each filtered URL back to the CSV

# Call the function with the CSV filename and the desired output filename
filter_and_remove_duplicates('unique_basobaas_Lalitpur.csv', 'filtered_basobaas_Lalitpur.csv')

print("URLs not containing 'house-for-sale' have been removed, and unique values are saved in 'filtered_basobaas.csv'.")
