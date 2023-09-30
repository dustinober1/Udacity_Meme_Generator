import docx
from typing import List
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel

class DOCXIngestor(IngestorInterface):
    """
    The DOCXIngestor class is responsible for parsing quotes from DOCX files.
    It inherits from the IngestorInterface and overrides the can_ingest and parse methods.
    This class can parse DOCX files containing quotes and return a list of QuoteModel objects.
    
    :param allowed_extensions: List of string representing the file extensions this ingestor can handle.
    """
    
    allowed_extensions = ['docx']
    
    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """
        Check if the given file can be ingested by this ingestor.
        
        :param path: String representing the path of the file to be ingested.
        :return: Boolean, True if the file can be ingested, False otherwise.
        """
        ext = path.split('.')[-1]  # Extracting the file extension from the path
        return ext in cls.allowed_extensions  # Checking if the file extension is in the list of allowed extensions
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse the given file and return a list of QuoteModel objects.
        
        :param path: String representing the path of the file to be parsed.
        :return: List of QuoteModel objects representing the quotes found in the file.
        """
        quotes = []  # Initializing the list to store the QuoteModel objects
        try:
            doc = docx.Document(path)  # Loading the DOCX file
            for paragraph in doc.paragraphs:  # Iterating over the paragraphs in the document
                if paragraph.text != "":  # Checking if the paragraph is not empty
                    body, author = paragraph.text.split(' - ')  # Extracting the body and author from the paragraph text
                    quotes.append(QuoteModel(body, author))  # Creating and appending a QuoteModel object to the list of quotes
        except Exception as e:  # Handling any exceptions that occur during parsing
            print(f"Error occurred: {e}")  # Printing the error message
            return []  # Returning an empty list in case of an error
        return quotes  # Returning the list of QuoteModel objects
