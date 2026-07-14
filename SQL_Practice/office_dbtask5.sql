USE office_db;
SELECT * FROM Employee;
SELECT  employee_name,salary FROM Employee;
SELECT  salary FROM Employee  WHERE salary>50000;
SELECT  age  FROM Employee  WHERE age BETWEEN 25 AND 30;

SELECT employee_name 
FROM employee
WHERE department_id IN (101, 103);

SELECT DISTINCT department_id FROM Employee;

SELECT * FROM Employee ORDER BY  salary DESC;
SELECT * FROM Employee LIMIT 5;
SELECT * FROM Employee  WHERE employee_name LIKE "J%";
SELECT MAX(salary),employee_name,employee_id,email,age,department_id FROM Employee ;
SELECT MIN(salary),employee_name,employee_id,email,age,department_id FROM Employee ;
SELECT AVG(salary),employee_name,employee_id,email,age,department_id  FROM Employee ;
 
 SELECT department_id , COUNT(*)  FROM Employee GROUP BY department_id;

 SELECT department_id , COUNT(*)  FROM Employee GROUP BY department_id  HAVING COUNT(*)>1;

SELECT department_name, employee_name
FROM Department
INNER JOIN Employee
ON Department.department_id = Employee.department_id;




