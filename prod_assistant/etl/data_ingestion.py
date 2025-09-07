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

        """Initialize the DataIngestion with configuration and model loader."""
        pass


    def load_env_varaibles(self):

        """Load environment variables from a .env file."""
        pass

    def get_csv_path(self):
        """Get the path to the CSV file containing product reviews."""
        pass

    def load_csv(self):
        """Load data from the CSV file into a pandas DataFrame."""
        pass

    def transform_data(self):
        """Transform the DataFrame into a list of Document objects."""
        pass

    def store_in_vector_db(self):
        """Store the list of Document objects into AstraDB vector database."""
        pass

    def run_pipeline(self):
        """Run the complete data ingestion pipeline."""
        pass