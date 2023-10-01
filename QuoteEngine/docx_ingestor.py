"""
This modeule ingest docx files
"""
from typing import List
import docx
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel

class DOCXIngestor(IngestorInterface):
    """
    The DOCXIngestor class is responsible for parsing quotes from DOCX files.
    It inherits from the IngestorInterface and overrides the can_ingest and parse methods.
    This class can parse DOCX files containing quotes and return a list of QuoteModel objects.

    :param allowed_extensions: List of string representing the file extensions 
    this ingestor can handle.
    """

    allowed_extensions = ['docx']

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
            doc = docx.Document(path)
            for paragraph in doc.paragraphs:
                if paragraph.text != "":
                    body, author = paragraph.text.split(' - ')
                    quotes.append(QuoteModel(body, author))
        except Exception as error:
            print(f"The following error occured: {error}")
            return []
        return quotes
