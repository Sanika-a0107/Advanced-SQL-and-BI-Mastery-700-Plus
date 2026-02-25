/* TECHNICAL RIGOR SERIES: Advanced Analytical Querying
   Focus: Ranking, Partitioning, and Multi-level Aggregations
   Application: Enterprise-scale Compensation and Performance Analysis
*/

-- 1. IDENTIFYING TOP TALENT: Finds top 3 highest paid employees per department.
-- Uses RANK() to handle ties and PARTITION BY to segment organizational units.
SELECT name, department_id, salary
FROM (
  SELECT name, department_id, salary,
         RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS rnk
  FROM Employee
) t
WHERE rnk <= 3;

-- 2. DEPARTMENTAL BENCHMARKING: Compares individual commission to department average.
-- This logic identifies outliers and ensures departmental pay equity.
SELECT name, department_id, commission,
       AVG(commission) OVER (PARTITION BY department_id) AS dept_avg_commission
FROM Employee;

-- 3. GLOBAL BENCHMARKING: Compares individual commission to the entire company average.
-- Essential for high-level executive reporting on compensation trends.
SELECT name, commission,
       AVG(commission) OVER () AS company_avg_commission
FROM Employee;

-- 4. PRECISION RANKING: Finds the exact second-highest salary per department.
-- Uses DENSE_RANK() to ensure skipped ranks don't occur in case of salary ties.
SELECT name, department_id, salary
FROM (
  SELECT name, department_id, salary,
         DENSE_RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS rnk
  FROM Employee
) t
WHERE rnk = 2;
