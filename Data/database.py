# _*_ coding: utf-8 _*_

from sqlalchemy import text
from sqlalchemy import create_engine
import mysql.connector
import pymysql.cursors

def database():
    """Connect to the database"""
    # db_connection_str = "mysql+pymysql://root:D0more&t4lkless@127.0.0.1/export_data_cn"
    # sql_engine = create_engine(db_connection_str, encoding="utf-8")
    # db_connection = sql_engine.connect()

    # db_connection = mysql.connector.connect(
    #     user = 'root',
    #     password = "D0more&t4lkless",
    #     host = "127.0.0.1",
    #     database = "export_data_cn")

    db_connection = pymysql.connect(
        user = 'root',
        password = "D0more&t4lkless",
        host = "127.0.0.1",
        db = "export_data_cn",
        charset = 'utf8mb4',
        cursorclass = pymysql.cursors.DictCursor
        )

    return db_connection
