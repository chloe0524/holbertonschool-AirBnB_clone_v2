-- 1_Create database 'hbnb_test_db'
-- 2_Add user 'hbnb_test' with password 'hbnb_test_pwd'
-- 3_Grant all privileges on 'hbnb_dev_db' to user 'hbnb_dev'
-- 4_Grant SELECT privilege on 'performance_schema' to user 'hbnb_test'

-- 1
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- 2
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- 3
GRANT ALL ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- 4
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
