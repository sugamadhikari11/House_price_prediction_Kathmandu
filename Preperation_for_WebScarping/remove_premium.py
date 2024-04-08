import csv

def filter_and_remove_duplicates(csv_filename, output_filename):
    with open(csv_filename, 'r') as infile, open(output_filename, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        filtered_data = set()  # Use a set to store unique and filtered values

        for row in reader:
            if row:  # Check if the row is not empty
                url = row[0]
                # Check if 'property' is in the URL and 'premium' is not
                if 'property' in url and 'premium' not in url:
                    filtered_data.add(url)  # Add the URL if it matches the criteria

        for item in filtered_data:
            writer.writerow([item])  # Write each filtered URL back to the CSV

# Call the function with the input and output file names
filter_and_remove_duplicates('filtered_basobaas_Lalitpur.csv', 'final_basobaas_Lalitpur.csv')

print("Links containing 'premium' have been removed and saved to 'final_basobaas.csv'.")
