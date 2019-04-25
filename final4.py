import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
from pyqtgraph import PlotWidget
import numpy as np

x = np.array([1, 2, 3])
y = np.array([1, 2, 3])
pg.setConfigOption('background', 'w')
penn = pg.mkPen('k', width = 2, style = QtCore.Qt.SolidLine)
pl = pg.plot(x, y, pen = penn, title = 'The firts pyqtgraph plot', symbol = 't', symbolSize = 20)
pl.setXRange(0, 4)
pl.setYRange(0, 4)
pl.setLabel('left', 'Voltage', 'V')
pl.setLable('bottom', 'Time', 's')

QtGui.QApplication.exec_()
