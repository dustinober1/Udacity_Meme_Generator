"""
meme.py
"""
import os
import random
import argparse
from QuoteEngine.ingestor import Ingestor
from QuoteEngine import quote_model
from MemeGenerator.meme_engine import MemeEngine

def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given a path and a quote """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = [os.path.join(images, name) for name in os.listdir(images)
                if os.path.isfile(os.path.join(images, name))]
        img = random.choice(imgs)
    else:
        img = path

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f_x in quote_files:
            quotes.extend(Ingestor.parse(f_x))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise ValueError('Author is required if a body is provided')
        quote = quote_model.QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate a Meme.')
    parser.add_argument('--path', type=str, help='path to an image file')
    parser.add_argument('--body', type=str, help='quote body to add to the image')
    parser.add_argument('--author', type=str, help='quote author to add to the image')

    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
