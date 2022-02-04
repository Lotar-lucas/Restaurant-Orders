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
        write_to_file(
            "data/mkt_campaign.txt",
            [
                str(most_requested_dish(data, "maria")),
                str(how_many_times_dish(data, "arnaldo", "hamburguer")),
                str(dishes_never_asked(data, "joao")),
                str(days_without_visits(data, "joao")),
            ],
        )
    except FileNotFoundError as file_broken:
        raise file_broken
