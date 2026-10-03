-- 1. Order status distribution
SELECT order_status, COUNT(*) AS total_orders
FROM orders
GROUP BY order_status
ORDER BY total_orders DESC;

-- 2. Monthly order trend
SELECT DATE_TRUNC('month', purchase_date::date)::date AS month,
       COUNT(*) AS total_orders
FROM orders
GROUP BY month
ORDER BY month;

-- 3. Top 10 months by order volume
SELECT DATE_TRUNC('month', purchase_date::date)::date AS month,
       COUNT(*) AS total_orders
FROM orders
GROUP BY month
ORDER BY total_orders DESC
LIMIT 10;

-- 4. Orders by weekday
SELECT TO_CHAR(purchase_date::date, 'Day') AS weekday,
       EXTRACT(ISODOW FROM purchase_date::date) AS day_number,
       COUNT(*) AS total_orders
FROM orders
GROUP BY weekday, day_number
ORDER BY day_number;

-- 5. Average delivery performance
SELECT ROUND(AVG(delivery_days::numeric), 2) AS avg_delivery_days,
       ROUND(AVG(estimated_delivery_days::numeric), 2) AS avg_estimated_days,
       ROUND(AVG(delivery_delay_days::numeric), 2) AS avg_delay_days
FROM orders
WHERE order_status = 'delivered';

-- 6. Monthly average delivery delay
SELECT DATE_TRUNC('month', purchase_date::date)::date AS month,
       ROUND(AVG(delivery_delay_days::numeric), 2) AS avg_delay_days
FROM orders
WHERE order_status = 'delivered'
  AND delivery_delay_days IS NOT NULL
GROUP BY month
ORDER BY month;

-- 7. Late and on-time delivery
SELECT COUNT(*) FILTER (WHERE delivery_delay_days::numeric > 0) AS late_orders,
       COUNT(*) FILTER (WHERE delivery_delay_days::numeric <= 0) AS on_time_or_early_orders
FROM orders
WHERE order_status = 'delivered';

-- 8. Overall order count
SELECT COUNT(*) AS total_orders
FROM orders;

-- 9. Customer distribution by state
SELECT customer_state, COUNT(*) AS total_customers
FROM customers
GROUP BY customer_state
ORDER BY total_customers DESC;
