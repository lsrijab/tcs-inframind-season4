"""pip install opencv-python
pip install pytesseract
pip install tesseract
pip install tesseract-ocr"""
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
text=pytesseract.image_to_string(r'img.jpg')
file = open("recognized.txt", "w+") 
file.write(text) 
file.close() 

