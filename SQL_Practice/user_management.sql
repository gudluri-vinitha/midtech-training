USE company_db;
CREATE USER 'vini'@'%'
IDENTIFIED BY 'vini@123';

SELECT user,
host
FROM mysql.user;

SHOW GRANTS
FOR 'vini'@'%';


GRANT
SELECT,
INSERT,
UPDATE
ON company_db.*
TO 'vini'@'%';

REVOKE UPDATE
ON company_db.*
FROM 'vini'@'%';



SHOW GRANTS
FOR 'vini'@'%';




