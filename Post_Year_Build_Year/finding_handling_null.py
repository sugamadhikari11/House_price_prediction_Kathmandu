import pandas as pd

# Read the FinalData from CSV file
final_data = pd.read_csv("FinalData.csv")

# Find rows where Bedroom or Bathroom have null or zero values
rows_bedroom_bathroom_null = final_data[((final_data['Bedroom'].isnull()) | (final_data['Bedroom'] == 0)) &
                                        ((final_data['Bathroom'].isnull()) | (final_data['Bathroom'] == 0))]


#creating a csv file with the rows where Bedroom or Bathroom have null or zero values
rows_bedroom_bathroom_null.to_csv('rows_bedroom_bathroom_null.csv', index=False)

# print("Rows where Bedroom or Bathroom has null or zero value:")
# for index, row in rows_bedroom_bathroom_null.iterrows():
#     print(f"Index: {index}, Row: {row}")

# Find rows where Bedroom, Bathroom, and Floor have null or zero values
rows_bedroom_bathroom_floor_null = final_data[((final_data['Bedroom'].isnull()) | (final_data['Bedroom'] == 0)) | 
                                               ((final_data['Bathroom'].isnull()) | (final_data['Bathroom'] == 0)) &
                                               ((final_data['Floor'].isnull()) | (final_data['Floor'] == 0))]

#creating a csv file with the rows where Bedroom, Bathroom, and Floor have null or zero values
rows_bedroom_bathroom_floor_null.to_csv('rows_bedroom_bathroom_floor_null.csv', index=False)

# print("\nRows where Bedroom, Bathroom, and Floor has null or zero value:")
# for index, row in rows_bedroom_bathroom_floor_null.iterrows():
#     print(f"Index: {index}, Row: {row}")

# Find rows where Bedroom, Bathroom, Floor, and Parking are all zero or null values
rows_all_zero_or_null = final_data[(final_data['Bedroom'].isnull() | (final_data['Bedroom'] == 0)) & 
                                   (final_data['Bathroom'].isnull() | (final_data['Bathroom'] == 0)) &
                                   (final_data['Floor'].isnull() | (final_data['Floor'] == 0)) &
                                   (final_data['Parking'].isnull() | (final_data['Parking'] == 0))]


#creating a csv file with the rows where Bedroom, Bathroom, Floor, and Parking are all zero or null values
rows_all_zero_or_null.to_csv('rows_all_zero_or_null.csv', index=False)

# print("\nRows where Bedroom, Bathroom, Floor, and Parking are all zero or null:")
# for index, row in rows_all_zero_or_null.iterrows():
#     print(f"Index: {index}, Row: {row}")

# remaining_data = final_data-rows_all_zero_or_null-rows_bedroom_bathroom_floor_null-rows_bedroom_bathroom_null

# # Save the remaining data to a new CSV file
# remaining_data.to_csv("remaining_data.csv", index=False)

#baderoom bathroom and floor null or zero

bedroom_bathroom_floor_null = final_data[((final_data['Bedroom'].isnull()) | (final_data['Bedroom'] == 0)) &
                                        ((final_data['Bathroom'].isnull()) | (final_data['Bathroom'] == 0)) &
                                        ((final_data['Floor'].isnull()) | (final_data['Floor'] == 0))]

#creating a csv file with the rows where Bedroom, Bathroom, and Floor have null or zero values
bedroom_bathroom_floor_null.to_csv('bedroom_bathroom_floor_null.csv', index=False)

#bedroom and floor null or zero
bedroom_floor_null = final_data[((final_data['Bedroom'].isnull()) | (final_data['Bedroom'] == 0)) |
                                        ((final_data['Floor'].isnull()) | (final_data['Floor'] == 0))]

#creating a csv file with the rows where Bedroom and Floor have null or zero values
bedroom_floor_null.to_csv('bedroom_floor_null.csv', index=False)

#beadroom null
bedroom_null = final_data[(final_data['Bedroom'].isnull()) | (final_data['Bedroom'] == 0)]

#creating a csv file with the rows where Bedroom has null or zero values
bedroom_null.to_csv('bedroom_null.csv', index=False)

#floor null
floor_null = final_data[(final_data['Floor'].isnull()) | (final_data['Floor'] == 0)]

#creating a csv file with the rows where Floor has null or zero values
floor_null.to_csv('floor_null.csv', index=False)

#bedroom and floor both not null
bedroom_floor_not_null = final_data[(final_data['Bedroom'].notnull()) & (final_data['Bedroom'] != 0) &
                                    (final_data['Floor'].notnull()) & (final_data['Floor'] != 0)]

#creating a csv file with the rows where Bedroom and Floor have not null values
bedroom_floor_not_null.to_csv('bedroom_floor_not_null.csv', index=False)