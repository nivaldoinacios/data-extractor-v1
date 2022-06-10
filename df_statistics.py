from elasticsearch import Elasticsearch
from df_base import df
from etl import Lista
import pandas as pd_df
from dotenv import load_dotenv
import eland as ed
import os

load_dotenv()

es = Elasticsearch(
    ['http://192.168.10.14:9200'],
    basic_auth=(os.getenv('ELK_USERNAME'), os.getenv('ELK_PASSWORD'))
)

pd_df = df[["MAC", "AP_NAME", "BYTES_SENT", "BYTES_RECEIVED"]]

tamanho = len(pd_df)

ed = ed.DataFrame(es, 'eland-fluxo').tail(tamanho)

ed_df = ed[['MAC','AP_NAME', 'BYTES_SENT', 'BYTES_RECEIVED', '@timestamp-py']]

ed_df = ed_df.to_pandas()

ed_df[['BYTES_SENT', 'BYTES_RECEIVED']] = ed_df[['BYTES_SENT', 'BYTES_RECEIVED']].astype(int)

pd_df[['BYTES_SENT', 'BYTES_RECEIVED']] = pd_df[['BYTES_SENT', 'BYTES_RECEIVED']].astype(int)

pd_df.insert(len(pd_df.columns), 'BYTES_SENT_CALC', 0, True)


for ind_ed in range(len(ed_df.BYTES_SENT)):
    for ind_pd in range(len(pd_df.BYTES_SENT)):
        if pd_df.MAC[ind_pd] == ed_df.MAC[ind_ed]:
            if pd_df.AP_NAME[ind_pd] == ed_df.AP_NAME[ind_ed]:
                if pd_df.BYTES_SENT[ind_pd] > ed_df.BYTES_SENT[ind_ed]:
                    print('Antigo -> ', pd_df.BYTES_SENT[ind_pd])
                    pd_df.BYTES_SENT_CALC[ind_pd] = pd_df.BYTES_SENT[ind_pd] - ed_df.BYTES_SENT[ind_ed]
                    print('Novo -> ', pd_df.BYTES_SENT_CALC[ind_pd])
#                 else:
#                     pd_df.BYTES_SENT_CALC[ind_pd] = pd_df.BYTES_SENT[ind_pd]
#             else:
#                 pd_df.BYTES_SENT_CALC[ind_pd] = pd_df.BYTES_SENT[ind_pd]
#         else:
#             pd_df.BYTES_SENT_CALC[ind_pd] = pd_df.BYTES_SENT[ind_pd]

pd_df = pd_df[['MAC', 'BYTES_SENT_CALC']]
