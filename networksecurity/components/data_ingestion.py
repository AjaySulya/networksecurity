from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

# configuration for data ingestion config
from networksecurity.Entity.config_entity import DataIngestionConfig
from networksecurity.Entity.artifact_entity import DataIngestionArtifact
# basic bibraries
import os 
import sys
import pymongo
import numpy as np
import pandas as pd
from typing import List
from sklearn.model_selection import train_test_split

from dotenv import load_dotenv # for reading the mongo url
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")

# for the reading the dataset  we make the class
class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config # making the object.
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def export_collection_as_dataframe(self):
        """
        Read the from the MongoDB database 
        """
        try:
            database_name = self.data_ingestion_config.database_name
            collection_name = self.data_ingestion_config.collection_name
            self.mongoclient = pymongo.MongoClient(MONGO_DB_URL)
            collection = self.mongoclient[database_name][collection_name]
            df = pd.DataFrame(list(collection.find()))
            if df is None:
                print("No data fetch from DB.")
            # ny default wherever i read data from the mongo the is a column add id
            if "_id" in df.columns.tolist():
                df = df.drop(columns=["_id"],axis=1)
            df.replace({"na":np.nan},inplace=True)
            return df
        except Exception as e:
            raise NetworkSecurityException(e,sys)    
        
        
    def export_data_into_feature_store(self,dataframe:pd.DataFrame):
        feature_store_file_path = self.data_ingestion_config.feature_store_file_path
        # creating folder
        dir_name = os.path.dirname(feature_store_file_path)
        os.makedirs(dir_name,exist_ok=True)
        dataframe.to_csv(feature_store_file_path,index=False,header=True)
        return dataframe    
    
    
    def split_data_as_train_test(self, dataframe: pd.DataFrame):
        try:
            if dataframe is None or dataframe.empty:
                raise ValueError("DataFrame is empty, can't split into train and test set")
            train_set, test_set = train_test_split(
                dataframe,
                test_size=self.data_ingestion_config.train_test_split_ratio,
                random_state=42
            )
            logging.info("Performed train test split on dataframe")
            logging.info("Exited split_data_as_train_test method of DataIngestion class")
            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_path, exist_ok=True)
            logging.info("Exporting train & test file path")
            train_set.to_csv(self.data_ingestion_config.training_file_path, index=False, header=True)
            test_set.to_csv(self.data_ingestion_config.testing_file_path, index=False, header=True)
            logging.info("Exported train & test file path")
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    def initiate_data_ingestion(self):
        try:
            dataframe = self.export_collection_as_dataframe()
            dataframe = self.export_data_into_feature_store(dataframe)
            self.split_data_as_train_test(dataframe)
            dataingestionartifact = DataIngestionArtifact(
                train_file_path = self.data_ingestion_config.training_file_path,
                test_file_path = self.data_ingestion_config.testing_file_path)
            return dataingestionartifact
        except Exception as e:
            raise NetworkSecurityException(e,sys)  