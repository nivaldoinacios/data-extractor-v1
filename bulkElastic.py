#!/usr/bin/python3
from elasticsearch import Elasticsearch, helpers
from dotenv import load_dotenv
import time
import csv
import os


load_dotenv()


es = Elasticsearch(
    ['http://192.168.10.14:9200'],
    basic_auth=(os.getenv('ELK_USERNAME'), os.getenv('ELK_PASSWORD'))
)

e = 'post dos dados'
try:
    with open(os.getenv('dados'), 'r') as f:
        reader = csv.DictReader(f, delimiter=';')
        helpers.bulk(es, reader, index='eland-fluxo')

        time.sleep(1)

        f.close()
except Exception as e:
    print(f'Erro ao executar o : {e}')
