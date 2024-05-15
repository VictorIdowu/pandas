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
# print(res.value_counts())

# //// Map Method
stock_symbols = {"Acme Corp":"ACMC","Anton Computers":"ANT","Maximo Construction":"MCX"}
stock_prices = {"ACMC":29,"MCX":15,"ANT":48}

symbol_series = Series(stock_symbols)
prices_series = Series(stock_prices)

# print(symbol_series.map(prices_series))

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

data = pd.read_csv('data_cleaned_2021.csv')

data.set_index('index', inplace=True)
data.index.name = "Job ID"
# print(data.head(10))
# print(data.tail())
# print(data.axes)
# print(data.info())
# print(data['Salary Estimate'])
# print(data.Location)
# print(data.size)

new_data = data[['Job Title','Salary Estimate','Company Name','Location','Size']]
# print(new_data)

# print(data[['Job Title','Lower Salary', 'Upper Salary', 'Avg Salary(K)']])

def parse_salary(salary_str):
  if ':' in salary_str:
    salary_range = salary_str.split(':')[1].strip()
  
  salary_range = salary_str.split(' ')[0]
  if "-" in salary_range:
    min_salary,max_salary = salary_range.split('-')
  else:
    min_salary = max_salary = salary_range
  
  def clean_and_convert(salary):
    try:
      return float(salary.replace('$', '').split('K')[0]) *1000
    except ValueError:
      return 0
  
  min_salary = clean_and_convert(min_salary)
  max_salary = clean_and_convert(max_salary)

  avg_salary = (min_salary + max_salary)/2

  return Series([min_salary,max_salary,avg_salary])

# for salary_str in data['Salary Estimate']:
#   print(parse_salary(salary_str))

data[['Min Salary','Max Salary','Avg Salary']] = data['Salary Estimate'].apply(parse_salary)
# print(data[['Min Salary','Max Salary','Avg Salary']])

# print(data['Job Title'].value_counts())

data['Max Salary'] = data['Max Salary'].astype('int')
data['Min Salary'] = data['Min Salary'].astype('int')
data['Avg Salary'] = data['Avg Salary'].astype('int')

# print(data['Min Salary'].dtype)
# print(data['Max Salary'].dtype)
# print(data['Avg Salary'].dtype)

# print(data.sort_values("Avg Salary", ascending=False))
# print(data.sort_values(["Rating","Max Salary"], ascending=False)[["Max Salary","Rating"]].head(30))

# Filter/////
# print(data[data['Job Title'] == 'Data Scientist'])
# print(data[data['Max Salary'] > 100000]) 
# print(data[data['Founded'] > 2015]) 
# print(data[data['Rating'] >= 4]) 
# print(data[(data['Job Title'] == 'Data Scientist') & (data['Max Salary'] > 100000) & (data['Rating'] >= 4)]) 
# print(data[(data['Max Salary'] > 100000) | (data['Rating'] > 4.5)]) 

# print(data[data['Job Title'].isin(['Data Scientist'])])
# print(data[data['Avg Salary'].between(100000,150000)])

data_copy = data.set_index('Job Title')
# print(data_copy.loc['Data Scientist'])

data['Job Title'] = data['Job Title'].replace("Data Scientist", "Data Specialist")
# print(data[data['Job Title'] == 'Data Specialist'])
# print(data.columns)
data = data.drop(columns = ['Python',
       'spark', 'aws', 'excel', 'sql', 'sas', 'keras', 'pytorch', 'scikit',
       'tensor', 'hadoop', 'tableau', 'bi', 'flink', 'mongo', 'google_an'])
# print(data.columns)

data = data.drop(index=[0])
# print(data)

hqs = data.pop('Headquarters')
# print(hqs)
# print(data.columns)

del data['Degree']
# print(data.columns)