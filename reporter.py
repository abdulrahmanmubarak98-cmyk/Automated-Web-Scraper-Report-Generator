import pandas as pd
import logging
from config.settings import CLEANED_CSV, REPORT_XLSX
import os

logger = logging.getLogger("project")


def generate_excel_report(input_file=CLEANED_CSV):
    logger.info("Generating Excel report")
    df = pd.read_csv(input_file)
    df.to_excel(REPORT_XLSX, index=False)
    logger.info(f"Excel report generated: {REPORT_XLSX}")
    if os.path.exists(REPORT_XLSX):
        return REPORT_XLSX
    else:
        raise Exception("Excel report was not created successfully")
