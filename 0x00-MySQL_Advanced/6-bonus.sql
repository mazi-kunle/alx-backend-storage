-- a SQL script that creates a stored procedure AddBonus that adds a new correction for a student.

DELIMITER //

CREATE PROCEDURE AddBonus(
    IN user_id INT,
    IN project_name VARCHAR(255),
    IN score INT
)
BEGIN
    DECLARE id_ INT; 
    
    IF (SELECT EXISTS(SELECT * FROM projects WHERE name = project_name)) =  0
    THEN INSERT INTO projects (name)
    VALUES (project_name);

    END IF;
    
    SELECT id INTO id_ FROM projects
    WHERE name = project_name;
    
    INSERT INTO corrections
    VALUES (user_id, id_, score);

END //

DELIMITER ;
