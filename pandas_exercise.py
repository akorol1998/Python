import numpy as np
import pandas as pd

df = pd.read_csv("Automobile_data.csv", na_values={
	'price':['?', 'n.a'],
	'stroke':['?', 'n.a'],
	'horsepower':['?', 'n.a'],
	'peak-rpm':['?', 'n.a'],
	'average-mileage':['?', 'n.a']
	})

# 1 From given data set print first and last five rows
print(df.head(), df.tail())

# 2 Clean data and update the CSV file
# print(df.head(30))
# df.replace({'?':'Nan', 'n.a': 'Nan'}, inplace=True)
# print(df.head(30))

# 3 Print most expensive car’s company name and price.

max_car_price_company = df[[ 'company', 'price']][df.price==df['price'].max()]
print(max_car_price_company)

# 4 Print All Toyota Cars details

toyota_details = df[:][df.company=="toyota"]
# Or
company_grouped = df.groupby("company")
toyota_details = company_grouped.get_group('toyota')
print(toyota_details)