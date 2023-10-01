"""
This file injest txt files.
"""
from typing import List
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel

class TXTIngestor(IngestorInterface):
    """
    The TXTIngestor class is responsible for parsing quotes from TXT files.
    It inherits from the IngestorInterface and overrides the can_ingest and parse methods.
    This class can parse TXT files containing quotes and return a list of QuoteModel objects.

    :param allowed_extensions: List of string representing the file extensions this 
    ingestor can handle.
    """

    allowed_extensions = ['txt']

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
            with open(path, 'r') as file:
                for line in file.readlines():
                    body, author = line.strip().split(' - ')
                    quotes.append(QuoteModel(body, author))
        except Exception as error:
            print(f"Error occurred: {error}")
            return []
        return quotes
