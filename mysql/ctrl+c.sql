
CREATE TABLE Customers
(
    Id INT PRIMARY KEY AUTO_INCREMENT,
    Age INT, 
    FirstName VARCHAR(20) NOT NULL,
    LastName VARCHAR(20) NOT NULL,
    Phone VARCHAR(20) NOT NULL UNIQUE
);
 
CREATE TABLE Orders
(
    Id INT PRIMARY KEY AUTO_INCREMENT,
    CustomerId INT,
    CreatedAt Date,
    FOREIGN KEY (CustomerId)  REFERENCES Customers (Id)
);

INSERT Products(ProductName, Manufacturer, Price, ProductCount) 
VALUES
('iPhone 8', 'Apple', 51000, 3),
('P20 Lite', 'Huawei', 34000, 4),
('Galaxy S8', 'Samsung', 46000, 2);


CREATE TABLE Products
(
    Id INT AUTO_INCREMENT PRIMARY KEY,
    ProductName VARCHAR(30) NOT NULL,
    Manufacturer VARCHAR(20) NOT NULL,
    ProductCount INT DEFAULT 0,
    Price DECIMAL NOT NULL
);
CREATE TABLE Customers
(
    Id INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(30) NOT NULL
);
CREATE TABLE Orders
(
    Id INT AUTO_INCREMENT PRIMARY KEY,
    ProductId INT NOT NULL,
    CustomerId INT NOT NULL,
    CreatedAt DATE NOT NULL,
    ProductCount INT DEFAULT 1,
    Price DECIMAL NOT NULL,
    FOREIGN KEY (ProductId) REFERENCES Products(Id) ON DELETE CASCADE,
    FOREIGN KEY (CustomerId) REFERENCES Customers(Id) ON DELETE CASCADE
);

INSERT INTO Products (ProductName, Manufacturer, ProductCount, Price)
VALUES ('iPhone X', 'Apple', 2, 76000),
('iPhone 8', 'Apple', 2, 51000),
('iPhone 7', 'Apple', 5, 42000),
('Galaxy S9', 'Samsung', 2, 56000),
('Galaxy S8', 'Samsung', 1, 46000),
('Honor 10', 'Huawei', 2, 26000),
('Nokia 8', 'HMD Global', 6, 38000);
 
INSERT INTO Customers(FirstName) VALUES ('Tom'), ('Bob'),('Sam');
 
INSERT INTO Orders (ProductId, CustomerId, CreatedAt, ProductCount, Price)
VALUES
( 
    (SELECT Id FROM Products WHERE ProductName='Galaxy S8'),
    (SELECT Id FROM Customers WHERE FirstName='Tom'),
    '2018-05-21', 
    2, 
    (SELECT Price FROM Products WHERE ProductName='Galaxy S8')
),
( 
    (SELECT Id FROM Products WHERE ProductName='iPhone X'),
    (SELECT Id FROM Customers WHERE FirstName='Tom'),
    '2018-05-23',  
    1, 
    (SELECT Price FROM Products WHERE ProductName='iPhone X')
),
( 
    (SELECT Id FROM Products WHERE ProductName='iPhone X'),
    (SELECT Id FROM Customers WHERE FirstName='Bob'),
    '2018-05-21',  
    1, 
    (SELECT Price FROM Products WHERE ProductName='iPhone X')
);

CREATE TABLE orders
    (id INT PRIMARY KEY AUTO_INCREMENT,
    text CHAR(20) UNIQUE,
    word CHAR(20),
    customer_id INT,
    );

INSERT INTO orders
(name)
VALUES
('surround','enemy'),
('cliff','burton'),
('evolve','me'),
('luggage','man'),
('text','listen'),
('desert','sun'),
('second','town'),
('lens','grow'),
('affair','home'),
('mule','swing'),
('urge','dog'),
('few','kill'),
('claw','koala'),
('pheasant','island'),
('material','harleston'),
('payment','league'),
('thrombosis','spread'),
('attendance','maverick');

SELECT C.FirstName, P.ProductName, O.CreatedAt 
FROM Orders AS O, Customers AS C, Products AS P
WHERE O.CustomerId = C.Id AND O.ProductId=P.Id;


SELECT C.FirstName, P.ProductName, O.*
FROM Orders AS O, Customers AS C, Products AS P
WHERE O.CustomerId = C.Id AND O.ProductId=P.Id;

CREATE TABLE Products
(
    Id INT AUTO_INCREMENT PRIMARY KEY,
    ProductName VARCHAR(30) NOT NULL,
    Manufacturer VARCHAR(20) NOT NULL,
    ProductCount INT DEFAULT 0,
    Price DECIMAL NOT NULL
);
CREATE TABLE Customers
(
    Id INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(30) NOT NULL
);
CREATE TABLE Orders
(
    Id INT AUTO_INCREMENT PRIMARY KEY,
    ProductId INT NOT NULL,
    CustomerId INT NOT NULL,
    CreatedAt DATE NOT NULL,
    ProductCount INT DEFAULT 1,
    Price DECIMAL NOT NULL,
    FOREIGN KEY (ProductId) REFERENCES Products(Id) ON DELETE CASCADE,
    FOREIGN KEY (CustomerId) REFERENCES Customers(Id) ON DELETE CASCADE
);



CREATE TABLE person
(id int AUTO_INCREMENT NOT NULL, name CHAR(20),
CONSTRAINT pk_person PRIMARY KEY (id) );

INSERT INTO person
(name) vALUES 
('test name1'),
('test name2'),
('test name3'),
('test name4'),
('test name5'),
('test name6'),
('test name7');

CREATE TABLE favorite_food
(person_id INT, name CHAR(20),
CONSTRAINT pk_fav_food PRIMARY KEY (person_id, name),
CONSTRAINT fk_fav_food FOREIGN KEY (person_id) REFERENCES person(id));

INSERT INTO favorite_food
(person_id, name)
VALUES
(1,' some food 32'),
(4,' some food 4'),
(3,' some food');



SELECT e.emp_id, CONCAT_WS(' ', e.fname, e.lname) as fname,
e.start_date, e.dept_id, d.name
FROM employee e
JOIN department d ON d.dept_id= e.dept_id;


SELECT dept_id, count(*) FROM employee
GROUP bY dept_id;

SELECT *, RIGHT(fed_id, 4) FROM customer
ORDER BY RIGHT(fed_id,4);

  

CREATE VIEW test_vw as 
SELECT CONCAT_WS(' ',e.fname, e.lname) as full_name, account_id, cust_id, avail_balance FROM account
JOIN employee e ON e.emp_id= account.open_emp_id
WHERE status = 'active' AND pending_balance > 2500
ORDER by pending_balance;

SELECT a.account_id, a.last_activity_date, a.status, p.product_type_cd FROM account a
JOIN product p ON a.product_cd = p.product_cd;



CREATE TABLE test (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    name CHAR(10) NOT NULL,
    some CHAR(5)
);
INSERT INTO test
(name, some)
VALUES
('name 1', '123'),
('name 2', '123'),
('name 3', '123'),
('name 4', null),
('name 5', 'xxx'),
('name 6', 'xxx'),
('name 7', null);

SELECT * FROM customer
WHERE fed_id NOT LIKE '___-__-____' OR address LEFT(address,4) IN (1, 99);


UPDATE person
SET job = 'true'
WHERE id  in (4,7);

 
  

CREATE TABLE job
(name CHAR(20));


SELECT p.name AS person_name, j.name AS Job name FROM person p
INNER JOIN job  j ON p.job_id = j.id;

SELECT e.fname, e.lname,d.name FROM employee e
LEFT OUTER JOIN department d ON e.dept_id = d.dept_id
ORDER by e.lname;



SELECT p.name, pp.name FROM person p
JOIN person pp;

