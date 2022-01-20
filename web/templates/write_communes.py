import requests
import time
import json
def list_cities():
    api ="https://opendata.paris.fr/api/records/1.0/search/?dataset=velib-disponibilite-en-temps-reel&rows=1435&q=&sort=nom_arrondissement_communes&facet=name&facet=is_installed&facet=is_renting&facet=is_returning&facet=nom_arrondissement_communes"
    json_data = requests.get(api).json()
    communes_list=json_data['facet_groups'][4]['facets']
    communes=[]

    for i in range(0,len(communes_list)):
        communes.append(communes_list[i]['name'])
    communes.sort()
    return communes
def write_in_json(json_file):
    with open(json_file, 'w',encoding='utf-8') as outfile:
    
        json.dump(list_cities(), outfile,ensure_ascii=False)

write_in_json('templates/ville.json')

    

