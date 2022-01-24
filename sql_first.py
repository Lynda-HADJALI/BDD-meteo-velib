import time
import sql_integration
def sql_first():
    cur=sql_integration.connection()
    sql_integration.create_table(cur)
    return cur
cur=sql_first()
while True:
    sql_integration.sql_integration(cur)
    time.sleep(900)
