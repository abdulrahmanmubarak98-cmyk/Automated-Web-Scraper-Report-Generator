import smtplib
from email.message import EmailMessage
from config.settings import REPORT_XLSX
from config.settings import EMAIL_ADDRESS, APP_PASSWORD


def send_email_report():
    msg = EmailMessage()
    msg["Subject"] = "Daily Books Report"
    msg["From"] = "your_email@gmail.com"
    msg["To"] = "client_email@example.com"
    msg.set_content("Please find the attached daily books report.")

    # Attach Excel file
    with open(REPORT_XLSX, "rb") as f:
        file_data = f.read()
        msg.add_attachment(
            file_data,
            maintype="application",
            subtype="vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            filename="books_report.xlsx",
        )

    # Send email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, APP_PASSWORD)
        smtp.send_message(msg)
