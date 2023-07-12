-- Creates stored procedure ComputeAverageScoreForUser that
-- computes and stores average score for student
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
UPDATE users
SET average_score = (SELECT AVG(score) FROM corrections WHERE corrections.user_id = user_id) WHERE id = user_id;
END//
DELIMITER ;
