/* Write your T-SQL query statement below */
SELECT C.name as Customers from Customers C FULL OUTER JOIN Orders O on C.id=O.customerId WHERE O.id is NULL