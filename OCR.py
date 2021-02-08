import  pytesseract
import requests
from PIL import Image
from PIL import  ImageFilter
import  io


def process_image(url):
    image= _get_image(url)
    image.filter(ImageFilter.SHARPEN)
    return pytesseract.image_to_string(image)

def _get_image(url):
    pattern_string = requests.get(url).content()
    return Image.open(io.StringIO(pattern_string))