# _*_ coding: utf-8 _*_

from urllib.request import urlopen
import json
import pandas as pd
import plotly.express as px
import dash_core_components as dcc


def testMap(data_source):

    counties = data_source["geoUS"]
    df = data_source["unemp"]

    fig = px.choropleth(
        df,
        geojson = counties,
        locations='fips',
        color='unemp',
        color_continuous_scale="Reds",
        range_color=(0, 12),
        center = {"lat": 37.0902, "lon": -95.7129},
        labels={'unemp':'unemployment rate'})

    fig.update_layout(
        margin={"r":0,"t":0,"l":0,"b":0})

    map = dcc.Graph(figure = fig)

    return map
