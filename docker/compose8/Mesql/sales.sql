CREATE TABLE sales_timeseries (
    id          SERIAL PRIMARY KEY,
    "time"      TIMESTAMP NOT NULL,   -- ось времени для Grafana
    country     TEXT NOT NULL,        -- страна (лейбл / серия)
    value       NUMERIC(10,2) NOT NULL -- агрегированная сумма продаж
);

INSERT INTO sales_timeseries ("time", country, value)
SELECT
    DATE(o.created_at)::timestamp AS "time",  -- только дата, но в типе timestamp
    c.country                     AS country,
    SUM(o.amount)                 AS value
FROM orders o
JOIN customers c ON o.customer_id = c.id
WHERE o.status = 'paid'
GROUP BY DATE(o.created_at), c.country
ORDER BY "time", country;

