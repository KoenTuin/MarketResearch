import json
import time

import requests


def calculatePercentage():
    with open('data.json', 'r') as f:
        list = json.load(f)["Time Series (1min)"]
        for time in list:
            print(list[time]["4. close"])
            # Calcuate percentage difference between each value and its previous value
            # Calculate percentage change over the last 100 entries
            #
    f.close


def getData():
    api_key = 'EJV3BXUMBKL7EZDP'
    interval = '1min'

    print('Enter the symbol you want to gather data about:')
    fsymbol = input()

    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' \
          + fsymbol + '&interval=' + interval + '&outputsize=compact&apikey=' + api_key

    i = 1
    while i == 1:
        forex = requests.get(url)
        data = forex.json()
        with open('data.json', 'w') as f:
            json.dump(data, f)
        print('Data written to file')
        print('Calculating percentages')
        calculatePercentage()
        time.sleep(60);


calculatePercentage()
