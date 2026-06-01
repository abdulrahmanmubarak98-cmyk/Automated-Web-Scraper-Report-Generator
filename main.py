# main.py

from scraper import scrape_books
from cleaner import clean_books
from reporter import generate_excel_report
from logger import setup_logger

logger = setup_logger("project")


def run_pipeline():
    logger.info("Pipeline started")

    scraped_books = scrape_books()

    if len(scraped_books) == 0:
        raise Exception("Scraping failed: No books scraped.")

    cleaned_books = clean_books()

    if len(cleaned_books) == 0:
        raise Exception("Cleaning failed: No books cleaned.")

    report_path = generate_excel_report()

    logger.info(f"Report generated: {report_path}")

    logger.info("Pipeline completed successfully")


if __name__ == "__main__":
    run_pipeline()
