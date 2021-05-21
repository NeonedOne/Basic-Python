# Алексей Головлев, группа БСБО-07-19

from PIL import Image


def makeanagliph(filename, delta):
    im = Image.open(filename)
    x, y = im.size
    result_image = Image.new('RGB', (x, y), (0, 0, 0))
    another_pixel = result_image.load()
    pixel = im.load()
    for i in range(x):
        for j in range(y):
            if i < delta:
                r, g, b = pixel[i, j]
                another_pixel[i, j] = 0, g, b
            else:
                another_pixel[i, j] = r, g, b
                g, b = pixel[i, j][1:]
                r = pixel[i - delta, j][0]
    result_image.save("res.jpg")
