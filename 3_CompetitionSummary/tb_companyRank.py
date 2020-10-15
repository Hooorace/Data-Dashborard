# _*_ coding: utf-8 _*_

import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import dash_table
import pandas as pd


def tb_companyRank(data_source):

    db_connection = data_source["db_connection"]

    df_views = data_source["df_views"]

    period = data_source["period"]
    product = data_source["product"]
    continents = data_source["continents"]
    subcontinents = data_source["subcontinents"]
    country = data_source["country"]
    company = data_source["company"]

    indicator = data_source["indicator"]

    year = data_source["year"]
    last_year = data_source["last_year"]

    current_year = year.replace("年", "")
    previous_year = last_year.replace("年", "")

    # Current Data
    df_current_data = df_views[(df_views["yr"] == year) & (df_views["month"].isin(period)) & (df_views["cn"].isin(country))][["company", indicator]].groupby("company").sum().sort_values(by = indicator, ascending = False)

    df_current_data["{year}%".format(year = current_year)] = round(df_current_data[indicator]/sum(df_current_data[indicator]) * 100, 2)

    df_current_data = df_current_data.rename(columns = {indicator: current_year})


    # Last Year's Data
    df_last_data = df_views[(df_views["yr"] == last_year) & (df_views["month"].isin(period)) & (df_views["cn"].isin(country))][["company", indicator]].groupby("company").sum().sort_values(by = indicator, ascending = False)

    df_last_data["{last_year}%".format(last_year = previous_year)] = round(df_last_data[indicator]/sum(df_last_data[indicator]) * 100, 2)

    df_last_data = df_last_data.rename(columns = {indicator: previous_year})

    df_concat = pd.concat([df_current_data, df_last_data],
                      axis = 1,
                      join = "outer",
                      sort = False).sort_values(by = current_year, ascending = False)

    df_concat["YoY"] = round((df_concat[current_year]/df_concat[previous_year] - 1) * 100, 2)

    df_final = df_concat.head(10).reset_index()
    df_final= df_final.rename(columns = {"index": "Company"})


    table = dash_table.DataTable(
        id = 'table',
        columns = [{"name": i, "id": i} for i in df_final.columns],
        data = df_final.to_dict("records"),
        page_size = 10,
        fixed_rows = {"headers": True},

        style_table = {
            'height': '380px',
            'width': '90%',
        },

        style_cell = {
            'width': "{}%".format(len(df_final.columns)),
            "textOverflow": "ellipsis",
            "overflow": "hidden",
        },

        style_header = {
            'height': '40px',
            "textAlign": "center",
            "fontWeight": "bold",
            "fontFamily": "Arial",
            "fontSize": "18px",
            "color": 'rgba(255, 255, 255, 0.8)',
            "backgroundColor": 'rgba(112, 112, 112, 0.8)',
            'border': '1px solid rgba(255, 255, 255, 0)',
        },

        style_data = {
            "textAlign": "center",
            "fontFamily": "Arial",
            "fontSize": "16px",
            "color": 'rgba(112, 112, 112, 1)',
            "backgroundColor": 'rgba(112, 112, 112, 0)',
            'border': '1px solid rgba(202, 202, 202, 0.5)',
        },

        style_data_conditional = [
            {
                'if': {'column_id': 'Company'},
                'textAlign': 'center',
                "fontFamily": "微软雅黑",
            },

            {
                'if': {
                    'filter_query': '{Company} contains "格兰仕"'},
                'color': 'white',
                'backgroundColor': 'rgba(180, 0, 13, 0.6)',
                'fontWeight': 'bold',
            },
        ],

        style_as_list_view = True,
    )


    return table
