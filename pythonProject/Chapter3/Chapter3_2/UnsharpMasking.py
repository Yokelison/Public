import cv2
import numpy as np

# 读取图像
image = cv2.imread('image0.png')

# 使用高斯模糊来创建模糊版本
blurred_image = cv2.GaussianBlur(image, (5, 5), 2)

# 计算非锐化屏蔽图像
unsharp_mask = cv2.addWeighted(image, 2, blurred_image, -1, 0)

# 显示原始图像和非锐化屏蔽图像
cv2.imshow('Original Image', image)
cv2.imshow('Unsharp Masked Image', unsharp_mask)
cv2.imwrite('Usharp_mask.jpg', unsharp_mask)

# 等待用户按下任意键后关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()
