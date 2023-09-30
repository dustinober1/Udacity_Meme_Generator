"""
app.py
"""
import os
import random
import requests
from flask import Flask, render_template, request
from QuoteEngine.ingestor import Ingestor
from MemeGenerator.meme_engine import MemeEngine

app = Flask(__name__)
meme = MemeEngine('./static')

def setup():
    """ 
    Load all resources including quote files and images.
    
    :return: Tuple containing a list of quotes and a list of image paths.
    """
    quote_files = [
        './_data/DogQuotes/DogQuotesTXT.txt',
        './_data/DogQuotes/DogQuotesDOCX.docx',
        './_data/DogQuotes/DogQuotesPDF.pdf',
        './_data/DogQuotes/DogQuotesCSV.csv'
    ]

    quotes = []
    for file in quote_files:
        quotes.extend(Ingestor.parse(file))

    images_path = "./_data/photos/dog/"
    imgs = [os.path.join(images_path, name) for name in
            os.listdir(images_path) if os.path.isfile
            (os.path.join(images_path, name))]
    return quotes, imgs

quotes, imgs = setup()

@app.route('/')
def meme_rand():
    """ 
    Generate and display a random meme.
    
    :return: Rendered template displaying a random meme.
    """
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ 
    Display form for user to input meme information.
    
    :return: Rendered template displaying the form.
    """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ 
    Create and display a user-defined meme based on form input.
    
    :return: Rendered template displaying the user-defined meme or an error message.
    """
    image_url = request.form['image_url']
    body = request.form['body']
    author = request.form['author']

    response = requests.get(image_url, timeout=10)
    if response.status_code != 200:
        return 'Error: Unable to fetch the image URL', 400

    tmp_path = './static/_tmp_image.jpg'
    with open(tmp_path, 'wb') as tmp_file:
        tmp_file.write(response.content)

    path = meme.make_meme(tmp_path, body, author)
    os.remove(tmp_path)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
