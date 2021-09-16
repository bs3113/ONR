# import matplotlib.pyplot as plt
# import cv2
#
# cap = cv2.VideoCapture(0)
# flag = False
# while True:
#
#     ret, frame = cap.read()
#     # frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
#     # frame = cv2.Canny(frame, 2, 20)
#     cv2.imshow('Input', frame)
#
#     cropped_image = frame[120:270, 220:360]
#     if flag:
#         flag = False
#         plt.imshow(cropped_image)
#         plt.show()
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()


import pycrafter6500

controller = pycrafter6500.dmd()
controller.stopsequence()