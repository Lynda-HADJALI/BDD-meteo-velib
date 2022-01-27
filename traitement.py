import weather_data
import sql_data
print('que faire ??? des requetes complexes ??? Comme quoi ?? En faisant un mix des données Mongo et Sql ? ')
col=weather_data.get_data()
def aggregation(col,pipeline):
    return col.aggregate(pipeline)
pipeline=[{"$match":{"$weather.main":'Mist'}},{"$group":{"_id":"$request_date","avgtemp":{"$avg":"$main.temp"}}}]
col=weather_data.get_data()
print(aggregation(col,pipeline))

