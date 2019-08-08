import numpy as np
import pandas as pd

import utils

filename = "CPI"
f = open("raw/{}.txt".format(filename), "r")
lines = f.readlines()

dates = []
cpis = []

count = 0
for line in lines:
    if count % 3 == 0:
        date = line[0:5].split('\n')[0]
        dates.append(date)
    elif count % 3 == 1:
        cpi = line.split('\n')[0]
        cpis.append(cpi)
    elif count % 3 == 2:
        pass
    count += 1

dates = np.array(dates, dtype='datetime64[Y]')
cpis = np.array(cpis, dtype='float64')

data = {'Date': dates,
        'CPI': cpis}

df = pd.DataFrame(data)

utils.pickle_object(df, "data/{}.pkl".format(filename))

data_path = "data/CPI.pkl"
df = utils.load_pickle(data_path)
utils.standard_plot(df, column_name='CPI')

if __name__ == "__main__":
    pass
