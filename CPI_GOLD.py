import utils

data_path = {"Gold" : "data/Gold_monthly.pkl",
             "CPI" : "data/CPI.pkl"}

df_gold = utils.load_pickle(data_path["Gold"])
df_cpi = utils.load_pickle(data_path["CPI"])

df_gold

if __name__ == "__main__":
    pass
