# _*_ coding: utf-8 _*_
import dash_core_components as dcc
import pandas as pd

# product
def dd_product(data_source):

    product_list = data_source["product_list"]

    dropDown = dcc.Dropdown(
        id = "product",
        options = ([{'label': i, 'value': i} for i in product_list]),
        value = "microwave")

    return dropDown


# Year
def dd_year(data_source):

    df_views = data_source["df_views"]
    year_list = list(df_views["yr"].unique())

    component = dcc.Dropdown(
        id = "year",
        options = [{'label': i, 'value': i} for i in year_list],
        value = '2019年')

    return component


# company
def rs_month(data_source):

    company_list = data_source["company_list"]

    rangeSlider = dcc.RangeSlider(
        id = "month",
        min = 1,
        max = 12,
        step = 1,
        value = [1, 12],
        marks={
            1: 'Jan', 2: 'Feb', 3: 'Mar',
            4: 'Apr', 5: 'May', 6: 'Jun',
            7: 'Jul', 8: 'Aug', 9: 'Sep',
            10: 'Oct', 11: 'Nov', 12: 'Dec',
        })

    return rangeSlider


# Country
def dd_country(data_source):

    cn_list = data_source["cn_list"]

    dropDown = dcc.Dropdown(
        id = "country",
        options = ([{'label': "All Countries", 'value': "All"}] + [{'label': i, 'value': i} for i in cn_list]),
        value = 'All')

    return dropDown


# company
def dd_company(data_source):

    company_list = data_source["company_list"]

    dropDown = dcc.Dropdown(
        id = "company",
        options = ([{'label': "All Companies", 'value': "All"}] + [{'label': i, 'value': i} for i in company_list]),
        value = "All")

    return dropDown


# Indicators
def dd_indicator():

    dropDown = dcc.RadioItems(
        id = "indicator",
        options = [{'label': i, 'value': i} for i in ["vol", "val"]],
        value = 'vol',
        labelStyle = {"display": "inline-block"})

    return dropDown
