from PIL import Image

# Open an image, show its size and format
img = Image.open("79.jpg")
print(img.size)
print(img.format)

# Show the image on an outside application
img.show()

# Crop the image
# Starting x, starting y, ending x, ending y
area = (100, 100, 300, 375)
croppedImg = img.crop(area)
croppedImg.show()

# Combine two images
img2 = Image.open("150.jpg")
print(img2.size)
# Starting x, starting y, beginning x, beginning y
area2 = (1, 15, 400, 420)
# Pasting img onto img2
img2.paste(img, area2)
img2.show()