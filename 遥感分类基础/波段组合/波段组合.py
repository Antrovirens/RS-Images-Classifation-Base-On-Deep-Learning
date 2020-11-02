from osgeo import gdal
import os
import numpy as np
 
class GRID:
 
    #读图像文件
    def read_img(self,filename):
        dataset=gdal.Open(filename)       #打开文件
 
        im_width = dataset.RasterXSize    #栅格矩阵的列数
        im_height = dataset.RasterYSize   #栅格矩阵的行数
 
        im_geotrans = dataset.GetGeoTransform()  #仿射矩阵
        im_proj = dataset.GetProjection() #地图投影信息
        im_data = dataset.ReadAsArray(0,0,im_width,im_height) #将数据写成数组，对应栅格矩阵
 
        del dataset #关闭对象，文件dataset
        return im_proj,im_geotrans,im_data,im_width,im_height
 
    #写文件，以写成tif为例
    def write_img(self,filename,im_proj,im_geotrans,im_data):
 
        #判断栅格数据的数据类型
        if 'int8' in im_data.dtype.name:
            datatype = gdal.GDT_Byte
        elif 'int16' in im_data.dtype.name:
            datatype = gdal.GDT_UInt16
        else:
            datatype = gdal.GDT_Float32
 
        #判读数组维数
        if len(im_data.shape) == 3:
            im_bands, im_height, im_width = im_data.shape
        else:
            im_bands, (im_height, im_width) = 1,im_data.shape
 
        #创建文件
        driver = gdal.GetDriverByName("GTiff")   #数据类型必须有，因为要计算需要多大内存空间
        dataset = driver.Create(filename, im_width, im_height, im_bands, datatype)
 
        dataset.SetGeoTransform(im_geotrans)              #写入仿射变换参数
        dataset.SetProjection(im_proj)                    #写入投影
 
        if im_bands == 1:
            dataset.GetRasterBand(1).WriteArray(im_data)  #写入数组数据
        else:
            for i in range(im_bands):
                dataset.GetRasterBand(i+1).WriteArray(im_data[i])
 
        del dataset
 
if __name__ == "__main__":
    os.chdir(r'E:\Python\temp\data')                        #切换路径到待处理图像所在文件夹
    run = GRID()
    #第一步
    proj,geotrans,data1,row1,column1 = run.read_img('Band_5_Clip.tif')  #读数据
    proj,geotrans,data2,row2,column2= run.read_img('Band_4_Clip.tif')  # 读数据
    proj,geotrans,data3,row3,column3 = run.read_img('Band_3_Clip.tif')  # 读数据
 
    #第二步
    data = np.array((data1, data2, data3),dtype = data1.dtype)  #按序将3个波段像元值放入
 
    #第三步
    run.write_img('com543.tif', proj, geotrans, data)  # 写为3波段数据