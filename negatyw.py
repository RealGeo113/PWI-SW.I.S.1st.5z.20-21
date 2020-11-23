from PIL import Image


img = Image.open("./tablica.jpg")


for i in range(0, img.size[0] - 1):

    for j in range(0, img.size[1] - 1):

        pixelColor = img.getpixel((i, j))


        red= 255 - pixelColor[0]

        green = 255 - pixelColor[1]

        blue = 255 - pixelColor[2]


        img.putpixel((i, j), (red, green, blue))


img.show()
