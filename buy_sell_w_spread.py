import utils

fname = "data/gold_daily.pkl"
df = utils.load_pickle(fname)
utils.standard_plot(df, column_name='Gold')

num_date = df.shape[0]
half_spread = 0.01
# days_holding = 4


def count_profitable_trade_date(days_holding):
    count = 0
    for idx in range(num_date-days_holding):
        curr_date = df.loc[idx]["Date"]
    #    print(curr_date)

        curr_price = df.loc[idx]["Gold"]
        buy_price_w_spread = curr_price * (1 + half_spread)

        sell_date = df.loc[idx+days_holding]["Date"]
        sell_date_price = df.loc[idx+days_holding]["Gold"]
        sell_price_w_spread = sell_date_price * (1 - half_spread)

        arbitrage = sell_price_w_spread - buy_price_w_spread
    #    print(arbitrage)

        if arbitrage >= 0:
            count += 1
            print("Buy Date: {} Arbitrage: {}".format(curr_date, arbitrage))
    print("Total Count: {}".format(count))
    return count


holding_days_list = [i for i in range(31, 61)]

holding_days_w_profitable_days_count = []

for holding_days in holding_days_list:
    count = count_profitable_trade_date(holding_days)
    holding_days_w_profitable_days_count.append((holding_days, count))

print(holding_days_w_profitable_days_count)


if __name__ == "__main__":
    pass
