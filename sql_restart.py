import time
import sql_integration
    
def sql_restart():
    cur=sql_integration.connection()
    sql_integration.sql_integration()
