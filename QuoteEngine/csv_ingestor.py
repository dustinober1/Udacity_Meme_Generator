from typing import List
import pandas as pd
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel

class CSVIngestor(IngestorInterface):
    """
    The CSVIngestor class is responsible for parsing quotes from CSV files.
    It inherits from the IngestorInterface and overrides the can_ingest and parse methods.
    This class can parse CSV files containing quotes and return a list of QuoteModel objects.
    
    :param allowed_extensions: List of string representing the file extensions this ingestor can handle.
    """
    
    allowed_extensions = ['csv']
    
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
            df = pd.read_csv(path)  # Reading the CSV file into a DataFrame
            for index, row in df.iterrows():  # Iterating over the rows of the DataFrame
                new_quote = QuoteModel(row['body'], row['author'])  # Creating a QuoteModel object for each row
                quotes.append(new_quote)  # Appending the QuoteModel object to the list of quotes
        except Exception as e:  # Handling any exceptions that occur during parsing
            print(f"Error occurred: {e}")  # Printing the error message
            return []  # Returning an empty list in case of an error
        return quotes  # Returning the list of QuoteModel objects
