-- Create the database hbtn_0e_100_usa
CREATE DATABASE IF NOT EXISTS hbtn_0e_100_usa;
USE hbtn_0e_100_usa;

-- Create the states table
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);

-- Create the cities table with a foreign key reference to states
CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    state_id INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id) ON DELETE CASCADE
);

-- Insert data into the states table
INSERT INTO states (name) VALUES ("California");

-- Insert data into the cities table
INSERT INTO cities (name, state_id) VALUES ("San Francisco", 1);
