try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

def OCR(source):
    pytesseract.pytesseract.tesseract_cmd = r'F:\Program Files\Tesseract-OCR\tesseract.exe'

    return (pytesseract.image_to_string(source, lang="pol"))
