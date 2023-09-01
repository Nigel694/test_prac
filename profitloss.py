import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('NAB.csv')

# Convert the Date column to a datetime format
data['Date'] = pd.to_datetime(data['Date'], format='%d %b %y')

# Calculate revenue and expenses
revenue = data[data['Amount'] > 0]
expenses = data[data['Amount'] < 0]

# Visualize revenue and expenses using a stacked bar chart
sns.set_style('whitegrid')
plt.figure(figsize=(10, 6))
plt.bar(revenue['Date'], revenue['Amount'], color='green', label='Revenue')
plt.bar(expenses['Date'], expenses['Amount'], color='red', label='Expenses')
plt.xlabel('Date')
plt.ylabel('Amount')
plt.title('Revenue and Expenses')
plt.legend()
plt.show()