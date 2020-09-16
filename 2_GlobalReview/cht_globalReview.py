# _*_ coding: utf_8 _*_

import plotly.graph_objects as go
import dash_core_components as dcc
import os

def cht_globalReview(geoData, mapData):

    z = mapData["vol"]
    zmax = z[0]

    fig = go.Figure(
        go.Choroplethmapbox(
            geojson = geoData,
            locations = mapData['cn'],
            featureidkey = "properties.ADMIN",
            z = z,
            zmin = 0,
            zmax = zmax,
            marker_opacity = 0.5,
            marker_line_width = 0,
            colorscale = [
                'rgba(172, 168, 168, 0.7)',
                'rgba(217, 217, 217, 0.7)',
                'rgba(255, 193, 197, 0.7)',
                'rgba(255, 143, 152, 0.7)',
                'rgba(254, 88, 100, 0.7)',
                'rgba(229, 1, 18, 0.7)',
                'rgba(180, 0, 13, 0.7)',
                'rgba(114, 0, 9, 0.7)'
                ],
            colorbar = dict(
                title="Volume",
                titleside="top",
                titlefont = dict(family = 'Arial Black',
                                size = 14,
                                color ='rgba(255, 255, 255, 0.8)',
                ),
                tickcolor = 'rgba(255, 255, 255, 0.8)',
                tickfont = dict(family = 'Arial',
                                size = 14,
                                color ='rgba(255, 255, 255, 0.8)',
                ),
            bgcolor = 'rgba(255, 255, 255, 0.5)',
            )
    ))

    fig.update_layout(
        height = 520,
        mapbox_style = "open-street-map",
        mapbox_zoom = 2,
        mapbox_center = {"lat": 37.0902, "lon": -95.7129},
        margin = {"r":0, "t":0, "l":0, "b":0},
        paper_bgcolor = 'rgba(255, 255, 255, 0)',
    )

    map = dcc.Graph(figure = fig)

    return map
