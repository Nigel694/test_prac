import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# Load the dataset
data = pd.read_csv('NAB.csv')

# Convert the Date column to a datetime format
data['Date'] = pd.to_datetime(data['Date'], format='%d %b %y')

# Calculate revenue and expenses
revenue = data[data['Amount'] > 0]
expenses = data[data['Amount'] < 0]
expenses['Amount'] = -expenses['Amount']

# Create a linear regression model for revenue
revenue_model = LinearRegression()
revenue_model.fit(revenue['Date'].dt.dayofyear.values.reshape(-1, 1), revenue['Amount'])

# Create a linear regression model for expenses
expenses_model = LinearRegression()
expenses_model.fit(expenses['Date'].dt.dayofyear.values.reshape(-1, 1), expenses['Amount'])

# Generate revenue and expenses forecasts
days = pd.date_range(start=data['Date'].min(), end='2023-12-31', freq='D')
revenue_forecast = pd.DataFrame({'Date': days, 'Amount': revenue_model.predict(days.dayofyear.values.reshape(-1, 1))})
expenses_forecast = pd.DataFrame({'Date': days, 'Amount': -expenses_model.predict(days.dayofyear.values.reshape(-1, 1))})

# Visualize revenue and expenses forecasts using Seaborn
sns.set_style('whitegrid')
plt.figure(figsize=(10, 6))
sns.lineplot(x='Date', y='Amount', data=revenue_forecast, label='Revenue')
sns.lineplot(x='Date', y='Amount', data=expenses_forecast, label='Expenses')
plt.xlabel('Date')
plt.ylabel('Amount')
plt.title('Revenue and Expenses Forecast')
plt.legend()
plt.show()