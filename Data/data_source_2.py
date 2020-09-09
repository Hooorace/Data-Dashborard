# _*_ coding: utf-8 _*_

import pandas as pd
import numpy as np
import json

path_test = r"C:\Users\tyrel\Desktop\Galanz_Dashboard\Data\companyRank.csv"
path_cnPercent = r"C:\Users\tyrel\Desktop\Galanz_Dashboard\Data\cn_percent.csv"
path_geoCN = r"C:\Users\tyrel\Desktop\Galanz_Dashboard\Data\geo_countries.json"
path_geoUS = r"C:\Users\tyrel\Desktop\Galanz_Dashboard\Data\geo_US_counties.json"
path_unemp = r"C:\Users\tyrel\Desktop\Galanz_Dashboard\Data\fips-unemp-16.csv"

### Market Scale
#### Product
product = "微波炉"
#### Continent
continents = "北美洲"
#### Subcontinent
subcontinents = "北美"
#### Country
country = "美国"

### Period Scale
#### Year
year = 2019
last_year = year - 1
#### Beginning Month
beginning_month = 1
#### End Month
end_month = 12


def get_period(end_month):
    period_list = []
    for m in range(end_month):
        month_int = m + 1
        if month_int < 10:
            month = "0%d月"%month_int
        else:
            month = "%d月"%month_int
        month_string = "standard_month = \"%s\""%month
        period_list.append(month_string)
    period = "(" + " OR ".join(period_list) +  ")"
    return period

data_source = {}

# Read data
data_source["companyRank"] = pd.read_csv(path_test)

with open(path_geoCN) as f_geoCN:
    data_source["geoCN"] = json.load(f_geoCN)

data_source["cnPercent"] = pd.read_csv(path_cnPercent)
