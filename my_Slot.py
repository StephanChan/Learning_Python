from PyQt5 import QtWidgets,QtCore
import time
class work(QtWidgets.QWidget):
    signal=QtCore.pyqtSignal(int)
    def slot(self,num):
        num-=1
        if num>0:
            print("Bob is doing work %d"% num)
            time.sleep(0.5)
            self.signal.emit(num)
