#coding:utf-8
from PIL import Image
im = Image.open('5.gif')
w,h = im.size
im2=im.convert('L')

def getywh(im2,s,e):
    start = 0
    end = 0
    ywh = []
    de = range(im2.size[1])
    for y in de:
        for x in range(s,e):
            pix = im2.getpixel((x, y))
            if pix != 255:
                start = y + 1

    de.reverse()
    for y in de:
        for x in range(im2.size[0]):
            pix = im2.getpixel((x, y))
            if pix != 255:
                end = y
    if s == 91:
        print start,end
    return start,end


def getxwh(im2):
    a = False
    b = False
    start = 0
    end = 0
    xwh = []
    for x in range(im2.size[0]):
        for y in range(im2.size[1]):
            pix = im2.getpixel((x, y))
            if pix != 255:
                a = True
        if b == False and a == True:
            b = True
            start = x
        if b == True and a == False:
            b = False
            end = x
            xwh.append((start, end))
        a = False
    print xwh
    return xwh


i = 0
for x in getxwh(im2):
    xs = x[0]
    xe = x[1]
    #print xs,xe
    ye,ys = getywh(im2,xs,xe)
    region = (xs,ys,xe,ye)
    #print region
    cropimg = im2.crop(region)
    cropimg.save('crop%s.png' % i)
    i+=1
