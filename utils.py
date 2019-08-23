import pickle

import matplotlib.pyplot as plt
import pandas as pd

import numpy as np


def pickle_object(python_obj, pickle_path):
    with open(pickle_path, 'wb') as f:
        pickle.dump(python_obj, f)
    return True


def load_pickle(pickle_path):
    with open(pickle_path, 'rb') as f:
        python_obj = pickle.load(f)
    return python_obj


def standard_plot(pd_dataframe,
                  column_name='Gold',
                  scatter=False):
    # print(pd_dataframe['Date'])
    plt.figure(figsize=(12, 6), dpi=100)
    if not scatter:
        plt.plot(pd_dataframe['Date'],
                 pd_dataframe[column_name])
    if scatter:
        plt.scatter(pd_dataframe['Date'],
                    pd_dataframe[column_name])
    plt.xlabel('Date')
    plt.ylabel(column_name)
    plt.grid()
    plt.show()


def concat_two_dfs(df_list):
    df = pd.concat(df_list,
                   axis=0)
    df = df.reset_index(drop=True)
    return df


def concat_n_dfs(df_list):
    if len(df_list) == 2:
        return concat_two_dfs(df_list)
    else:
        df_0_1 = df_list[0:2]
        df_cat = concat_two_dfs(df_0_1)
        for df_follow in df_list[2:]:
            df_cat = concat_two_dfs([df_cat, df_follow])
        return df_cat


def make_as_pandas_df(dates_list, content_name, content_list):

    data_dict = {'Date': np.array(dates_list, dtype='datetime64[D]'),
                 content_name: np.array(content_list, dtype='float64')}

    df = pd.DataFrame(data_dict)

    return df


if __name__ == "__main__":
    data = load_pickle("KRW_USD_2017.pkl")
    print(data)