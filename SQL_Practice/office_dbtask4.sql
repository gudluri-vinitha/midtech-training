
-- 13-07-2026 Task 1
CREATE DATABASE office_db;

USE office_db;

-- Department table
CREATE TABLE Department (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50) NOT NULL
);

--  Employee table
CREATE TABLE Employee (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    salary INT DEFAULT 25000,
    age INT CHECK (age >= 18),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES Department(department_id)
);

-- Insert 5 departments
INSERT INTO Department (department_id, department_name)
VALUES
(101, 'Drawing'),
(102, 'Engineering'),
(103, 'Non Tech'),
(104, 'Marketing'),
(105, 'Artist');

-- Insert 10 employees
INSERT INTO Employee (employee_id, employee_name, email, salary, age, department_id)
VALUES
(1, 'Sonu', 'sonu@gmail.com', 30000, 21, 104),
(2, 'Sumi', 'sumi@gmail.com', 35000, 27, 101),
(3, 'Greshma', 'greshma@gmail.com', DEFAULT, 20, 105),
(4, 'Muskan', 'muskan@gmail.com', 40000, 23, 103),
(5, 'Rushmiya', 'rushmiya@gmail.com', 20000, 22, 102),
(6, 'Motu', 'motu@gmail.com', 32000, 27, 103),
(7, 'Ayeman', 'ayeman@gmail.com', 70000, 29, 104),
(8, 'Shaoib', 'shaoib@gmail.com', 45000, 28, 105),
(9, 'Shahid', 'shahid@gmail.com', 38000, 26, 104),
(10, 'Khaja', 'khaja@gmail.com', DEFAULT, 21, 103);

SELECT * FROM Department;
SELECT * FROM Employee;

