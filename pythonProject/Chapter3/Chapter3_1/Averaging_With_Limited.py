import cv2
import numpy as np

# 读取图像
image = cv2.imread('image_added_noises0.jpg', 1)

# 定义处理窗口大小
window_size = 5

# 复制原始图像以保留原始数据
processed_image = np.copy(image)

# 遍历图像像素并应用平均处理，考虑像素有效性
for y in range(window_size // 2, image.shape[0] - window_size // 2):
    for x in range(window_size // 2, image.shape[1] - window_size // 2):
        window = image[y - window_size // 2: y + window_size // 2 + 1, x - window_size // 2: x + window_size // 2 + 1]

        # 限制窗口内像素有效性
        valid_pixels = [pixel for pixel in window.flatten() if pixel >= 0]

        if valid_pixels:
            average = sum(valid_pixels) / len(valid_pixels)
            processed_image[y, x] = average

# 显示原始图像和处理后的图像
cv2.imshow('Original Image', image)
cv2.imshow('Processed Image', processed_image)
cv2.imwrite('denoisesanddesscratch.jpg', processed_image)

# 等待用户按下任意键后关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()
