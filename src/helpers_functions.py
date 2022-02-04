import csv
from math import prod


def read(path_to_file):
    with open(path_to_file) as csv_file:
        data = csv.DictReader(csv_file, fieldnames=["name", "product", "day"])
        return list(data)


def most_requested_dish(data, name_client):
    customer_orders = []

    for element in data:
        if element["name"] == name_client:
            customer_orders.append(element["product"])

    return max(customer_orders, key=customer_orders.count)


def how_many_times_dish(data, name_client, product):
    list_orders = []

    for element in data:
        if element["name"] == name_client and element["product"] == product:
            list_orders.append(element["product"])

    return list_orders.count(product)


def dishes_never_asked(data, name_client):
    all_the_products = set()
    list_orders_never_asked = set()

    for element in data:
        all_the_products.add(element["product"])
        if element["name"] == name_client:
            list_orders_never_asked.add(element["product"])

    return all_the_products - list_orders_never_asked


def days_without_visits(data, name_client):
    all_days = set()
    list_days_never_asked = set()

    for element in data:
        all_days.add(element["day"])
        if element["name"] == name_client:
            list_days_never_asked.add(element["day"])

    return all_days - list_days_never_asked


def write_to_file(path_file, list_data):
    with open(path_file, "w") as file:
        file.writelines("\n".join(list_data))
