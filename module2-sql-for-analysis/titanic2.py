import psycopg2
import pandas as pd
import sqlite3
from titanic_queries import *

sl_conn = sqlite3.connect("titanic_db.sqlite3")
sl_curs = sl_conn.cursor()
print('SL Connection successful')


all_titanic = sl_curs.execute(GET_TITANIC).fetchall()
print('SL Query Successful')


# Connecting to PostGreSQL
dbname = ?
user = ?
password = ?
host = ?

pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
pg_curs = pg_conn.cursor()

print('PostGres Connection Successfull')

pg_curs.execute(CREATE_PG_TABLE)
pg_conn.commit()
print('New table created')

# data transfer
for line in all_titanic:

    INSERT_STATEMENT = """
        INSERT INTO titanic (
            df_idx, Survived, Pclass, Name, Sex, Age, Sibling_Spouse_count, Parents_Children_count, Fare
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
    pg_curs.execute(INSERT_STATEMENT, line)
pg_conn.commit()
pg_conn.close()

print('PG table populated')
