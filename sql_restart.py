import time
import sql_integration
    
def sql_restart():
    connection,cur=sql_integration.connection()
    return connection,cur
connection,cur=sql_restart()
while True:
    sql_integration.sql_integration(connection,cur)
    time.sleep(900)
