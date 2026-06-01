import logging
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://books.toscrape.com/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/114.0.0.0 Safari/537.36"
}

# Data paths
DATA_FOLDER = os.path.join(os.getcwd(), "data")
os.makedirs(DATA_FOLDER, exist_ok=True)

RAW_CSV = os.path.join(DATA_FOLDER, "books.csv")
CLEANED_CSV = os.path.join(DATA_FOLDER, "books_cleaned.csv")
REPORT_XLSX = os.path.join(DATA_FOLDER, "books_report.xlsx")


# Ensure logs folder exists
os.makedirs("logs", exist_ok=True)

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    filename="logs/project.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
)

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
APP_PASSWORD = os.getenv("APP_PASSWORD")
DEBUG = os.getenv("DEBUG")
