from df_users_and_stations import df
from actions import (os, load_dotenv)

load_dotenv()

# df.to_csv(os.getenv('dir_users_stations'), sep=';', header=True, index=False, line_terminator='\n')
df.to_csv(sep=';', na_rep=0, header=False, index=False, line_terminator='\n', retur_format='string')

#%%
