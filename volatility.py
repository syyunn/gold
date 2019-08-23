import utils

fname = "data/gold_daily.pkl"
df = utils.load_pickle(fname)
utils.standard_plot(df, column_name='Gold')

num_data = df.shape[0]

volatiles = []
dates = []

for idx in range(num_data-1):
    curr_day = df.loc[idx]["Date"]
    curr_gold = df.loc[idx]["Gold"]
    tmr_gold = df.loc[idx+1]["Gold"]
    target_volatility = (tmr_gold - curr_gold) / curr_gold
    target_volatility_percentage = target_volatility * 100
    print("idx: {}, vol: {}".format(curr_day, target_volatility_percentage))

    volatiles.append(target_volatility_percentage)
    dates.append(curr_day)

df_volatile = utils.make_as_pandas_df(dates, content_list=volatiles,
                                      content_name="Volatility")

utils.standard_plot(df_volatile, column_name="Volatility")

utils.pickle_object(df_volatile, "gold_daily.pkl")


if __name__ == "__main__":
    pass
