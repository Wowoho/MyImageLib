import cv2
from MyImageLib import basic, noise, advanced

img = cv2.imread('img.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(img.shape)
# img = basic.EnlargeCanvas(img, (800, 800), True)
# img = basic.Resize(img, (300, 100))
# img = basic.Translation(img, (-100, 59))
# img = basic.Rotate(img, 0, (500, 0))
# img = noise.SaltAndPepper(img, 0.1)
# img = advanced.removeBorder(img, (0, 0))
cv2.imshow('', img)
cv2.waitKey()
