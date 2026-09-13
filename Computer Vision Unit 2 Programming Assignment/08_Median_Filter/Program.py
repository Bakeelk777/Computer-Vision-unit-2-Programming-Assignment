import cv2

img = cv2.imread("./08_Median_Filter\input.jpeg")
filtered = cv2.medianBlur(img, 5)

cv2.imwrite("output.jpg", filtered)

cv2.imshow("Salt-and-Pepper Noisy Image", img)
cv2.imshow("Median Filtered Image", filtered)

cv2.waitKey(0)
cv2.destroyAllWindows()
