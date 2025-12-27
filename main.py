# ===============================
# Stock Market Trend Analysis
# ===============================

# 1. Import libraries
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


# 2. Stock configuration
STOCK_SYMBOL = "TCS.NS"       # Change to RELIANCE.NS / TCS.NS if needed
START_DATE = "2025-01-01"
END_DATE = "2025-12-20"


# 3. Fetch stock data
print("Downloading stock data...")
df = yf.download(STOCK_SYMBOL, start=START_DATE, end=END_DATE)

# 4. Data cleaning
df.dropna(inplace=True)
df.reset_index(inplace=True)

print("\nData sample:")
print(df.head())


# 5. Time-Series Analysis (Closing Price)
plt.figure()
plt.plot(df['Date'], df['Close'])
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.title(f"{STOCK_SYMBOL} Closing Price Trend")
plt.show()


# 6. Moving Average Analysis
df['MA_20'] = df['Close'].rolling(window=20).mean()
df['MA_50'] = df['Close'].rolling(window=50).mean()

plt.figure()
plt.plot(df['Date'], df['Close'], label='Close Price')
plt.plot(df['Date'], df['MA_20'], label='20-Day MA')
plt.plot(df['Date'], df['MA_50'], label='50-Day MA')
plt.xlabel("Date")
plt.ylabel("Price")
plt.title("Moving Average Analysis")
plt.legend()
plt.show()


# 7. Daily Returns
df['Daily_Return'] = df['Close'].pct_change()

plt.figure()
plt.plot(df['Date'], df['Daily_Return'])
plt.xlabel("Date")
plt.ylabel("Daily Return")
plt.title("Daily Returns")
plt.show()


# 8. Volatility Analysis
df['Volatility_20'] = df['Daily_Return'].rolling(window=20).std()

plt.figure()
plt.plot(df['Date'], df['Volatility_20'])
plt.xlabel("Date")
plt.ylabel("Volatility")
plt.title("20-Day Rolling Volatility")
plt.show()


# 9. Volume Analysis
plt.figure()
plt.plot(df['Date'], df['Volume'])
plt.xlabel("Date")
plt.ylabel("Volume")
plt.title("Trading Volume Over Time")
plt.show()


# 10. Save cleaned data
df.to_csv("stock_analysis_output.csv", index=False)
print("\nAnalysis completed. Data saved to stock_analysis_output.csv")
