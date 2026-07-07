from celery import Celery

celery = Celery(
    "order_app",
    broker="pyamqp://admin:admin123@localhost//"
)

