import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time
import json

# api key from: https://www.alphavantage.co/support/#api-key
api_key = 'EJV3BXUMBKL7EZDP'

# user input
print("Type the symbol you want to get alerts about")
fsymbol = input()

ts = TimeSeries(key=api_key, output_format='pandas')

i = 1
while i == 1:
    data, meta_data = ts.get_intraday(symbol=fsymbol, interval='1min', outputsize='compact')
    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)
    # data.to_excel("output.xlsx")
    print("Output written")

    close_data = data['4. close']
    percentage_change = close_data.pct_change()

    print(percentage_change)

    last_change = percentage_change[-1]

    if abs(last_change) > 0.0004:
        print("Alert:" + str(last_change))

    time.sleep(50)
    print("ten seconds to exit the excel file")
    time.sleep(10)
