
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

df = pd.read_csv(os.getenv('dir_neighbors'))

print(df)

