import cv2
from numpy import *


def SaltAndPepper(src, percetage):
    img = src
    NoiseNum = int(percetage * src.shape[0] * src.shape[1])
    for i in range(NoiseNum):
        randX = random.random_integers(0, src.shape[0] - 1)
        randY = random.random_integers(0, src.shape[1] - 1)
        if random.random_integers(0, 1) == 0:
            img[randX, randY] = 0
        else:
            img[randX, randY] = 255
    return img

