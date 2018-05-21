import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QColor, QBrush
import threading
import random

class Labella(QLabel):

    def __init__(self, parent):
        super().__init__(parent=parent)

        self.setStyleSheet('QFrame {background-color:grey;}')
        self.resize(200, 200)
        self.color=0

    def paintEvent(self, e):
        qp = QPainter(self)
        self.color=random.randint(0,255)
        self.drawRectangles(qp,self.color)
        print(self.color)
        qp.setBrush(QColor(200, 0, 0))
        qp.drawRect(0,0,20,20)

    def drawRectangles(self, qp,color):
        qp.setBrush(QColor(color, 0, 0, 100))
        qp.save() # save the QPainter config

        qp.drawRect(10, 15, 20, 20)

        qp.setBrush(QColor(0, 0, color, 100))
        qp.drawRect(50, 15, 20, 20)

        qp.restore() # restore the QPainter config
        qp.drawRect(100, 15, 20, 20)

class Example(QWidget):

    def __init__(self):
        super().__init__()

        lb = Labella(self)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Colours')
        self.show()
def update(target):
    for i in range(10):
        target.color=i*25
        target.update()
        time.sleep(0.5)
        #print(i)

if __name__ == '__main__':
    import time
    app = QApplication(sys.argv)
    ex = Example()
    a_thread=threading.Thread(target=update,args=(ex,))
    a_thread.start()
    sys.exit(app.exec_())