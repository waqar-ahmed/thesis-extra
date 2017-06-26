from PyQt4 import QtGui,QtCore
import sys
import ui_main
import numpy as np
import pylab
import time
import pyqtgraph
from collections import deque
import serial

class ExampleApp(QtGui.QMainWindow, ui_main.Ui_MainWindow):
    def __init__(self, parent=None):
        pyqtgraph.setConfigOption('background', 'w') #before loading widget
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        #self.btnAdd.clicked.connect(self.update)
        self.grPlot.plotItem.showGrid(True, True, 0.7)
        self.grPlot2.plotItem.showGrid(True, True, 0.7)
        self.grPlot3.plotItem.showGrid(True, True, 0.7)
        self.grPlot4.plotItem.showGrid(True, True, 0.7)
        self.xs = deque(maxlen=1000)
        self.ys = deque(maxlen=1000)
        self.ys2 = deque(maxlen=1000)
        self.ys3 = deque(maxlen=1000)
        self.ys4 = deque(maxlen=1000)
        self.raw = serial.Serial("COM8", 115200, timeout=0.5)
        self.pen = pyqtgraph.mkPen(color='r', width=3)
        self.curve = self.grPlot.plot(pen=self.pen,downsample=10)
        self.curve2 = self.grPlot2.plot(pen=self.pen,downsample=10)
        self.curve3 = self.grPlot3.plot(pen=self.pen)
        self.curve4 = self.grPlot4.plot(pen=self.pen)

    def update(self):
        command = self.raw.read(2)
        if command.hex() == "0050":
            data = self.raw.read(8)
            num1 = int(data[:2].hex(), 16)
            num2 = int(data[2:].hex(), 16)
            num3 = int(data[4:].hex(), 16)
            num4 = int(data[6:].hex(), 16)
            self.ys.append(num1)
            self.ys2.append(num2)
            self.ys3.append(num3)
            self.ys4.append(num4)
            tx=time.clock()*1000
            self.xs.append(tx)
            self.curve.setData(self.xs, self.ys)
            #time.sleep(0.00001)
            #self.curve2.setData(self.ys2)
            #self.curve3.setData(self.ys3)
            #self.curve4.setData(self.ys4)
            #self.grPlot.plot(np.array(self.xs),np.array(self.ys),pen=pen,clear=True)


if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    #form.update() #start with something
    timer = QtCore.QTimer()
    timer.timeout.connect(form.update)
    timer.start(0)
    app.exec_()
    print("DONE")