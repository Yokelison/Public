import cv2
import numpy as np

# 读取图像
image = cv2.imread('image_added_noises.jpg', 1)

# 定义旋转掩膜参数
kernel_size = 25 # 掩膜大小
angle = 0  # 旋转角度

# 创建旋转掩膜
rotation_mask = cv2.getRotationMatrix2D((kernel_size // 2, kernel_size // 2), angle, 1)
rotation_mask = np.uint8(rotation_mask)

# 应用旋转掩膜平均
smoothed_image = cv2.filter2D(image, -1, rotation_mask)

# 显示原始图像和处理后的图像
cv2.imshow('Original Image', image)
cv2.imshow('Smoothed Image', smoothed_image)
cv2.imwrite('Smoothed_image.jpg', smoothed_image)

# 等待用户按下任意键后关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()
