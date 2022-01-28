import time
import velib_integration
    
def sql_restart():
    connection,cur=velib_integration.connection()
    return connection,cur
connection,cur=sql_restart()
while True:
    velib_integration.sql_integration(connection,cur)
    print('Time Stop')
    time.sleep(900)
