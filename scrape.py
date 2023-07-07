import sys
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

# Command-line argument
stock_ticker = sys.argv[1]

# Calculate start and end dates for the 3-month period
end_date = datetime.now().date()
start_date = end_date - timedelta(days=90)

# Fetch stock data using yfinance
data = yf.download(stock_ticker, start=start_date, end=end_date)
data.reset_index(inplace=True)  # Convert index to a column

# Convert the Date column to datetime type
data['Date'] = pd.to_datetime(data['Date'])

# Extract stock prices from the data
dates = data['Date'].dt.strftime("%Y-%m-%d")
prices = data['Close']

# Plotting the stock prices
plt.figure(figsize=(15, 10))
plt.plot(dates, prices)
plt.title(f"Stock Prices for {stock_ticker} (Last 3 Months)")
plt.xlabel("Date")
plt.ylabel("Price")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Perform ARIMA forecasting
model = ARIMA(prices, order=(1, 1, 1))
model_fit = model.fit()
forecast = model_fit.predict(start=len(prices), end=len(prices) + 30)

# Plotting the forecasted prices
plt.figure(figsize=(15, 10))
plt.plot(dates, prices, label="Actual Prices")
plt.plot(forecast.index, forecast, label="Forecasted Prices")
plt.title(f"Stock Price Forecast for {stock_ticker}")
plt.xlabel("Date")
plt.ylabel("Price")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
