import os
import random
import requests
from flask import Flask, render_template, request
from QuoteEngine import ingestor, quote_model
from MemeGenerator import MemeEngine

app = Flask(__name__)
meme = MemeEngine('./static')

def setup():
    """ Load all resources """
    quote_files = [
        './_data/DogQuotes/DogQuotesTXT.txt',
        './_data/DogQuotes/DogQuotesDOCX.docx',
        './_data/DogQuotes/DogQuotesPDF.pdf',
        './_data/DogQuotes/DogQuotesCSV.csv'
    ]
    
    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))
    
    images_path = "./_data/photos/dog/"
    imgs = [os.path.join(images_path, name) for name in os.listdir(images_path) if os.path.isfile(os.path.join(images_path, name))]
    
    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """
    image_url = request.form['image_url']
    body = request.form['body']
    author = request.form['author']
    
    response = requests.get(image_url)
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
