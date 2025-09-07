import os
import pandas as pd
from dotenv import load_dotenv
from typing import List, Dict
from langchain_core.documents import Document
from langchain_astradb import AstraDBVectorStore
from prod_assistant.utils.model_loader import ModelLoader
from prod_assistant.utils.config_loader import load_config

class DataIngestion:
    
    """Class to handle data ingestion from various sources and store in AstraDB.
    class to handle transforming and loading data into AstraDB vector database."""


    def __init__(self):
        pass


    def load_env_varaibles(self):
        pass

    def get_csv_path(self):
        pass

    def load_csv(self):
        pass

    def transform_data(self):
        pass

    def store_in_vector_db(self):
        pass

    def run_pipeline(self):
        pass