import weather_data
import sql_data
import pprint
col=weather_data.get_data()
def aggregation(col,pipeline):
    return col.aggregate(pipeline)
pipeline=[{"$match":{'weather.main':'Mist'}},{"$group":{"_id":'$request_date',"avgtemp":{"$avg":'$main.temp'}}}]
col=weather_data.get_data()
agg=aggregation(col,pipeline)
for ag in agg:
	print(ag) 

