"""
This module is responsible for generating memes by adding text to images.
"""
import os
from PIL import Image, ImageDraw, ImageFont

class MemeEngine:
    """
    The MemeEngine class is responsible for creating meme images.
    It takes an image and adds a quote with its author as text to the image,
    then saves the modified image to a specified output directory.

    :param output_dir: The directory where the generated memes will be saved.
    """

    def __init__(self, output_dir: str):
        """
        Initialize the MemeEngine object with the specified output directory.
        
        :param output_dir: The directory where the generated memes will be saved.
        """
        self._output_dir = output_dir  # Setting the output directory for the memes
        os.makedirs(output_dir, exist_ok=True)  # Creating the output directory if it does not exist

    def make_meme(self, img_path: str, text: str, author: str, width=500) -> str:
        """
        Create a meme with the given image, quote body, and author.
        
        :param img_path: Path to the image file.
        :param text: Quote body to be added to the image.
        :param author: Author of the quote to be added to the image.
        :param width: Desired width of the image. Default is 500px.
        :return: Path to the created meme image, or None if an error occurs.
        """
        try:
            img = Image.open(img_path)
            ratio = width / float(img.width)
            height = int(ratio * float(img.height))
            img = img.resize((width, height), Image.NEAREST)

            draw = ImageDraw.Draw(img)
            font = ImageFont.load_default()
            text = f"{text} - {author}"
            text_position = (10, img.height - 30)
            draw.text(text_position, text, font=font, fill="white")

            output_path = os.path.join(self._output_dir, 'meme.jpg')
            img.save(output_path)
            return output_path
        except (FileNotFoundError, IOError) as file_error:
            print(f"Error occurred: {file_error}")
            return None
