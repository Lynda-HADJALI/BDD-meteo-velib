import time
import sql_integration
    
def sql_restart():
    cur=sql_integration.connection()
    return cur
cur=sql_restart()
while True:
    sql_integration.sql_integration(cur)
    time.sleep(900)
