import sys
from yahoo_historical import Fetcher
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Command-line argument
stock_ticker = sys.argv[1]

# Calculate start and end dates for the 3-month period
end_date = datetime.now().date()
start_date = end_date - timedelta(days=90)

# Fetch stock data using yahoo-historical
data = Fetcher(stock_ticker, start_date, end_date).get_historical()
data.reset_index(inplace=True)  # Convert index to a column
data['Date'] = pd.to_datetime(data['Date'])

# Extract stock prices from the data
dates = data['Date']
prices = data['Close']

# Plotting the stock prices
plt.plot(dates, prices)
plt.title(f"Stock Prices for {stock_ticker} (Last 3 Months)")
plt.xlabel("Date")
plt.ylabel("Price")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
