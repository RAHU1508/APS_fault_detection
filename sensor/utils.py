#creating dataframe from the dataset fetched from mongodb. This is one helper function. 

import pandas as pd
from sensor.config import mongo_client  #mongo_client is created as the environment variable which is holding the url of mongodb from where data is needed to be fetched. see config.py
from sensor.logger import logging
from sensor.exception import SensorException
import os, sys


def get_collection_as_dataframe(database_name:str, collection_name:str) -> pd.DataFrame:
    """
    Description: This function return collection as dataframe
    =========================================================
    Params:
    database_name: database name
    collection_name: collection name
    =========================================================
    return Pandas dataframe of a collection
    """
    try:
        logging.info(f"Reading data from database: {database_name} and collection: {collection_name}")
        df=pd.DataFrame(list(mongo_client[database_name][collection_name].find())) #find function will return all the records, this will return generator (cursor) & we need to typecast it into list
        logging.info(f"Found columns: {df.columns}")
        if "_id" in df.columns:  # first column called _id is created by mongodb which is not required, so this column needs to be dropped, before that check if it is present
            logging.info(f"Dropping column: _id ")
            df = df.drop("_id",axis=1)
        logging.info(f"Row and columns in df: {df.shape}")
        return df
    except Exception as e:
        raise SensorException(e, sys)