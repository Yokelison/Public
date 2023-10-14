# 导入所需的库
import numpy as np
import cv2

# 加载图像
image = cv2.imread('eg.png')

# 定义亮度增量  可以设置按照比例增加也可以设置为按照固定数值增强，如需修改，相应的计算公式也应当修改
brightness_increment_precent = 100

# 获取图像的高度和宽度
height, width, channels = image.shape

# 创建一个新图像，以便保存处理后的图像
adjusted_image = np.copy(image)

# 遍历图像的每个像素
for i in range(height):
    for j in range(width):
        # 获取当前像素的RGB通道值
        pixel = image[i, j]

        # 增加亮度增量到每个通道
        pixel[0] = min(pixel[0] + brightness_increment_precent, 255)  # 确保通道值不超过255
        pixel[1] = min(pixel[1] + brightness_increment_precent, 255)
        pixel[2] = min(pixel[2] + brightness_increment_precent, 255)

        # 更新像素的RGB通道值
        adjusted_image[i, j] = pixel

# 保存处理后的图像
cv2.imwrite('output_image.jpg', adjusted_image)

# 显示原始和处理后的图像
cv2.imshow('Original Image', image)
cv2.imshow('Adjusted Image', adjusted_image)

# 等待用户按下任意键后关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()
