-- Ranks country origins of bands
-- Ordered by number of (non-unique) fans
SELECT origin, SUM(fans) AS nb_fans from metal_bands GROUP BY origin ORDER BY nb_fans DESC;
