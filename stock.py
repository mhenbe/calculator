import requests

# Replace 'YOUR_API_KEY' with your actual API key from Alpha Vantage
API_KEY = 'I1UYF4O31T6XIXD6'  # Replace 'YOUR_API_KEY' with your actual API key

def get_stock_data(symbol):
    base_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY'
    params = {
        'symbol': symbol,
        'interval': '1min',
        'apikey': API_KEY
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        time_series = data.get('Time Series (1min)')
        if time_series:
            latest_data = list(time_series.values())[0]
            print(f'Symbol: {symbol}')
            print(f'Open: {latest_data["1. open"]}')
            print(f'High: {latest_data["2. high"]}')
            print(f'Low: {latest_data["3. low"]}')
            print(f'Close: {latest_data["4. close"]}')
            print(f'Volume: {latest_data["5. volume"]}')
        else:
            print('No data available for this symbol.')
    else:
        print('Error fetching data')

if __name__ == '__main__':
    symbol = input('Enter a stock symbol (e.g., AAPL): ')
    get_stock_data(symbol)

