USE CourierManagementSystem;
GO


INSERT INTO Customers (
    CustomerID,
    Name,
    Email,
    ContactNumber,
    Address
)
VALUES
(1, 'John Doe', 'john@example.com', '1234567890', '123 Main Street'),
(2, 'Jane Smith', 'jane@example.com', '0987654321', '456 Elm Street'),
(3, 'Alice Johnson', 'alice@example.com', '9876543210', '789 Oak Street');


INSERT INTO Users (
    UserID,
    Name,
    Email,
    Password,
    ContactNumber,
    Address
)
VALUES
(101, 'John Smith', 'john.smith@example.com', 'password123', '1234567890', '123 Main Street'),
(102, 'Jane Doe', 'jane.doe@example.com', 'password456', '0987654321', '456 Elm Street'),
(103, 'Alice Johnson', 'alice.johnson@example.com', 'password789', '9876543210', '789 Oak Street');


INSERT INTO Couriers (
    CourierID,
    UserID,
    SenderName,
    SenderAddress,
    ReceiverName,
    ReceiverAddress,
    Weight,
    Status,
    TrackingNumber,
    DeliveryDate
)
VALUES
(201, 101, 'John Smith', '123 Main Street', 'Alice Johnson', '789 Oak Street', 2.5, 'In Transit', 'TN123456', '2024-05-05'),
(202, 102, 'Jane Doe', '456 Elm Street', 'Bob Brown', '101 Pine Street', 3.2, 'Delivered', 'TN654321', '2024-04-25'),
(203, 103, 'Alice Johnson', '789 Oak Street', 'Emily Wilson', '202 Maple Street', 1.8, 'Pending', 'TN987654', NULL);


INSERT INTO Orders (
    OrderID,
    CustomerID,
    CourierID,
    OrderDate,
    DeliveryDate,
    Status
)
VALUES
(301, 1, 201, '2024-04-20', '2024-04-25', 'Delivered'),
(302, 2, 202, '2024-04-22', '2024-04-27', 'Delivered'),
(303, 3, 203, '2024-04-24', NULL, 'Pending');


INSERT INTO Parcels (
    ParcelID,
    OrderID,
    ParcelWeight,
    ParcelDescription
)
VALUES
(401, 301, 2.5, 'Electronics'),
(402, 302, 3.2, 'Clothing'),
(403, 303, 1.8, 'Books');


INSERT INTO CourierServices (
    ServiceID,
    ServiceName,
    Cost
)
VALUES
(501, 'Standard', 10.00),
(502, 'Express', 20.00),
(503, 'Premium', 30.00);


INSERT INTO Employee (
    EmployeeID,
    Name,
    Email,
    ContactNumber,
    Role,
    Salary
)
VALUES
(601, 'Sarah Brown', 'sarah@example.com', '9876543210', 'Manager', 50000),
(602, 'David Lee', 'david@example.com', '9123456780', 'Courier', 30000);


INSERT INTO Location (
    LocationID,
    LocationName,
    Address
)
VALUES
(701, 'Main Branch', 'New York'),
(702, 'West Branch', 'California');


INSERT INTO Payment (
    PaymentID,
    CourierID,
    LocationID,
    Amount,
    PaymentDate
)
VALUES
(801, 201, 701, 150.00, '2024-05-01'),
(802, 202, 702, 200.00, '2024-05-02');


INSERT INTO CourierServiceMapping (
    CourierID,
    ServiceID
)
VALUES
(201, 501),
(202, 502),
(203, 503);


INSERT INTO EmployeeCourier (
    EmployeeID,
    CourierID
)
VALUES
(602, 201),
(602, 202);


SELECT * FROM Customers;

SELECT * FROM Couriers;

SELECT * FROM Orders;

SELECT * FROM Parcels;

SELECT * FROM Payment;


SELECT *
FROM Orders
WHERE Status = 'Delivered';


SELECT *
FROM Parcels
WHERE ParcelWeight BETWEEN 2 AND 5;


SELECT CourierID,
       COUNT(*) AS TotalOrders
FROM Orders
GROUP BY CourierID;


SELECT CourierID,
       AVG(DATEDIFF(day, OrderDate, DeliveryDate))
       AS AverageDeliveryDays
FROM Orders
WHERE DeliveryDate IS NOT NULL
GROUP BY CourierID;


SELECT Payment.PaymentID,
       Payment.Amount,
       Couriers.TrackingNumber
FROM Payment
INNER JOIN Couriers
ON Payment.CourierID = Couriers.CourierID;


SELECT Customers.Name,
       Orders.OrderID
FROM Customers
LEFT JOIN Orders
ON Customers.CustomerID = Orders.CustomerID;


SELECT *
FROM Couriers
WHERE Weight > (
    SELECT AVG(Weight)
    FROM Couriers
);


SELECT *
FROM Couriers
WHERE EXISTS (
    SELECT 1
    FROM Payment
    WHERE Payment.CourierID = Couriers.CourierID
);
