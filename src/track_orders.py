class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        return self.orders.append(
            {"name": costumer, "product": order, "day": day}
        )

    def get_most_ordered_dish_per_costumer(self, costumer):
        customer_orders = []

        for element in self.orders:
            if element["name"] == costumer:
                customer_orders.append(element["product"])

        return max(customer_orders, key=customer_orders.count)

    def get_never_ordered_per_costumer(self, costumer):
        all_the_products = set()
        list_orders_never_asked = set()

        for element in self.orders:
            all_the_products.add(element["product"])
            if element["name"] == costumer:
                list_orders_never_asked.add(element["product"])

        return all_the_products - list_orders_never_asked

    def get_days_never_visited_per_costumer(self, costumer):
        all_days = set()
        list_days_never_asked = set()

        for element in self.orders:
            all_days.add(element["day"])
            if element["name"] == costumer:
                list_days_never_asked.add(element["day"])

        return all_days - list_days_never_asked

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
