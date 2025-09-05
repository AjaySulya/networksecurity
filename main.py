from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig
from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.entity.config_entity import TrainingPipelineConfig
import sys

if __name__=="__main__":
    try:
        
        training_pipeline_config = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        data_ingestion = DataIngestion(data_ingestion_config=dataingestionconfig)
        logging.info("Initiate data ingestion")
        dataingestionartifacts = data_ingestion.initiate_data_ingestion()
        logging.info("Data Ingestion completed.")
        print(dataingestionartifacts)
        data_validation_config = DataValidationConfig(training_pipelineconfig=training_pipeline_config)
        data_validation = DataValidation(data_ingestion_artifact=dataingestionartifacts,
                       data_validation_config=data_validation_config)
        logging.info("Initiate Data Validation")
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info("Data Validation Completed")
        print(data_validation_artifact)
    except Exception as e:
        raise NetworkSecurityException(e,sys)
