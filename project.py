from PIL import Image


def scale(source, ratio):
    image = Image.open(source)
    width = image.size[0] * ratio
    height = image.size[1] * ratio
    resizedimage = image.resize((width, height), Image.ANTIALIAS)

    return resizedimage


def gray(source):

    image = Image.open(source);

    for i in range(0, image.size[0] - 1):

        for j in range(0, image.size[1] - 1):

            pixelColor = image.getpixel((i, j))

            newpixel = round((pixelColor[0]+pixelColor[1]+pixelColor[2])/3)
            image.putpixel((i, j), (newpixel, newpixel, newpixel))

    return image


def lumi(source, ratio):

    image = Image.open(source)
    newpixel = [1,2,3]
    for i in range(0, image.size[0] - 1):

        for j in range(0, image.size[1] - 1):

            pixelColor = image.getpixel((i, j))

            for k in range(0,3):
                newpixel[k] = round(float(pixelColor[k])*float(ratio)/100)

            image.putpixel((i, j), (newpixel[0], newpixel[1], newpixel[2]))

    return image


def negative(source):

    image = Image.open(source)
    for i in range(0, image.size[0] - 1):
        for j in range(0, image.size[1] - 1):

            pixelcolor = image.getpixel((i, j))

            red = 255 - pixelcolor[0]

            green = 255 - pixelcolor[1]

            blue = 255 - pixelcolor[2]

            image.putpixel((i, j), (red, green, blue))

    return image
