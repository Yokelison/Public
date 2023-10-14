# 1 load 2 info 3 resize 4 check
import cv2
import numpy as np

img = cv2.imread('image0.png',1)
imgInfo = img.shape
print(imgInfo)
height = imgInfo[0]
width = imgInfo[1]
mode = imgInfo[2]
# 1 放大 缩小 2 等比例 非 2:3
dstHeight = int(height*0.5)
dstWidth = int(width*0.5)

#最近临域插值 双线性插值 像素关系重采样 立方插值
dst = cv2.resize(img,(dstWidth,dstHeight))
cv2.imshow('image',dst)


matScale = np.float32([[0.5,0,0],[0,0.7,0]])
dst2 = cv2.warpAffine(img,matScale,(int(width*0.5),int(height*0.7)))
cv2.imshow('dst2',dst2)
cv2.imwrite('image0zoomed.jpg', dst2)
# 图片宽*0.5，高*0.7

cv2.waitKey(0)
