from PIL import Image, ImageDraw, ImageFont
import os

class MemeEngine:
    def __init__(self, output_dir):
        self._output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
    
    def make_meme(self, img_path: str, text: str, author: str, width=500) -> str:
        """
        Create a meme with the given image, quote body, and author.
        
        :param img_path: Path to the image file
        :param text: Quote body to be added to the image
        :param author: Author of the quote to be added to the image
        :param width: Desired width of the image. Default is 500px.
        :return: Path to the created meme image.
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
        except Exception as e:
            print(f"Error occurred: {e}")
            return None
