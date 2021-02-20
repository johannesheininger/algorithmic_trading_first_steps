import pandas as pd


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('PyCharm')
    stocks = pd.read_csv('files/sp_500_stocks.csv')
    print(stocks.count())
