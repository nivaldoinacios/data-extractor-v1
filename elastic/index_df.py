from utils.world_itens import (os, load_dotenv)
from dataframes.df_users_and_stations import df
from elasticsearch import Elasticsearch
import eland as ed
import pandas as pd
import numpy as np


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
