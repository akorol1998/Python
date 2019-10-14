import numpy as np
import pandas as pd

# df = pd.read_csv("Automobile_data.csv", na_values={
# 	'price':['?', 'n.a'],
# 	'stroke':['?', 'n.a'],
# 	'horsepower':['?', 'n.a'],
# 	'peak-rpm':['?', 'n.a'],
# 	'average-mileage':['?', 'n.a']
# 	})

# # 1 From given data set print first and last five rows
# print(df.head(), df.tail())

# # 2 Clean data and update the CSV file
# # print(df.head(30))
# # df.replace({'?':'Nan', 'n.a': 'Nan'}, inplace=True)
# # print(df.head(30))

# # 3 Print most expensive car’s company name and price.

# max_car_price_company = df[[ 'company', 'price']][df.price==df['price'].max()]
# print(max_car_price_company)

# # 4 Print All Toyota Cars details

# toyota_details = df[:][df.company=="toyota"]
# # Or
# company_grouped = df.groupby("company")
# toyota_details = company_grouped.get_group('toyota')
# print(toyota_details)

# 5 Count total cars per company

# print(df['num-of-cylinders'].value_counts())
# print(df['company'].value_counts())

# 6 Print the most expensive car in each company

# group = df.groupby("company")
# res = group[["company", 'price']].max()
# print(res)

# 7 Print the average price
# group = df.groupby("company")
# res = group[['company', 'price']].mean()
# print(res)


# 8 Sort all cars by their price
# s_arr = df.sort_values(by=['price'], ascending=False)
# print(s_arr.head())

# 9 Concatenate two data frames (two dicts) and set keys

# german = {"Company":["Ford", "Mercedes", "Bmw", "Bentley"], "Price":[23845, 171995, 135925 , 71400]}
# japan = {"Company":["Honda", "Nissan", "Mitsubishi", "Hiroshima"], "Price":[245, 175, 135 , 23]}

# df1 = pd.DataFrame.from_dict(german)
# df2 = pd.DataFrame.from_dict(japan)

# df3 = pd.concat([df1, df2], keys=["Germany", "Japan"], )
# print(df3)

# 10 Concatenate two data frames (two dicts) , but from the second dataframe add only 'horsepower' column

Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
Car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}

df1 = pd.DataFrame.from_dict(Car_Price)
df2 = pd.DataFrame.from_dict(Car_Horsepower)

df3 = df1.merge(df2, on='Company')
print(df3)
