import random
import urllib.request

def downloadImage(url):
    name = random.randrange(1, 1000)
    fullName = str(name) + ".jpg"
    urllib.request.urlretrieve(url, fullName)

downloadImage("https://upload.wikimedia.org/wikipedia/commons/f/f9/Romeo_and_Juliet_%28watercolour%29_by_Ford_Maddox_Brown.jpg")