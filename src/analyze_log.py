import csv


def analyze_log(path_to_file):
    data = read(path_to_file)
    print(data)
    raise NotImplementedError


def read(path_to_file):
    with open(path_to_file) as csv_file:
        data = csv.DictReader(csv_file, fieldnames=["Nome", "Produto", "Dia"])
        return list(data)


analyze_log("data/orders_1.csv")
