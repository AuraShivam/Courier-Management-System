# Task 1

# 1. Check Delivery Status

import re
import random
import string
import time


def check_delivery_status(status):

    if status.lower() == "delivered":
        return True

    return False


status = "Delivered"

print("Is Delivered:", check_delivery_status(status))


# 2. Categorize Parcels by Weight

def categorize_parcel(weight):

    if weight < 2:
        return "Light"

    elif 2 <= weight <= 5:
        return "Medium"

    return "Heavy"


print("Parcel Category:", categorize_parcel(3.5))


# 3. User Authentication

def login(username, password):

    if username == "admin" and password == "password":
        return True

    return False


print("Login Status:", login("admin", "password"))


# 4. Courier Assignment Logic

class Courier:

    def __init__(self, name, capacity, available):

        self.name = name
        self.capacity = capacity
        self.available = available

    def is_available(self):

        return self.available

    def has_capacity(self, weight):

        return self.capacity >= weight

    def assign_order(self, order):

        print(f"Order assigned to {self.name}")


class Order:

    def __init__(self, order_id, weight):

        self.order_id = order_id
        self.weight = weight


def assign_courier(order, couriers):

    for courier in couriers:

        if courier.is_available() and courier.has_capacity(order.weight):

            courier.assign_order(order)

            return courier

    return None


courier1 = Courier("John", 10, True)
courier2 = Courier("David", 5, False)

available_couriers = [courier1, courier2]

order = Order(101, 4)

assign_courier(order, available_couriers)


# Task 2

# 5. Display Orders for Customer

def get_orders_for_customer(customer_id):

    orders = {
        1: ["ORD101", "ORD102"],
        2: ["ORD201", "ORD202"]
    }

    return orders.get(customer_id, [])


orders = get_orders_for_customer(1)

print("\nOrders for Customer:")

for order in orders:
    print(order)


# 6. Track Courier Location

locations = [
    "Warehouse",
    "Sorting Center",
    "Out for Delivery",
    "Delivered"
]


def track_courier():

    for location in locations:

        print("Current Location:", location)

        time.sleep(1)


track_courier()


# Task 3

# 7. Parcel Tracking History

class Parcel:

    def __init__(self, tracking_number):

        self.tracking_number = tracking_number
        self.tracking_history = []

    def add_update(self, update):

        self.tracking_history.append(update)

    def show_history(self):

        print("\nTracking History:")

        for update in self.tracking_history:
            print(update)


parcel = Parcel("TN123456")

parcel.add_update("Package Picked Up")
parcel.add_update("Reached Hub")
parcel.add_update("Out for Delivery")

parcel.show_history()


# 8. Find Nearest Courier

class NearbyCourier:

    def __init__(self, name, distance, available):

        self.name = name
        self.distance = distance
        self.available = available

    def is_available(self):

        return self.available


def find_nearest_available_courier(couriers):

    available = []

    for courier in couriers:

        if courier.is_available():
            available.append(courier)

    if not available:
        return None

    return min(available, key=lambda x: x.distance)


c1 = NearbyCourier("Courier A", 12, True)
c2 = NearbyCourier("Courier B", 5, True)

nearest = find_nearest_available_courier([c1, c2])

print("\nNearest Courier:", nearest.name)


# Task 4

# 9. Parcel Tracking

parcel_tracking = {
    "TN123456": "In Transit",
    "TN654321": "Delivered"
}


def track_parcel(tracking_number):

    if tracking_number in parcel_tracking:

        print(
            f"Parcel {tracking_number} is "
            f"{parcel_tracking[tracking_number]}"
        )

    else:
        print("Tracking number not found")


track_parcel("TN123456")


# 10. Customer Validation

def validate_customer_info(data, detail):

    if detail.lower() == "name":

        return bool(re.match(r"^[A-Za-z ]+$", data))

    elif detail.lower() == "address":

        return bool(re.match(r"^[A-Za-z0-9\s,'-]*$", data))

    elif detail.lower() == "phone":

        return bool(re.match(r"^\d{10}$", data))

    return False


print(
    "\nValid Name:",
    validate_customer_info("John Doe", "name")
)


# 11. Address Formatting

def format_address(address):

    return address.title()


print(
    "\nFormatted Address:",
    format_address(
        "123 main street new york ny"
    )
)


# 12. Order Confirmation Email

def generate_order_confirmation_email(
    order_number,
    customer_name,
    delivery_address,
    delivery_date
):

    email = f'''
Dear {customer_name},

Your order has been confirmed.

Order Number: {order_number}

Delivery Address:
{delivery_address}

Expected Delivery Date:
{delivery_date}

Thank you for choosing our service.

Regards,
Courier Team
'''

    return email


print(
    generate_order_confirmation_email(
        "ORD123",
        "John Doe",
        "123 Main Street",
        "2024-05-25"
    )
)


# 13. Calculate Shipping Cost

def calculate_shipping_cost(distance, parcel_weight):

    cost_per_km = 2

    return (distance * cost_per_km) + (parcel_weight * 5)


print(
    "Shipping Cost:",
    calculate_shipping_cost(100, 5)
)


# 14. Password Generator

def generate_password(length=10):

    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    return ''.join(
        random.choice(characters)
        for _ in range(length)
    )


print("\nGenerated Password:", generate_password())


# 15. Find Similar Addresses

def find_similar_addresses(address, address_list):

    similar = []

    for addr in address_list:

        if address.lower() in addr.lower():

            similar.append(addr)

    return similar


addresses = [
    "123 Main Street New York",
    "456 Park Avenue",
    "789 Main Street California"
]

result = find_similar_addresses(
    "Main Street",
    addresses
)

print("\nSimilar Addresses:")

for addr in result:
    print(addr)
