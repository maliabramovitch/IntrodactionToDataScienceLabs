import pandas as pd
import numpy as np
import datetime
from calendar import monthrange
import matplotlib.pyplot as plt

""" Part 1 """
# 1
sfrain = pd.read_csv('SFWeather.csv', header=0, usecols=['DATE', 'PRCP'])
print(f'DATE type = {sfrain["DATE"].dtype}    PRCP type = {sfrain["PRCP"].dtype}')

# 2
l = lambda x: datetime.datetime.strptime(str(x), '%Y%m%d')
sfrain["DATE"] = sfrain["DATE"].apply(l)

# 3
sfrain.sort_values(["DATE"], inplace=True)

# 4
sfrain.set_index(["DATE"], inplace=True)

# 5
print(f"Number of rows in table = {sfrain.shape[0]}")

# 6
negative_values = sfrain[sfrain['PRCP'] < 0]
missing_meas_value = negative_values.iloc[0, 0]
print(f'The missing value is {missing_meas_value}')

# 7
sfrain.replace(missing_meas_value, np.nan, inplace=True)
sfrain.dropna(inplace=True)
print(f"Number of rows in table after dropna = {sfrain.shape[0]}")

""" Part 2 """
# 8
ndays = sfrain.groupby(sfrain.index.map(lambda x: datetime.datetime(x.year, x.month, 1))).count()

# 9
rainy_days = sfrain[sfrain["PRCP"] > 0]
nraindays = rainy_days.groupby(rainy_days.index.map(lambda x: datetime.datetime(x.year, x.month, 1))).count()
# 10
prcp = sfrain.groupby(sfrain.index.map(lambda x: datetime.datetime(x.year, x.month, 1))).sum()

# 11
sfrain_summary = pd.concat([ndays, nraindays, prcp], axis='columns')
sfrain_summary.columns = ['ndays', 'nraindays', 'prcp']

# 12
min_days = [monthrange(i.year, i.month)[1] * 0.9 for i in sfrain_summary.index]
above90 = sfrain_summary[sfrain_summary['ndays'] >= min_days]

# 13
daily_prcp = sfrain.groupby(sfrain.index.map(lambda x: datetime.datetime(x.year, x.month, 1))).mean()
sfrain_summary['daily_prcp'] = daily_prcp

""" Part 3 """
# 14
nrainmonth = sfrain.groupby(sfrain.index.map(lambda x: datetime.datetime(1, x.month, 1))).mean()
nrainmonth.plot(kind='bar')
plt.title('Number of Rainy Days Each Month')
plt.xticks(range(0, 12), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
           rotation=45)
plt.xlabel('Month')
plt.ylabel('Rainy Days')
plt.show()

# 15
"didnt know how to do"
