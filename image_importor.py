import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mping
import cv2
import os
import glob
import time
import datetime

path = 'C:/Users/cheng sun/Desktop/SharpCap Captures'
today = datetime.date.today()
#Always processes the lastest the image and the remove the folder after?

# Getting the path of the image folder
d1 = today.strftime("%Y-%m-%d")
img_file_name = "/Capture/10_43_26/" #Hard Coding
img_path = path + "/" + d1 + img_file_name


img_path = 'C:/Users/cheng sun/Desktop/SharpCap Captures/2021-09-08/Capture/19_05_47/'
img_file_list = glob.glob(img_path + '*.png')
img = mping.imread(img_file_list[0])
plt.imshow(img)
plt.show()

print(img_path)
# Extract the images
count = 0
while (count < 100):
    img_file_list = glob.glob(img_path + '*.png')
    if img_file_list:
        count = 0
        if cv2.waitKey(1) & 0xFF == ord('c'):
            img = mping.imread(img_file_list[-1])
            plt.imshow(img)
            plt.show()
        img = cv2.imread(img_file_list[-1])
        img = cv2.resize(img, (960, 540))
        img = cv2.normalize(img,  img, 0, 255, cv2.NORM_MINMAX)
        cv2.imshow('Capture', img)

        for f in os.listdir(img_path):
            os.remove(os.path.join(img_path, f))
        # the 'q' button is set as the quitting button
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    time.sleep(1)
    count += 1
cv2.destroyAllWindows()

# count = 0
# temp = None
# while count < 5:
#     img_file_list = glob.glob(img_path +'*.png')
#     if temp == img_file_list[-1]:
#         count += 1
#     else:
#         count = 0
#         img = cv2.imread(img_file_list[-1])
#         img *= 250.0
#         img = img.astype(np.uint8)
#         plt.imshow(img)
#         plt.show()
#     temp = img_file_list[-1]
#     time.sleep(1)

# import cv2
# import os
# import numpy as np
#
# image_folder = 'C:/Users/cheng sun/BoyuanSun/ScreenShots/7.26/movie'
# video_name = 'video.avi'
#
# images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
# img = cv2.imread(os.path.join(image_folder, images[0]))
# print(img.shape)
# img *= 250.0
# img = img.astype(np.uint8)
# frame = cv2.imread(os.path.join(image_folder, images[0]))
# height, width, layers = frame.shape
#
# video = cv2.VideoWriter(video_name, 0, 1, (width, height))
#
# for image in images:
#     video.write(cv2.imread(os.path.join(image_folder, image)))
#
# cv2.destroyAllWindows()
# video.release()
# #
# import numpy as np
# from matplotlib import image
# from matplotlib import pyplot
# # load image as pixel array
# image = image.imread('C:/Users/cheng sun/BoyuanSun/ScreenShots/7.26/Sun_00002.png')
# # summarize shape of the pixel array
# print(np.max(image), np.min(image))
# print(image.dtype)
# print(image.shape)
# # display the array of pixels as an image
# pyplot.imshow(image)
# pyplot.show()
