"""Association (Knows-a): independent objects hold references to each other."""


class Customer:
    def __init__(self, name: str):
        self.name = name
        self.orders = []  # Keeps track of orders


class Order:
    def __init__(self, order_id: int, customer: Customer):
        self.order_id = order_id
        self.customer = customer  # Establishes a standard reference link
        customer.orders.append(self)


if __name__ == "__main__":
    # 1. Instantiate the customer
    alice = Customer("Alice")

    # 2. Instantiate individual orders and pass the customer object
    order_1 = Order(101, alice)
    order_2 = Order(102, alice)

    # 3. Verify the cross-referencing
    print(f"Customer Profile: {alice.name}")
    print("Linked orders tracked inside Customer list:")
    for o in alice.orders:
        print(f"  - Order ID: {o.order_id}")

    print(f"\nOrder #101 lookup -> Placed by customer: {order_1.customer.name}")
