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
from PIL import ImageTk, Image, ImageEnhance
from tkinter import *
import numpy as np

img_path='C:/Users/Do Yeon/oosp/oosp'


#밝기 조절 구현
img = cv2.imread(img_path+'/'+"sea.png")

def Bright(original_image):
    plt.figure(figsize=(5,5))

    val = 50
    array = np.full(img.shape, (val,val,val), dtype=np.uint8)
    
    add = cv2.add(img, array)
    numpy_horizontal = np.hstack((img, add))

    cv2.imshow('Brightness', numpy_horizontal)

Bright(img)
cv2.waitKey()