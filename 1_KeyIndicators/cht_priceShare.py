# _*_ coding: utf-8 _*_

import plotly.express as px
import plotly.graph_objects as go
import dash_core_components as dcc
import pandas as pd
from sqlalchemy import text

def cht_priceShare(data_source):

    df_views = data_source["df_views"]

    period = data_source["period"]
    country = data_source["country"]
    company = data_source["company"]

    year = data_source["year"]
    last_year = data_source["last_year"]

    bottom_price = data_source["bottom_price"]

    bins = [-float("inf"), 20, 24, 28, 30, 32, 35, 40, 50, 70, 100, float("inf")]

    top_labels = [
        '<20',
        '20-24',
        '24-28',
        '28-30',
        '30-32',
        '32-35',
        '35-40',
        '40-50',
        '50-70',
        '70-100',
        '>=100'
        ]

    df_priceSection = df_views[(df_views["month"].isin(period)) & (df_views["cn"].isin(country)) & (df_views["company"].isin(company))]

    df_priceSection["price"] = round(df_priceSection["val"]/df_priceSection["vol"], 2)

    df_priceSection = df_priceSection[["yr", "vol", "price"]][df_priceSection["price"] >= bottom_price]

    df_priceSection["priceSection"] = pd.cut(df_priceSection["price"],
                                         bins,
                                         labels = top_labels, right = False)

    pivoted = df_priceSection.pivot_table("vol", index = "priceSection", columns = "yr")

    df_sorted = pivoted.sort_index()

    df_final = (df_sorted/df_sorted.sum()).round(4) * 100

    colors = {
        '20-24': 'rgba(114, 0, 9, 0.7)',
        '24-28': 'rgba(180, 0, 13, 0.7)',
        '28-30': 'rgba(229, 1, 18, 0.7)',
        '30-32': 'rgba(254, 88, 100, 0.7)',
        '32-35': 'rgba(255, 143, 152, 0.7)',
        '35-40': 'rgba(255, 193, 197, 0.7)',
        '40-50': 'rgba(217, 217, 217, 0.7)',
        '50-70': 'rgba(172, 168, 168, 0.7)',
        '70-100': 'rgba(118, 113, 113, 0.7)',
        '>=100': 'rgba(59, 56, 56, 0.7)'
    }

    y_data = df_final.columns.values.tolist()
    x_data = df_final.values
    sectionList = df_final.index.values.tolist()

    fig = go.Figure()

    for i in range(len(x_data)):
        fig.add_trace(go.Bar(
            x = x_data[i],
            y = y_data,
            name = sectionList[i],
            orientation = "h",
            marker = dict(
                color = colors[sectionList[i]],
                line = dict(color = 'rgba(202, 202, 202, 0.5)', width = 3)
        )))

    fig.update_layout(

        xaxis = dict(
            showline = False,
            showticklabels = False,
            title_standoff = 25
        ),

        yaxis = dict(
            # Title
            title_text = "Year",
            title_font = dict(family='Arial Black',
                            size= 18,
                            color='rgba(255, 255, 255, 0.8)'),
            # Ticks
            showticklabels = True,
            tickfont = dict(family = 'Microsoft YaHei UI',
                            size = 16,
                            color ='rgba(255, 255, 255, 0.8)',
                            ),
            title_standoff = 25
        ),

        legend = dict(
            title_font_family="Microsoft YaHei UI",
            title_font_color = 'rgba(255, 255, 255, 0.8)',
            orientation = "h",
            x = 0,
            y = - 0.05,
            xanchor = "left",
            yanchor = "top",
            bgcolor = 'rgba(0, 0, 0, 0)',
            font = dict(family='Arial',
                        size= 14,
                        color='rgba(202, 202, 202, 0.8)'),
        ),

        barmode = 'relative',
        paper_bgcolor = 'rgba(255, 255, 255, 0)',
        plot_bgcolor = 'rgba(255, 255, 255, 0)',
        margin = dict(l = 20, r = 20, t = 60, b = 10),
        showlegend = False,
        height = 280
    )

    annotations = []
    title = "Share of Different Price Section"

    # Title
    annotations.append(dict(
        xref = 'paper',
        yref = 'paper',
        x = 0,
        y = 1.15,
        xanchor = 'left',
        yanchor = 'middle',
        text = title,
        font = dict(family='Arial Black', size= 20, color='rgba(255, 255, 255, 0.8)'),
        showarrow = False
    ))

    fig.update_layout(annotations = annotations)

    bar = dcc.Graph(figure = fig)

    return bar
