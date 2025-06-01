LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\customers-100.csv'
INTO TABLE customers 
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;


SET GLOBAL local_infile = 'ON';
SHOW VARIABLES LIKE "local_infile";  
SHOW VARIABLES LIKE "secure_file_priv";



SELECT @@session.sql_mode;

select student_name, sum(test_score) 
from student
group by 1;


create table numbers
(val INT)
;

INSERT INTO NUMBERS
(val)
values
(1),
(1),
(2),
(3),
(3),
(3),
(4),
(4),
(5)
;

select * from numbers;

SELECT
         val,
         ROW_NUMBER()   OVER w AS 'row_number',
         CUME_DIST()    OVER w AS 'cume_dist',
         PERCENT_RANK() OVER w AS 'percent_rank'
       FROM numbers
       WINDOW w AS (ORDER BY val)
;

SELECT
         val,
         ROW_NUMBER() OVER w AS 'row_number',
         RANK()       OVER w AS 'rank',
         DENSE_RANK() OVER w AS 'dense_rank'
       FROM numbers
       WINDOW w AS (ORDER BY val)
;

create table observations(
time time,
subject varchar(10),
val int
)
;

INSERT INTO observations(
time,
subject,
val
)
VALUES
('07:00:00', 'st113', 10),
('07:15:00', 'st113',  9),
('07:30:00', 'st113', 25),
('07:45:00', 'st113', 20),
('07:00:00', 'xh458',  0),
('07:15:00', 'xh458', 10),
('07:30:00', 'xh458',  5),
('07:45:00', 'xh458', 30),
('08:00:00', 'xh458', 25)