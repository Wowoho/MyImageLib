import cv2
import numpy as np
from MyImageLib.basic import *


def removeBorder(src, background=(0, 0)):
    res = src
    top = 0
    bottom = res.shape[0]
    left = res.shape[1]
    right = 0
    for i in range(res.shape[0]):
        for j in range(res.shape[1]):
            if not(background[0] <= res[i][j] <= background[1]):
                top = max(top, i)
                bottom = min(bottom, i)
                left = min(left, j)
                right = max(right, j)
    res = CropRect(res, left, right, bottom, top)
    return res


def addBorder(src, width, color=0):
    res = cv2.copyMakeBorder(src, width, width, width, width, cv2.BORDER_CONSTANT, value=color)
    return res


def standardiz(src, size, board):
    (width, heigth) = size
    (h, w) = src.shape

    width -= board
    heigth -= board

    if heigth / width > h / w:
        img = Resize(src, (width, heigth * h // w))
    else:
        img = Resize(src, (width * w // h, heigth))

    img = EnlargeCanvas(img, size, fit=True)

    return img