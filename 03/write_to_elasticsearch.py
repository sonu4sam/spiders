from elasticsearch import Elasticsearch
from get_planet_data import get_planet_data

# create an elastic search object
es = Elasticsearch(hosts='http://localhost:9200')

# get the data
planet_data = get_planet_data()

for planet in planet_data:
    # insert each planet data into elasticsearch server
    res = es.index(index='planets', document=planet)
    print(res)