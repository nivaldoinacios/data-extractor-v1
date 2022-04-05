from dataframes.df_users_and_stations import (doc)
from elasticsearch import Elasticsearch
from utils.world_itens import (os, load_dotenv)

load_dotenv()

es = Elasticsearch(
    ['http://192.168.10.14:9200'],
    basic_auth=(os.getenv('ELK_USERNAME'), os.getenv('ELK_PASSWORD'))
)


resp = es.index(index="teste-index", document=doc)
print(resp['result'])
