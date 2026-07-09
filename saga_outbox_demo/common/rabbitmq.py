import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost")
)

channel = connection.channel()

channel.queue_declare(queue="order_created")
channel.queue_declare(queue="inventory_reserved")
channel.queue_declare(queue="inventory_failed")


def get_channel():
    return channel