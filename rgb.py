import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import colors
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter
import cv2
import os
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter import *





#print(os.listdir("C:/Users/Do Yeon/oosp/oosp"))

#이미지 여러 개를 출력하고 싶을 때 -> matplotlib의 subplot을 이용해야 함


img_path='C:/Users/Do Yeon/oosp/oosp'
whale = cv2.imread(img_path+'/'+'dog.png')
whale_rgb = cv2.cvtColor(whale, cv2.COLOR_BGR2RGB)


#5번
red = whale_rgb.copy()
# set blue and green channels to 0
red[:, :, 1] = 0
red[:, :, 2] = 0
# RGB - Red
#plt.imshow(red)
#plt.show()

#6번
green = whale_rgb.copy()
# set blue and red channels to 0
green[:, :, 0] = 0
green[:, :, 2] = 0
# RGB - Green
#plt.imshow(green)
#plt.show()

#7번
blue = whale_rgb.copy()
# set green and red channels to 0
blue[:, :, 0] = 0
blue[:, :, 1] = 0
# RGB - Blue
#plt.imshow(blue)
#plt.show()


numpy_horizontal = np.hstack((red, green, blue))

cv2.imshow('RGB', numpy_horizontal)
cv2.waitKey()