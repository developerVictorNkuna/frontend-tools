import sys
import requests
import  pytesseract

from PIL import  Image
import io

def get_image(url):
    return Image.open(io.StringIO(requests.get(url).content))

if __name__ == '__main__':
    """tool to tet the raw input of pytessecract withgiven input"""
    sys.stdout.write("""
===OOOO=====CCCCC===RRRRRR=====\n
==OO==OO===CC=======RR===RR====\n
==OO==OO===CC=======RR===RR====\n
==OO==OO===CC=======RRRRRR=====\n
==OO==OO===CC=======RR==RR=====\n
==OO==OO===CC=======RR== RR====\n
===OOOO=====CCCCC===RR====RR===\n\n
""")
    sys.stdout.write("A simple OCR utility\n")
    url = input("What is the url of the image you would like to analyze?\n")
    image = get_image(url)
    sys.stdout.write("The raw output from tesseract with no processing is:\n\n")
    sys.stdout.write("-----------------BEGIN-----------------\n")
    sys.stdout.write(pytesseract.image_to_string(image) + "\n")
    sys.stdout.write("------------------END------------------\n")
