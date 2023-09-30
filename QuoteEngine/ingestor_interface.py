# ingestor_interface.py
from abc import ABC, abstractmethod
from typing import List
from .quote_model import QuoteModel

class IngestorInterface(ABC):
    
    @classmethod
    @abstractmethod
    def can_ingest(cls, path: str) -> bool:
        pass
    
    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass
