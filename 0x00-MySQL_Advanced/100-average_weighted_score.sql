-- a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student.
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
    IN user_id INT
)
BEGIN

    UPDATE users
    SET average_score = (SELECT SUM(projects.weight*corrections.score) / SUM(projects.weight)
    FROM projects
    INNER JOIN corrections ON
    projects.id =  corrections.project_id
    WHERE corrections.user_id = user_id)
    WHERE users.id = user_id;

END //

DELIMITER ;
