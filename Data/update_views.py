# _*_ coding: utf-8 _*_
import pandas as pd

def update_views(data_source):

    # Database Connection
    db_connection = data_source["db_connection"]
    current_view = data_source["current_view"]

    df_views = pd.read_sql(
    """
    Select
        yr,
        standard_month as month,
        English_cn as cn,
        sum(export_volume) as vol,
        sum(export_value) as val,
        company_abbr as company
    From
        {current_view}
    Group By
        yr, month, cn, company;
    """.format(current_view = current_view), con = db_connection)

    data_source["df_views"] = df_views

    # Update Company List
    company_list = list(df_views[["company", "val"]].groupby("company").sum().sort_values(by = "val", ascending = False).head(10).index)
    data_source["company_list"] = company_list

    # Update Country List
    cn_list = list(df_views[["cn", "val"]].groupby("cn").sum().sort_values(by = "val", ascending = False).head(30).index)
    data_source["cn_list"] = cn_list

    data_source["cnPercent"] = df_views[["cn", "vol"]].groupby("cn").sum().sort_values(by = "vol", ascending = False).reset_index()
