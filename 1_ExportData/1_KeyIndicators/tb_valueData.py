# _*_ coding: utf-8 _*_

import plotly.express as px
import plotly.graph_objects as go
import dash_core_components as dcc
import pandas as pd

def tb_valueData(data_source):

    df_views = data_source["df_views"]

    period = data_source["period"]
    country = data_source["country"]
    company = data_source["company"]

    year = data_source["year"]
    last_year = data_source["last_year"]

    val_data = {}

    value = df_views[(df_views["yr"] == year) & (df_views["month"].isin(period)) & (df_views["cn"].isin(country))]["val"].sum()

    value_company = df_views[(df_views["yr"] == year) & (df_views["month"].isin(period)) & (df_views["cn"].isin(country)) & (df_views["company"].isin(company))]["val"].sum()

    value_company_lastYear = df_views[(df_views["company"].isin(company)) & (df_views["yr"] == last_year) & (df_views["month"].isin(period)) & (df_views["cn"].isin(country))]["val"].sum()


    value_share = round((value_company/value) * 100, 2)
    print(value_share)
    value_YoY = round((value_company/value_company_lastYear-1) * 100, 2)
    print(value_YoY)

    val_data["value"] = "{}M".format(round(value_company/1000000, 2))
    val_data["value_share"] = value_share
    val_data["value_YoY"] = value_YoY

    return val_data
