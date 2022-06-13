# Ошибка mysql access denied for user 'root'@'localhost'
# Решение: sudo mysql (чтоб зайти под рутом)

# Создание пользрователя:
CREATE USER 'test_user'@'localhost' IDENTIFIED BY 'password';
CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';

# Удалить пользователяя: 
DROP USER username@host;

# Подключиться к базе 
mysql -u test_user -h localhost -p

# Посмотреть пользователей 
SELECT USER,HOST FROM mysql.user;

# Просмотр базданных 
SHOW DATABASES;

# Просмотр прав пользователя 
SHOW GRANTS FOR test_user@localhost;

# Расдать права пользователю 
GRANT SELECT, INSERT ON *.* TO 'user_name'@'localhost';
GRANT ALL ON test_user TO test_user@localhost;  #  раздача прав на конкретную базу данных
GRANT ALL ON test_user.* to test_user@localhost;

# Создать базу данных
CREATE DATABASE db_name;

# Создать таблицу
CREATE TABLE название_таблицы (id INT, age INT, name VARCHAR(20), last_name VARCHAR(20));

# Переименовать таблицу
RENAME TABLE старое_название TO новое_название;

# Отчистка таблицы
TRUNCATE TABLE имя_таблицы;

# Уладить таблицу
DROP TABLE table_name;

# Показать схему талицы
DESCRIBE customers;

# Удалить строку
DELETE FROM table_name WHERE id=1;

# Сделать клолнку PRIMARY KEY
ALTER TABLE table_name ADD PRIMARY KEY (id);

# Добавить колонку
ALTER TABLE table_name ADD COLUMN column_name INT [PRIMARY KEY AUTO_INCREMENT];

# Удалить колонку
ALTER TABLE table_name DROP COLUMN column_name;

# добавить ограничение для поля 
ALTER TABLE customers ADD CHECK (age IN (18,30));

CREATE TABLE customers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name CHAR(20) CONSTRAINT null_name CHECK(name !=''),
    age INT CONSTRAINT full_age CHECK (age IN (18,100))
    );