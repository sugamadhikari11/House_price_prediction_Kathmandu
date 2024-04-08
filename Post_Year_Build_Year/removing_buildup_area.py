import pandas as pd

# Read the original dataset from vallydata.csv
original_df = pd.read_csv("vallydata.csv")

# Drop the "Build Up Area" column
modified_df = original_df.drop(columns=["Build Up Area"])

# Save the modified dataset to a new CSV file
modified_df.to_csv("rmb_vallyData.csv", index=False)

print("The 'Build Up Area' column has been removed. The modified dataset is saved as 'rmb_vallyData.csv'.")