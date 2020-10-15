# _*_ coding: utf-8 _*_

# Import Modules
## Dash
import dash_html_components as html
import dash_core_components as dcc

## plotly
import plotly.express as px
import plotly.graph_objects as go

## Charts & Tables
from tb_volumeData import tb_volumeData
from tb_valueData import tb_valueData
from tb_priceData import tb_priceData

from cht_priceShare import cht_priceShare
from cht_globalReview import cht_globalReview
from tb_companyRank import tb_companyRank
from cht_topFiveAnnualTrend import cht_topFiveAnnualTrend
from cht_topFiveMonthlyTrend import cht_topFiveMonthlyTrend
from cht_companyPositioning import cht_companyPositioning
from testMap import testMap

from dcc import dd_product, dd_country, dd_year, dd_indicator, dd_company, rs_month


def layout_export(data_source):

    layout = html.Div([
        html.Header([
            html.Div([
                html.Div(
                    [dcc.Link('Home', href = '/')],
                    id = "home_export"),
                html.H1(["Galanz | Export Data Analysis"], id = "logo"),
            ], id = "headerBackground"),
            html.Div([
                html.Div([
                    html.Div(
                        [dd_product(data_source)],
                        className = "menuName",
                        id = "product_dd"),
                    html.Div(
                        [dd_company(data_source)],
                        className = "menuName",
                        id = "company_dd"),
                    html.Div(
                        [dd_country(data_source)],
                        className = "menuName",
                        id = "country_dd"),
                    html.Div(
                        [dd_year(data_source)],
                        className = "menuName")
                ], id = "Menu_dd"),
                html.Div([rs_month(data_source)], id = "Menu_rs"),
            ], className = "headerMenu")
        ]),

        html.Div([
            html.Div([
                # Section 1: Key Indicators
                html.Div(children = [
                    html.H2("Key Indicators"),
                    html.Div([

                        # Key Indicators - Volume
                        html.Div([
                            html.Div([
                                html.Div(["Volume"], className = "tdName"),
                                html.Div(
                                    [tb_volumeData(data_source)["volume"]], id = "kiVolume")
                            ], className = "kiData"),

                            html.Div([
                                html.Div([
                                    html.Div(["Share"], className = "tdName"),
                                    html.Div(
                                        [tb_volumeData(data_source)["volume_share"]], className = "tdPercent", id = 'kiVolShare')
                                ], id = 'tbVolShare'),
                                html.Div([
                                    html.Div(["YoY"], className = "tdName"),
                                    html.Div(
                                        [tb_volumeData(data_source)["volume_YoY"]], className = "tdPercent", id = 'kiVolYoY')
                                ], id = 'tbVolYoY'),
                            ], className = "kiPercent")
                        ], className = "tb_keyIndicators"),


                        # Key Indicators - Price
                        html.Div([
                            html.Div([
                                html.Div(["Price"], className = "tdName"),
                                html.Div(
                                    [tb_priceData(data_source)["price"]],
                                    id = "kiPrice")
                                ], className = "kiData"),

                            html.Div([
                                html.Div([
                                    html.Div(["Average"], className = "tdName"),
                                    html.Div(
                                        [tb_priceData(data_source)["price_diff"]], className = "tdPercent", id = "kiPriceShare")
                                ], id = "tbPriceShare"),
                                html.Div([
                                    html.Div(["YoY"], className = "tdName"),
                                    html.Div(
                                        [tb_priceData(data_source)["price_YoY"]], className = "tdPercent", id = "kiPriceYoY")
                                ], id = "tbPriceYoY"),
                            ], className = "kiPercent")
                        ], className = "tb_keyIndicators"),


                        # Key Indicators - Value
                        html.Div([
                            html.Div([
                                html.Div(["Value"], className = "tdName"),
                                html.Div([
                                    tb_valueData(data_source)["value"]
                                ], id = "kiValue")
                            ], className = "kiData"),

                            html.Div([
                                html.Div([
                                    html.Div(["Share"], className = "tdName"),
                                    html.Div([
                                        tb_valueData(data_source)["value_share"]], className = "tdPercent", id = "kiValueShare")
                                ], id = "tbValueShare"),
                                html.Div([
                                    html.Div(["YoY"], className = "tdName"),
                                    html.Div([tb_valueData(data_source)["value_YoY"]], className = "tdPercent", id = "kiValueYoY")
                                ], id = "tbValueYoY"),
                            ], className = "kiPercent")
                        ], className = "tb_keyIndicators"),


                    ], id = "keyIndicatorsFig"),

                    # Key Indicators = Price Share
                    html.Div(
                        cht_priceShare(data_source),
                        id = "priceShare")

                ], id = "keyIndicators"),

                # Section 2: Global Review
                html.Div(children = [
                    html.H2("Global Review"),
                    html.Div([
                        cht_globalReview(
                            data_source["geoCN"],
                            data_source["cnPercent"])
                    ], id = "cht_globalReview")
                ], id = "globalReview"),
            ], id = "first_layer"),


            html.Div([
                # Section 3: Competition Summary
                html.Div(children = [
                    html.H2("Competition Summary"),
                    html.Div(
                        children = [dd_indicator()],
                        id = "secondMenu"),
                    html.Div(
                        [tb_companyRank(data_source)],
                        id = "tb_companyRank"),
                    html.Div(
                        [html.Div([
                            html.Div(
                                ["Annual Trend"],
                                className = "chtTitle"),
                            html.Div(
                                [cht_topFiveAnnualTrend(data_source)],
                                id = "cht_topFiveAnnualTrend")
                        ], id = "AnnualTrend"),
                        html.Div([
                            html.Div(
                                ["Monthly Trend"],
                                className = "chtTitle"),
                            html.Div(
                                [cht_topFiveMonthlyTrend(data_source)],
                                id = "cht_topFiveMonthlyTrend")
                        ], id = "MonthlyTrend"),
                    ], id = "companyTrend"),
                    html.Div(
                        [cht_companyPositioning(data_source)],
                        id = "cht_companyPositioning")
                ], id = "competitionSummary")
            ], id = "second_layer")

        ], id = "figures"),

    html.Div(
        ["Developed by MKT Data Team"],
        id = "bottom")
    ], id = "body")

    return layout
