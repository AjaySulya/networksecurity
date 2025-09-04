from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.Entity.config_entity import DataIngestionConfig
from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.Entity.config_entity import TrainingPipelineConfig
import sys

if __name__=="__main__":
    try:
        
        training_pipeline_config = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        data_ingestion = DataIngestion(data_ingestion_config=dataingestionconfig)
        logging.info("Initiate data ingestion")
        dataingestionartifacts = data_ingestion.initiate_data_ingestion()
        print(dataingestionartifacts)
    except Exception as e:
        raise NetworkSecurityException(e,sys)
