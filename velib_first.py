import time
import velib_integration
def sql_first():
    connection,cur=velib_integration.connection()
    velib_integration.create_table(cur)
    return connection,cur
connection,cur=sql_first()
while True:
    velib_integration.sql_integration(connection,cur)
    print('Time Stop')
    time.sleep(900)
