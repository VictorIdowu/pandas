from pandas import Series,DataFrame
import pandas as pd
import numpy as np

data = pd.read_csv('happiness_report.csv')
# print(data)

# print(data.index.get_level_values('Year'))
# print(data.loc['Nigeria', 2010])
# print(data.loc[('Nigeria', 2010):('Nigeria', 2021)])

# data = data.set_index(['Country Name'])

data = data.set_index(['Country Name','Year'])
data = data.stack()
# print(data['Nigeria',2008,'Generosity'])

# print(data.unstack())
# print(data.unstack(level=1))


data = pd.read_csv('happiness_report.csv')

# print(data.pivot(index='Year',columns='Country Name'))
# print(data.pivot(index=['Country Name','Year'],columns=[]))
# print(data.pivot(index='Country Name',columns='Year',values=['Generosity', 'Social Support']))

# print(data.melt(id_va

# print(data.pivot_table(values="Generosity",index="Country Name",aggfunc="sum"))
# print(data.pivot_table(values=["Generosity","Social Support","Life Ladder"],index=["Country Name","Year"]))

countries = data.groupby("Country Name")

# print(len(countries))
# print(countries.get_group("Nigeria"))
# print(countries.get_group("Nigeria").max())
# print(countries.get_group("Nigeria").min())
# print(countries.max())

# print(countries["Generosity"].mean().sort_values(ascending=False))
# print(countries["Log GDP Per Capita"].mean().sort_values(ascending=False).head(50))

df1 = DataFrame({'fruit':['apple','orange','banana','peach'],'prices 2023':[10,20,30,40]})

df2 = DataFrame({'fruit':['apple','orange','mango'],'prices 2024':[12,33,35]})

# print(pd.merge(df1,df2,how='outer'))
# print(pd.merge(df1,df2,how='left'))
print(pd.merge(df1,df2,how='right'))