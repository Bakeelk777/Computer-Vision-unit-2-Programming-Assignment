import cv2
import numpy as np
img = cv2.imread("./03_Contrast_Straching/input.jpeg", 0)
min = np.min(img)
max = np.max(img)
stress = (img - min) * (255.0 / (max - min))
stress = stress.astype(np.uint8)

# cv2.imshow("original",img)
# cv2.imshow("stress",stress)

cv2.imwrite("output.jpeg", stress)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
