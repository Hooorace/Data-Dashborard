# -*- coding: utf-8 -*-

# Import Modules
## General Modules
import time
import sys
sys.path.append("C:/Users/tyrel/Desktop/Galanz_Dashboard/0_Main")
sys.path.append("C:/Users/tyrel/Desktop/Galanz_Dashboard/1_KeyIndicators")
sys.path.append("C:/Users/tyrel/Desktop/Galanz_Dashboard/2_GlobalReview")
sys.path.append("C:/Users/tyrel/Desktop/Galanz_Dashboard/3_CompetitionSummary")
sys.path.append("C:/Users/tyrel/Desktop/Galanz_Dashboard/Data")

## Dash
import dash

## Components of the Application
from layout import layout
# from layout_export import layout_export

from callbacks import callbacks

## Import data source
from database import database
from data_source import data_source
from update_views import update_views

## Beginning Argument

# The application
## Connect to the database
data_source["db_connection"] = database()
update_views(data_source)

## Create a dash application
app = dash.Dash(__name__)
app.config.suppress_callback_exceptions = True

## Callback of the Application
callbacks(app, data_source)

## Layout of the Application
layout(app, data_source)


# Run a program
if __name__ == '__main__':
	app.run_server(debug = True, use_reloader = True)
