-- Something useful
CREATE database if not exists hbnb_test_db;
CREATE user if not exists 'hbnb_test'@'localhost' identified by 'hbnb_test_pwd';
GRANT all privileges on hbnb_test_db.* to 'hbnb_test'@'localhost';
GRANT SELECT on performance_schema.* to 'hbnb_test'@'localhost';
