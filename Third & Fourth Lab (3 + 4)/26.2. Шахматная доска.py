# Алексей Головлев, группа БСБО-07-19

from PIL import Image, ImageDraw


def board(num, size):
    cell_color = (255, 255, 255)
    result_image = Image.new("RGB", (num * size, num * size), cell_color)
    y = x = size * num
    draw = ImageDraw.Draw(result_image)
    for i in range(0, x, size):
        if i % (size * 2) == 0:
            for j in range(0, y, size):
                if j % (size * 2) == 0:
                    draw.rectangle(
                        [i, j, i + size - 1, j + size - 1], fill='black')
        else:
            for j in range(size, y, size):
                if j % (size * 2) != 0:
                    draw.rectangle(
                        [i, j, i + size - 1, j + size - 1], fill='black')
    result_image.save('res.png', "PNG")
