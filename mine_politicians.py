import os
import time
from datetime import datetime, timedelta
from src.twitter.tweets import store_politician_tweets
import pandas as pd
import nest_asyncio

# In order to run multiple asynchronous calls in twint
# we need to apply() nest_asyncio
nest_asyncio.apply()

# Constants
SINCE = "2020-01-01"

# Get absolute path of project folder
folder = os.path.dirname(os.path.abspath(__file__))

# Get the list of politicans to mine
politician_list = folder + "/data/politicians.csv"
politicians = pd.read_csv(politician_list)

# Go through each politican and store their tweets
for index, row in politicians.iterrows():
    print(row["username"])
    store_politician_tweets(folder=folder, 
    since=SINCE, 
    username=row["username"][1:])
    time.sleep(15)



