-- Create the school database
CREATE DATABASE school;

-- Use the school database
USE school;

-- Create the student table with student_name as the primary key
CREATE TABLE student (
    student_name VARCHAR(50) PRIMARY KEY NOT NULL,
    password VARCHAR(50) NOT NULL
);
