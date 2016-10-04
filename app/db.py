import mysql.connector
import os

config = {
    'user': os.getenv("MYSQL_USER"),
    'password': os.getenv("MYSQL_PASSWORD"),
    'host': "databox_notifier_mysql",
    'database': os.getenv("MYSQL_DATABASE")
}
cnx = mysql.connector.connect(**config)


def get():
    return cnx;
