import pandas as pd

# Read the original dataset from vallydataset.csv
original_df = pd.read_csv("rmb_vallyData.csv")

# Convert "Build Year" values to integers
original_df["Build Year"] = original_df["Build Year"].apply(lambda year: int(year + 57) if 1990 <= year <= 2024 else year)

# Save the modified dataset to a new CSV file
original_df.to_csv("byu_vallyData.csv", index=False)

print("The 'Build Year' values have been adjusted. The modified dataset is saved as 'byu_vallyData.csv'.")

