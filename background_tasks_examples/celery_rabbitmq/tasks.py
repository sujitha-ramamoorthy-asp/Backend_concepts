from email.mime.text import MIMEText
import smtplib

from celery_app import celery
from config import settings


@celery.task
def send_order_email(email: str, order_id: int):

    body = f"""
Hi,

Your Order #{order_id} has been placed successfully.

Thank you for shopping with us.

Regards,
ABC Store
"""

    message = MIMEText(body)

    message["Subject"] = "Order Confirmation"
    message["From"] = settings.EMAIL_ADDRESS
    message["To"] = email
    print(message)

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:

        smtp.starttls()

        smtp.login(
            settings.EMAIL_ADDRESS,
            settings.EMAIL_PASSWORD
        )
        print("ghghg")
        smtp.send_message(message)