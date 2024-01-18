-- Desc: Create a table with unique users
-- id integer
-- email varchar(255)
-- name varchar(255)
-- password varchar(255)

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
