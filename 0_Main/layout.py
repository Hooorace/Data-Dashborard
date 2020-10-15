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


def layout(app, data_source):

    app.layout = html.Div([
        dcc.Location(id = 'url', refresh = False),
        html.Div(id = 'page-content')
    ])
