#criação do arquivo da lista MAC em .csv
#Adicionar dependencia à access-user.py para sempre obter uma lista atualizada
import access_user
from dotenv import load_dotenv
import pandas as pd
import os

load_dotenv()

df = pd.read_csv(os.getenv('dir_users'), delim_whitespace=True)
df.columns = ["UserID", "Username", "IPADDRESS", "MAC", "Status", "DATA", "HORA"]
mac_list = df['MAC']

mac_list.to_csv(os.getenv('dir_mac'), index=False)
#%%
