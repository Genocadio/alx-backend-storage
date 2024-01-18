-- Creates a table with certain requirements
-- id integer
-- email varchar(255)
-- name varchar(255)
-- country enum('US', 'CO', 'TN') not null default 'US'

CREATE TABLE IF NOT EXISTS users (
       id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
       email VARCHAR(255) NOT NULL UNIQUE,
       name VARCHAR(255),
       country ENUM ('US', 'CO', 'TN') NOT NULL
);
