import csv

# Function to read a CSV file and return a set of links
def read_csv(file_name):
    with open(file_name, mode='r', newline='') as file:
        reader = csv.reader(file)
        return set(row[0] for row in reader if row)  # Assuming links are in the first column

# Read both CSV files
basobaas_links = read_csv('final_basobaas.csv')
lalitpur_links = read_csv('final_basobaas_Lalitpur.csv')

# Find links that are in Lalitpur but not in Basobaas
unmatched_links = lalitpur_links - basobaas_links

# Write unmatched links to a new CSV file
with open('unmatched_links.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    for link in unmatched_links:
        writer.writerow([link])

# Print a success message
print(f"Unmatched links have been written to unmatched_links.csv.")
