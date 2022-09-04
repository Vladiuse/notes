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