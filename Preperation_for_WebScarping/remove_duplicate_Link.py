import csv

def remove_duplicates(csv_filename, output_filename):
    with open(csv_filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        unique_data = set()  # Use a set to store unique values

        for row in reader:
            if row:  # Check if the row is not empty
                unique_data.add(row[0])  # Assuming the URL is in the first column

    with open(output_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for item in unique_data:
            writer.writerow([item])  # Write each unique URL back to the CSV

# Call the function with the CSV filename and the desired output filename
remove_duplicates('basobaas_Lalitpur.csv', 'unique_basobaas_Lalitpur.csv')

print("Duplicate values have been removed, and unique values are saved in 'unique_basobaas.csv'.")
