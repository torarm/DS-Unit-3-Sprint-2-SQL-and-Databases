"""Queries for Titanic Assignment"""


#SQLite Queries

CREATE_TITANIC_TABLE = """
     CREATE TABLE titanic (
         df_idx INT,
         Survived INT,
         Pclass INT,
         Name TEXT,
         Sex TEXT,
         Age INT,
         Sibling_Spouse_count INT,
         Parents_Children_count INT,
         Fare NUM
     );
"""

GET_TITANIC = """
   SELECT *
   FROM titanic
"""

# Postgres Queries

CREATE_PG_TABLE = """
   CREATE TABLE IF NOT EXISTS titanic (
    df_idx SERIAL PRIMARY KEY,
    Survived INTEGER,
    Pclass INTEGER,
    Name VARCHAR(100),
    Sex VARCHAR(7),
    Age INTEGER,
    Sibling_Spouse_count INTEGER,
    Parents_Children_count INTEGER,
    Fare FLOAT
   );
"""