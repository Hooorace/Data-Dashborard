# _*_ coding: utf-8 _*_

import update_data
from update_views import update_views

from data_source import data_source
from dash.dependencies import Input, Output

from tb_volumeData import tb_volumeData
from tb_valueData import tb_valueData
from tb_priceData import tb_priceData

from cht_priceShare import cht_priceShare
from tb_companyRank import tb_companyRank
from cht_topFiveAnnualTrend import cht_topFiveAnnualTrend
from cht_topFiveMonthlyTrend import cht_topFiveMonthlyTrend
from cht_companyPositioning import cht_companyPositioning

def callbacks(app, data_source):

    @app.callback(
        [
            ####### Key Indicator s#######
            ### Volume ###
            Output(component_id = "kiVolume", component_property = "children"),
            Output(component_id = "kiVolShare", component_property = "children"),
            Output(component_id = "kiVolYoY", component_property = "children"),
            ### Price ###
            Output(component_id = "kiPrice", component_property = "children"),
            Output(component_id = "kiPriceShare", component_property = "children"),
            Output(component_id = "kiPriceYoY", component_property = "children"),
            ### Value ###
            Output(component_id = "kiValue", component_property = "children"),
            Output(component_id = "kiValueShare", component_property = "children"),
            Output(component_id = "kiValueYoY", component_property = "children"),
            ### Share of Price Section ###
            Output(component_id = "priceShare", component_property = "children"),

            ####### Competition Summary s#######
            ### Company Rank ###
            Output(component_id = "tb_companyRank", component_property = "children"),
            ### Company Annual & Monthly Trend ###
            Output(component_id = "cht_topFiveAnnualTrend", component_property = "children"),
            Output(component_id = "cht_topFiveMonthlyTrend", component_property = "children"),
            ### Company Positioning ###
            Output(component_id = "cht_companyPositioning", component_property = "children")
        ],
        [Input(component_id = "company", component_property = "value"),
        Input(component_id = "country", component_property = "value"),
        Input(component_id = "year", component_property = "value"),
        Input(component_id = "month", component_property = "value"),
        Input(component_id = "indicator", component_property = "value")]
    )
    def update_condition(company, cn, year, month, indicator, data_source = data_source):

        update_data.updateData_company(data_source, company)
        update_data.updateData_cn(data_source, cn)
        update_data.updateData_year(data_source, year)
        update_data.updateData_period(data_source, month)
        update_data.updateData_indicator(data_source, indicator)

        print(data_source["company"])
        print(data_source["country"])
        print(data_source["year"])
        print(data_source["last_year"])
        print(data_source["period"])
        print(data_source["indicator"])
        print("\n")

        update_views(data_source)

        Volume = tb_volumeData(data_source)["volume"]
        VolShare = tb_volumeData(data_source)["volume_share"]
        VolYoY = tb_volumeData(data_source)["volume_YoY"]

        Price = tb_priceData(data_source)["price"]
        PriceShare = tb_priceData(data_source)["price_diff"]
        PriceYoY = tb_priceData(data_source)["price_YoY"]

        Value = tb_valueData(data_source)["value"]
        ValShare = tb_valueData(data_source)["value_share"]
        ValYoY = tb_valueData(data_source)["value_YoY"]

        priceShare = cht_priceShare(data_source)
        table = tb_companyRank(data_source)
        chartAnnual = cht_topFiveAnnualTrend(data_source)
        chartMonthly = cht_topFiveMonthlyTrend(data_source)
        chartPositioning = cht_companyPositioning(data_source)

        return Volume, VolShare, VolYoY, Price, PriceShare, PriceYoY, Value, ValShare, ValYoY, priceShare, table, chartAnnual, chartMonthly, chartPositioning
