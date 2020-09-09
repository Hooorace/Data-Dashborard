# _*_ coding: utf-8 _*_

import plotly.express as px
import plotly.graph_objects as go
import dash_core_components as dcc
import pandas as pd

def tb_volumeData(data_source):

    db_connection = data_source["db_connection"]

    df_views = data_source["df_views"]

    period = data_source["period"]
    product = data_source["product"]
    continents = data_source["continents"]
    subcontinents = data_source["subcontinents"]
    country = data_source["country"]
    company = data_source["company"]

    year = data_source["year"]
    last_year = data_source["last_year"]

    vol_data = {}

    volume = df_views[(df_views["yr"] == year) & (df_views["month"].isin(period)) & (df_views["cn"].isin(country))]["vol"].sum()

    volume_company = df_views[(df_views["yr"] == year) & (df_views["month"].isin(period)) & (df_views["cn"].isin(country)) & (df_views["company"].isin(company))]["vol"].sum()

    volume_company_lastYear = df_views[(df_views["company"].isin(company)) & (df_views["yr"] == last_year) & (df_views["month"].isin(period)) & (df_views["cn"].isin(country))]["vol"].sum()


    volume_share = round(volume_company/volume * 100, 2)
    volume_YoY = round((volume_company/volume_company_lastYear-1) * 100, 2)

    vol_data["volume"] = "{}M".format(round(volume_company/1000000, 2))
    vol_data["volume_share"] = volume_share
    vol_data["volume_YoY"] = volume_YoY

    return vol_data
