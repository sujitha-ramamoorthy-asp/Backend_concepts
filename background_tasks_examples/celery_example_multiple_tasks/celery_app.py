from celery import Celery

celery = Celery(
    "my_app",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
    include=[
        "tasks.email",
        "tasks.report",
        ]
)
celery.conf.task_routes = {
    "tasks.email.send_order_email": {
        "queue": "email_queue"
    },
    "tasks.report.generate_order_report": {
        "queue": "report_queue"
    }
}
# celery.conf.task_routes = {
    # "tasks.send_order_email": {
        # "queue": "email_queue"
    # }
# }