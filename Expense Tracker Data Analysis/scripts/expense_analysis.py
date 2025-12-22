
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../data/expenses_data.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month

# Category-wise expenses
category_sum = df.groupby('Category')['Amount'].sum().reset_index()
sns.barplot(x='Category', y='Amount', data=category_sum)
plt.title('Category-wise Expenses')
plt.xticks(rotation=45)
plt.show()

# Monthly expenses
monthly_sum = df.groupby('Month')['Amount'].sum().reset_index()
sns.lineplot(x='Month', y='Amount', data=monthly_sum, marker='o')
plt.title('Monthly Expense Trend')
plt.show()
