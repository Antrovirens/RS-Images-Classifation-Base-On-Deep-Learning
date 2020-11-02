import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import wx
import gdal
import cv2

from scipy import misc
from libtiff import TIFF
from PIL import Image

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# fileName = 'C:\\Users\\sheld\\Desktop\\ms.tif' #其实在这里存在一个问题，就是打开普通jpg图片的时候，用的是\而打开tif文件的时候，用的是/ 

#filepath = 'C:\\Users\\sheld\\Desktop\\ms.tif'

#filepath = 'C:\\Users\\sheld\\Desktop\\Band1.tif'

filepath = 'C:\\Users\\sheld\\Desktop\\ms.bsq'

##src = cv2.imread(filepath) #按照路径打开
##cv2.imshow("band1",src)

dataset = gdal.Open(filepath)   

if dataset == None:
    print(filepath+"文件无法打开")
    
im_width = dataset.RasterXSize #列数 
im_height = dataset.RasterYSize #行数
im_bands = dataset.RasterCount #波段数 
im_data = dataset.ReadAsArray(0,0,im_width,im_height)#获取数据 
im_geotrans = dataset.GetGeoTransform()#获取仿射矩阵信息 
im_proj = dataset.GetProjection()#获取投影信息

print(im_proj)

band1= im_data[0,0:im_height,0:im_width] 
band2= im_data[1,0:im_height,0:im_width] 
band3= im_data[2,0:im_height,0:im_width] 
band4= im_data[3,0:im_height,0:im_width] 


##print(band1)
##
##mat_band1 = np.array(band1)

plt.imshow(band1)
plt.show()

print(mat_band1)

