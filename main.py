from dataframes.df_users_and_stations import df
from elasticsearch import Elasticsearch
import pandas as pd
import numpy as np
import eland as ed

df = ed.pandas_to_eland(
    df,

)
