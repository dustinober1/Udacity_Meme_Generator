"""
This modeule ingest csv files
"""
from typing import List
import pandas as pd
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel

class CSVIngestor(IngestorInterface):
    """
    The CSVIngestor class is responsible for parsing quotes from CSV files.
    It inherits from the IngestorInterface and overrides the can_ingest and parse methods.
    This class can parse CSV files containing quotes and return a list of QuoteModel objects.
    :param allowed_extensions: List of string representing the file extensions this ingestor 
    can handle.
    """

    allowed_extensions = ['csv']

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """
        Check if the given file can be ingested by this ingestor.
        
        :param path: String representing the path of the file to be ingested.
        :return: Boolean, True if the file can be ingested, False otherwise.
        """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse the given file and return a list of QuoteModel objects.
        
        :param path: String representing the path of the file to be parsed.
        :return: List of QuoteModel objects representing the quotes found in the file.
        """
        quotes = []
        try:
            dataframe = pd.read_csv(path)
            for row in dataframe.iterrows():
                new_quote = QuoteModel(row['body'], row['author'])
                quotes.append(new_quote)
        except Exception as error:
            print(f"Error occurred: {error}")
            return []
        return quotes
