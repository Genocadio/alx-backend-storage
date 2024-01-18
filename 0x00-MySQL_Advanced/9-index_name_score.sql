--  script that creates an index

CREATE INDEX idx_name_first_score ON names (SUBSTRING(name, 1, 1), SUBSTRING(score, 1, 1));
