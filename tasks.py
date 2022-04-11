from elasticsearch import Elasticsearch, helpers
import csv
import os

es = Elasticsearch(
    ['http://192.168.10.14:9200'],
    basic_auth=(os.getenv('ELK_USERNAME'), os.getenv('ELK_PASSWORD'))
)


with open(os.getenv('dir_users_stations'), 'r') as f:
    reader = csv.DictReader(f, delimiter=';')
    helpers.bulk(es, reader, index='teste1')


#%%
