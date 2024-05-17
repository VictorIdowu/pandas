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
# print(pd.merge(df1,df2,how='right'))

prices = DataFrame({'productid':[1001,1002,1003,1004],'name':['phone','book','computer','microwave'],'prices':[100,200,300,400]})
categories = DataFrame({'productid':[1001,1002,1003,1004],'name':['phone','book','computer','microwave'],'categories':['electronics','education','electronics','appliances']})
# print(prices)
# print(categories)
# print(pd.merge(prices,categories,on='name'))

df_names = DataFrame({'Product Name':['Laptop','Mouse','Keyboard','Monitor']},['P1','P2','P3','P4'])
df_prices = DataFrame({'Price':[1200,25,80,250], 'ProductID':['P1','P2','P3','P4']})

# print(pd.merge(df_names,df_prices,left_index=True,right_on='ProductID'))

df_names = DataFrame({'Product Name':['Laptop','Mouse','Keyboard','Monitor'], 'ProductID':['P1','P2','P3','P4']})
df_prices = DataFrame({'Price':[1200,25,80,250]},['P1','P2','P3','P4'])
# print(pd.merge(df_names,df_prices,right_index=True,left_on='ProductID'))

df_names = DataFrame({'Product Name':['Laptop','Mouse','Keyboard','Monitor']},['P1','P2','P3','P4'])
df_prices = DataFrame({'Price':[1200,25,80,250]},['P1','P2','P3','P4'])
# print(pd.merge(df_names,df_prices,right_index=True,left_index=True))

phy_products = DataFrame({'name':['Phone','Laptop','Tablet'],'prices':[100,200,300]})
dig_products = DataFrame({'name':['Yoga for Beginners','The Calm Mind'],'prices':[500,600]})

products = pd.concat([phy_products,dig_products],keys=['Physical','Digital'])
# print(products.loc['Digital'])

temp1 = Series([14,np.nan,23,45,np.nan],index=['New York','London','Chicago','Berlin','Dallas'])
temp2 = Series([12,16,20,42,45],index=['New York','London','Chicago','Berlin','Dallas'])

# print(temp1.combine_first(temp2))

data1 = {
  'Cities':['New York','London','Chicago','Berlin','Dallas'],
  'Temperature':[14,np.nan,23,45,np.nan],
  'Precipitation':[0.1,np.nan,5.4,2.3,5.5]
}
data2 = {
  'Cities':['New York','London','Chicago','Berlin','Dallas'],
  'Temperature':[12,16,20,42,45],
  'Precipitation':[0.1,0.5,5.4,2.3,np.nan]
}

df1 = DataFrame(data1)
df2 = DataFrame(data2)
# print(df1.combine_first(df2))