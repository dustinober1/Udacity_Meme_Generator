# txt_ingestor.py
from typing import List
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel

class TXTIngestor(IngestorInterface):
    
    allowed_extensions = ['txt']
    
    @classmethod
    def can_ingest(cls, path: str) -> bool:
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        quotes = []
        try:
            with open(path, 'r') as file:
                for line in file.readlines():
                    body, author = line.strip().split(' - ')
                    quotes.append(QuoteModel(body, author))
        except Exception as e:
            print(f"Error occurred: {e}")
            return []
        return quotes
