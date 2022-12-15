#connecting python with mongodb, related code

import pandas as pd
import json
import pymongo
from dataclasses import dataclass

# Provide the mongodb localhost url to connect python to mongodb.
import os
@dataclass
class EnvironmentVariable:
    mongo_db_url:str = os.getenv('MONGO_DB_URL') #we are reading the url from .env file & storing that url into mongo_db_url which is a string

env_var = EnvironmentVariable()
mongo_client = pymongo.MongoClient(env_var.mongo_db_url)
TARGET_COLUMN = "class"

