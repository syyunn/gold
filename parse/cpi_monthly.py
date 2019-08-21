""" Make pandas f/ monthly CPI raw data"""
import datetime
# import numpy as np
# import pandas as pd

import utils

filename = "cpi_monthly"
f = open("../raw/{}.txt".format(filename), "r")
lines = f.readlines()

dates = []
cpis = []

for line in lines:
    split = line.split('\t')
    try:
        year = int(split[0])
    except ValueError: # get rid of str column data
        continue
    print(split)

    for month, cpi in enumerate(split[1:13]):
        date = datetime.datetime(year, month+1, 1, 0, 0)
        dates.append(date)
        cpis.append(float(cpi))

df = utils.make_as_pandas_df(dates_list=dates,
                             content_list=cpis,
                             content_name='CPI')

utils.standard_plot(df, column_name='CPI')
utils.pickle_object(df, "../data/cpi_monthly.pkl")

if __name__ == "__main__":
    pass
