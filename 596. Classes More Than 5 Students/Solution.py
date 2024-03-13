# Write your MySQL query statement below
SELECT class from Courses 
Group BY class
Having count(*) >=5
