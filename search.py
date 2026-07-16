import pandas as pd
import os

if not os.path.exists("books.csv"):
    print("books.csv not found! Run scraper.py first.")
    exit()

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


while True:

    print("\n========== BOOK SEARCH SYSTEM ==========")
    print("1. Search Book")
    print("2. Filter by Rating")
    print("3. Sort by Price")
    print("4. Top 10 Expensive Books")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        keyword = input("Enter Book Name: ").lower()

        result = df[df["Title"].str.lower().str.contains(keyword)]

        if len(result) == 0:
            print("No Book Found.")
        else:
            print(result[["Title", "Price", "Rating", "Availability"]])

    elif choice == "2":

        rating = int(input("Enter Rating (1-5): "))

        result = df[df["Rating"] == rating]

        print(result[["Title", "Price", "Rating"]])

    elif choice == "3":

        order = input("Ascending(A) or Descending(D): ").upper()

        if order == "A":
            result = df.sort_values("Price")
        else:
            result = df.sort_values("Price", ascending=False)

        print(result[["Title", "Price"]].head(20))

    elif choice == "4":

        result = df.sort_values("Price", ascending=False)

        print(result[["Title", "Price"]].head(10))

    elif choice == "5":

        print("Thank You!")
        break

    else:

        print("Invalid Choice!")
