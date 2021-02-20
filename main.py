import pandas as pd  # The Pandas data science library
import datetime  # Module supplies classes for manipulating dates and times
import requests  # The requests library for HTTP requests in Python
from tabulate import tabulate  # Pretty-print tabular data in Python
from secrets import IEX_CLOUD_API_TOKEN


def print_start(name):
    print(f'Hi, {name} the program starts now at @ {datetime.datetime.now()}')


if __name__ == '__main__':
    # Start the program and use a first function to say hi and note the current time
    print_start('Johannes')
    # Read csv with stock ticker list to pandas dataframe
    stocks = pd.read_csv('files/sp_500_stocks.csv')
    # Print the stock ticker dataframe with tabulate formatting
    print(tabulate(stocks.head(5), headers='keys', tablefmt='psql', showindex=True))
    # Select a specific symbol from the ticker as a variable
    symbol = 'AAPL'
    # Prepare the API call URL with symbol via variable and the secret for the token
    api_url = f'https://sandbox.iexapis.com/stable/stock/{symbol}/quote?token={IEX_CLOUD_API_TOKEN}'
    # Use the prepared api_url and make a get request and retrieve the response as JSON
    data = requests.get(api_url).json()

    # Prepare columns for a pandas dataframe
    my_columns = ['Ticker', 'Price', 'Market Capitalization', 'Number Of Shares to Buy']
    # Create the structure of a pandas dataframe with the column information
    final_dataframe = pd.DataFrame(columns=my_columns)
    # Fill data to the pandas dataframe
    final_dataframe = final_dataframe.append(
        pd.Series(['AAPL',
                   data['latestPrice'],
                   data['marketCap'],
                   'N/A'],
                  index=my_columns),
        ignore_index=True)
    # Print the symbol data retrieved via the API in the dataframe with tabulate formatting
    print(tabulate(final_dataframe.head(5), headers='keys', tablefmt='psql', showindex=True))
