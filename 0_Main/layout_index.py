# _*_ coding: utf-8 _*_

# Import Modules
## Dash
import dash_html_components as html
import dash_core_components as dcc

## Plotly
import plotly.express as px
import plotly.graph_objects as go


def layout_index(data_source):

    layout = html.Div([
        html.Div([
            html.Div(["Galanz"], id = "logo_index")
        ], id = "header_index"),

        html.Div([
            html.Div(
                [dcc.Link("Export Data", href = "/export_data")],
                id = "export_data", className = "menuIndex"),
            html.Div(
                [dcc.Link("Product Data", href = "/product_data")],
                id = "product_data", className = "menuIndex"),
            html.Div(
                [dcc.Link("Social Media", href = "/social_media")],
                id = "social_media", className = "menuIndex")
        ], id = "body_index"),

        html.Div([
            html.Div(["Developed by Data Team"], id = "footnote")],
            id = "bottom_index")
    ], id = "index")

    return layout
