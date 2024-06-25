-- Step 1: Backup your database (optional but highly recommended)
-- mysqldump -u username -p hbtn_0c_0 > hbtn_0c_0_backup.sql

-- Step 2: Alter database character set and collation
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Step 3: Alter table character set and collation
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Step 4: Alter specific column character set and collation
ALTER TABLE first_table MODIFY name VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
