import pymongo
import pandas as pd
import json
# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATA_FILE_PATH='/config/workspace/aps_failure_training_set1.csv'
DATABASE_NAME='aps'
COLLECTION_NAME='sensor'

if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    #print(f'Rows & Columns: {df.shape}')

    #converting dataframe to json format so that it can be dumped in mongodb
    df.reset_index(drop=True, inplace=True)
    json_record = list(json.loads(df.T.to_json() ).values())#.T will transpose the rows to columns & vice versa
    #print(json_record[0])

    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)