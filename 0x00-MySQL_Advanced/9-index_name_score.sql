-- Creates index idx_name_first on the table names
-- and the first letter of the name
-- as well as the score
CREATE INDEX idx_name_first_score ON names (name(1), score);
