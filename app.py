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