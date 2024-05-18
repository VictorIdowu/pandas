import matplotlib.pyplot as plt
from datetime import datetime
from pandas import Series,DataFrame
import pandas as pd
import numpy as np

# plot = plt.plot([1,2,3,4,5])
# plt.xlabel('X axis')
# plt.ylabel('Y axis')
# print(plt.show())

months = ['Jan','Feb','Mar','April','May','June']
sales_2023 = [50000,90000,120000,140000,111000,150000]
sales_2024 = [60000,120000,130000,111000,150000,190000]
# sales_graph = plt.plot(months,sales_2023,sales_2024)
# plt.xlabel('Months')
# plt.ylabel('Sales in USD')
# plt.legend([2023,2024])


time = np.arange(0,10,0.2)
# plt.plot(time,time,'b--')
# plt.plot(time,time**2,'r^')
# plt.plot(time,time**3,'gs')

# plt.plot([1,2,3,4],[10,20,30,40],linewidth=4)
# line = plt.plot([1,2,3,4],[10,20,30,40])
# plt.setp(line,linewidth=4,color='r',linestyle='--')
# plt.show()

# fig = plt.figure()
# a = fig.add_subplot(2,2,1)
# b = fig.add_subplot(2,2,2)
# c = fig.add_subplot(2,2,3)
# d = fig.add_subplot(2,2,4)

# a.plot(months,sales_2023,sales_2024)
# a.legend([2023,2024])
# a.grid(True)
# a.text('Mar',100000,'Sales v/s Month')

# b.plot(time,time**3,'gs')
# b.plot(time,time,'b--')
# b.plot(time,time**2,'r^')

# c.plot([1,2,3,4],[10,20,30,40],linewidth=4)

# d.plot(time**4,time)

# plt.show()

# Creating a series
ser = Series(np.random.randn(10),np.arange(0,100,10))
# print(ser)
# ser.plot()
df = DataFrame(np.random.randn(10,4),columns=['a','b','c','d'],index=np.arange(10))
# print(df)
# df.plot(kind='bar')
df.plot(kind='barh')

plt.show()