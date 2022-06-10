from elasticsearch import Elasticsearch
from etl import Lista
import pandas as pd
import eland as ed
import os

es = Elasticsearch(
    ['http://192.168.10.14:9200'],
    basic_auth=('nivaldo', '#Roost2021!')
)

pd = pd.DataFrame(Lista.statistics,
                             columns=["MAC", "PCKT_SENT", "PCKT_RECEIVED", "BYTES_SENT",
                                      "BYTES_RECEIVED", "WID_RATE_SENT", "WID_RATE_RECEIVED",
                                      "TRIGGER_R_TOTAL", "TRIGGER_R_FAILED", "STA_POWER_SAVE"]
                             )
#%%

query_size = len(pd)

ed = ed.DataFrame(es, 'eland-fluxo').tail(query_size)
#%%
ed_df = ed[['MAC', 'BYTES_SENT', 'BYTES_RECEIVED', '@timestamp-py']]
ed_df = ed_df.to_pandas()
#%%
ed_df
#%%
pd[['MAC', 'BYTES_SENT', 'BYTES_RECEIVED']]

#%%



#%%
