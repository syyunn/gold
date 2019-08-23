import utils
import numpy as np

fname = "volatility_data/gold_daily.pkl"
df = utils.load_pickle(fname)
utils.standard_plot(df, column_name='Volatility')

num_data = df.shape[0]

dates = []
signs = []

count_plus = 0
count_minus = 0
count_zero = 0

spread = 2
bigger_than_spread_dates = []
vols_of_bigger_than_spread_dates = []
how_biggers = []

for idx in range(num_data):
    curr_date = df.loc[idx]["Date"]
    curr_vol = df.loc[idx]["Volatility"]
    if curr_vol > 2:
        bigger_than_spread_dates.append(curr_date)
        vols_of_bigger_than_spread_dates.append(curr_vol)
        print(curr_date, " ", curr_vol, " ", curr_vol-spread)
        how_biggers.append(curr_vol-spread)

    #print(curr_vol)
    sign = np.sign(curr_vol)
    #print(sign)

    if sign == 1:
        count_plus +=1
    elif sign == -1:
        count_minus +=1
    elif sign == 0:
        count_zero +=1

    dates.append(curr_date)
    signs.append(sign)

df_sign = utils.make_as_pandas_df(dates_list=dates,
                                  content_list=signs,
                                  content_name="sign_of_volatility")

utils.pickle_object(df_sign, "volatility_data/sign_daily_gold.pkl")

utils.standard_plot(df_sign[:100],
                    column_name="sign_of_volatility",
                    scatter=True)

print("count_plus: {}, count_minus: {}, conut_zero: {}".format(count_plus,
                                                               count_minus,
                                                               count_zero))

if __name__ == "__main__":
    pass
