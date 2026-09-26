SELECT 
    MAX(num) AS num
FROM (
    SELECT 
        num,
        COUNT(*) AS frequency
    FROM MyNumbers
    GROUP BY num
    HAVING frequency = 1
) t;