import image

img = image.Image("adn.jpg")
width = img.getWidth()
height = img.getHeight()
win = image.ImageWin(width * 2, height * 2)
img.draw(win)
avgRed = 0
avgGreen = 0
avgBlue = 0

newimg = image.EmptyImage(width*2, height*2)

for row in range(height):
    for col in range(width):
        p = img.getPixel(col, row)

        # start at 1 and stop 1 short so border pixels are not evalutated
        while row > 0 and row < height - 1:
            while col > 0 and col < width - 1:
                p1 = img.getPixel(col - 1, row -1)
                p2 = img.getPixel(col, row -1)
                p3 = img.getPixel(col + 1, row -1)
                p4 = img.getPixel(col - 1, row)
                p5 = img.getPixel(col, row)
                p6 = img.getPixel(col + 1, row)
                p7 = img.getPixel(col - 1, row +1)
                p8 = img.getPixel(col, row +1)
                p9 = img.getPixel(col + 1, row +1)

                avgRed = (p1.getRed() + p2.getRed() + p3.getRed() + p4.getRed() + p5.getRed() +
                         p6.getRed() + p7.getRed() + p8.getRed() + p9.getRed())/9
                avgGreen = (p1.getGreen() + p2.getGreen() + p3.getGreen() + p4.getGreen() + p5.getGreen() +
                         p6.getGreen() + p7.getGreen() + p8.getGreen() + p9.getGreen())/9
                avgBlue = (p1.getBlue() + p2.getBlue() + p3.getBlue() + p4.getBlue() + p5.getBlue() +
                         p6.getBlue() + p7.getBlue() + p8.getBlue() + p9.getBlue())/9

        newpixel = image.Pixel(avgRed, avgGreen, avgBlue)

        newimg.setPixel(2*col, 2*row, newpixel)
        newimg.setPixel(2*col + 1, 2*row, newpixel)
        newimg.setPixel(2*col, 2*row + 1, newpixel)
        newimg.setPixel(2*col + 1, 2*row + 1, newpixel)

newimg.draw(win)
win.exitonclick()
