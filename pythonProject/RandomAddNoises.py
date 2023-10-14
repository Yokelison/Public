import cv2
import numpy as np

# 读取图像
image = cv2.imread('image0.png')

# 获取图像的高度和宽度
height, width, channels = image.shape

# 定义噪声参数
mean = 0  # 噪声均值
stddev = 25  # 噪声标准差

# 生成与图像相同大小的随机高斯噪声
noise = np.random.normal(mean, stddev, (height, width, channels))

# 将噪声添加到图像
noisy_image = image + noise

# 确保图像像素值在0和255之间
noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)

# 显示原始图像和叠加噪声后的图像
cv2.imshow('Original Image', image)
cv2.imshow('Noisy Image', noisy_image)

# 保存叠加噪声后的图像
cv2.imwrite('noisy_image.jpg', noisy_image)

# 等待用户按下任意键，然后关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()
