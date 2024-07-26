import sys
import os
import signal
import subprocess
import psutil

from test1 import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QThread, pyqtSignal, QTimer

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
        # Start subprocess and wait for it to finish
        p = subprocess.Popen(["python", f"{self.input1}dcan/util/automation_test.py", self.input1, self.input2, self.input3, self.input4, self.input5, self.input6, self.input7, self.input8]) 
        self.processes.append(p)
        p.wait()
        self.finished.emit() # Tells the program that the subprocess finished
        
    def stop(self):
        if len(self.processes) > 0:
            print("Stopping Process...")
            parent = psutil.Process(self.processes[-1].pid) 
            for child in parent.children(recursive=True):  # Kill current subprocess and all child subprocesses
                child.kill()
            parent.kill()
            print("PROCESS STOPPED")

class Window(Ui_MainWindow):
    temp_thread = None
    inputDict = {}
    
    def __innit__(self):
        super.__innit__()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        
        # Put all input fields in a dictionary
        self.inputDict['dcan_path'] = self.line_dcan_path
        self.inputDict['synth_path'] = self.line_synth_path
        self.inputDict['task_path'] = self.line_task_path
        self.inputDict['raw_data_base_path'] = self.line_raw_data_base_path
        self.inputDict['modality'] = self.line_modality
        self.inputDict['task_number'] = self.line_task_number
        self.inputDict['distribution'] = self.line_distribution
        self.inputDict['synth_img_amt'] = self.line_synth_img_amt
        
        # Some setup stuff
        self.menuiuhwuaibfa.setTitle("TEST PROGRAM")
        self.pushButton.setText('run')
        self.pushButton_2.setText('Populate Preset')
        self.pushButton.clicked.connect(self.run_program)
        self.pushButton_2.clicked.connect(self.populate_inputs)
        self.button_clear.clicked.connect(self.clear_inputs)
        self.button_save.clicked.connect(self.save_presets)
    
    def run_program(self):
        # If process isn't currently running
        if self.pushButton.text() == "run":
            # Make sure all inputs are filled
            if any(inp.text() == "" for inp in self.inputDict.values()):
                print("Please fill out all input fields")
                self.menuiuhwuaibfa.setTitle("Please fill out all input fields")
            else:
                self.menuiuhwuaibfa.setTitle("Running...")
                # Start new worker thread to run main program. Allows UI to continue working along with it
                self.temp_thread = Thread(self.line_dcan_path.text(), self.line_task_path.text(), self.line_synth_path.text(), self.line_raw_data_base_path.text(),
                                        self.line_modality.text(), self.line_task_number.text(), self.line_distribution.text(), self.line_synth_img_amt.text())
                self.temp_thread.finished.connect(lambda: self.pushButton.setText('run')) # Listen for when process finishes
                self.temp_thread.start()
                self.pushButton.setText('cancel')
        # If process is currently running
        elif self.pushButton.text() == "cancel":
            self.menuiuhwuaibfa.setTitle("Program Stopped")
            self.temp_thread.stop() # Stops subrocesses within thread. This will cause the finish signal to be sent
            self.pushButton.setText('run')
            
    def populate_inputs(self):
        f = open(f"automation_presets/preset_test.txt")
        lines = [line for line in f.readlines() if line.strip()] # Ignore blank lines

        for line in lines:
            line = line.strip().split('=')
            # If there is no info associated with a certain input, clear the input line
            if len(line) == 1:
                self.inputDict[line[0]].clear() 
            elif len(line) == 2:
                self.inputDict[line[0]].setText(line[1])
                    
        f.close()
            
    def save_presets(self):
        # Make sure file doesn't exist yet and create presets data
        if not os.path.isfile("./automation_presets/preset_test.txt"):
            f = open("./automation_presets/preset_test.txt", "w")
            for key, val in self.inputDict.items():
                f.write(f"{key}={val.text()}\n")
            f.close()
        else:
            print("File already exists")
            self.menuiuhwuaibfa.setTitle("File already exists")
        
    def clear_inputs(self):
        # Clear all input fields
        for key in self.inputDict.keys():
            self.inputDict[key].clear()
        
    def sleepSec(self, sec):
        # Disable buttons if needed
        self.pushButton.setEnabled(False)
        QTimer.singleShot(sec * 1000, lambda: self.pushButton.setDisabled(False))
        
def main(): 
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow() 
    ui = Window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()