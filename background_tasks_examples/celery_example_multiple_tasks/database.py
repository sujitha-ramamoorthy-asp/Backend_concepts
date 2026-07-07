orders = []


def save_order(order):

    order["id"] = len(orders) + 1

    orders.append(order)

    return order