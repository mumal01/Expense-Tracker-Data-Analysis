1️⃣ Load & Clean Data
import pandas as pd

df = pd.read_csv("hostel_life_expense_tracker.csv")
df['Date'] = pd.to_datetime(df['Date'])

df.info()

2️⃣ Monthly Expense Trend
monthly_expense = (
    df.groupby(df['Date'].dt.to_period('M'))['Amount']
    .sum()
    .reset_index()
)

monthly_expense['Date'] = monthly_expense['Date'].astype(str)
monthly_expense


Insight:
Helps track spending increase/decrease per month.

3️⃣ Category-Wise Expense Analysis
category_expense = (
    df.groupby('Expense_Type')['Amount']
    .sum()
    .sort_values(ascending=False)
)

category_expense


Insight:
Identifies top spending categories (e.g., Food, Snacks, Travel).

4️⃣ Daily Average Spend
daily_avg = df.groupby('Date')['Amount'].sum().mean()
daily_avg


Use Case:
Benchmark daily spending to control unnecessary expenses.

5️⃣ High-Expense Transactions Detection
threshold = df['Amount'].mean() * 2

high_expenses = df[df['Amount'] > threshold]
high_expenses


Business Insight:
Flags unplanned or unusually high expenses.

6️⃣ Payment Mode Analysis
payment_summary = (
    df.groupby('Payment_Mode')['Amount']
    .agg(['count', 'sum'])
)

payment_summary


Insight:
Shows shift towards digital payments (UPI).
