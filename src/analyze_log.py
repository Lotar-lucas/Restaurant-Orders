import csv
from src.helpers_functions import (
    read,
    most_requested_dish,
    how_many_times_dish,
    dishes_never_asked,
    days_without_visits,
    write_to_file,
)


def analyze_log(path_to_file):
    try:
        data = read(path_to_file)
        most_ordered = most_requested_dish(data, "maria")
        quantity_ordered = how_many_times_dish(data, "arnaldo", "hamburguer")
        dishes_never_requested = dishes_never_asked(data, "joao")
        days_without_visits_to_restaurant = days_without_visits(data, "joao")

        write_to_file(
            "data/mkt_campaign.txt",
            [
                most_ordered,
                quantity_ordered,
                dishes_never_requested,
                days_without_visits_to_restaurant,
            ],
        )

    except FileNotFoundError:
        raise FileNotFoundError


analyze_log("data/orders_1.csv")
