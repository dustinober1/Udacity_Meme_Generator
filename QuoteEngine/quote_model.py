class QuoteModel:
    """
    The QuoteModel class represents a quote with a body and an author.
    It is used to encapsulate the quote's body and author as a single object.
    
    :param body: String representing the body of the quote.
    :param author: String representing the author of the quote.
    """
    
    def __init__(self, body: str, author: str):
        """
        Initialize the QuoteModel object with the given body and author.
        
        :param body: String representing the body of the quote.
        :param author: String representing the author of the quote.
        """
        self.body = body  # Setting the body of the quote
        self.author = author  # Setting the author of the quote
