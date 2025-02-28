import os
import urllib.request as request
from src.datascience import logger
import zipfile
from src.datascience.entity.config_entity import (DataIngestionConfig)

## Component- Data Ingestion
class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config=config

    # Download the file from the source
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers= request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} downloaded successfully, with info: \n{headers}")
        else:
            logger.info("File already exists")

    #Extract the zip file
    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)