--CHANGING
ALTER database hbtn_0c_0 CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER table second_table CONVERT TO CHARACTER SET utf8 COLLATE utf8_unicode_ci;
ALTER table second_table MODIFY name VARCHAR(256) CHARACTER SET utf8 COLLATE utf8_unicode_ci;

