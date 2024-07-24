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
    input3 = ''
    input4 = ''
    input5 = ''
    input6 = ''
    input7 = ''
    input8 = ''
    processes = []

    def __init__(self, input1, input2, input3, input4, input5, input6, input7, input8):
        QtCore.QThread.__init__(self)
        self.input1 = input1
        self.input2 = input2
        self.input3 = input3
        self.input4 = input4
        self.input5 = input5
        self.input6 = input6
        self.input7 = input7
        self.input8 = input8

    def run(self):
        # TODO: make this a selected path
        #print("RUNNING!")
        #p = subprocess.run(["bash", "/home/faird/efair/projects/dcan-nn-unet/dcan/util/export_automation_test.sh", self.input1, self.input2, self.input3, self.input4, self.input5, self.input6, self.input7, self.input8])
        p = subprocess.run(["python", "/home/faird/efair/projects/dcan-nn-unet/dcan/util/automation_test.py", self.input1, self.input2, self.input3, self.input4, self.input5, self.input6, self.input7, self.input8])     
        self.processes.append(p)
        
        self.finished.emit()
        #self.str_signal.emit('Emitted message from StringThread. Name = ' + self._name)
        #print("Done run")
        
    def stop(self):
        print("Stopped process.")
        
        if len(self.processes) > 0:
            self.processes[0].kill()
            

class Window(Ui_MainWindow):
    #p = None
    temp_thread = None
    
    def __innit__(self):
        super.__innit__()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        
        self.line_dcan_path.setText("/home/faird/efair/projects/dcan-nn-unet/")
        self.line_synth_path.setText("/home/faird/efair/projects/SynthSeg/")
        self.line_modality.setText("t2")
        self.line_distribution.setText("uniform")
        self.line_synth_img_amt.setText("0")
        self.line_task_number.setText("545")
        self.line_task_path.setText("/scratch.global/lundq163/nnUNet_HBCD_noFlip_noMirr/nnUNet_raw_data_base/nnUNet_raw_data/Task545/")
        self.line_raw_data_base_path.setText("/scratch.global/lundq163/nnUNet_HBCD_noFlip_noMirr/nnUNet_raw_data_base/")
        
        self.pushButton.setText('run')
        self.pushButton.clicked.connect(self.on_clicked)
        
        
    
    def on_clicked(self):
        if self.pushButton.text() == "run":
            self.pushButton.setText('cancel')
            self.temp_thread = Thread(self.line_dcan_path.text(), self.line_task_path.text(), self.line_synth_path.text(), self.line_raw_data_base_path.text(),
                                      self.line_modality.text(), self.line_task_number.text(), self.line_distribution.text(), self.line_synth_img_amt.text())
            self.temp_thread.finished.connect(lambda: self.pushButton.setText('run'))
            self.temp_thread.start()
        elif self.pushButton.text() == "cancel":
            print("STOPPING PROCESSSSSSS")
            self.temp_thread.stop()
            self.temp_thread.exit()
            self.pushButton.setText('run')
            #self.p.kill()     
    
    def change_label_text(self, label):
        self.menuiuhwuaibfa.setText(label)
        
def main(): 
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow() 
    ui = Window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()