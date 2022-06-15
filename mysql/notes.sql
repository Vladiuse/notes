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
ALTER TABLE table_name 
ADD COLUMN column_name INT [PRIMARY KEY AUTO_INCREMENT];

# Удалить колонку
ALTER TABLE table_name
DROP COLUMN column_name;

#Изменение значения по умолчанию
ALTER TABLE table_name
ALTER COLUMN column_name SET DEFAULT 18;

# Сделать значение колонки уникальной
ALTER TABLE table_name
ADD UNIQUE (col_name);

Изменение типа столбца
ALTER TABLE table_name
MODUFY COLUMN name CHAR(100);

# добавить ограничение для поля 
ALTER TABLE customers
ADD CHECK (age IN (18,30));

# Удалить первичный ключ ( если на припари стоит AUTO_INCREMENT - его сначало нужно убрать)
ALTER TABLE table_name
DROP PRIMARY KEY;

# вывод уникальных значение 
SELECT DISTINCT

# Добавлени данных
INSERT INTO table_name (col_1, col_2) VALUES (data_1, data_2);

# обновление данных
UPDATE table_name SET col_name='data';

# Удаление данных
DELETE FROM table_name;

#Поститать количество уникальных значений
SELECT COUNT(DISTINCT(race)) FROM persons;
