-- CReate user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- CREate database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
--ADDING PRIVILEHE
GRANT SELECT on hbtn_0d_2.* TO 'user_0d_2'@'localhost' WITH GRANT OPTION;
-- askdaf
FLUSH PRIVILEGES;
