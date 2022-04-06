from actions import (os, load_dotenv)
from elasticsearch import Elasticsearch

load_dotenv()

es = Elasticsearch(
    ['http://192.168.10.14:9200'],
    basic_auth=(os.getenv('ELK_USERNAME'), os.getenv('ELK_PASSWORD'))
)
