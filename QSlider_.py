from PyQt5.QtWidgets import QApplication, QLabel, QSlider
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

class slider(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):

        self.slider = QSlider(Qt.Horizontal, self)
        #self.slider.setFocusPolicy(Qt.NoFocus)
        #self.slider.setGeometry(30, 40, 100, 30)
        self.slider.valueChanged.connect(self.changeValue)
        self.slider.setRange(0,65534)

    def changeValue(self):
        print(self.slider.value())

if __name__=='__main__':
    import sys

    app = QApplication(sys.argv)
    qb = slider()
    qb.show()
    sys.exit(app.exec_())