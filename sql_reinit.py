import time
import sql_integration
def sql_reinit():
    cur=sql_integration.connection()
    drop="DROP TABLE velib2"
    cur.execute(drop)
    sql_integration.create_table(cur)
    sql_integration.sql_integration()