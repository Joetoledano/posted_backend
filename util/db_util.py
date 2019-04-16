import pymysql
from util.constants import *


def get_deals():
    try:
        db = pymysql.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, db=DB, cursorclass=pymysql.cursors.DictCursor)
        cursor = db.cursor()
    except Exception as e:
        print(e)
    else:
        sql_statement = 'select * from deals'
        cursor.execute(sql_statement)
        db.close()
        return cursor.fetchall()


def get_category_deals(primary, secondary):
    try:
        db = pymysql.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, db=DB, cursorclass=pymysql.cursors.DictCursor)
        cursor = db.cursor()
    except Exception as e:
        print(e)
    else:
        secondary = " and secondary_category ='{}'".format(secondary) if secondary else ''
        sql_statement = """ select * from deals where primary_category = '{}' {}""".format(primary, secondary)
        print(sql_statement)
        cursor.execute(sql_statement)
        db.close()
        return cursor.fetchall()
