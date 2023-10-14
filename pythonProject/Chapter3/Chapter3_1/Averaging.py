import cv2
import numpy as np

# 读取图像
image = cv2.imread('image_added_noises.jpg')

# 定义滤波器大小
kernel_size = 5

# 使用均值滤波器进行平均噪声抑制
filtered_image = cv2.blur(image, (kernel_size, kernel_size))

# 显示原始图像和处理后的图像
cv2.imshow('Original Image', image)
cv2.imshow('Filtered Image', filtered_image)
cv2.imwrite('denoises.jpg', filtered_image)

# 等待用户按下任意键后关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()
