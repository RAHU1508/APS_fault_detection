import os, sys
from sensor.exception import SensorException
from sensor.logger import logging
from datetime import datetime

FILE_NAME = "sensor.csv"
TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"

class TrainingPipelineConfig:
     def __init__(self):
        try:
            self.artifact_dir = os.path.join(os.getcwd(),"artifact",f"{datetime.now().strftime('%m%d%Y__%H%M%S')}") #folder named 'artifact' is created in the current directory. For every timestamp, new folder will be created in the 'artifact' directory & all the outputs corresponding to that timestamp will get stored in that folder.
        except Exception  as e:
            raise SensorException(e,sys)  

class DataIngestionConfig:
    def __init__(self, training_pipeline_config:TrainingPipelineConfig): #object of above class is passed as a parameter in this class so folder structure from above will get inherited in this class which is noting but artifact directory & within it, timestamps directory
        try:
            self.database_name="aps"
            self.collection_name="sensor"
            self.data_ingestion_dir = os.path.join(training_pipeline_config.artifact_dir , "data_ingestion") #data_ingestion_dir folder will get created in each of the timestamps directory
            self.feature_store_file_path = os.path.join(self.data_ingestion_dir,"feature_store",FILE_NAME)
            self.train_file_path = os.path.join(self.data_ingestion_dir,"dataset",TRAIN_FILE_NAME)
            self.test_file_path = os.path.join(self.data_ingestion_dir,"dataset",TEST_FILE_NAME)
            self.test_size = 0.2
        except Exception  as e:
            raise SensorException(e,sys)     
    
    def to_dict(self,)->dict:   #we want all the outputs in the JSON format which is nothing but dictionary in order to store them in mongodb, dataset will be called from mongodb & converted into dataframe after which dataset is ready for train-test split
        try:
            return self.__dict__
        except Exception  as e:
            raise SensorException(e,sys)     


class DataValidationConfig:...
class DataTransformationConfig:...
class ModelTrainerConfig:...
class ModelEvaluationConfig:...
class ModelPusherConfig:...