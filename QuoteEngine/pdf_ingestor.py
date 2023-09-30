# pdf_ingestor.py
import fitz
from typing import List
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel

class PDFIngestor(IngestorInterface):
    
    allowed_extensions = ['pdf']
    
    @classmethod
    def can_ingest(cls, path: str) -> bool:
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        quotes = []
        try:
            with fitz.open(path) as doc:
                for page_num in range(len(doc)):
                    page = doc[page_num]
                    text = page.get_text()
                    for line in text.split('\n'):
                        if line != "":
                            body, author = line.strip().split(' - ')
                            quotes.append(QuoteModel(body, author))
        except Exception as e:
            print(f"Error occurred: {e}")
            return []
        return quotes
