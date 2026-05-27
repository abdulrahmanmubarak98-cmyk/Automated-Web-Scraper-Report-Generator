import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin
import time

books_data = []
url = "https://books.toscrape.com/"
current_page_url = url
base_url = "https://books.toscrape.com/catalogue"

while current_page_url:
    try:
        response = requests.get(current_page_url, timeout=10)
        print("Status Code:", response.status_code)

        if response.status_code != 200:
            break
        soup = BeautifulSoup(response.text, "html.parser")
        print("Connection Successful!")

        books = soup.find_all("article", class_="product_pod")

        for book in books:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text
            rating = book.find("p", class_="star-rating")["class"][1]
            availability = book.find("p", class_="instock availability").text.strip()

            book_data = {
                "title": title,
                "price": price,
                "rating": rating,
                "availability": availability,
            }

            books_data.append(book_data)
            print(
                f"Title: {title}, Price: {price}, Rating: {rating}, Availability: {availability}"
            )

        # Find next page
        next_link = soup.find("li", class_="next")
        print("Next URL:", current_page_url)
        if next_link:
            current_page_url = urljoin(base_url, next_link.a["href"])
        else:
            current_page_url = None

        time.sleep(1)  # polite pause between requests

    except requests.exceptions.Timeout:
        print("The request timed out.")
        break
    except requests.exceptions.ConnectionError:
        print("Connection failed.")
        break
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
        break

# Export CSV after all pages are scraped
fieldnames = ["title", "price", "rating", "availability"]
with open("data/books.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for book in books_data:
        writer.writerow(book)
