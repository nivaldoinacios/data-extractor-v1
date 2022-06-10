from etl import Lista
import pandas as pd

global df_access_users

df_access_users = pd.DataFrame(Lista.users,
                               columns=["UserID", "Username", "IPADDRESS", "MAC",
                                        "Status", "@timestamp-py"]
                               )

df_access_users