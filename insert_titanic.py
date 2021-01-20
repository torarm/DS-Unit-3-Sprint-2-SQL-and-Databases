"""CSV to SQLite3 to PostGreSQL Pipeline"""

import psycopg2
import pandas as pd
import sqlite3
from titanic_queries import *

"""
url = 'https://raw.githubusercontent.com/torarm/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module2-sql-for-analysis/titanic.csv'
df = pd.read_csv(url, names=[
    'Survived', 'Pclass', 'Name', 'Sex', 'Age',
    'Sibling_Spouse_count', 'Parents_Children_count', 'Fare'
])

# Connect / Create SQLite DB
sl_conn = sqlite3.connect('titanic_db.sqlite3')
sl_curs = sl_conn.cursor()


# DF to SQLite
sl_curs.execute(CREATE_TITANIC_TABLE)
sl_conn.commit()
df.to_sql(name='titanic', con=sqlite3.connect('titanic_db.sqlite3'), if_exists='replace',
            index=True, index_label='df_idx')
sl_curs.execute(GET_TITANIC)
sl_curs.fetchall()
"""
sl_conn = sqlite3.connect("titanic_db.sqlite3")
sl_curs = sl_conn.cursor()

def df_2_db(url):
    df = pd.read_csv(url, names=[
    'Survived', 'Pclass', 'Name', 'Sex', 'Age',
    'Sibling_Spouse_count', 'Parents_Children_count', 'Fare'], header=0)
    df = df
    df.to_sql(name='titanic', con=sl_conn, if_exists='replace',
            index=True, index_label='df_idx')
    sl_curs.execute(GET_TITANIC)
    sl_curs.fetchall()
    return sl_curs


# Connecting to PostGreSQL
dbname = ?
user = ?
password = ?
host = ?

pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
pg_curs = pg_conn.cursor()


def execute_query(curs, query):
    result = curs.execute(query)
    return result


def populate_pg(pg_curs, char_list):
    for titanic in char_list:
        insert_state = """
        INSERT INTO titanic (
            Survived, Pclass, Name, Sex, Age, Sibling_Spouse_count, Parents_Children_count, Fare
        ) VALUES{}
        """.format(titanic[1:])
        pg_curs.execute(insert_state)
    pg_conn.commit()

if __name__ == "__main__":
    sl_curs = df_2_db('https://raw.githubusercontent.com/torarm/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module2-sql-for-analysis/titanic.csv')
    execute_query(pg_curs, CREATE_PG_TABLE)
    get_titanic = execute_query(sl_curs, GET_TITANIC).fetchall()
    populate_pg(pg_curs, get_titanic)

