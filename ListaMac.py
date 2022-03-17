#criação do arquivo da lista MAC em .csv
from dotenv import load_dotenv
import pandas as pd
import os

load_dotenv()

df = pd.read_csv(os.getenv('dir_users'), delim_whitespace=True)
df.columns = ["UserID", "Username", "IPADRESS", "MAC", "Status", "DATA", "HORA"]
mac_list = df['MAC']

mac_list.to_csv(os.getenv('dir_mac'), index=False)
#%%
