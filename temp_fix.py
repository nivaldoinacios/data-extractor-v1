from df_users_and_stations import df
from actions import (os, load_dotenv)

load_dotenv()

df.to_csv(os.getenv('dir_users_stations'), sep=';', header=True, index=False, line_terminator='\n')
