# _*_ coding: utf-8 _*_

import dash_core_components as dcc
import plotly.graph_objects as go
import pandas as pd
import numpy as np

def cht_topFiveAnnualTrend(data_source):

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


    df_current_data = df_views[(df_views["yr"] == year) & (df_views["month"].isin(period)) & (df_views["cn"].isin(country))][["company", indicator]].groupby("company").sum().sort_values(by = indicator, ascending = False).head(5)


    company_list = []
    for company in df_current_data.index:
        company_list.append(company)


    df_annual_history = df_views[df_views["company"].isin(company_list)][["company", "yr", indicator]].groupby(["company", "yr"]).sum().unstack("yr")


    final_data = df_annual_history.reindex(df_current_data.index)
    y_data = final_data.values
    x_data = np.vstack((np.arange(2017, 2021),) * 5)
    labels = final_data.index.values.tolist()

    colors = [
        'rgba(114, 0, 9, 0.5)',
        'rgba(229, 1, 18, 0.5)',
        'rgba(254, 88, 100, 0.5)',
        'rgba(255, 143, 152, 0.5)',
        'rgba(202, 202, 202, 0.5)']

    mode_size = [10, 10, 10, 10, 10]
    line_size = [8, 8, 8, 8, 8]

    fig = go.Figure()

    for i in range(0, 5):
        fig.add_trace(
            go.Scatter(
                x = x_data[i],
                y = y_data[i],
                mode = 'lines+markers',
                name = labels[i],
                line = dict(color = colors[i], width  = line_size[i]),
                connectgaps = False,
                line_shape = "spline",
        ))

    fig.update_layout(

        xaxis = dict(
            title_text = "Year",
            title_font = dict(
                family = 'Arial Black',
                size = 18,
                color = 'rgba(255, 255, 255, 0.8)'),
            showline = False,

            # Ticks
            showticklabels = True,
            tickfont = dict(family='Arial',
                            size= 16,
                            color='rgba(255, 255, 255, 0.7)'),
            tickwidth = 2,
            ticks = 'outside',
            tickcolor = 'rgba(112, 112, 112, 0.5)',

            # Line
            linecolor = 'rgba(41, 41, 41, 0.8)',
            linewidth = 2,

            showgrid = False,
        ),

        yaxis = dict(
            # Title
            title_text = "Volume",
            title_font = dict(family='Arial Black',
                            size= 18,
                            color='rgba(255, 255, 255, 0.8)'),
            # Grid
            showgrid=True,
            gridwidth = 1,
            gridcolor = 'rgba(202, 202, 202, 0.3)',

            zeroline=True,
            zerolinecolor = 'rgba(202, 202, 202, 0.5)',

            showline=False,
            # Ticks
            showticklabels=True,
            tickfont = dict(family='Arial',
                            size= 16,
                            color='rgba(255, 255, 255, 0.7)'),
            tickwidth = 2,
            nticks = 10,
        ),

        autosize = True,

        legend = dict(
            title_text = "Company",
            title_font = dict(family = '微软雅黑',
                            size = 14,
                            color = 'rgba(255, 255, 255, 0.8)'),
            font = dict(family = '微软雅黑',
                        size = 14,
                        color = 'rgba(255, 255, 255, 0.5)'),
        ),

        paper_bgcolor = 'rgba(255, 255, 255, 0)',
        plot_bgcolor = 'rgba(255, 255, 255, 0)',
        # height = 480,
    )

    chart = dcc.Graph(figure = fig)

    return chart
