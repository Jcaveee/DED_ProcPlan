# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ded_gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

"""

---------------------------------------
PyQt Generated GUI. Don't code here!!!! (Mb mplt3d widget tho...)
---------------------------------------

"""
import mp3d_widget as mp3d
import mp_widget as mp
from matplotlibwidget import MatplotlibWidget
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(835, 713)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        #self.checkBox = QtGui.QCheckBox(self.centralwidget)
        #self.checkBox.setObjectName(_fromUtf8("checkBox"))
        #self.gridLayout_5.addWidget(self.checkBox, 0, 0, 1, 1)
        self.checkBox_3 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.gridLayout_5.addWidget(self.checkBox_3, 0, 2, 1, 1)
        self.checkBox_2 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.gridLayout_5.addWidget(self.checkBox_2, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_5, 7, 2, 1, 1)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 14, 2, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_13 = QtGui.QLabel(self.centralwidget)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_2.addWidget(self.label_13, 1, 2, 1, 1)
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_2.addWidget(self.label_11, 1, 0, 1, 1)
        self.label_12 = QtGui.QLabel(self.centralwidget)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_2.addWidget(self.label_12, 0, 2, 1, 1)
        self.lineEdit_8 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.gridLayout_2.addWidget(self.lineEdit_8, 1, 1, 1, 1)
        self.lineEdit_9 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.gridLayout_2.addWidget(self.lineEdit_9, 0, 3, 1, 1)
        self.lineEdit_7 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.gridLayout_2.addWidget(self.lineEdit_7, 0, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 1)
        self.lineEdit_10 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.gridLayout_2.addWidget(self.lineEdit_10, 1, 3, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 26, 0, 1, 1)
        self.label_14 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout.addWidget(self.label_14, 6, 2, 1, 1)
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.gridLayout.addWidget(self.line_4, 5, 2, 1, 1)
        self.line_8 = QtGui.QFrame(self.centralwidget)
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.gridLayout.addWidget(self.line_8, 18, 0, 1, 1)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 14, 0, 1, 1)
        
        # Replaced with MP3D widget
        #self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        #self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        #self.gridLayout.addWidget(self.graphicsView, 1, 0, 7, 1)
        
        # Replacement
        self.graphicsView = mp3d.QtMplDynCanvas(self.centralwidget)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.gridLayout.addWidget(self.graphicsView, 1, 0, 7, 1)
        
        
        
        self.label_9 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 19, 0, 1, 1)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_4.addWidget(self.pushButton, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setFrameShape(QtGui.QFrame.NoFrame)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.line_7 = QtGui.QFrame(self.centralwidget)
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.gridLayout.addWidget(self.line_7, 2, 2, 1, 1)
        
        # Replace
        #self.graphicsView_3 = QtGui.QGraphicsView(self.centralwidget)
        #self.graphicsView_3.setObjectName(_fromUtf8("graphicsView_3"))
        #self.gridLayout.addWidget(self.graphicsView_3, 17, 0, 1, 1) 
        
        # With
        self.graphicsView_3 = mp3d.QtMplDynCanvas(self.centralwidget)
        self.graphicsView_3.setObjectName(_fromUtf8("graphicsView"))
        self.gridLayout.addWidget(self.graphicsView_3, 17, 0, 1, 1)        
        
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout_3.addWidget(self.pushButton_2, 2, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_3.addWidget(self.label_2, 2, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 15, 0, 1, 1)
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout.addWidget(self.line_3, 18, 2, 1, 1)
        self.label_15 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout.addWidget(self.label_15, 3, 2, 1, 1)
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.label_17 = QtGui.QLabel(self.centralwidget)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_6.addWidget(self.label_17, 1, 0, 1, 1)
        self.label_16 = QtGui.QLabel(self.centralwidget)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_6.addWidget(self.label_16, 0, 0, 1, 1)
        self.lineEdit_5 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.gridLayout_6.addWidget(self.lineEdit_5, 0, 1, 1, 1)
        self.lineEdit_6 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.gridLayout_6.addWidget(self.lineEdit_6, 1, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_6, 4, 2, 1, 1)
        
        # Replace
        #self.graphicsView_2 = QtGui.QGraphicsView(self.centralwidget)
        #self.graphicsView_2.setObjectName(_fromUtf8("graphicsView_2"))
        #self.gridLayout.addWidget(self.graphicsView_2, 17, 2, 1, 1)
        
        # With
        self.matplotlibwidget = mp.MyDynamicMplCanvas(self.centralwidget)
        self.matplotlibwidget.setObjectName(_fromUtf8("matplotlibwidget"))
        self.gridLayout.addWidget(self.matplotlibwidget, 17, 2, 1, 1)        
        
        self.gridLayout_8 = QtGui.QGridLayout()
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.label_20 = QtGui.QLabel(self.centralwidget)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout_8.addWidget(self.label_20, 1, 0, 1, 1)
        #self.horizontalSlider_2 = QtGui.QSlider(self.centralwidget)
        #self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        #self.horizontalSlider_2.setObjectName(_fromUtf8("horizontalSlider_2"))
        #self.gridLayout_8.addWidget(self.horizontalSlider_2, 1, 3, 1, 1)
        #self.horizontalSlider = QtGui.QSlider(self.centralwidget)
        #self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        #self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        #self.gridLayout_8.addWidget(self.horizontalSlider, 0, 3, 1, 1)
        self.label_19 = QtGui.QLabel(self.centralwidget)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout_8.addWidget(self.label_19, 0, 0, 1, 1)
        self.label_22 = QtGui.QLabel(self.centralwidget)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.gridLayout_8.addWidget(self.label_22, 0, 4, 1, 1)
        self.label_24 = QtGui.QLabel(self.centralwidget)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.gridLayout_8.addWidget(self.label_24, 2, 4, 1, 1)
        self.label_23 = QtGui.QLabel(self.centralwidget)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.gridLayout_8.addWidget(self.label_23, 1, 4, 1, 1)
        #self.line_5 = QtGui.QFrame(self.centralwidget)
        #self.line_5.setFrameShape(QtGui.QFrame.VLine)
        #self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        #self.line_5.setObjectName(_fromUtf8("line_5"))
        #self.gridLayout_8.addWidget(self.line_5, 0, 1, 1, 1)
        self.label_21 = QtGui.QLabel(self.centralwidget)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout_8.addWidget(self.label_21, 2, 0, 1, 1)
        #self.horizontalSlider_3 = QtGui.QSlider(self.centralwidget)
        #self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        #self.horizontalSlider_3.setObjectName(_fromUtf8("horizontalSlider_3"))
        #self.gridLayout_8.addWidget(self.horizontalSlider_3, 2, 3, 1, 1)
        self.label_25 = QtGui.QLabel(self.centralwidget)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.gridLayout_8.addWidget(self.label_25, 0, 2, 1, 1)
        #self.line_6 = QtGui.QFrame(self.centralwidget)
        #self.line_6.setFrameShape(QtGui.QFrame.VLine)
        #self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        #self.line_6.setObjectName(_fromUtf8("line_6"))
        #self.gridLayout_8.addWidget(self.line_6, 1, 1, 1, 1)
        #self.line_9 = QtGui.QFrame(self.centralwidget)
        #self.line_9.setFrameShape(QtGui.QFrame.VLine)
        #self.line_9.setFrameShadow(QtGui.QFrame.Sunken)
        #self.line_9.setObjectName(_fromUtf8("line_9"))
        #self.gridLayout_8.addWidget(self.line_9, 2, 1, 1, 1)
        self.label_26 = QtGui.QLabel(self.centralwidget)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.gridLayout_8.addWidget(self.label_26, 1, 2, 1, 1)
        self.label_27 = QtGui.QLabel(self.centralwidget)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.gridLayout_8.addWidget(self.label_27, 2, 2, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_8, 26, 2, 1, 1)
        self.line_12 = QtGui.QFrame(self.centralwidget)
        self.line_12.setFrameShape(QtGui.QFrame.HLine)
        self.line_12.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_12.setObjectName(_fromUtf8("line_12"))
        self.gridLayout.addWidget(self.line_12, 27, 2, 1, 1)
        self.line_11 = QtGui.QFrame(self.centralwidget)
        self.line_11.setFrameShape(QtGui.QFrame.HLine)
        self.line_11.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_11.setObjectName(_fromUtf8("line_11"))
        self.gridLayout.addWidget(self.line_11, 27, 0, 1, 1)
        self.gridLayout_9 = QtGui.QGridLayout()
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_9.addWidget(self.label_3, 0, 0, 1, 1)
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.gridLayout_9.addWidget(self.pushButton_5, 0, 2, 1, 1)
        self.spinBox = QtGui.QSpinBox(self.centralwidget)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.gridLayout_9.addWidget(self.spinBox, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_9, 15, 2, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 28, 2, 1, 1)
        self.label_18 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout.addWidget(self.label_18, 19, 2, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout.addWidget(self.pushButton_4, 28, 0, 1, 1)
        self.gridLayout_7 = QtGui.QGridLayout()
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_7.addWidget(self.label_6, 1, 0, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout_7.addWidget(self.lineEdit_3, 1, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_7.addWidget(self.label_7, 0, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_7.addWidget(self.label_5, 0, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout_7.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout_7.addWidget(self.lineEdit_2, 0, 3, 1, 1)
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_7.addWidget(self.label_8, 1, 2, 1, 1)
        self.lineEdit_4 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.gridLayout_7.addWidget(self.lineEdit_4, 1, 3, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_7, 1, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 17, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 835, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSettings = QtGui.QAction(MainWindow)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_4.setText(_translate("MainWindow", "Process Parameters", None))
        #self.checkBox.setText(_translate("MainWindow", "Structural", None))
        self.checkBox_3.setText(_translate("MainWindow", "Freeform", None))
        self.checkBox_2.setText(_translate("MainWindow", "Cavity", None))
        self.label_13.setText(_translate("MainWindow", "Cost (CAD)", None))
        self.label_11.setText(_translate("MainWindow", "Shielding Gas (cfm)", None))
        self.label_12.setText(_translate("MainWindow", "Wire (in)", None))
        self.label_10.setText(_translate("MainWindow", "Build Time (mins)", None))
        self.label_14.setText(_translate("MainWindow", "Process Options", None))
        self.label_9.setText(_translate("MainWindow", "Time and Material Consumption Estimates", None))
        self.pushButton.setText(_translate("MainWindow", "Open", None))
        self.label.setText(_translate("MainWindow", "STL File", None))
        self.pushButton_2.setText(_translate("MainWindow", "Slice", None))
        self.label_2.setText(_translate("MainWindow", "Slice Viewer", None))
        self.label_15.setText(_translate("MainWindow", "Process Geometry", None))
        self.label_17.setText(_translate("MainWindow", "Layer Height (in)", None))
        self.label_16.setText(_translate("MainWindow", "Bead Width (in)", None))
        #self.label_20.setText(_translate("MainWindow", "Cost", None))
        #self.label_19.setText(_translate("MainWindow", "Build Time", None))
        #self.label_22.setText(_translate("MainWindow", "100", None))
        #self.label_24.setText(_translate("MainWindow", "100", None))
        #self.label_23.setText(_translate("MainWindow", "100", None))
        #self.label_21.setText(_translate("MainWindow", "Strength", None))
        #self.label_25.setText(_translate("MainWindow", "0", None))
        #self.label_26.setText(_translate("MainWindow", "0", None))
        #self.label_27.setText(_translate("MainWindow", "0", None))
        self.label_3.setText(_translate("MainWindow", "Path Viewer", None))
        self.pushButton_5.setText(_translate("MainWindow", "Calculate", None))
        self.pushButton_3.setText(_translate("MainWindow", "Output Results to File", None))
        #self.label_18.setText(_translate("MainWindow", "Preferences", None))
        self.pushButton_4.setText(_translate("MainWindow", "Print Window View", None))
        self.label_6.setText(_translate("MainWindow", "Feed Rate (ipm)", None))
        self.label_7.setText(_translate("MainWindow", "Travel Speed (ipm)", None))
        self.label_5.setText(_translate("MainWindow", "Power (W)", None))
        self.label_8.setText(_translate("MainWindow", "Focal Distance(in)", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionSettings.setText(_translate("MainWindow", "Settings", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))


if __name__ == "__main__":
    print(__doc__)
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

