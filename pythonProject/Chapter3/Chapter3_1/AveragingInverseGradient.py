import cv2
import numpy as np

# 读取图像
image = cv2.imread('image0.png', 1)

# 使用Sobel滤波器计算图像梯度
gradient_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
gradient_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)

# 计算梯度幅值
gradient_magnitude = np.sqrt(gradient_x**2 + gradient_y**2)

# 应用反梯度平均
smoothed_image = cv2.blur(image, (5, 5))
enhanced_image = image + (image - smoothed_image)

# 显示原始图像和处理后的图像
cv2.imshow('Original Image', image)
cv2.imshow('Enhanced Image', enhanced_image)
cv2.imwrite('EnhancedImage.jpg', enhanced_image)

# 等待用户按下任意键后关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()
