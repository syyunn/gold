import utils
import matplotlib.pyplot as plt

# fname = "data/gold_daily_normal_cpi_monthly.pkl"
# df_gold_daily = utils.load_pickle(fname)
# utils.standard_plot(df_gold_daily, column_name='Gold_Normal')

data = [(1, 404), (2, 793), (3, 1164), (4, 1474), (5, 1756), (6, 1977), (7, 2183), (8, 2343), (9, 2514), (10, 2614), (11, 2694), (12, 2823), (13, 2955), (14, 2997), (15, 3080), (16, 3156), (17, 3182), (18, 3266), (19, 3287), (20, 3337), (21, 3375), (22, 3425), (23, 3445), (24, 3469), (25, 3489), (26, 3538), (27, 3565), (28, 3593), (29, 3616), (30, 3663), (31, 3673), (32, 3703), (33, 3744), (34, 3772), (35, 3798), (36, 3810), (37, 3844), (38, 3842), (39, 3853), (40, 3890), (41, 3906), (42, 3927), (43, 3951), (44, 3951), (45, 3978), (46, 4002), (47, 4015), (48, 3999), (49, 3998), (50, 4010), (51, 4024), (52, 4038), (53, 4067), (54, 4089), (55, 4073), (56, 4050), (57, 4064), (58, 4094), (59, 4117), (60, 4115)]


dates = []
counts = []
for datum in data:
    dates.append(datum[0])
    counts.append(datum[1])

plt.plot(dates,counts)
plt.show()

if __name__ == "__main__":
    pass
