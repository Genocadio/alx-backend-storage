-- Creates a table with certain requirements

IF NOT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'users') THEN

    CREATE TABLE users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        email VARCHAR(255) NOT NULL UNIQUE,
        name VARCHAR(255),
        country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
    );

END IF;
