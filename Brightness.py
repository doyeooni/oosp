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
import numpy as np

img_path='C:/Users/Do Yeon/oosp/oosp'


#밝기 조절 구현
img = cv2.imread(img_path+'/'+"sea.png")

def Bright(original_image):
    plt.figure(figsize=(5,5))
    alpha = 1.0
    plt.subplot(121)
    plt.imshow(cv2.cvtColor(original_image,cv2.COLOR_BGR2RGB))
    plt.title('Original')
    plt.xticks([]), plt.yticks([])

    bright = np.clip((1+alpha) * img - 128 * alpha, 0, 255).astype(np.uint8)
    
    plt.subplot(122)
    plt.imshow(bright)
    plt.title('Brightness')
    plt.xticks([]), plt.yticks([])
    plt.show()

Bright(img)
