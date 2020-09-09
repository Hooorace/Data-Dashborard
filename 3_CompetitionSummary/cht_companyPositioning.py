# _*_ coding: utf-8 _*_

import plotly.graph_objects as go
import dash_core_components as dcc
import pandas as pd
from sqlalchemy import text

def cht_companyPositioning(data_source):

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


    df_primary = df_views[(df_views["yr"] == year) & (df_views["month"].isin(period)) & (df_views["cn"].isin(country))][["company", "vol", "val"]].groupby("company").sum()
    df_primary["price"] = round(df_primary["val"] / df_primary["vol"], 2)

    df_final = df_primary[(df_primary["price"] <= 260) & (df_primary["vol"] >= 1000)].sort_values(by = "vol", ascending = False).head(100)


    x = df_final["vol"].values.tolist()
    y = df_final["price"].values.tolist()
    text = df_final.index.tolist()
    size = df_final["val"].values.tolist()
    sizeref = 2.* max(size)/(100.**2)


    fig = go.Figure(data = [
        go.Scatter(
            x = x,
            y = y,
            text = text,
            mode = "markers",
            marker = dict(
                opacity = 0.6,
                size = size,
                sizemode = "area",
                sizeref = sizeref,
                sizemin = 5,
                showscale = True,
                color = x,
                colorscale=[
                    # Let first 10% (0.1) of the values have color rgb(0, 0, 0)
                    [0, 'rgba(202, 202, 202, 0.7)'],
                    [0.2, 'rgba(255, 143, 152, 0.7)'],

                    # Let values between 10-20% of the min and max of z
                    # have color rgb(20, 20, 20)
                    [0.2, 'rgba(255, 143, 152, 0.7)'],
                    [0.4, 'rgba(254, 88, 100, 0.7)'],

                    # Values between 20-30% of the min and max of z
                    # have color rgb(40, 40, 40)
                    [0.4, 'rgba(254, 88, 100, 0.7)'],
                    [0.6, 'rgba(229, 1, 18, 0.7)'],

                    [0.6, 'rgba(229, 1, 18, 0.7)'],
                    [0.8, 'rgba(114, 0, 9, 0.7)'],

                    [0.8, 'rgba(114, 0, 9, 0.7)'],
                    [1.0, 'rgba(114, 0, 9, 0.7)']
                ],
            )
        )
    ])

    title = "Company Positioning"

    annotations = []
    # Title
    annotations.append(dict(
        xref = 'paper',
        yref = 'paper',
        x = 0,
        y = 1.1,
        xanchor = 'left',
        yanchor = 'middle',
        text = title,
        font = dict(family='Arial Black',
                    size= 20,
                    color='rgba(255, 255, 255, 0.8)'),
        showarrow = False
    ))
    fig.update_layout(annotations = annotations)

    fig.update_layout(
        xaxis=dict(
            title_text = "Volume",
            title_font = dict(family='Arial Black',
                            size= 18,
                            color='rgba(255, 255, 255, 0.8)'),
            gridcolor='rgba(202, 202, 202, 0.3)',
            type='log',
            gridwidth = 1,
            tickfont = dict(family='Arial',
                            size= 16,
                            color='rgba(255, 255, 255, 0.7)'),
        ),

        yaxis=dict(
            title='Price',
            title_font = dict(family='Arial Black',
                            size= 18,
                            color='rgba(255, 255, 255, 0.8)'),
            gridcolor = 'rgba(202, 202, 202, 0.3)',
            gridwidth = 1,
            tickfont = dict(family='Arial',
                            size= 16,
                            color='rgba(255, 255, 255, 0.7)'),
        ),

        paper_bgcolor = 'rgba(255, 255, 255, 0)',
        plot_bgcolor = 'rgba(255, 255, 255, 0)',
        height = 600,
    )

    chart = dcc.Graph(figure = fig)

    return chart
