import cv2

# 读取图像
image = cv2.imread('image_added_noises.jpg')

# 应用中值滤波
filtered_image = cv2.medianBlur(image, 5)  # 5表示滤波窗口大小

# 显示原始图像和处理后的图像
cv2.imshow('Original Image', image)
cv2.imshow('Filtered Image', filtered_image)
cv2.imwrite('MedianFilteredImage.jpg', filtered_image)

# 等待用户按下任意键后关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()
