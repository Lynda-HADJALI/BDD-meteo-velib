import sqlite3
from unittest import result

'''conn = sqlite3.connect('data.db')

cur = conn.cursor()

req = "select * from velib2"
result = cur.execute(req)'''
'''for row in result:
     print(row[1])'''
def sql_connection():
     conn=sqlite3.connect('data.db')
     cur=conn.cursor()
     return cur
def find_all(cur):
     req="SELECT * FROM velib2"
     result=cur.execute(req)
     return result
def find_elem(cur,elem_name):
     req="select "+elem_name+" from velib2"
     result=cur.execute(req)
     return result
def find_all_with_query(cur,query):
     req="""select * from velib2 where"""+query
     result=cur.execute(req)
     return result
def find_elem_with_query(cur,query,elem_name):
     req="""select """+elem_name+"""from velib2 where """+query
     result=cur.execute(req)
     return result
def find_station_town(cur,town):  
     return cur.execute('SELECT station2 FROM velib2 WHERE commune=:city',{'city':town})
