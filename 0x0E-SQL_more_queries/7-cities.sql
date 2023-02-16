-- Create database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Create table states
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`cities` (
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL,
	state_id INT NOT NULL,
	FOREIGN KEY (state_id) REFERENCES states(id),
	PRIMARY KEY (id)
);
