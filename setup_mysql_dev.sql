-- Something useful
CREATE database if not exists hbnb_dev_db;
CREATE user if not exists 'hbnb_dev'@'localhost' identified by 'hbnb_dev_pwd';
GRANT all privileges on `hbnb_dev_db`.* to 'hbnb_dev'@'localhost';
GRANT SELECT on `performance_schema`.* to 'hbnb_dev'@'localhost';
