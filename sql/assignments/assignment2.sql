CREATE TABLE employee (
    EmpNo INT PRIMARY KEY,
    EmpName NVARCHAR(255) NOT NULL,
    BirthDay DATE,
    DeptNo SMALLINT,
    MgrNo INT NOT NULL,
    StartDate DATE,
    Salary MONEY,
    [Level] TINYINT CHECK (Level BETWEEN 1 AND 7),
    [Status] TINYINT CHECK (Status IN (0, 1, 2)),
    Note NVARCHAR(MAX)
);

CREATE TABLE skill (
    SkillNo SMALLINT IDENTITY(1,1) PRIMARY KEY,
    SkillName NVARCHAR(255),
    Note NVARCHAR(MAX)
);

CREATE TABLE emp_skill (
    SkillNo SMALLINT NOT NULL,
    EmpNo INT NOT NULL,
    SkillLevel TINYINT CHECK (SkillLevel BETWEEN 1 AND 3),
    RegDate DATE,
    [Description] NVARCHAR(MAX),
    PRIMARY KEY (SkillNo, EmpNo),
    CONSTRAINT FK_EMP_SKILL_SkillNo FOREIGN KEY (SkillNo) REFERENCES skill(SkillNo),
    CONSTRAINT FK_EMP_SKILL_EmpNo FOREIGN KEY (EmpNo) REFERENCES employee(EmpNo),
);

CREATE TABLE department (
    DeptNo SMALLINT IDENTITY(1, 1) PRIMARY KEY,
    DeptName NVARCHAR(255),
    [Note] NVARCHAR(MAX)
);

-- Q2
-- a. Add an Email field to EMPLOYEE table and make sure that the database will not allow the value for Email 
-- to be inserted into a new row if that value has already been used in another row. 
ALTER TABLE employee
ADD Email VARCHAR(255) UNIQUE;

-- b. Modify EMPLOYEE table to set default values to 0 of MgrNo and Status fields. 
ALTER TABLE employee
ADD CONSTRAINT DF_employee_MgrNo DEFAULT 0 FOR MgrNo;

ALTER TABLE employee
ADD CONSTRAINT DF_employee_Status DEFAULT 0 FOR Status;

-- Q3:  

-- a. Add the FOREIGN KEY constrain of DeptNo field to the EMPLOYEE table that will relate the DEPARTMENT table. 
ALTER TABLE employee
ADD CONSTRAINT FK_employee_DeptNo
FOREIGN KEY (DeptNo)
REFERENCES department(DeptNo);

-- b. Remove the Description field from the EMP_SKILL table. 
ALTER TABLE emp_skill
DROP COLUMN Description;

-- Q4: 

-- a. Add at least 5 records into each the created tables.

-- Inserting records into department table
INSERT INTO department (DeptName, Note)
VALUES
('Human Resources', 'Handles recruitment and employee relations'),
('Finance', 'Manages company finances and accounting'),
('IT Support', 'Provides technical support to employees'),
('Sales', 'Handles customer relations and sales transactions'),
('Marketing', 'Manages company promotions and advertising');

-- Inserting records into employee table
INSERT INTO employee (EmpNo, EmpName, BirthDay, DeptNo, MgrNo, StartDate, Salary, [Level], [Status], Note, Email)
VALUES
(1, 'John Doe', '1985-03-15', 1, 0, '2020-01-10', 60000.00, 5, 0, 'HR manager', 'john.doe@email.com'),
(2, 'Jane Smith', '1990-07-25', 2, 1, '2021-05-01', 75000.00, 4, 0, 'Accountant', 'jane.smith@email.com'),
(3, 'Michael Brown', '1982-11-30', 3, 2, '2018-06-18', 85000.00, 6, 0, 'IT technician', 'michael.brown@email.com'),
(4, 'Linda White', '1993-09-10', 4, 1, '2022-07-15', 50000.00, 3, 0, 'Sales representative', 'linda.white@email.com'),
(5, 'David Johnson', '1988-02-20', 5, 0, '2019-03-30', 65000.00, 4, 1, 'Marketing manager', 'david.johnson@email.com');

-- Inserting records into skill table
INSERT INTO skill (SkillName, Note)
VALUES
('Java Programming', 'Used for building enterprise-level applications'),
('Data Analysis', 'Proficient in data interpretation and visualization'),
('Project Management', 'Experience managing multiple projects simultaneously'),
('Sales Techniques', 'Understanding customer needs and closing sales'),
('Digital Marketing', 'Expert in online marketing strategies and tools');

-- Inserting records into emp_skill table
INSERT INTO emp_skill (SkillNo, EmpNo, SkillLevel, RegDate)
VALUES
(1, 1, 3, '2021-01-15'),
(2, 2, 2, '2021-05-10'),
(3, 3, 1, '2018-07-20'),
(4, 4, 3, '2022-08-01'),
(5, 5, 2, '2019-04-10');

-- b. Write a SQL query to list user with EmpNo, Emp_Name, and Level. It has Level satisfied the criteria: Level >=3 and Level <= 5.
SELECT EmpNo, EmpName, [Level]
FROM employee
WHERE [Level] BETWEEN 3 AND 5;