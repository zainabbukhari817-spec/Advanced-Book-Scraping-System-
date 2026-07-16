import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

BASE_URL = "https://books.toscrape.com/"


def get_rating(star_class):
    ratings = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }
    return ratings.get(star_class, 0)


books_data = []

print("Starting Scraping...\n")

for page in range(1, 51):

    if page == 1:
        url = BASE_URL + "catalogue/page-1.html"
    else:
        url = BASE_URL + f"catalogue/page-{page}.html"

    print(f"Scraping Page {page}...")

    try:

        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            print("Page not found.")
            continue

        soup = BeautifulSoup(response.text, "lxml")

        books = soup.find_all("article", class_="product_pod")

        for book in books:

            title = book.h3.a["title"]

            price = book.find("p", class_="price_color").text

            availability = book.find(
                "p",
                class_="instock availability"
            ).text.strip()

            rating = get_rating(book.p["class"][1])

            relative_link = book.h3.a["href"]
            product_url = (
                BASE_URL
                + "catalogue/"
                + relative_link.replace("../", "")
            )

            image = book.find("img")["src"]
            image_url = (
                BASE_URL
                + image.replace("../", "")
            )

            books_data.append({
                "Title": title,
                "Price": price,
                "Rating": rating,
                "Availability": availability,
                "Product URL": product_url,
                "Image URL": image_url
            })

        time.sleep(1)

    except Exception as e:
        print("Error:", e)

df = pd.DataFrame(books_data)

df.to_csv("books.csv", index=False, encoding="utf-8")

print("\nScraping Completed Successfully!")
print(f"Total Books Collected: {len(df)}")
print("Data saved as books.csv")
