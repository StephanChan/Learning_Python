from PyQt5 import QtWidgets,QtCore
import sys
import my_Slot
import my_Signal



if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_signal=my_Signal.work()
    my_slot=my_Slot.work()
    my_signal.signal.connect(my_slot.slot)
    my_slot.signal.connect(my_signal.slot)
    my_signal.signal.emit(10)
    sys.exit(app.exec_())





