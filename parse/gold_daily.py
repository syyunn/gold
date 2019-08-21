import utils

fname = "../raw/gold_daily.csv"
f = open(fname, 'r')

dates = []
golds = []

for line in f.readlines():
    content = line.split(',')
    idx = content[0]
    if len(idx) == 0:
        continue
    date = content[1]
    gold = float(content[2])

    dates.append(date)
    golds.append(gold)

df = utils.make_as_pandas_df(dates, content_name='Gold', content_list=golds)

utils.standard_plot(df)

utils.pickle_object(df, "../data/gold_daily.pkl")


if __name__ == "__main__":
    pass
