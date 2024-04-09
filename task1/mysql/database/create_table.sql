CREATE TABLE IF NOT EXISTS users (
  id int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  email varchar(256) NOT NULL,
  first_name varchar(256) NOT NULL,
  last_name varchar(256) NOT NULL
);