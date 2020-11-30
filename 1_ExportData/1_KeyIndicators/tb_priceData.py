# _*_ coding: utf-8 _*_

import plotly.express as px
import plotly.graph_objects as go
import dash_core_components as dcc
import pandas as pd

def tb_priceData(data_source):

    df_views = data_source["df_views"]

    period = data_source["period"]
    country = data_source["country"]
    company = data_source["company"]

    year = data_source["year"]
    last_year = data_source["last_year"]

    price_data = {}

    volume = df_views[(df_views["yr"] == year) & (df_views["month"].isin(period)) & (df_views["cn"].isin(country))]["vol"].sum()
    value = df_views[(df_views["yr"] == year) & (df_views["month"].isin(period)) & (df_views["cn"].isin(country))]["val"].sum()
    price = round(value/volume, 2)


    volume_company = df_views[(df_views["yr"] == year) & (df_views["month"].isin(period)) & (df_views["cn"].isin(country)) & (df_views["company"].isin(company))]["vol"].sum()
    value_company = df_views[(df_views["yr"] == year) & (df_views["month"].isin(period)) & (df_views["cn"].isin(country)) & (df_views["company"].isin(company))]["val"].sum()
    price_company = round(value_company/volume_company, 2)


    volume_company_lastYear = df_views[(df_views["company"].isin(company)) & (df_views["yr"] == last_year) & (df_views["month"].isin(period)) & (df_views["cn"].isin(country))]["vol"].sum()

    value_company_lastYear = df_views[(df_views["company"].isin(company)) & (df_views["yr"] == last_year) & (df_views["month"].isin(period)) & (df_views["cn"].isin(country))]["val"].sum()

    price_company_lastYear = round(value_company_lastYear/volume_company_lastYear, 2)

    differenceOfAverage = round(price_company - price, 2)
    price_YoY = round(price_company - price_company_lastYear, 2)

    price_data["price"] = "${price_company}".format(price_company = price_company)
    price_data["price_diff"] = differenceOfAverage
    price_data["price_YoY"] = price_YoY

    return price_data
