"""
This file integrates with the other injester modules
"""
from typing import List
from .ingestor_interface import IngestorInterface
from .csv_ingestor import CSVIngestor
from .docx_ingestor import DOCXIngestor
from .pdf_ingestor import PDFIngestor
from .txt_ingestor import TXTIngestor
from .quote_model import QuoteModel

class Ingestor(IngestorInterface):
    """
    The Ingestor class is responsible for selecting the appropriate concrete ingestor
    to parse quotes from files with different formats. It inherits from the IngestorInterface
    and overrides the can_ingest and parse methods.
    
    :param ingestors: List of concrete ingestor classes that can parse different file formats.
    """

    ingestors = [CSVIngestor, DOCXIngestor, PDFIngestor, TXTIngestor]

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """
        Check if any of the available concrete ingestors can ingest the given file.

        :param path: String representing the path of the file to be ingested.
        :return: Boolean, True if any of the available ingestors can ingest the
        file, False otherwise.
        """
        return any(ingestor.can_ingest(path) for ingestor in cls.ingestors)

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Select the appropriate concrete ingestor to parse the given file and return a list
        of QuoteModel objects.

        :param path: String representing the path of the file to be parsed.
        :return: List of QuoteModel objects representing the quotes found in the file,
        or an empty list if no suitable ingestor is found.
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
        print(f"Cannot parse the file {path}")
        return []
