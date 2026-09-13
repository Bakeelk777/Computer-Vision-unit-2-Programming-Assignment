import cv2
original_img = cv2.imread("./01_Grayscale/input.jpeg")
img_gray = cv2.imread("./01_Grayscale/input.jpeg", cv2.IMREAD_GRAYSCALE)

print("Gray Scale Image shape: ", img_gray.shape)
print("Original Image Shape: ", original_img.shape)
cv2.imwrite("output.png", img_gray)
