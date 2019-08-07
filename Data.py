import numpy as np
import pandas as pd

import utils

filename = "monthly"
f = open("raw/{}.csv".format(filename), "r")
lines = f.readlines()

dates = []
prices = []
for line in lines:
    date, price = line.split(',')
    dates.append(date)
    prices.append(price)

dates = np.array(dates, dtype='datetime64[M]')

data = {'Date': dates,
        'Gold': prices}

df = pd.DataFrame(data)


utils.pickle_object(df, "data/Gold_{}.pkl".format(filename))

if __name__ == "__main__":
    pass
