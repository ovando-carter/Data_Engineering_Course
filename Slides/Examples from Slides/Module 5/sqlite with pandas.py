import sqlite3
import pandas as pd
try:
    conn = sqlite3.connect('animals.db')
    df_query = pd.read_sql_query("select * from animals", conn)
    print(df_query)
except Exception as e:
    conn.rollback()
    print(e)
finally:
    conn.close()

