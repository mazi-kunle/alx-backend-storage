-- a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers that 
-- computes and store the average weighted score for all students.
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users
    SET average_score = (SELECT SUM(projects.weight*corrections.score) / SUM(projects.weight)
    FROM projects
    INNER JOIN corrections ON
    projects.id =  corrections.project_id
    WHERE corrections.user_id = users.id);
END //

DELIMITER ;
