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
whale = cv2.imread(img_path+'/'+"dog.png", cv2.IMREAD_COLOR)

plt.figure(figsize=(7,7))
plt.subplot(1,2,1)

plt.title("Original")
plt.imshow(whale)

kernel_sharpneing = np.array([ [-1,-1,-1], [-1,9,-1],[-1,-1,-1]])

sharpened = cv2.filter2D(whale, -1, kernel_sharpneing)

plt.subplot(1,2,2)
plt.title("Definition")
plt.imshow(sharpened)

plt.show()