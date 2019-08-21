"""Normalize Gold Price with CPI data """

import utils

import pandas as pd
import numpy as np
import datetime


data_path = {"Gold": "../data/gold_daily.pkl",
             "CPI": "../data/cpi_monthly.pkl"}

df_gold = utils.load_pickle(data_path["Gold"])
df_cpi = utils.load_pickle(data_path["CPI"])

# utils.standard_plot(df_cpi, column_name="CPI")
# utils.standard_plot(df_gold, column_name="Gold")

normal_target_dates = df_gold['Date']

gold_normals_date = []
gold_normals = []

for gold_idx, date in enumerate(normal_target_dates):
    gold = df_gold['Gold'][gold_idx]

    cpi_date = datetime.datetime(date.year, date.month, 1, 0, 0)
    cpi_idx = df_cpi['Date'][df_cpi['Date'] == cpi_date].index.tolist()

    if len(cpi_idx) == 0:
        continue
    else:
        cpi_idx = cpi_idx[0]
    # print(cpi_idx)
    cpi = df_cpi['CPI'][cpi_idx]
    print("cpi: {}, gold: {}".format(cpi, gold))

    normalizer = 100/cpi
    gold_normal = gold * normalizer
    gold_normals.append(gold_normal)
    gold_normals_date.append(date)

data_cpi_normalized = {'Date': gold_normals_date,
                       'Gold_Normal': gold_normals}

df_gold_normal = pd.DataFrame(data_cpi_normalized)

utils.standard_plot(df_gold_normal, column_name="Gold_Normal")
utils.pickle_object(df_gold_normal, "../data/gold_daily_normal_cpi_monthly.pkl")
if __name__ == "__main__":
    pass
