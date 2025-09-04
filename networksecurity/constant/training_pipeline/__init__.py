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

""""
Data Ingestion Related constant start with DATA_INGESTION VAR NAME
. this are my constant variable names
"""
DATA_INGESTION_COLLECTION_NAME:str = "NetworkData" 
DATA_INGESTION_DATABASE_NAME:str = "Ajay"
DATA_INGESTION_DIR_NAME:str = "data_ingestion"
DATA_INGESTION_FEATURE_STRORE_DIR:str = "feature_store"
DATA_INGESTION_INGESTED_DIR:str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO:float = 0.2
