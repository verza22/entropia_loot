import pytesseract
from PIL import Image,ImageGrab
import time

while(True):
    #Capture image
    img = ImageGrab.grab(bbox=(0,0,400,650))

    #Transform image to black and white
    image_file = img.convert('L')

    #img to text
    text = pytesseract.image_to_string(image_file)
    print(text)

    #sleep 2 seconds
    time.sleep(2)