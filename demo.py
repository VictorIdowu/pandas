from pandas import Series,DataFrame
import numpy as np
s = Series([1,3,5,7,8])
# print(s.index)

s = Series([100,200,300], index=['a','b','c'])


series = Series({'a':100,'b':700,'c':1400})


s = Series([10,20,30,40,50,10,20,50])
# print(s.sum())
# print(s.product())
# print(s.mean())
# print(s.ndim)
# print(s.size)
# print(s.index)
# print(s.values)
# print(type(s.values))

# 
# DataFrame

people = {'name':['Jim', 'Rob', 'Tom'], 'age':[22,44,55], 'location':['NG', 'GH', 'KEN']}
df = DataFrame(people, columns=['name', 'location', 'age', 'salary'])
# print(df)

# print(df.location) # df['location'] works as well
# print(df.iloc[1])
# print(df.iloc[0:2])

salaries = Series([1000,2000,3000])
df['salary'] = salaries

del df['salary']

# print(df)


#///// Reindexing
s = Series([10,20,30,40,50], index=['c','a','d','b','e'])
# print(s)
# print(s.reindex(['a','b','c','d','e']))

# print(s.reindex(['a','b','c','d','e','f'], fill_value=0))

df = DataFrame(np.arange(9).reshape(3,3), index=['c','a','b'], columns=['apple','mango','banana'])


df = df.reindex(['a','b','c'])
# print(df.reindex(columns=['apple','banana','mango']))

# //////// Arithmetic Operation with Fill values
s1 = Series([1,2,3,4,5], index=['a','b','c','d','e'])
s2 = Series([1,2,3,4,5,6,7], index=['a','b','c','d','e','f','g'])

# print(s1 + s2)
# print(s1.add(s2, fill_value=0))

d1 = DataFrame(np.arange(12).reshape(3,4), columns=['a','b','c','d'])
d2 = DataFrame(np.arange(16).reshape(4,4), columns=['a','b','c','d'])
# print(d1.add(d2,fill_value=0))

# ///////// Adding Series and DataFrame
s = Series([1,2,3,4])
d = DataFrame(np.arange(8).reshape(2,4))
# print(s)
# print(d)
# print(d + s)

# /////// Function Application and Mapping
d = DataFrame(np.arange(16).reshape(4,4))
f = lambda x: x+10
f2 = lambda x: x*x
# print(d.apply(f2))

# //////// Sorting & Ranking
s = Series([10,20,30,40,50], index=['c','a','d','b','e'])
# print(s.sort_index())
df = DataFrame(np.arange(16).reshape(4,4), index=[3,4,1,2], columns=['c','a','d','b'])
# sort_df = df.sort_index(axis=1)
# print(sort_df.sort_index())

prices = Series([300,200,900,500])
# print(prices.sort_values(ascending=False))

products = DataFrame({'name':['phone','laptop','tablet'], 'price':[200,300,100]})
# print(products.sort_values(by='price'))

# ///// Duplicate Index Values
s = Series([1,2,3,4,5], index=['a','b','c','d','a'])
# print(s.index.is_unique)

# //////// Statistical Methods
products = DataFrame({'name':['phone','laptop','tablet'], 'price':[200,300,100]})
# print(products.sum())
# print(products.count())
# print(products.describe())

# //////// Nan Values
s = Series([1,2,3,np.nan,4,np.nan,5])
# print(s.dropna())

data = DataFrame([[1,2,3],[np.nan,np.nan,np.nan],[2,np.nan,4],[np.nan,3,np.nan]])
# print(data.dropna())
# print(data.dropna(how='all'))
# print(data.dropna(how='all',axis=1))
data[3]=np.nan
# print(data)
data = data.dropna(how='all',axis=1)
data = data.dropna(how='all')
data = data.fillna(0)
# print(data)

# ////// Hierarchical Indexing
s = Series([10,20,30,40])

s1 = Series(np.arange(10),index=[['a','a','b','b','b','c','c','d','e','e'],[1,2,1,2,3,1,2,1,1,2]])

# print(s1['b'][3]) # = 4
# print(s1.index)
# print(s1['c'])
# print(s1['a':'c'])
s1_df = s1.unstack() # Convert a 2-index Series to a DataFrame
# print(s1_df)

data_frame = DataFrame(np.arange(15).reshape(5,3),index=['a','b','c','d','e'])
df_s = data_frame.stack() # Convert DataFrame to 2-index Series
# print(df_s)

# ///////////////////////////////////////////////////////////
# /////DRIVING DEEPER///////////////////
s = Series(data=['Laptop','Phone','Computer','Tablet'], index=[1001,1002,1003,1004])
print(s)