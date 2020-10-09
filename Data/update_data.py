from data_source import data_source


def updateData_product(data_source, product):

    product_views = {
        'microwave': 'data_source',
        'refridgerator': 'data_source_fridge'
    }

    current_view = product_views[product]

    data_source["product"] = product
    data_source["current_view"] = current_view


def updateData_year(data_source, year):
    year = int(year.replace("年", ""))
    last_year = year - 1
    data_source["year"] = "{}年".format(year)
    data_source["last_year"] = "{}年".format(last_year)


def updateData_cont(data_source, continent):
    data_source["continent"] = continent


def updateData_subcont(data_source, subcontinent):
    data_source["subcontinent"] = subcontinent


def updateData_cn(data_source, country):
    df_views = data_source["df_views"]
    cn_list = data_source["cn_list"]
    if country == "All":
        data_source["country"] = cn_list
    else:
        data_source["country"] = [country]


def updateData_company(data_source, company):
    df_views = data_source["df_views"]
    company_list = data_source["company_list"]
    if company == "All":
        data_source["company"] = company_list
    else:
        data_source["company"] = [company]


def updateData_period(data_source, month):
    """Month"""
    beginning_month = month[0]
    end_month = month[1]
    """"Period"""
    period = []
    for m in range(beginning_month, end_month+1):
        if m < 10:
            month = "0%d月"%m
        else:
            month = "%d月"%m
        period.append(month)
    data_source["period"] = period


def updateData_indicator(data_source, indicator):
    data_source["indicator"] = indicator
