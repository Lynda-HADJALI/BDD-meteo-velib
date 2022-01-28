import sqlite3
from unittest import result
def sql_connection():
     conn=sqlite3.connect('data.db')
     cur=conn.cursor()
     return cur
def find_all(cur):
     req="SELECT * FROM velib"
     result=cur.execute(req)
     return result
def find_column(cur,column_name):
     req="select "+column_name+" from velib"
     result=cur.execute(req)
     return result
def find_all_with_query(cur,query):
     req="""select * from velib where"""+query
     result=cur.execute(req)
     return result
def find_column_with_query(cur,query,column_name,query_arguments):
     req="""select distinct """+column_name+""" from velib where """+query
     result=cur.execute(req,query_arguments)
     return result
def query_with_order(cur,column_name,order_by_column,query,query_arguments):
	return cur.execute('SELECT '+column_name +' from velib WHERE '+query+ ' ORDER BY '+order_by_column+' DESC',query_arguments)
