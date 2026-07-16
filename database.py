import sqlite3
import pandas as pd
import os

if not os.path.exists("books.csv"):
    print("books.csv not found! Run scraper.py first.")
    exit()

# Read CSV
df = pd.read_csv("books.csv")

# Clean Price
df["Price"] = (
    df["Price"]
    .astype(str)
    .str.replace("Â£", "", regex=False)
    .str.replace("£", "", regex=False)
    .str.strip()
)

df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

# Connect to SQLite database
conn = sqlite3.connect("books.db")

# Save DataFrame to SQL table
df.to_sql("books", conn, if_exists="replace", index=False)

conn.commit()
conn.close()

print("Database created successfully!")
print("Data stored in books.db")
