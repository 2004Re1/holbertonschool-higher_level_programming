--CHANGING
Copy ALTER DATABASE dbname CHARACTER SET utf8 COLLATE utf8_general_ci;
Copy ALTER TABLE second_table CONVERT TO CHARACTER SET utf8 COLLATE utf8_unicode_ci;
Copy ALTER TABLE second_table MODIFY name VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci;

