-- Creates Table With following atrributes
--	id: integer, nevr null, auto increment and primary key
--	email: string(255 chars), nver null and unique
--	name: string(255 chars)
CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL AUTO_INCREMENT PRIMARY_KEY,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255)
);
