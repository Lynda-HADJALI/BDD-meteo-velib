import time
import sql_integration
def sql_first():
    connection,cur=sql_integration.connection()
    sql_integration.create_table(cur)
    return connection,cur
connection,cur=sql_first()
while True:
    sql_integration.sql_integration(connection,cur)
    print('Time Stop')
    time.sleep(900)
