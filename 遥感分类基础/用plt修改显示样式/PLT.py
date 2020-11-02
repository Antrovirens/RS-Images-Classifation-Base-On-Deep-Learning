import sys

import wx
import gdal
import cv2

from scipy import misc
from libtiff import TIFF
from PIL import Image

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg



filepath = 'C:\\Users\\sheld\\Desktop\\ms.bsq'

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

cv2.imshow("band1",band1)

# data = np.array((band4,band3,band2),dtype = band2.dtype) 

# cv2.imshow("data",data)

# plt.imshow(band1)#, cmap='gray', norm= None,)
# plt.show()


