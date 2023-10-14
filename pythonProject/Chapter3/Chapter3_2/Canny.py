import cv2
import numpy as np

# 读取图像
image = cv2.imread('image0.png')

# 使用Canny边缘检测
edges = cv2.Canny(image, threshold1=100, threshold2=200)

# 显示原始图像和边缘检测结果
cv2.imshow('Original Image', image)
cv2.imshow('Canny Edges', edges)
cv2.imwrite('Canny_image.jpg', edges)

# 等待用户按下任意键后关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()
