import sys
from Xray.entity.artificat_entity import DataIngestionArtifact
from Xray.entity.config_entity import DataIngestionConfig
from Xray.exception import XrayException
from Xray.logger import logging
from Xray.cloud_storage.azure_blob_operations import azureBolbOperation


class DataIgnestion:
    def __init__(self) :
        pass
    def get_data_from_blob(self):
        try:
            pass
        except Exception as e:
            XrayException(e,sys)
    
    def initiate_data_ingestion(self):
        try:
            pass
        except Exception as e:
            XrayException(e,sys)

