-- CREATE USER  'user'@'localhost' IDENTIFIED BY 'user@123';
-- CREATE DATABASE userdb;
-- GRANT ALL PRIVILEGES ON auth.* TO 'user'@'localhost';

USE userdb;

CREATE TABLE user (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  email VARCHAR(255) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL
);

INSERT INTO user (email, password) VALUES ('rahula7200@gmail.com', 'admin@123');
