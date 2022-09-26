import pyshorteners
import pyqrcode
from PIL import Image

def shortner(blink):
    if len(blink) > 30:
        shortener = pyshorteners.Shortener()
        short_link = shortener.tinyurl.short(blink)
    return short_link

def qr_generater(blink):
    short_link = shortner(blink)
    qr = pyqrcode.create(short_link)
    qr.png('myqr.png', scale = 10)
    im = Image.open("myqr.png")
    im.show()

blink = input("Enter the link: ")
n = int(input("Select 1 for Reduce the URL\nSelect 2 to Generate QR Coad "))
if n == 1:
    print(shortner(blink))
elif n == 2:
    qr_generater(blink)
else:
    print("Select Proper option!")