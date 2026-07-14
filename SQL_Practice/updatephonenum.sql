-- task to enter the phone numbers column in the table
-- phone column
ALTER TABLE Employee
ADD phone VARCHAR(15);

--  phone for 3 employees
UPDATE Employee
SET phone = '9876543210'
WHERE employee_id = 1;

UPDATE Employee
SET phone = '9123456789'
WHERE employee_id = 2;

UPDATE Employee
SET phone = '9988776655'
WHERE employee_id = 3;

SELECT * FROM Employee;