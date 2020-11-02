# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\GitHub\SAR-Images-Classifation-Base-On-TensorFlow\深度学习入门\人脸识别\图片显示\Window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(420, 408)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 20, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralWidget)
        self.graphicsView.setGeometry(QtCore.QRect(40, 50, 321, 271))
        self.graphicsView.setObjectName("graphicsView")
        self.comboBox = QtWidgets.QComboBox(self.centralWidget)
        self.comboBox.setGeometry(QtCore.QRect(160, 330, 131, 22))
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(60, 340, 81, 16))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 20, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_Clear = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_Clear.setGeometry(QtCore.QRect(220, 20, 61, 23))
        self.pushButton_Clear.setObjectName("pushButton_Clear")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 420, 23))
        self.menuBar.setObjectName("menuBar")
        self.menu1 = QtWidgets.QMenu(self.menuBar)
        self.menu1.setObjectName("menu1")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.actionclose = QtWidgets.QAction(MainWindow)
        self.actionclose.setObjectName("actionclose")
        self.action_Open = QtWidgets.QAction(MainWindow)
        self.action_Open.setObjectName("action_Open")
        self.actionAdd = QtWidgets.QAction(MainWindow)
        self.actionAdd.setObjectName("actionAdd")
        self.actionClear = QtWidgets.QAction(MainWindow)
        self.actionClear.setObjectName("actionClear")
        self.menu1.addAction(self.actionclose)
        self.menu1.addAction(self.action_Open)
        self.menu.addAction(self.actionAdd)
        self.menu.addAction(self.actionClear)
        self.menuBar.addAction(self.menu1.menuAction())
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.actionclose.triggered.connect(MainWindow.close)
        self.pushButton.clicked.connect(MainWindow.close)
        self.pushButton_Clear.clicked.connect(self.graphicsView.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Close"))
        self.label.setText(_translate("MainWindow", "Gray Display"))
        self.pushButton_2.setText(_translate("MainWindow", "Open Image"))
        self.pushButton_Clear.setText(_translate("MainWindow", "Clear"))
        self.menu1.setTitle(_translate("MainWindow", "图像框"))
        self.menu.setTitle(_translate("MainWindow", "下拉菜单"))
        self.actionclose.setText(_translate("MainWindow", "close"))
        self.action_Open.setText(_translate("MainWindow", "&Open"))
        self.actionAdd.setText(_translate("MainWindow", "&Add"))
        self.actionClear.setText(_translate("MainWindow", "&Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
