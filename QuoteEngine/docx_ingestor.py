# docx_ingestor.py
import docx
from typing import List
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel

class DOCXIngestor(IngestorInterface):
    
    allowed_extensions = ['docx']
    
    @classmethod
    def can_ingest(cls, path: str) -> bool:
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        quotes = []
        try:
            doc = docx.Document(path)
            for paragraph in doc.paragraphs:
                if paragraph.text != "":
                    body, author = paragraph.text.split(' - ')
                    quotes.append(QuoteModel(body, author))
        except Exception as e:
            print(f"Error occurred: {e}")
            return []
        return quotes
