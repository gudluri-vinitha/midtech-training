-- update

UPDATE Employee
SET salary=600000
WHERE employee_id=2;
select *from employee;

UPDATE employee
SET age=56
WHERE employee_id=3;
select *from employee;
COMMIT;

UPDATE Employee
SET salary=600-190
WHERE employee_id=4;
select *from employee;


UPDATE Employee
SET salary=20000+200
WHERE employee_id=4;
select *from employee;
COMMIT;

#transactions

START TRANSACTION;
UPDATE Employee
SET salary=salary-100
WHERE  employee_id=6;
SELECT * FROM employee;
ROLLBACK; 
SELECT * FROM employee;


#ALTER 
ALTER TABLE employee 
ADD phone INT;

#MODIFY
ALTER TABLE Employee
MODIFY employee_name  varchar(60);

#RENAME
ALTER TABLE Employee
rename COLUMN phone to mobile_num ;

#delete

DELETE FROM employee
WHERE employee_id=10;









