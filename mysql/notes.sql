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
ALTER column_name SET DEFAULT 18;

# Сделать значение колонки уникальной
ALTER TABLE table_name
ADD UNIQUE (col_name);

# Изменение типа столбца
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

# Создание таблицы с проверкой
CREATE TABLE person
(name CHAR(10), gender CHAR(1) CHECK(gender IN ('m', 'w')));

CREATE TABLE person
(name CHAR(10), gender CHAR(1)
CONSTRAINT check_gender CHECK(gender IN ('m', 'w')));

# создание ограничения через ENUM
CREATE TABLE person
(name CHAR(20), gender ENUM('m','w'));


# удаление проверки
ALTER TABLE person
DROP CONSTRAINT check_gender;
# Добавление проверки
ALTER TABLE person
ADD CONSTRAINT check_gender CHECK (gender IN ('m', 'w', 'q'));



#
CREATE TABLE person
(id int, name CHAR(20),
CONSTRAINT pk_person PRIMARY KEY AUTO_INCREMENT (id));

# посмотреть ограничения
SELECT TABLE_NAME, CONSTRAINT_TYPE, CONSTRAINT_NAME
FROM information_schema.table_constraints
WHERE table_name=`table_name`;

# удаление внешнего ключа
ALTER TABLE favorite_food
DROP foreign key fk_fav_food;

# ограничние ключа с автоудалением
ALTER TABLE favorite_food
ADD CONSTRAINT fk_fav_food FOREIGN KEY (person_id) REFERENCES person(id) ON DELETE CASCADE;



# Создание виртуальной таблицы(вью представления)
CREATE VIEW  emploee_vw AS
SELECT fname, lname FROM employee;

# удаление представления
DROP VIEW  emploee_vw;


