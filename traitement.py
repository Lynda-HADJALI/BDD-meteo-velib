import weather_data
import velib_data
import pprint
import pymongo
col=weather_data.connect_to_mongo()
cur=velib_data.sql_connection()
def aggregation(col,pipeline):
    return col.aggregate(pipeline)
##temperature moyenne pour les villes au climat brouillard
print('La temperature moyenne des communes ou il y a du brouillard selon l horaire')
pipeline=[{"$match":{'weather.main':'Mist'}},{"$group":{"_id":'$request_date',"avgtemp":{"$avg":'$main.temp'}}}]
col=weather_data.get_data()
agg=aggregation(col,pipeline)
for ag in agg:
	print(ag)
##station velos avec capacite superieur à 25 et qui est deployé
print('Les stations velib  deployés qui ont une capacité superieur à 25')
column_name='station'
query='capacity>:number and station_en_fonctionnement=:boolean'
query_arguments={'number':25,'boolean':'OUI'}
query_result=velib_data.find_elem_with_query(cur,query,column_name,query_arguments)
for r in query_result:
    print(r)
query={'name':'Alfortville'}
sort_by_field="request_date"
sort_order=pymongo.DESCENDING
query_result=weather_data.sort_weather_data(col,query,sort_by_field,sort_order)
list_weather=[]
for r in query_result:
	list_weather.append(r)
print(list_weather[0])
column_name='station,ebike,mechanical'
order_by_column='request_date'
query='commune=:town'
query_arguments={'town':'Alfortville'}
query_result=velib_data.select_with_order(cur,column_name,order_by_column,query,query_arguments)
list_station=[]
for r in query_result:
	list_station.append(r)
print(list_station)
