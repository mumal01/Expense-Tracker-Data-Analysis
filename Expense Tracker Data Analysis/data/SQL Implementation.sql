1️⃣ Table Schema
CREATE TABLE expenses (
    expense_date DATE,
    expense_type VARCHAR(50),
    amount INT,
    payment_mode VARCHAR(20),
    notes VARCHAR(255)
);

2️⃣ Monthly Expense Report
SELECT 
    DATE_FORMAT(expense_date, '%Y-%m') AS month,
    SUM(amount) AS total_expense
FROM expenses
GROUP BY month
ORDER BY month;

3️⃣ Category-Wise Spending
SELECT 
    expense_type,
    SUM(amount) AS total_spent
FROM expenses
GROUP BY expense_type
ORDER BY total_spent DESC;

4️⃣ Identify High Spending Days
SELECT 
    expense_date,
    SUM(amount) AS daily_spend
FROM expenses
GROUP BY expense_date
HAVING daily_spend > (
    SELECT AVG(amount) * 2 FROM expenses
);

5️⃣ Payment Mode Usage
SELECT 
    payment_mode,
    COUNT(*) AS transactions,
    SUM(amount) AS total_amount
FROM expenses
GROUP BY payment_mode;
