from df_statistics import *
from df_base import *
import pandas as pd

df = pd.merge(df, pd_df, how='outer', on=['MAC'])

print(df)
