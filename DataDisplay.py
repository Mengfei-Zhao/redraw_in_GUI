from Ui_DataDisplayUI import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout
import sys
import numpy as np

from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.lines import Line2D


class Figure_Canvas(FigureCanvas):
    def __init__(self, parent=None, width=3.9, height=2.7, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        super(Figure_Canvas, self).__init__(self.fig)
        self.ax = self.fig.add_subplot(111)


class ImgDisp(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(ImgDisp, self).__init__(parent)
        self.setupUi(self)
        self.Init_Widgets()
        self.pushButton.clicked.connect(
            self.updatePlot)
        self.pushButtonClickedTimes = 1

    def Init_Widgets(self):
        self.PrepareSamples()
        self.PrepareLineCanvas()

    def PrepareSamples(self):
        self.x = np.arange(-4, 4, 0.02)
        self.y = np.sin(self.x)

    def PrepareLineCanvas(self):
        self.LineFigure = Figure_Canvas()
        self.LineFigureLayout = QGridLayout(self.LineDisplayGB)
        self.LineFigureLayout.addWidget(self.LineFigure)
        # self.LineFigure.ax.set_xlim(-4, 4)
        # self.LineFigure.ax.set_ylim(-1, 1)
        self.line = Line2D(self.x, self.y)
        self.LineFigure.ax.add_line(self.line)
        self.LineFigure.ax.autoscale_view()

    def updatePlot(self):
        self.LineFigure.ax.cla()
        self.x = np.arange(0, 10*self.pushButtonClickedTimes, 1)
        self.y = np.sin(self.x) * self.pushButtonClickedTimes
        self.LineFigure.ax.set_xlabel('x')
        self.LineFigure.ax.set_ylabel('y')
        # self.LineFigure.ax.plot(self.x, self.y) # This is same as the two line behind
        self.line = Line2D(self.x, self.y)
        self.LineFigure.ax.add_line(self.line)

        self.LineFigure.ax.autoscale_view()  # must lies behind add_line()
        self.LineFigure.draw()
        self.pushButtonClickedTimes += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = ImgDisp()
    ui.show()
    sys.exit(app.exec_())
