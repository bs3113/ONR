import numpy as np
import cv2

array = np.arange(0, 737280, 1, np.uint8)
array = np.reshape(array, (1024, 720))

cv2.imwrite('filename.jpeg', array)