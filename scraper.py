import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
import csv
from logger import setup_logger
from config.settings import RAW_CSV

logger = setup_logger("project")

BASE_URL = "https://books.toscrape.com/catalogue/"
START_PAGE = "page-1.html"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
}


def scrape_books():
    books_data = []
    current_page_url = urljoin(BASE_URL, START_PAGE)

    session = requests.Session()
    session.headers.update(HEADERS)

    logger.info("Scraping started")

    while current_page_url:
        try:
            response = session.get(current_page_url, timeout=10)
            response.encoding = "utf-8"
            logger.info(
                f"Requesting URL: {current_page_url} | Status Code: {response.status_code}"
            )

            if response.status_code != 200:
                logger.error(f"Failed to fetch page: {current_page_url}")
                break

            soup = BeautifulSoup(response.text, "html.parser")
            books = soup.select("article.product_pod")

            for book in books:
                title = book.h3.a["title"]
                price = book.select_one(".price_color").text
                rating = book.find("p", class_="star-rating")["class"][1]
                availability = book.find(
                    "p", class_="instock availability"
                ).text.strip()

                books_data.append(
                    {
                        "title": title,
                        "price": price,
                        "rating": rating,
                        "availability": availability,
                    }
                )
                logger.info(f"Scraped: {title}")
            print(repr(price))

            next_link = soup.find("li", class_="next")
            if next_link:
                current_page_url = urljoin(BASE_URL, next_link.a["href"])
            else:
                current_page_url = None

            time.sleep(1)

        except Exception as e:
            logger.error(f"Error scraping {current_page_url}: {e}")
            break

    # Write CSV
    fieldnames = ["title", "price", "rating", "availability"]
    with open(RAW_CSV, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(books_data)

    logger.info(f"Scraping completed | Total books scraped: {len(books_data)}")
    return books_data
