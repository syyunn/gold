import utils

fname = "data/gold_daily_normal_cpi_monthly.pkl"
df_gold_daily = utils.load_pickle(fname)
utils.standard_plot(df_gold_daily, column_name='Gold_Normal')

if __name__ == "__main__":
    pass
