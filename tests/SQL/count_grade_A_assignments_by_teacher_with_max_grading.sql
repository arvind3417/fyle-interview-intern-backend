SELECT COUNT(*) AS grade_a_count
FROM assignments
WHERE teacher_id = (
    SELECT teacher_id
    FROM assignments
    WHERE grade = 'A'
    GROUP BY teacher_id
    ORDER BY COUNT(*) DESC
    LIMIT 1
) AND grade = 'A';