# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Task2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1065, 873)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Browse = QtWidgets.QPushButton(self.centralwidget)
        self.Browse.setObjectName("Browse")
        self.verticalLayout.addWidget(self.Browse)
        self.PhantomSize = QtWidgets.QComboBox(self.centralwidget)
        self.PhantomSize.setObjectName("PhantomSize")
        self.PhantomSize.addItem("")
        self.PhantomSize.addItem("")
        self.PhantomSize.addItem("")
        self.PhantomSize.addItem("")
        self.verticalLayout.addWidget(self.PhantomSize)
        self.TissueProperty = QtWidgets.QComboBox(self.centralwidget)
        self.TissueProperty.setObjectName("TissueProperty")
        self.TissueProperty.addItem("")
        self.TissueProperty.addItem("")
        self.TissueProperty.addItem("")
        self.TissueProperty.addItem("")
        self.verticalLayout.addWidget(self.TissueProperty)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ST = QtWidgets.QLabel(self.centralwidget)
        self.ST.setObjectName("ST")
        self.verticalLayout_2.addWidget(self.ST)
        self.SpanTime = QtWidgets.QSpinBox(self.centralwidget)
        self.SpanTime.setMaximum(200)
        self.SpanTime.setObjectName("SpanTime")
        self.verticalLayout_2.addWidget(self.SpanTime)
        self.TE_2 = QtWidgets.QLabel(self.centralwidget)
        self.TE_2.setObjectName("TE_2")
        self.verticalLayout_2.addWidget(self.TE_2)
        self.TE = QtWidgets.QSpinBox(self.centralwidget)
        self.TE.setMaximum(6000)
        self.TE.setObjectName("TE")
        self.verticalLayout_2.addWidget(self.TE)
        self.TR_2 = QtWidgets.QLabel(self.centralwidget)
        self.TR_2.setObjectName("TR_2")
        self.verticalLayout_2.addWidget(self.TR_2)
        self.TR = QtWidgets.QSpinBox(self.centralwidget)
        self.TR.setMaximum(6000)
        self.TR.setObjectName("TR")
        self.verticalLayout_2.addWidget(self.TR)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.sliderc = QtWidgets.QScrollBar(self.tab)
        self.sliderc.setMinimum(-30)
        self.sliderc.setMaximum(30)
        self.sliderc.setOrientation(QtCore.Qt.Vertical)
        self.sliderc.setObjectName("sliderc")
        self.horizontalLayout_2.addWidget(self.sliderc)
        self.Sliderb = QtWidgets.QScrollBar(self.tab)
        self.Sliderb.setMinimum(-30)
        self.Sliderb.setMaximum(30)
        self.Sliderb.setOrientation(QtCore.Qt.Vertical)
        self.Sliderb.setObjectName("Sliderb")
        self.horizontalLayout_2.addWidget(self.Sliderb)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.phantom = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phantom.sizePolicy().hasHeightForWidth())
        self.phantom.setSizePolicy(sizePolicy)
        self.phantom.setMinimumSize(QtCore.QSize(20, 20))
        self.phantom.setMaximumSize(QtCore.QSize(512, 512))
        self.phantom.setScaledContents(True)
        self.phantom.setObjectName("phantom")
        self.gridLayout_2.addWidget(self.phantom, 0, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Recovery = PlotWidget(self.tab)
        self.Recovery.setMaximumSize(QtCore.QSize(1000000, 1000000))
        self.Recovery.setObjectName("Recovery")
        self.verticalLayout_3.addWidget(self.Recovery)
        self.Decay = PlotWidget(self.tab)
        self.Decay.setMaximumSize(QtCore.QSize(1000000, 1000000))
        self.Decay.setObjectName("Decay")
        self.verticalLayout_3.addWidget(self.Decay)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 2, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.phantom_2 = QtWidgets.QLabel(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phantom_2.sizePolicy().hasHeightForWidth())
        self.phantom_2.setSizePolicy(sizePolicy)
        self.phantom_2.setMinimumSize(QtCore.QSize(500, 500))
        self.phantom_2.setScaledContents(True)
        self.phantom_2.setObjectName("phantom_2")
        self.horizontalLayout_3.addWidget(self.phantom_2)
        self.output_2 = QtWidgets.QLabel(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output_2.sizePolicy().hasHeightForWidth())
        self.output_2.setSizePolicy(sizePolicy)
        self.output_2.setMinimumSize(QtCore.QSize(500, 500))
        self.output_2.setScaledContents(True)
        self.output_2.setObjectName("output_2")
        self.horizontalLayout_3.addWidget(self.output_2)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.kspace = QtWidgets.QPushButton(self.tab_2)
        self.kspace.setObjectName("kspace")
        self.verticalLayout_4.addWidget(self.kspace)
        self.FA = QtWidgets.QSpinBox(self.tab_2)
        self.FA.setMaximum(270)
        self.FA.setObjectName("FA")
        self.verticalLayout_4.addWidget(self.FA)
        self.verticalLayout_6.addLayout(self.verticalLayout_4)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_5.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1065, 21))
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
        self.Browse.setText(_translate("MainWindow", "Browse"))
        self.PhantomSize.setItemText(0, _translate("MainWindow", "Phantom size"))
        self.PhantomSize.setItemText(1, _translate("MainWindow", "128*128"))
        self.PhantomSize.setItemText(2, _translate("MainWindow", "512*512"))
        self.PhantomSize.setItemText(3, _translate("MainWindow", "20*20"))
        self.TissueProperty.setItemText(0, _translate("MainWindow", "Tissue property"))
        self.TissueProperty.setItemText(1, _translate("MainWindow", "T1"))
        self.TissueProperty.setItemText(2, _translate("MainWindow", "T2"))
        self.TissueProperty.setItemText(3, _translate("MainWindow", "PD"))
        self.ST.setText(_translate("MainWindow", "Span time"))
        self.TE_2.setText(_translate("MainWindow", "TE"))
        self.TR_2.setText(_translate("MainWindow", "TR"))
        self.phantom.setText(_translate("MainWindow", "phantom"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.phantom_2.setText(_translate("MainWindow", "phantom"))
        self.output_2.setText(_translate("MainWindow", "output"))
        self.kspace.setText(_translate("MainWindow", "Kspace"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))

from pyqtgraph import PlotWidget
