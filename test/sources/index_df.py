

from elasticsearch import Elasticsearch
import eland as ed

load_dotenv()


es = Elasticsearch(
    ['http://192.168.10.14:9200'],
    basic_auth=(os.getenv('ELK_USERNAME'), os.getenv('ELK_PASSWORD'))
)

df_ed = ed.pandas_to_eland(
    pd_df=df,
    es_client=es,
    es_dest_index='eland-fluxo',
    es_if_exists='append',
    es_refresh=True,
)

##
from elasticsearch import Elasticsearch, helpers
import csv
import os

es = Elasticsearch(
    ['http://192.168.10.14:9200'],
    basic_auth=(os.getenv('ELK_USERNAME'), os.getenv('ELK_PASSWORD'))
)


with open(os.getenv('dir_users_stations'), 'r') as f:
    reader = csv.DictReader(f, delimiter=';')
    helpers.bulk(es, reader, index='fluxo')
