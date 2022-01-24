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
     req="select * from velib2"
     result=cur.execute(req)
     return result
def find_elem(cur,elem_name):
     req="select "+elem_name+" from velib2"
     result=cur.execute(req)
     return result
def find_all_with_query(cur,query):
     req="select * from velib2 where"+query
     result=cur.execute(req)
     return result
def find_elem_with_query(cur,query,elem_name):
     req="select "+elem_name+"from velib2 where "+query
     result=cur.execute(req)
     return result
cur=sql_connection()
result=find_all(cur)
for row in result:
     print(row[4])