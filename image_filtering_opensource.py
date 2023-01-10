import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import colors

import cv2

import os
print(os.listdir("C:/Users/Do Yeon/oosp/oosp"))

img_path='C:/Users/Do Yeon/oosp/oosp'
#whale_image_list=os.listdir(img_path)
#whale_image_list[0:10]

flags = [i for i in dir(cv2) if i.startswith('COLOR_')]

len(flags)
#flags[30:40]
whale = cv2.imread(img_path+'/'+"dog.jpg")
plt.imshow(whale)
plt.show()

whale_rgb = cv2.cvtColor(whale, cv2.COLOR_BGR2RGB)
plt.imshow(whale_rgb)
plt.show()

whale_gray = cv2.cvtColor(whale, cv2.COLOR_BGR2GRAY)
plt.imshow(whale_gray)
plt.show()

whale_hsv = cv2.cvtColor(whale, cv2.COLOR_BGR2HSV)
plt.imshow(whale_hsv)
plt.show()

red = whale_rgb.copy()
# set blue and green channels to 0
red[:, :, 1] = 0
red[:, :, 2] = 0
# RGB - Red
plt.imshow(red)
plt.show()

green = whale_rgb.copy()
# set blue and red channels to 0
green[:, :, 0] = 0
green[:, :, 2] = 0
# RGB - Green
plt.imshow(green)
plt.show()

blue = whale_rgb.copy()
# set green and red channels to 0
blue[:, :, 0] = 0
blue[:, :, 1] = 0
# RGB - Blue
plt.imshow(blue)
plt.show()
