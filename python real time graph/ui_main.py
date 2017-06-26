# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

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
        MainWindow.resize(1243, 605)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.grPlot = PlotWidget(self.centralwidget)
        self.grPlot.setEnabled(True)
        self.grPlot.setGeometry(QtCore.QRect(10, 10, 611, 281))
        self.grPlot.setObjectName(_fromUtf8("grPlot"))
        self.grPlot2 = PlotWidget(self.centralwidget)
        self.grPlot2.setEnabled(True)
        self.grPlot2.setGeometry(QtCore.QRect(640, 10, 591, 281))
        self.grPlot2.setObjectName(_fromUtf8("grPlot2"))
        self.grPlot4 = PlotWidget(self.centralwidget)
        self.grPlot4.setEnabled(True)
        self.grPlot4.setGeometry(QtCore.QRect(640, 300, 591, 281))
        self.grPlot4.setObjectName(_fromUtf8("grPlot4"))
        self.grPlot3 = PlotWidget(self.centralwidget)
        self.grPlot3.setEnabled(True)
        self.grPlot3.setGeometry(QtCore.QRect(10, 300, 611, 281))
        self.grPlot3.setObjectName(_fromUtf8("grPlot3"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))

from pyqtgraph import PlotWidget
