import os
from dotenv import load_dotenv

load_dotenv()

RABBITMQ_URL = os.getenv(
    "RABBITMQ_URL",
    "amqp://admin:admin123@localhost/"
)

EXCHANGE_NAME = "saga_exchange"