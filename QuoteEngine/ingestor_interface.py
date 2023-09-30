from abc import ABC, abstractmethod
from typing import List
from .quote_model import QuoteModel

class IngestorInterface(ABC):
    """
    The IngestorInterface class is an abstract base class that defines the interface
    for all concrete ingestor classes. It declares the can_ingest and parse methods
    that all concrete ingestor classes must implement.
    
    Concrete ingestor classes are responsible for parsing quotes from files with
    different formats and returning a list of QuoteModel objects.
    """
    
    @classmethod
    @abstractmethod
    def can_ingest(cls, path: str) -> bool:
        """
        Abstract method to check if the given file can be ingested by the concrete ingestor.
        
        :param path: String representing the path of the file to be ingested.
        :return: Boolean, True if the file can be ingested, False otherwise.
        """
        pass
    
    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Abstract method to parse the given file and return a list of QuoteModel objects.
        
        :param path: String representing the path of the file to be parsed.
        :return: List of QuoteModel objects representing the quotes found in the file.
        """
        pass
