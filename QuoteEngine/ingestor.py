# ingestor.py
from .ingestor_interface import IngestorInterface
from .csv_ingestor import CSVIngestor
from .docx_ingestor import DOCXIngestor
from .pdf_ingestor import PDFIngestor
from .txt_ingestor import TXTIngestor

class Ingestor(IngestorInterface):
    
    ingestors = [CSVIngestor, DOCXIngestor, PDFIngestor, TXTIngestor]
    
    @classmethod
    def can_ingest(cls, path: str) -> bool:
        return any(ingestor.can_ingest(path) for ingestor in cls.ingestors)
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
        print(f"Cannot parse the file {path}")
        return []
