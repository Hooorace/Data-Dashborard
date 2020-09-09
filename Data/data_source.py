# _*_ coding: utf-8 _*_

import json
import pandas as pd

"""Primary Data"""
### Market Scale
#### Product
product = "微波炉"
#### Continent
continents = "北美洲"
#### Subcontinent
subcontinents = "北美"
#### Country
country = ["United States of America"]
### Company
company = ["格兰仕"]
### Least price
bottom_price = 20

### Period Scale
#### Year
year = 2019
last_year = year - 1
#### Beginning Month
beginning_month = 1
#### End Month
end_month = 12

indicator = "vol"


""""Period"""
period = []
for m in range(beginning_month, end_month+1):
    if m < 10:
        month = "0%d月"%m
    else:
        month = "%d月"%m
    period.append(month)


"""Data Source Dictionary"""
data_source = {}

# Category and Products
data_source["product"] = product

# Market Scale
data_source["continents"] = continents
data_source["subcontinents"] = subcontinents
data_source["country"] = country
data_source["company"] = company

# Time and Period
data_source["year"] = "{}年".format(year)
data_source["last_year"] = "{}年".format(last_year)
data_source["period"] = period

path_cnPercent =  r"C:\Users\tyrel\Desktop\Galanz_Dashboard\Data\cn_percent.csv"
path_geoCN = r"C:\Users\tyrel\Desktop\Galanz_Dashboard\Data\geo_countries.json"
with open(path_geoCN) as f_geoCN:
    data_source["geoCN"] = json.load(f_geoCN)

data_source["indicator"] = indicator
data_source["bottom_price"] = bottom_price
