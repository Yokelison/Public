import cv2
import numpy as np

img = cv2.imread('image0.png', 1)
cv2.imshow('src', img)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
deep = imgInfo[2]

newImgInfo = (height * 2, width, deep)
newImgInfo2 = (height, width * 2, deep)
newImgInfo3 = (height * 2, width * 2, deep)

dst = np.zeros(newImgInfo, np.uint8)

# 垂直翻转
cv2.imshow('dst', dst)
for i in range(0, height):
    for j in range(0, width):
        dst[i, j] = img[i, j]
        # x , y=2*h-y-1
        dst[height * 2 - i - 1, j] = img[i, j]
cv2.imshow('dst', dst)
cv2.imwrite('imagevertical.png', dst)

# 水平翻转
dst2 = np.zeros(newImgInfo2, np.uint8)
for i in range(0, height):
    for j in range(0, width):
        dst2[i, j] = img[i, j]
        # x=2*w-x-1 , y
        dst2[i, width * 2 - j - 1] = img[i, j]
cv2.imshow('dst2', dst2)
cv2.imwrite('imagehorizion.png', dst2)

# 水平垂直都翻转
dst3 = np.zeros(newImgInfo3, np.uint8)
for i in range(0, height):
    for j in range(0, width):
        dst3[i, j] = img[i, j]
        # x=2*w-x-1 , y=2*h-y-1
        dst3[height * 2 - i - 1, width * 2 - j - 1] = img[i, j]
cv2.imshow('dst3', dst3)
cv2.imwrite('imageverticvalandhorizion.png', dst3)

cv2.waitKey(0)
