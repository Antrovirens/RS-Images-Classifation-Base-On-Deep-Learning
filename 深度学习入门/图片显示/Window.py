# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import cv2
import numpy as np
from scipy import misc
from PIL import Image
from libtiff import TIFF
from Ui_Window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_action_Open_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: open tiff files
        filename,_ = QFileDialog.getOpenFileName(self, "Open File",  "C:\\Users\\sheld\\Desktop",   "Images (*.*)")
        
        img=QImage()
        img.load(filename)
        
        #cv2.imread("filename",0)
        
        img=img.scaled(self.graphicsView.width()-10,self.graphicsView.height()-10)
        
        scene=QGraphicsScene()
        
        scene.addPixmap(QPixmap().fromImage(img))
        self.graphicsView.setScene(scene)
        

    @pyqtSlot()
    def on_actionAdd_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.comboBox.addItem('item added')
    
    @pyqtSlot()
    def on_actionClear_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.comboBox.clear()

    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        filename,_ = QFileDialog.getOpenFileName(self, "Open File",  "C:\\Users\\sheld\\Desktop",   "Images (*.*)")
        
        
        #        print(src.shape)    
#        h,w,ch = np.shape(src)
#        print(h,w,ch)
#        print(src.shape)
        src = cv2.imread(filename)
        bgr = cv2.split(src)
        cv2.imshow("blue",bgr[0])
        cv2.imshow("green",bgr[1])
        cv2.imshow("red",bgr[2])
        cv2.imshow("Band4",bgr[3] )

        cv2.waitKey(0)
        cv2.destroyAllWindows()


        img=QImage()
        img.load(filename)
        
        #cv2.imread("filename",0)
        
        img=img.scaled(self.graphicsView.width()-10,self.graphicsView.height()-10)
        
        scene=QGraphicsScene()
        
        scene.addPixmap(QPixmap().fromImage(img))
        self.graphicsView.setScene(scene)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = MainWindow()
    dlg.show()
    sys.exit(app.exec_())
    
