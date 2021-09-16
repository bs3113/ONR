import pycrafter6500
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mping
from mpl_toolkits import mplot3d
import cv2
import os
import glob
import time
import datetime
from stl import mesh
import PIL.Image
import datetime

# # Using an existing stl file:
# your_mesh = mesh.Mesh.from_file('C:/Users/cheng sun/Desktop/Slicing Codes from Xiangfan/3D HEMA_Conductive Project_150um_125details.STL')
# volume, cog, inertia = your_mesh.get_mass_properties()
# # print("Volume                                  = {0}".format(volume))
# # print("Position of the center of gravity (COG) = {0}".format(cog))
# # print("Inertia matrix at expressed at the COG  = {0}".format(inertia[0,:]))
# # print("                                          {0}".format(inertia[1,:]))
# # print("                                          {0}".format(inertia[2,:]))
#
# # Accessing individual points (concatenation of v0, v1 and v2 in triplets)
# figure = plt.figure()
# axes = mplot3d.Axes3D(figure)
#
# # Load the STL files and add the vectors to the plot
# axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))
# print(your_mesh.vectors[1])
# # Auto scale to the mesh size
# scale = your_mesh.points.flatten()
# axes.auto_scale_xyz(scale, scale, scale)
# # Show the plot to the screen
# plt.show()

controller = pycrafter6500.dmd()
# controller.idle_on()
# #sets the DMD to idle mode
# controller.idle_off()
# #wakes the DMD from idle mode
# controller.standby()
# #sets the DMD to standby
# controller.wakeup()
# #wakes the DMD from standby
# controller.reset()
# #resets the DMD
controller.stopsequence()
controller.changemode(3)
#changes the dmd operating mode:
#mode=0 for normal video mode
#mode=1 for pre stored pattern mode
#mode=2 for video pattern mode
#mode=3 for pattern on the fly mode
path = 'C:/Users/cheng sun/BoyuanSun/CLIP1&2&etc/Slicing/2/*.png'
exposures_time = 3
layers = 400
#Always processes the lastest the image and the remove the folder after?
img_file_list = glob.glob(path)
img_list = []
exposures_list = []
trigger_in_list = []
trigger_out_list = []
dark_time_list = []
exposures = np.int(exposures_time *1000000)
trigger_in = False
trigger_out = False
dark_time = 0
repetitions = np.int(1.1*layers)
# count_outloop = 0
# while count_outloop < len(img_file_list) - 400:
count = 0
for idx in range(0, len(img_file_list)):
    if count >= layers:
        # count_outloop += count
        break
    print(img_file_list[idx])
    # img = np.int8(np.asarray(PIL.Image.open(img_file_list[idx])))
    img = np.asarray(PIL.Image.open(img_file_list[idx]))
    img_list.append(img)
    # img_list.append(np.rot90(img))
    # plt.imshow(img)
    # plt.show()
    print((img.shape), count)
    print(np.max(img),np.min(img),type(img[0][0]))
    exposures_list.append(exposures)
    trigger_in_list.append(trigger_in)
    trigger_out_list.append(trigger_out)
    dark_time_list.append(dark_time)
    count += 1

# images: python list of numpy arrays, with size (1080,1920), dtype uint8, and filled with binary values (1 and 0 only)
# exposures: python list or numpy array with the exposure times in microseconds of each image. Length must be equal to the images list.
# trigger in: python list or numpy array of boolean values determing wheter to wait for an external trigger before exposure. Length must be equal to the images list.
# dark time: python list or numpy array with the dark times in microseconds after each image. Length must be equal to the images list.
# trigger out: python list or numpy array of boolean values determing wheter to emit an external trigger after exposure. Length must be equal to the images list.
# repetitions: number of repetitions of the sequence. set to 0 for infinite loop.
# controller.defsequence(img_list,exposures_list,trigger_in_list,dark_time_list,trigger_out_list, repetitions)
# # Getting the path of the image folder
# controller.startsequence()
# time.sleep(20)
# controller.stopsequence()
controller.defsequence(img_list,exposures_list,trigger_in_list,dark_time_list,trigger_out_list, repetitions)
# Getting the path of the image folder
controller.startsequence()
# time.sleep(exposures_time*layers+2)
