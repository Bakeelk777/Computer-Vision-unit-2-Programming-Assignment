import cv2
import numpy as np

img = cv2.imread("./02_Brightness/input.jpeg")
brightness = 50
x, y = 100, 100
before = img[x, y].copy
print(before)
enhance_image = np.clip(img.astype(np.int16) + brightness, 0, 255).astype(np.uint8)
after = enhance_image[y, x]
print("pixel value before enhancement: ", before)
print("Pixel values after enhancemnt: ", after)
cv2.imwrite("Output.png", enhance_image)
cv2.imshow("Original Image", img)
cv2.imshow("Brightness Enhanced Image", enhance_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

