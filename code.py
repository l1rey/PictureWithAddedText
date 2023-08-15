from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def main():
    print(im.format, im.size, im.mode)


im = Image.open("picture.jpg")
draw = ImageDraw.Draw(im)

font = ImageFont.truetype(r"C:\Windows\Fonts\Calibri.ttf", 60)
draw.text((224, 130), "Text", (255, 255, 255), font=font)
im.save('picturewithtext.jpg')
im.close()


if __name__ == '__main__':
    main()