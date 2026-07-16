import pandas as pd
import os

if not os.path.exists("books.csv"):
    print("books.csv not found! Run scraper.py first.")
    exit()

df = pd.read_csv("books.csv")

# Clean Price column
df["Price"] = (
    df["Price"]
    .astype(str)
    .str.replace("Â£", "", regex=False)
    .str.replace("£", "", regex=False)
    .str.strip()
)

df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

# Export to Excel
df.to_excel("books.xlsx", index=False)

# Export to JSON
df.to_json("books.json", orient="records", indent=4)

print("✅ books.xlsx created successfully.")
print("✅ books.json created successfully.")
