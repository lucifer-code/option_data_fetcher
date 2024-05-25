import yfinance as yf
import pandas as pd
import time

# Function to fetch historical data for a given ticker
def fetch_stock_data(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1d")  # Fetching one year of data
    return hist

# Function to calculate EMAs for different periods
def calculate_emas(data, periods=[5, 20, 50, 100, 200]):
    emas = pd.DataFrame()
    for period in periods:
        emas[f'EMA_{period}'] = data['Close'].ewm(span=period, adjust=False).mean()
    return emas

# Function to check if the EMAs are converging
def check_convergence(emas, threshold=0.01):
    # Calculate the difference between the maximum and minimum EMA values
    ema_diff = emas.max(axis=1) - emas.min(axis=1)
    
    # Check if the difference is below a threshold (e.g., 1% of the stock price)
    close_prices = emas.mean(axis=1)
    convergence = ema_diff / close_prices < threshold
    
    return convergence

# Function to screen a list of stocks
def screen_stocks(tickers, threshold=0.01):
    results = []
    for ticker in tickers:
        try:
            data = fetch_stock_data(ticker)
            if data.empty:
                continue
            emas = calculate_emas(data)
            convergence = check_convergence(emas, threshold)
            if convergence.iloc[-1]:  # Check the latest date for convergence
                results.append(ticker)
        except Exception as e:
            print(f"Error processing {ticker}: {e}")
    return results

# List of Indian stock tickers (NSE)
tickers = ['RELIANCE.NS', 'TCS.NS', 'INFY.NS', 'HDFCBANK.NS']  # Add more tickers as needed

# Main loop to run the stock screener every 3 minutes
if __name__ == "__main__":
    while True:
        converging_stocks = screen_stocks(tickers)
        print("Stocks with converging EMAs:", converging_stocks)
        # print(fetch_stock_data('TCS.NS'))
        print(f"Next run in 3 minutes...")
        time.sleep(10)  # Sleep for 180 seconds (3 minutes)
