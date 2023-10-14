import cv2
import numpy as np

# 读取图像
image = cv2.imread('eg1.png', 0)  # 0以灰度模式读取图像 1用于加载彩色图像 -1用于加载包括Alpha通道的图像，如果图像包含透明度信息的话

# 计算图像的直方图
histogram, bins = np.histogram(image.flatten(), 256, [0, 256])

# 计算累积直方图
cumulative_histogram = histogram.cumsum()

# 计算直方图均衡化的映射表
cdf_min = cumulative_histogram.min()
num_pixels = image.shape[0] * image.shape[1]
cdf_normalized = (cumulative_histogram - cdf_min) * 255 / (num_pixels - cdf_min)
cdf_normalized = cdf_normalized.astype(np.uint8)

# 使用映射表进行直方图均衡化
equalized_image = cdf_normalized[image]

# 显示原始图像和均衡化后的图像
cv2.imshow('Original Image', image)
cv2.imshow('Equalized Image', equalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 保存均衡化后的图像
cv2.imwrite('output1.jpg', equalized_image)
