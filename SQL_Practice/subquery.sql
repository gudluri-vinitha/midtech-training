-- 14-07-2026 task
-- this is used to select the maximum salary from the employee table
SELECT *FROM Employee
WHERE salary = (
    SELECT MAX(salary)
    FROM Employee
);
