-- customers
CREATE TABLE customers (
    id          SERIAL PRIMARY KEY,
    name        TEXT NOT NULL,
    country     TEXT NOT NULL
);

-- orders
CREATE TABLE orders (
    id           SERIAL PRIMARY KEY,
    customer_id  INT NOT NULL REFERENCES customers(id),
    amount       NUMERIC(10,2) NOT NULL,
    status       TEXT NOT NULL,          -- 'paid', 'cancelled', 'pending'
    created_at   TIMESTAMP NOT NULL
);

INSERT INTO customers (id, name, country) VALUES
  (1, 'Alice Müller',      'Germany'),
  (2, 'Bob Schmidt',       'Germany'),
  (3, 'Charlie Johnson',   'USA'),
  (4, 'Denis Dupont',      'France'),
  (5, 'Elena García',      'Spain'),
  (6, 'Femke Jansen',      'Netherlands'),
  (7, 'Gregor Fischer',    'Germany'),
  (8, 'Hiro Tanaka',       'Japan');

INSERT INTO orders (customer_id, amount, status, created_at) VALUES
  -- Germany
  (1,  45.50,  'paid',      '2025-11-25 10:15:00'),
  (1,  89.99,  'paid',      '2025-11-25 16:30:00'),
  (2,  15.00,  'cancelled', '2025-11-26 09:10:00'),
  (2, 120.00,  'paid',      '2025-11-27 13:05:00'),
  (7,  60.00,  'pending',   '2025-11-28 08:20:00'),
  (7,  75.00,  'paid',      '2025-11-29 11:45:00'),

  -- USA
  (3, 200.00,  'paid',      '2025-11-25 12:00:00'),
  (3, 350.00,  'paid',      '2025-11-26 18:40:00'),
  (3,  59.99,  'cancelled', '2025-11-27 14:10:00'),

  -- France
  (4,  80.00,  'paid',      '2025-11-25 09:00:00'),
  (4,  95.00,  'paid',      '2025-11-26 09:30:00'),
  (4,  10.00,  'cancelled', '2025-11-27 09:45:00'),
  (4, 5000.00,'paid',      '2025-11-28 21:15:00'), -- выброс для задания с аномалиями

  -- Spain
  (5,  35.00,  'paid',      '2025-11-25 15:20:00'),
  (5,  40.00,  'pending',   '2025-11-26 17:00:00'),
  (5, 150.00,  'paid',      '2025-11-27 19:30:00'),

  -- Netherlands
  (6,  55.00,  'paid',      '2025-11-25 08:10:00'),
  (6,  70.00,  'paid',      '2025-11-26 08:15:00'),
  (6,  30.00,  'cancelled', '2025-11-27 08:20:00'),

  -- Japan
  (8,  99.90,  'paid',      '2025-11-28 10:00:00'),
  (8,  10.00,  'cancelled', '2025-11-28 12:00:00'),
  (8, 300.00,  'paid',      '2025-11-29 20:00:00');
