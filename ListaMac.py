#criação do arquivo da lista MAC em .csv

import pandas as pd

df = pd.read_csv("users.csv", delim_whitespace=True)
df.columns = ["UserID", "Username", "IPADRESS", "MAC", "Status", "DATA", "HORA"]
mac_list = df['MAC']

mac_list.to_csv('mac_list.csv', index=False)
#%%
