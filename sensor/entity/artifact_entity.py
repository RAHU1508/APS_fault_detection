from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:   #contains the path for those files
    feature_store_file_path:str
    train_file_path:str 
    test_file_path:str

@dataclass
class DataValidationArtifact:
    report_file_path:str      #contains the path where the generated report will be getting stored

class DataTransformationArtifact:...
class ModelTrainerArtifact:...
class ModelEvaluationArtifact:...
class ModelPusherArtifact:...