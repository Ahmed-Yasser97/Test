# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Task.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(718, 596)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.sliderc = QtWidgets.QSlider(self.tab_3)
        self.sliderc.setOrientation(QtCore.Qt.Vertical)
        self.sliderc.setObjectName("sliderc")
        self.gridLayout_3.addWidget(self.sliderc, 0, 0, 1, 1)
        self.Sliderb = QtWidgets.QSlider(self.tab_3)
        self.Sliderb.setOrientation(QtCore.Qt.Vertical)
        self.Sliderb.setObjectName("Sliderb")
        self.gridLayout_3.addWidget(self.Sliderb, 0, 1, 1, 1)
        self.phantom = QtWidgets.QLabel(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phantom.sizePolicy().hasHeightForWidth())
        self.phantom.setSizePolicy(sizePolicy)
        self.phantom.setMinimumSize(QtCore.QSize(20, 20))
        self.phantom.setMaximumSize(QtCore.QSize(512, 512))
        self.phantom.setScaledContents(True)
        self.phantom.setObjectName("phantom")
        self.gridLayout_3.addWidget(self.phantom, 0, 2, 1, 1)
        self.Decay = PlotWidget(self.tab_3)
        self.Decay.setMaximumSize(QtCore.QSize(1000000, 1000000))
        self.Decay.setObjectName("Decay")
        self.gridLayout_3.addWidget(self.Decay, 0, 5, 1, 1)
        self.Recovery = PlotWidget(self.tab_3)
        self.Recovery.setMaximumSize(QtCore.QSize(1000000, 1000000))
        self.Recovery.setObjectName("Recovery")
        self.gridLayout_3.addWidget(self.Recovery, 1, 5, 1, 1)
        self.Browse = QtWidgets.QPushButton(self.tab_3)
        self.Browse.setObjectName("Browse")
        self.gridLayout_3.addWidget(self.Browse, 2, 2, 1, 1)
        self.ST = QtWidgets.QLabel(self.tab_3)
        self.ST.setObjectName("ST")
        self.gridLayout_3.addWidget(self.ST, 2, 3, 1, 1)
        self.SpanTime = QtWidgets.QSpinBox(self.tab_3)
        self.SpanTime.setMaximum(200)
        self.SpanTime.setObjectName("SpanTime")
        self.gridLayout_3.addWidget(self.SpanTime, 2, 4, 1, 1)
        self.TissueProperty = QtWidgets.QComboBox(self.tab_3)
        self.TissueProperty.setObjectName("TissueProperty")
        self.TissueProperty.addItem("")
        self.TissueProperty.addItem("")
        self.TissueProperty.addItem("")
        self.TissueProperty.addItem("")
        self.gridLayout_3.addWidget(self.TissueProperty, 3, 2, 1, 1)
        self.TR_3 = QtWidgets.QLabel(self.tab_3)
        self.TR_3.setObjectName("TR_3")
        self.gridLayout_3.addWidget(self.TR_3, 3, 3, 1, 1)
        self.TR = QtWidgets.QSpinBox(self.tab_3)
        self.TR.setMaximum(6000)
        self.TR.setObjectName("TR")
        self.gridLayout_3.addWidget(self.TR, 3, 4, 1, 1)
        self.PhantomSize = QtWidgets.QComboBox(self.tab_3)
        self.PhantomSize.setObjectName("PhantomSize")
        self.PhantomSize.addItem("")
        self.PhantomSize.addItem("")
        self.PhantomSize.addItem("")
        self.PhantomSize.addItem("")
        self.gridLayout_3.addWidget(self.PhantomSize, 4, 2, 1, 1)
        self.TE_3 = QtWidgets.QLabel(self.tab_3)
        self.TE_3.setObjectName("TE_3")
        self.gridLayout_3.addWidget(self.TE_3, 4, 3, 1, 1)
        self.TE = QtWidgets.QSpinBox(self.tab_3)
        self.TE.setMaximum(6000)
        self.TE.setObjectName("TE")
        self.gridLayout_3.addWidget(self.TE, 4, 4, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.tab_4)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 3, 1, 1)
        self.phantom_2 = QtWidgets.QLabel(self.tab_4)
        self.phantom_2.setScaledContents(True)
        self.phantom_2.setObjectName("phantom_2")
        self.gridLayout_2.addWidget(self.phantom_2, 1, 0, 1, 1)
        self.output_2 = QtWidgets.QLabel(self.tab_4)
        self.output_2.setScaledContents(True)
        self.output_2.setObjectName("output_2")
        self.gridLayout_2.addWidget(self.output_2, 1, 3, 1, 1)
        self.kspace = QtWidgets.QPushButton(self.tab_4)
        self.kspace.setObjectName("kspace")
        self.gridLayout_2.addWidget(self.kspace, 2, 1, 1, 1)
        self.FA = QtWidgets.QSpinBox(self.tab_4)
        self.FA.setObjectName("FA")
        self.gridLayout_2.addWidget(self.FA, 2, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab_4)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab_4)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 3, 3, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 718, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.phantom.setText(_translate("MainWindow", "phantom"))
        self.Browse.setText(_translate("MainWindow", "Browse"))
        self.ST.setText(_translate("MainWindow", "Span time"))
        self.TissueProperty.setItemText(0, _translate("MainWindow", "Tissue property"))
        self.TissueProperty.setItemText(1, _translate("MainWindow", "T1"))
        self.TissueProperty.setItemText(2, _translate("MainWindow", "T2"))
        self.TissueProperty.setItemText(3, _translate("MainWindow", "PD"))
        self.TR_3.setText(_translate("MainWindow", "TR"))
        self.PhantomSize.setItemText(0, _translate("MainWindow", "Phantom size"))
        self.PhantomSize.setItemText(1, _translate("MainWindow", "128*128"))
        self.PhantomSize.setItemText(2, _translate("MainWindow", "512*512"))
        self.PhantomSize.setItemText(3, _translate("MainWindow", "20*20"))
        self.TE_3.setText(_translate("MainWindow", "TE"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Tab 1"))
        self.phantom_2.setText(_translate("MainWindow", "phantom"))
        self.output_2.setText(_translate("MainWindow", "output"))
        self.kspace.setText(_translate("MainWindow", "Kspace"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Tab 2"))

from pyqtgraph import PlotWidget
