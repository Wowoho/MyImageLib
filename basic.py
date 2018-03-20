import numpy as np
import cv2


def Rotate(src, angle, center=(-1, -1)):
    if center == (-1, -1):
        center = (src.shape[1] / 2, src.shape[0] / 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    res = cv2.warpAffine(src, M, (src.shape[1], src.shape[0]))
    return res


def Translation(src, direction):
    M = np.float32([[1, 0, direction[0]], [0, 1, direction[1]]])
    res = cv2.warpAffine(src, M, (src.shape[1], src.shape[0]))
    return res


def Resize(src, size):
    # 采用双线性插值
    res = cv2.resize(src, size, interpolation=cv2.INTER_LINEAR)
    return res


def EnlargeCanvas(src, size, fit=False):
    M = np.float32([[1, 0, 0], [0, 1, 0]])
    res = cv2.warpAffine(src, M, size)
    if fit == True:
        res = Translation(res, (int((res.shape[1] - src.shape[1]) / 2), int((res.shape[0] - src.shape[0]) / 2)))
    return res


def CropRect(src, xmin, xmax, ymin, ymax):
    return src[ymin:ymax, xmin:xmax]


def Binary(src, tresh, maxval):
    _, img = cv2.threshold(src, tresh, maxval, cv2.THRESH_BINARY)
    return img