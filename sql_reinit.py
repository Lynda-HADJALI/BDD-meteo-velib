import time
import sql_integration
def sql_reinit():
    connection,cur=sql_integration.connection()
    drop="DROP TABLE velib2"
    cur.execute(drop)
    sql_integration.create_table(cur)
    return connection,cur
connection,cur=sql_reinit()
while True:
    sql_integration.sql_integration(connection,cur)
    time.sleep(900)
