#criação do arquivo da lista MAC em .csv
# import access_user
from dotenv import load_dotenv
import pandas as pd
import os

load_dotenv()

df = pd.read_csv(os.getenv('dir_users'), delim_whitespace=True)
df.columns = ["UserID", "Username", "IPADDRESS", "MAC", "Status", "@timestamp-py"]
mac_list = df['MAC']

mac_list.to_csv(os.getenv('dir_mac'), index=False)
#%%
df
#%%
mac_list
#%%
