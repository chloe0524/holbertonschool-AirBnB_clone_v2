-- 1_Create database 'hbnb_dev_db'
-- 2_Add user 'hbnb_dev' with password 'hbnb_dev_pwd'
-- 3_Grant all privileges on 'hbnb_dev_db' to user 'hbnb_dev'
-- 4_Grant SELECT privilege on 'performance_schema' to user 'hbnb_dev'

-- 1
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- 2
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- 3
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- 4
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

FLUSH PRIVILEGES;