from datetime import datetime
from pandas import Series,DataFrame
import pandas as pd
import numpy as np


# print(datetime.now())
date = datetime(2024,5,17)
# print(date.day)
# print(date.month)
# print(date.year)

instance = datetime(2024,1,2,9,45,34)
# print(instance.hour)
# print(instance.minute)
# print(instance.second)

# print(datetime.now() - datetime(1999,7,7))

date = datetime.now()

date_str = str(date)
# print(datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f"))

# range_data = pd.date_range('1/1/2024', '17/5,2024')
range_data = pd.date_range(end='1/1/2024 10:45:23', periods=10)
# print(range_data)

time = Series(np.random.randn(13),pd.date_range(datetime(2024,4,2),datetime(2024,4,14)))
date_str = time.index[3]
# print(time)
# print(time[date_str])
# print(time['4/7/2024':'4/11/2024'])
# print(time.truncate('4/11/2024'))

date_range = pd.date_range(start='1/1/2024',periods=20)
date_range = pd.date_range(start='1/1/2024 02:00:00',periods=20,freq='h')
date_range = pd.date_range(start='1/1/2024 02:00:00',periods=20,freq='9h34min')
date_range = pd.date_range(start='1/1/2024 02:00:00',periods=20,freq='D')
date_range = pd.date_range(start='1/1/2024 02:00:00',periods=20,freq='b')
# print(date_range)

ts = Series(np.random.randn(10), pd.date_range('1/1/2024',periods=10,freq='ME'))
# print(ts.shift(7))
# print(ts.shift(20,freq='D'))
# print(ts.shift(-10,freq='D'))
