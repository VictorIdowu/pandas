from pandas import Series,DataFrame
import pandas as pd
import numpy as np

# with open('fruit_prices.csv', 'r') as file:
#   content = file.read()

fruit_prices = pd.read_csv('fruit_prices.csv')
# print(fruit_prices.stack())
fruit_names = pd.read_csv('fruit_prices.csv', usecols=['Fruit']).squeeze('columns')
fruit_prices = pd.read_csv('fruit_prices.csv', usecols=['RetailPrice']).squeeze('columns')
# print(fruit_prices)
# print(list(fruit_prices))

fruit_list = list(fruit_names)
for i,fruit in enumerate(fruit_list):
  # print(f'({i+1}):-{fruit}')
  pass

fruit_dict = dict(fruit_names)
# print(fruit_dict[18])

# print(type(fruit_list))

# print(sorted(fruit_prices))
# print('Apples' in fruit_names.values)

# Indexing and Slicing
s = Series([10,20,30,40], index=['a','b','c','d'])

# Label Indexing: Accessing an element using the index label
# print(s['d'])

# Label Slicing: Slicing using index label
# print(s['a':'c'])

# Integer Indexing: Accessing a value using its integer index
# print(s.iloc[1])

# Integer Slicing: Slicing using integer index
# print(s[0:4])


# loc & iloc indexing

# loc: is used for label based indexing where you use the index labels to select data
# print(s.loc['c'])

# iloc: is integer position based indexing where we use integer indexes to select data 
# print(s.iloc[3])

# Boolean indexing 'Indexing based on condition'
# print(s[s>20])

# //
# print(s[['a','c','d']])
# print(s.iloc[[0,2]])

# //// Get Method
# print(fruit_names.get(100, 'Fruit doesn\'t exist'))

# Altering Series ////
fruit_names[0] = 'Oranges'
fruit_names.iloc[0] = 'Pears'

fruit_names[[1,2,3]] = ['Peach', 'Pineapple', 'Watermelon']
# print(fruit_names)


s = Series([10,20,30,40],['apple','banana','cherry','date'])
s.loc['cherry'] = 90
s.loc[['apple', 'date']] = [100,300]
# print(s)

# Value count method
# print(fruit_names.value_counts())

prices = Series([100,200,300,400,500])

def summer_discount(x):
  return x - (x*0.1)

# print(prices.apply(summer_discount))

scores = Series([56,78,34,98,23,43,59])

def pass_or_fail(num):
  if num >= 40:
    return 'Pass'
  else:
    return 'Fail'

res = scores.apply(pass_or_fail)
print(res.value_counts())