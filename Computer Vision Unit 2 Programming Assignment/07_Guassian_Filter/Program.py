import cv2

img = cv2.imread("./07_Guassian_Filter/input.jpeg")


gaussian = cv2.GaussianBlur(img, (5, 5), 0)

cv2.imwrite("Output.png", gaussian)
cv2.imshow("Original Noisy Image", img)
cv2.imshow("Gaussian Smoothed Image", gaussian)

cv2.waitKey(0)
cv2.destroyAllWindows()
