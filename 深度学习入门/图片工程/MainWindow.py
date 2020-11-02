# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *

from Ui_MainWindow import Ui_MainWindow


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
    
    @pyqtSlot(QAction)
    def on_menu_triggered(self, action):
        """
        Slot documentation goes here.
        
        @param action DESCRIPTION
        @type QAction
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot(QAction)
    def on_menu_2_triggered(self, action):
        """
        Slot documentation goes here.
        
        @param action DESCRIPTION
        @type QAction
        """
        # TODO: not implemented yet
        filename,_=QFileDialog.getOpenFileName(None,'open',r"C:\Users\sheld\Desktop\Antrovirens\cloud\pic\portrait")
        img=QImage()
        img.load(filename)
        img=img.scaled(self.graphicsView.width(),self.graphicsView.height())
        scene=QGraphicsScene()
        scene.addPixmap(QPixmap().fromImage(img))
        self.graphicsView.setScene(scene)

    
    @pyqtSlot(QAction)
    def on_menu_3_triggered(self, action):
        """
        Slot documentation goes here.
        
        @param action DESCRIPTION
        @type QAction
        """
        # TODO: not implemented yet
        raise NotImplementedError




if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = MainWindow()
    dlg.show()
    sys.exit(app.exec_())
