CREATE TABLE orders
    (id INT PRIMARY KEY AUTO_INCREMENT,
    text CHAR(20) UNIQUE,
    customer_id INT,
    FOREIGN KEY(customer_id) REFERENCES customers(id) ON DELETE SET NULL
    );