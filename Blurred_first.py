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

img_path='C:/Users/Do Yeon/oosp/oosp'
whale = cv2.imread(img_path+'/'+"dog.jpg")



#블러처리 구현
def plotFigures(original_image, blurred_image):
    plt.figure(figsize=(5,5))
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
