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
