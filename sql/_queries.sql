--- View first 10 orders
SELECT * FROM orders
LIMIT 10;

-- Total number of orders
SELECT COUNT(*) AS total_orders
FROM orders;

-- Total number of customers
SELECT COUNT(*) AS total_customers
FROM customers;

-- Average payment value
SELECT AVG(payment_value) AS avg_payment
FROM payments;

-- Top 10 highest payment orders
SELECT order_id, payment_value
FROM payments
ORDER BY payment_value DESC
LIMIT 10;

-- Number of orders by payment type
SELECT payment_type, COUNT(*) AS total_orders
FROM payments
GROUP BY payment_type
ORDER BY total_orders DESC;

-- Total products
SELECT COUNT(*) AS total_products
FROM products;

-- Total order items
SELECT COUNT(*) AS total_items
FROM order_items;

-- Customer distribution by state
SELECT customer_state, COUNT(*) AS total_customers
FROM customers
GROUP BY customer_state
ORDER BY total_customers DESC;

-- Top states with most customers
SELECT customer_state, COUNT(*) AS total_customers
FROM customers
GROUP BY customer_state
ORDER BY total_customers DESC
LIMIT 10;
