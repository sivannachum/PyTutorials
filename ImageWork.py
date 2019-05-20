from PIL import Image

# Open an image, show its size and format
img = Image.open("79.jpg")
print(img.size)
print(img.format)

# Show the image on an outside application
# img.show()

# Crop the image
# Starting x, starting y, ending x, ending y
area = (100, 100, 300, 375)
croppedImg = img.crop(area)
# croppedImg.show()

# Combine two images
img2 = Image.open("150.jpg")
print(img2.size)
# Starting x, starting y, beginning x, beginning y
area2 = (1, 15, 400, 420)
# Pasting img onto img2
img2.paste(img, area2)
# img2.show()

# Make sure the image only has three channels (RGB)
print(img.mode)
# Split the image into its red, green, and blue channels
r, g, b = img.split()
# r.show()
# g.show()
# b.show()
newImage = Image.merge("RGB", (r, g, b))
# newImage.show()
newImage = Image.merge("RGB", (b, g, r))
# newImage.show()
newImage = Image.merge("RGB", (r, b, g))
# newImage.show()
newImage = Image.merge("RGB", (g, b, r))
# newImage.show()

croppedImg2 = img2.crop(area)
r1, g1, b1 = croppedImg.split()
r2, g2, b2 = croppedImg2.split()
newImage = Image.merge("RGB", (r1, g2, b1))
# newImage.show()

# Resize an image
squareImg = img.resize((399, 399))
# squareImg.show()
# Flip an image
# Can also do FLIP_LEFT_RIGHT
flipImg = img.transpose(Image.FLIP_TOP_BOTTOM)
# flipImg.show()
# Rotate an image
# Can also do 180 or 270
spinImg = img.transpose(Image.ROTATE_90)
# spinImg.show()

