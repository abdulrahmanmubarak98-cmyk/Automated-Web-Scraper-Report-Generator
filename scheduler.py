# scheduler.py

import schedule
import time

from main import run_pipeline
from logger import setup_logger

logger = setup_logger("project")


def scheduled_job():
    """
    Wrapper around the pipeline.
    Responsible for logging and error handling.
    """
    try:
        logger.info("Scheduled task started")

        run_pipeline()

        logger.info("Scheduled task completed successfully")

    except Exception as e:
        logger.error(f"Scheduled task failed: {e}")


# Development schedule
# schedule.every(1).minutes.do(scheduled_job)

# Production schedule
schedule.every().day.at("8:00").do(scheduled_job)
logger.info("Scheduler started. Waiting for scheduled tasks...")

while True:
    schedule.run_pending()
    time.sleep(1)
