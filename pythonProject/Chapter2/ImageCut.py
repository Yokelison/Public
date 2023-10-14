import cv2
img = cv2.imread('image0.png',1)
imgInfo = img.shape
dst = img[0:200,0:300]
# 从X轴的100px到200px，y轴的100px到300px
cv2.imshow('image',img)
# 剪切前
cv2.imshow('image',dst)
cv2.imwrite('imageocuted.jpg', dst)
# 剪切后
cv2.waitKey(0)
