import csv
import logging
from config.settings import RAW_CSV, CLEANED_CSV

logger = logging.getLogger("project")

RATING_MAP = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}


def clean_books():
    logger.info("Cleaning started")
    cleaned_data = []

    with open(RAW_CSV, "r", encoding="utf-8") as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            try:
                price = float(row["price"].replace("£", "").strip())
                rating = RATING_MAP.get(row["rating"].strip(), 0)
                availability = "In stock" in row["availability"]

                cleaned_data.append(
                    {
                        "title": row["title"],
                        "price": price,
                        "rating": rating,
                        "availability": availability,
                    }
                )
            except Exception as e:
                logger.warning(f"Skipping row due to error: {e}")

    fieldnames = ["title", "price", "rating", "availability"]
    with open(CLEANED_CSV, "w", newline="", encoding="utf-8") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(cleaned_data)

    logger.info(f"Cleaning completed | Total books processed: {len(cleaned_data)}")
    return cleaned_data
