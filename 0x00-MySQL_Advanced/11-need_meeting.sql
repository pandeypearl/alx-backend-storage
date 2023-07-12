-- Creates view need_meeting
-- lists all students that have score below 80
-- and no last_meeting of more that 1 month
CREATE VIEW need_meeting
AS
SELECT
    name
FROM
    students
WHERE score < 80 AND ((last_meeting IS NULL) OR ADDDATE(CURDATE(), INTERVAL -1 MONTH) > last_meeting);
