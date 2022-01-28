import time
import velib_integration
def sql_reinit():
    connection,cur=velib_integration.connection()
    drop="DROP TABLE velib2"
    cur.execute(drop)
    velib_integration.create_table(cur)
    return connection,cur
connection,cur=sql_reinit()
while True:
    velib_integration.sql_integration(connection,cur)
    print('Time Stop')
    time.sleep(900)
