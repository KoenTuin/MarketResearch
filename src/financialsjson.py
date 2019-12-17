import json
import time

import requests

#problem list:
#json file needs to be empty before reading every time
#
#
#


def calculatePercentage():
    with open('data.json', 'r') as f:
        list = json.load(f)["Time Series (1min)"]
        for each in list:
            print(each)

    f.close

    # with open('data.json') as f:
    #     data = json.load(f)
    #
    #     print(data["Time Series (1min)"][{}]["4. close"])


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
