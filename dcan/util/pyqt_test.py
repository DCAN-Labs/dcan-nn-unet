import sys
import os
import subprocess
from test1 import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QThread, pyqtSignal

class Thread(QtCore.QThread):

    finished = pyqtSignal()
    input1 = ''
    input2 = ''
    p = None

    def __init__(self, input1, input2):
        QtCore.QThread.__init__(self)
        self.input1 = input1
        self.input2 = input2

    def run(self):
        self.p = subprocess.Popen(f"python /home/faird/efair/projects/dcan-nn-unet/dcan/img_processing/resize_images.py {self.input1} {self.input2}".split())       
        self.p.wait()
        self.p.kill()
        self.finished.emit()
        #self.str_signal.emit('Emitted message from StringThread. Name = ' + self._name)
        #print("Done run")
        
    def stopp(self):
        print("Stopped process.")
        self.p.kill()

class Window(Ui_MainWindow):
    p = None
    temp_thread = None
    
    def __innit__(self):
        super.__innit__()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.pushButton.clicked.connect(self.on_clicked)     
    
    def on_clicked(self):
        if self.pushButton.text() == "run":
            self.pushButton.setText('cancel')
            # TODO: make this a selected path
            self.temp_thread = Thread(self.lineEdit.text(), self.lineEdit_2.text())
            self.temp_thread.finished.connect(lambda: self.pushButton.setText('run'))
            self.temp_thread.start()
            #self.p = subprocess.Popen(f"python /home/faird/efair/projects/dcan-nn-unet/dcan/img_processing/resize_images.py {self.lineEdit.text()} {self.lineEdit_2.text()}".split())       
        elif self.pushButton.text() == "cancel":
            self.pushButton.setText('run')
            self.temp_thread.stopp()
            self.temp_thread.exit()
            #self.p.kill()     
        
def main(): 
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow() 
    ui = Window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()