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
#whale = cv2.imread(img_path+'/'+"dog.jpg")


#img_path='C:/Users/Do Yeon/oosp/oosp'
#whale_image_list=os.listdir(img_path)
#whale_image_list[0:10]

flags = [i for i in dir(cv2) if i.startswith('COLOR_')]

len(flags)
#flags[30:40]

#1번
whale = cv2.imread(img_path+'/'+"dog.jpg")
plt.imshow(whale)
plt.show()

#2번
whale_rgb = cv2.cvtColor(whale, cv2.COLOR_BGR2RGB)
plt.imshow(whale_rgb)
plt.show()

#3번
whale_gray = cv2.cvtColor(whale, cv2.COLOR_BGR2GRAY)
plt.imshow(whale_gray)
plt.show()

#4번
whale_hsv = cv2.cvtColor(whale, cv2.COLOR_BGR2HSV)
plt.imshow(whale_hsv)
plt.show()

#5번
red = whale_rgb.copy()
# set blue and green channels to 0
red[:, :, 1] = 0
red[:, :, 2] = 0
# RGB - Red
plt.imshow(red)
plt.show()

#6번
green = whale_rgb.copy()
# set blue and red channels to 0
green[:, :, 0] = 0
green[:, :, 2] = 0
# RGB - Green
plt.imshow(green)
plt.show()

#7번
blue = whale_rgb.copy()
# set green and red channels to 0
blue[:, :, 0] = 0
blue[:, :, 1] = 0
# RGB - Blue
plt.imshow(blue)
plt.show()


#8번
#블러처리 구현
def plotFigures(original_image, blurred_image):
    plt.figure(figsize=(50,50))
    plt.subplot(121)
    plt.imshow(cv2.cvtColor(original_image,cv2.COLOR_BGR2RGB))
    plt.title('Original')
    plt.xticks([]), plt.yticks([])

    plt.subplot(122)
    plt.imshow(cv2.cvtColor(blurred_image,cv2.COLOR_BGR2RGB))
    plt.title('Blurred')
    plt.xticks([]), plt.yticks([])
    plt.show()

blurI = cv2.blur(whale, (10,10))
plotFigures(whale,blurI)



#블러처리 구현
def plotFigures(original_image, blurred_image):
    plt.figure(figsize=(50,50))
    plt.subplot(121)
    plt.imshow(cv2.cvtColor(original_image,cv2.COLOR_BGR2RGB))
    plt.title('Original')
    plt.xticks([]), plt.yticks([])

    plt.subplot(122)
    plt.imshow(cv2.cvtColor(blurred_image,cv2.COLOR_BGR2RGB))
    plt.title('Blurred_1')
    plt.xticks([]), plt.yticks([])
    plt.show()

blurI = cv2.blur(whale, (10,10))
plotFigures(whale,blurI)