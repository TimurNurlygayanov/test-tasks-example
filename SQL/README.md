# FROM hakerrank

# Select all cities in USA with population larger than 120k
SELECT NAME FROM CITY WHERE COUNTRYCODE='USA' AND POPULATION>120000;

# Select unique cities with even IDs
SELECT DISTINCT CITY FROM STATION WHERE MOD(ID, 2) = 0;

# Find the difference between the total number of CITY entries in the table and
# the number of distinct CITY entries in the table.
SELECT (COUNT(CITY) - COUNT(DISTINCT CITY)) FROM STATION;

# Select the shortest and the longest city name in the table
SELECT * FROM (SELECT CITY, LENGTH(CITY) FROM STATION ORDER BY LENGTH(CITY), CITY) WHERE ROWNUM  = 1;
SELECT * FROM (SELECT CITY, LENGTH(CITY) FROM STATION ORDER BY LENGTH(CITY) DESC) WHERE ROWNUM = 1;

# SQL Substrings
SELECT DISTINCT CITY FROM STATION where SUBSTR(CITY,1,1) IN('A','E','I','O','U');
SELECT DISTINCT CITY FROM STATION where SUBSTR(CITY,LENGTH(CITY),1) IN('a','e','i','o','u');

# Query the Name of any student in STUDENTS who scored higher than  Marks.
# Order your output by the last three characters of each name. If two or
# more students both have names ending in the same last three characters
# (i.e.: Bobby, Robby, etc.), secondary sort them by ascending ID.
SELECT NAME FROM STUDENTS WHERE MARKS > 75 ORDER BY SUBSTR(NAME,LENGTH(NAME)-2, 3), ID;


# JOINS
SELECT SUM(my_city.POPULATION) FROM CITY AS my_city JOIN COUNTRY AS my_country ON my_city.COUNTRYCODE=my_country.CODE WHERE my_country.CONTINENT='Asia';

# with GROUP BY
SELECT my_country.CONTINENT, FLOOR(AVG(my_city.POPULATION)) FROM CITY AS my_city JOIN COUNTRY AS my_country ON my_city.COUNTRYCODE=my_country.CODE GROUP BY my_country.CONTINENT;

