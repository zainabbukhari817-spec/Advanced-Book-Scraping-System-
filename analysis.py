import os
import pandas as pd
import matplotlib.pyplot as plt

# Check if books.csv exists
if not os.path.exists("books.csv"):
    print("books.csv not found! Please run scraper.py first.")
    exit()

# Create charts folder
os.makedirs("charts", exist_ok=True)

# Read CSV
df = pd.read_csv("books.csv")

# -----------------------------
# Clean Price Column
# -----------------------------
df["Price"] = (
    df["Price"]
    .astype(str)
    .str.replace("Â£", "", regex=False)
    .str.replace("£", "", regex=False)
    .str.replace("Â", "", regex=False)
    .str.strip()
)

# Convert to float
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

# Remove invalid rows
df = df.dropna(subset=["Price"])

# Statistics

print("\n========== BOOK ANALYSIS ==========\n")

print(f"Total Books: {len(df)}")
print(f"Average Price: £{df['Price'].mean():.2f}")
print(f"Highest Price: £{df['Price'].max():.2f}")
print(f"Lowest Price: £{df['Price'].min():.2f}")

print("\nAverage Price by Rating:")
print(df.groupby("Rating")["Price"].mean())



plt.figure(figsize=(8, 5))
plt.hist(df["Price"], bins=15)
plt.title("Book Price Distribution")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")
plt.grid(True)
plt.tight_layout()
plt.savefig("charts/price_distribution.png")
plt.close()

# Rating Distribution

rating_counts = df["Rating"].value_counts().sort_index()

plt.figure(figsize=(6, 4))
plt.bar(rating_counts.index.astype(str), rating_counts.values)
plt.title("Book Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Books")
plt.grid(True)
plt.tight_layout()
plt.savefig("charts/rating_distribution.png")
plt.close()


# Top 10 Most Expensive Books

top_books = df.nlargest(10, "Price")

plt.figure(figsize=(10, 6))
plt.barh(top_books["Title"], top_books["Price"])
plt.title("Top 10 Most Expensive Books")
plt.xlabel("Price (£)")
plt.tight_layout()
plt.savefig("charts/top_expensive_books.png")
plt.close()

print("\nCharts have been saved in the 'charts' folder.")
print("Analysis completed successfully!")
