import cv2
import numpy as np

# 读取图像
image = cv2.imread('image0.png')

# 定义锐化滤波器
sharpening_filter = np.array([[-1, -1, -1],
                              [-1, 9, -1],
                              [-1, -1, -1]])

# 应用锐化滤波器
sharpened_image = cv2.filter2D(image, -1, sharpening_filter)

# 显示原始图像和处理后的图像
cv2.imshow('Original Image', image)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.imwrite('Sharpening.jpg', sharpened_image)

# 等待用户按下任意键后关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()
