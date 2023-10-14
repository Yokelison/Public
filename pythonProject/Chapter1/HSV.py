import cv2
import numpy as np

# 读取图像
image = cv2.imread('eg.png')

# 将图像从BGR颜色空间转换为HSV颜色空间
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 定义亮度增加量（正数增加亮度，负数降低亮度）
brightness_factor = 100

# 获取亮度通道
v_channel = hsv[:, :, 2]

# 调整亮度通道的值
v_channel = np.where(v_channel + brightness_factor > 255, 255, v_channel + brightness_factor)
v_channel = np.where(v_channel + brightness_factor < 0, 0, v_channel + brightness_factor)

# 将修改后的亮度通道重新赋给HSV图像
hsv[:, :, 2] = v_channel

# 将图像从HSV颜色空间转换回BGR颜色空间
adjusted_image = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

# 保存调整后的图像
cv2.imwrite('output.jpg', adjusted_image)

# 显示原始和调整后的图像
cv2.imshow('Original Image', image)
cv2.imshow('Adjusted Image', adjusted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
