"""In an MLOps project, a constant file (often named `constant.py`) typically contains fixed values used throughout the project, such as:

- Directory paths (e.g., for data, models, logs)
- File names
- Configuration keys
- Environment variable names
- Training parameters (e.g., batch size, epochs)
- Status codes or labels

This helps centralize configuration and makes the codebase easier to maintain.

This often use to contains the constaint variables , object or file path which i use the throughout the project #myunderstading
"""
import os 
import sys
import pandas as pd
import numpy as np

"""
Define the comman constant variable for the training pipeline
"""
TARGET_COLUMN = "Result"
PIPELINE_NAME:str = "NetworkData"
ARTIFACT_DIR:str = "Artifacts"
FILE_NAME:str = "phisingData.csv"
TRAIN_FILE_NAME:str = "train.csv"
TEST_FILE_NAME:str = "test.csv"


SCHEMA_FILE_PATH:str = os.path.join("data_schema","schema.yaml")

""""
Data Ingestion Related constant start with DATA_INGESTION VAR NAME
. this are my constant variable names
"""
DATA_INGESTION_COLLECTION_NAME:str = "NetworkData" 
DATA_INGESTION_DATABASE_NAME:str = "AJAY"
DATA_INGESTION_DIR_NAME:str = "data_ingestion"
DATA_INGESTION_FEATURE_STRORE_DIR:str = "feature_store"
DATA_INGESTION_INGESTED_DIR:str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO:float = 0.2

"""
Data Validation related constant  start with DATA_VALIDATION VAR NAME 
"""
DATA_VALIDATION_DIR_NAME:str = "data_validation"
DATA_VALIDATION_VALID_DIR:str = "validated"
DATA_VALIDATION_INVALID_DIR:str = "invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR:str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_PATH:str = "report.yaml"