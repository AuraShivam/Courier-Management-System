import pyodbc
import re
import random
import string
import time


# Database Connection

conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=localhost;'
    'DATABASE=CourierManagementSystem;'
    'Trusted_Connection=yes;'
)

cursor = conn.cursor()


# Task 1

# 1. Check Delivery Status

def check_delivery_status(order_id):

    query = """
    SELECT Status
    FROM Orders
    WHERE OrderID = ?
    """

    cursor.execute(query, (order_id,))

    result = cursor.fetchone()

    if result:

        status = result[0]

        if status.lower() == "delivered":
            return True

    return False


print("Is Delivered:", check_delivery_status(301))


# 2. Categorize Parcels by Weight

def categorize_parcel(parcel_id):

    query = """
    SELECT ParcelWeight
    FROM Parcels
    WHERE ParcelID = ?
    """

    cursor.execute(query, (parcel_id,))

    result = cursor.fetchone()

    if result:

        weight = result[0]

        if weight < 2:
            return "Light"

        elif 2 <= weight <= 5:
            return "Medium"

        return "Heavy"

    return "Parcel Not Found"


print("Parcel Category:", categorize_parcel(401))


# 3. User Authentication

def login(email, password):

    query = """
    SELECT *
    FROM Users
    WHERE Email = ? AND Password = ?
    """

    cursor.execute(query, (email, password))

    result = cursor.fetchone()

    return result is not None


print(
    "Login Status:",
    login("john.smith@example.com", "password123")
)


# 4. Courier Assignment Logic

def assign_courier(order_id):

    query = """
    SELECT TOP 1 CourierID
    FROM Couriers
    WHERE Status = 'In Transit'
    """

    cursor.execute(query)

    result = cursor.fetchone()

    if result:

        courier_id = result[0]

        print(
            f"Order {order_id} assigned "
            f"to Courier {courier_id}"
        )

    else:
        print("No courier available")


assign_courier(301)


# Task 2

# 5. Display Orders for Customer

def get_orders_for_customer(customer_id):

    query = """
    SELECT *
    FROM Orders
    WHERE CustomerID = ?
    """

    cursor.execute(query, (customer_id,))

    orders = cursor.fetchall()

    return orders


orders = get_orders_for_customer(1)

print("\nOrders for Customer:")

for order in orders:
    print(order)


# 6. Track Courier Location

def track_courier(courier_id):

    query = """
    SELECT SenderAddress,
           ReceiverAddress
    FROM Couriers
    WHERE CourierID = ?
    """

    cursor.execute(query, (courier_id,))

    result = cursor.fetchone()

    if result:

        print("Courier Route:")

        print("From:", result[0])

        time.sleep(1)

        print("To:", result[1])

    else:
        print("Courier not found")


track_courier(201)


# Task 3

# 7. Tracking History of Parcel

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


# 8. Find Nearest Available Courier

def find_nearest_available_courier():

    query = """
    SELECT TOP 1 CourierID,
                 SenderAddress
    FROM Couriers
    WHERE Status = 'In Transit'
    """

    cursor.execute(query)

    result = cursor.fetchone()

    if result:

        print(
            f"Nearest Available Courier: "
            f"{result[0]}"
        )

    else:
        print("No courier available")


find_nearest_available_courier()


# Task 4

# 9. Parcel Tracking

def track_parcel(tracking_number):

    query = """
    SELECT Status
    FROM Couriers
    WHERE TrackingNumber = ?
    """

    cursor.execute(query, (tracking_number,))

    result = cursor.fetchone()

    if result:

        print(
            f"Parcel {tracking_number} "
            f"is {result[0]}"
        )

    else:
        print("Tracking number not found")


track_parcel("TN123456")


# 10. Customer Data Validation

def validate_customer_info(name, phone):

    valid_name = bool(
        re.match(r"^[A-Za-z ]+$", name)
    )

    valid_phone = bool(
        re.match(r"^\d{10}$", phone)
    )

    return valid_name and valid_phone


print(
    "\nCustomer Validation:",
    validate_customer_info(
        "John Doe",
        "9876543210"
    )
)


# 11. Address Formatting

def format_address(address):

    return address.title()


query = """
SELECT Address
FROM Customers
WHERE CustomerID = 1
"""

cursor.execute(query)

result = cursor.fetchone()

if result:

    print(
        "\nFormatted Address:",
        format_address(result[0])
    )


# 12. Order Confirmation Email

def generate_order_confirmation_email(order_id):

    query = """
    SELECT Customers.Name,
           Customers.Address,
           Orders.DeliveryDate
    FROM Orders
    INNER JOIN Customers
    ON Orders.CustomerID = Customers.CustomerID
    WHERE Orders.OrderID = ?
    """

    cursor.execute(query, (order_id,))

    result = cursor.fetchone()

    if result:

        customer_name = result[0]

        address = result[1]

        delivery_date = result[2]

        email = f'''
Dear {customer_name},

Your order has been confirmed.

Order Number: {order_id}

Delivery Address:
{address}

Expected Delivery Date:
{delivery_date}

Thank you for choosing our service.
'''

        print(email)


generate_order_confirmation_email(301)


# 13. Calculate Shipping Cost

def calculate_shipping_cost(parcel_id):

    query = """
    SELECT ParcelWeight
    FROM Parcels
    WHERE ParcelID = ?
    """

    cursor.execute(query, (parcel_id,))

    result = cursor.fetchone()

    if result:

        weight = result[0]

        cost = weight * 10

        return cost

    return 0


print(
    "Shipping Cost:",
    calculate_shipping_cost(401)
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


print(
    "\nGenerated Password:",
    generate_password()
)


# 15. Find Similar Addresses

def find_similar_addresses(keyword):

    query = """
    SELECT Address
    FROM Customers
    WHERE Address LIKE ?
    """

    cursor.execute(query, ('%' + keyword + '%',))

    results = cursor.fetchall()

    print("\nSimilar Addresses:")

    for address in results:
        print(address[0])


find_similar_addresses("Street")


# Close Connection

conn.close()
