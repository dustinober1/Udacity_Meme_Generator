# csv_ingestor.py
import pandas as pd
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel

class CSVIngestor(IngestorInterface):
    
    allowed_extensions = ['csv']
    
    @classmethod
    def can_ingest(cls, path: str) -> bool:
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        quotes = []
        try:
            df = pd.read_csv(path)
            for index, row in df.iterrows():
                new_quote = QuoteModel(row['body'], row['author'])
                quotes.append(new_quote)
        except Exception as e:
            print(f"Error occurred: {e}")
            return []
        return quotes
