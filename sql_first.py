import time
import sql_integration
def sql_first():
    cur=sql_integration.connection()
    sql_integration.create_table(cur)
    sql_integration.sql_integration()
