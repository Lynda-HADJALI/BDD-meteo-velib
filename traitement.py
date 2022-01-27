import weather_data
import sql_data
import pprint
col=weather_data.get_data()
cur=sql_data.sql_connection()
def aggregation(col,pipeline):
    return col.aggregate(pipeline)
##temperature moyenne pour les villes au climat brouillard
pipeline=[{"$match":{'weather.main':'Mist'}},{"$group":{"_id":'$request_date',"avgtemp":{"$avg":'$main.temp'}}}]
col=weather_data.get_data()
agg=aggregation(col,pipeline)
for ag in agg:
	print(ag)
##station velos avec capacite superieur à 25 et qui est deployé
elem_name='station2'
query='capacity>:number and station_en_fonctionnement=:boolean'
dico={'number':25,'boolean':'OUI'}
res=sql_data.find_elem_with_query(cur,query,elem_name,dico)
for r in res:
    print(r)

