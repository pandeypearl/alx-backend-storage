-- Creates table users with following atrributes
--	id: integer, never null, auto increment and primary key
--	email: string(255 chars), never null and unique
--	name: string(255 chars),
--	country, enumeration of countries: US, CO, TN, never null, default US
CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255),
	country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
