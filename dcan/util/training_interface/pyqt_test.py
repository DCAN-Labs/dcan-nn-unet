import sys
import os
import signal
import subprocess
import psutil

from test1 import Ui_MainWindow
from k_login import Ui_LoginWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject, QThread, pyqtSignal, QTimer, Qt

class Thread(QtCore.QThread):
    finished = pyqtSignal()
    input1 = ''
    input2 = ''
    input3 = ''
    input4 = ''
    #input5 = ''
    input6 = ''
    input7 = ''
    input8 = ''
    input9 = ''
    processes = []
    script_dir = ""

    def __init__(self, input1, input2, input3, input4, input6, input7, input8, input9, script_dir):
        QtCore.QThread.__init__(self)
        self.input1 = input1
        self.input2 = input2
        self.input3 = input3
        self.input4 = input4
        #self.input5 = input5
        self.input6 = input6
        self.input7 = input7
        self.input8 = input8
        self.input9 = input9
        self.script_dir = script_dir

    def run(self):
        # Start subprocess and wait for it to finish
        p = subprocess.Popen(["python", f"{self.script_dir}/automation_test.py", self.input1, self.input2, self.input3, self.input4, self.input6, self.input7, self.input8, self.input9]) 
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

class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    temp_thread = None
    inputDict = {}
    script_dir = ''
    running = False
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
                
        # Get the directory of this file
        self.script_dir = os.path.abspath(os.path.dirname(__file__))
        os.chdir(self.script_dir)  
        
        # Set up presets
        num = 0
        for file in os.listdir(f"{self.script_dir}/automation_presets"):
            file = file[:-7]
            self.comboBox_preset.addItem(file)
            num += 1 
        if num == 0:
            self.comboBox_preset.setItemText(0, 'You do not have any presets')
            self.comboBox_preset.setStyleSheet("background-color: rgb(137, 137, 137)")
        
        # Put all input fields in a dictionary
        self.inputDict['dcan_path'] = self.line_dcan_path
        self.inputDict['synth_path'] = self.line_synth_path
        self.inputDict['task_path'] = self.line_task_path
        self.inputDict['raw_data_base_path'] = self.line_raw_data_base_path
        self.inputDict['modality'] = self.line_modality
        self.inputDict['task_number'] = self.line_task_number
        self.inputDict['distribution'] = self.line_distribution
        self.inputDict['synth_img_amt'] = self.line_synth_img_amt
        #self.inputDict['slurm_scripts_path'] = self.line_slurm_scripts_path
        
        # Some setup stuff
        self.menuiuhwuaibfa.setTitle("TEST PROGRAM")
        self.pushButton.setText('run')
        self.pushButton_2.setText('Populate Preset')
        self.pushButton.clicked.connect(self.run_program)
        self.pushButton_2.clicked.connect(self.populate_inputs)
        self.button_clear.clicked.connect(self.clear_inputs)
        self.button_save.clicked.connect(self.save_preset)
        self.button_remove.clicked.connect(self.remove_preset)
    
    def run_program(self):
        # If process isn't currently running
        if self.running == False:
            # Make sure all inputs are filled
            if any(inp.text() == "" for inp in self.inputDict.values()):
                print("Please fill out all input fields")
                self.menuiuhwuaibfa.setTitle("Please fill out all input fields")
            else:
                self.menuiuhwuaibfa.setTitle("Running...")
                # Start new worker thread to run main program. Allows UI to continue working along with it
                self.temp_thread = Thread(self.line_dcan_path.text(), self.line_task_path.text(), self.line_synth_path.text(), self.line_raw_data_base_path.text(), 
                                          self.line_modality.text(), self.line_task_number.text(), self.line_distribution.text(), self.line_synth_img_amt.text(), self.script_dir)
                #self.temp_thread.finished.connect(lambda: self.pushButton.setText('run')) # Listen for when process finishes
                self.temp_thread.finished.connect(self.on_finish_thread) # Listen for when process finishes
                self.temp_thread.start()
                self.running = True
                self.pushButton.setText('cancel')
        # If process is currently running
        elif self.running == True:
            self.menuiuhwuaibfa.setTitle("Program Stopped")
            self.temp_thread.stop() # Stops subrocesses within thread. This will cause the finish signal to be sent
            self.running = False
            self.pushButton.setText('run')
        
    def on_finish_thread(self):
        self.running = False
        self.pushButton.setText('run')
            
    def populate_inputs(self):
        if self.comboBox_preset.currentIndex()>0:
            try:
                f = open(f"{self.script_dir}/automation_presets/{self.comboBox_preset.currentText()}.config")
                lines = [line for line in f.readlines() if line.strip()] # Ignore blank lines

                for line in lines:
                    line = line.strip().split('=')
                    # If there is no info associated with a certain input, clear the input line
                    if len(line) == 1:
                        self.inputDict[line[0]].clear() 
                    elif len(line) == 2:
                        self.inputDict[line[0]].setText(line[1])
                            
                f.close()
                print("Preset Loaded")
                self.menuiuhwuaibfa.setTitle("Preset Loaded")
            except:
                print("File Does Not Exist")
                self.menuiuhwuaibfa.setTitle("File Does Not Exist")
            
    def save_preset(self):
        if self.line_save_preset.text().strip() == "":
            return
        if any(inp.text() == "" for inp in self.inputDict.values()):
            print("Please fill out at least one input")
            self.menuiuhwuaibfa.setTitle("Please fill out at least one input")
            return
        # If overwrite is checked, delete the file if it exists already
        if self.check_overwrite.isChecked(): 
            if os.path.isfile(f"{self.script_dir}/automation_presets/{self.line_save_preset.text()}.config"):
                os.remove(f"{self.script_dir}/automation_presets/{self.line_save_preset.text()}.config")
                self.comboBox_preset.removeItem(self.comboBox_preset.findText(self.line_save_preset.text()))
        # Make sure file doesn't exist yet and create presets data
        if not os.path.isfile(f"{self.script_dir}/automation_presets/{self.line_save_preset.text()}.config"):
            f = open(f"{self.script_dir}/automation_presets/{self.line_save_preset.text()}.config", "w")
            for key, val in self.inputDict.items():
                f.write(f"{key}={val.text()}\n")
            f.close()
            self.comboBox_preset.setItemText(0, '-- Select Preset --')
            self.comboBox_preset.setStyleSheet("")
            self.comboBox_preset.addItem(self.line_save_preset.text())
            self.comboBox_preset.setCurrentText(self.line_save_preset.text())
            print("Preset Saved")
            self.menuiuhwuaibfa.setTitle("Preset Saved")
        else:
            print("File Already Exists")
            self.menuiuhwuaibfa.setTitle("File Already Exists")
            
    def remove_preset(self):
        # Delete file if it exists
        if os.path.isfile(f"{self.script_dir}/automation_presets/{self.line_remove_preset.text()}.config"):
            os.remove(f"{self.script_dir}/automation_presets/{self.line_remove_preset.text()}.config")
            self.comboBox_preset.removeItem(self.comboBox_preset.findText(self.line_remove_preset.text()))
            
            # if self.comboBox_preset.count() < 2:
            #     self.comboBox_preset.setItemText(0, 'You do not have any presets')
            #     self.comboBox_preset.setStyleSheet("background-color: rgb(137, 137, 137)")
            
            print("Preset Removed")
            self.menuiuhwuaibfa.setTitle("Preset Removed")
        else:
            print("File Does Not Exist")
            self.menuiuhwuaibfa.setTitle("File Does Not Exist")
        
    def clear_inputs(self):
        # Clear all input fields
        for key in self.inputDict.keys():
            self.inputDict[key].clear()
        
    def sleepSec(self, sec):
        # Disable buttons if needed
        self.pushButton.setEnabled(False)
        QTimer.singleShot(sec * 1000, lambda: self.pushButton.setEnabled(True))
        
    def closeEvent(self, event):
        print("CLOSING")
        # Override the close event to execute a function first
        if self.running == True:
            reply = QMessageBox.question(self, 'Close Confirmation', 
                                        "A program is currently running. Quitting now will cause it to stop at its current step, you will be able to start from here again if you wish to continue later. Are you sure you want to quit?", 
                                        QMessageBox.Yes | QMessageBox.No, 
                                        QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.run_program()
                event.accept()  # Accept the event to close the window
            else:
                event.ignore()  # Ignore the event to prevent the window from closing
        
class LoginWindow(QtWidgets.QMainWindow, Ui_LoginWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        #self.comboBox_preset = SearchableComboBox(self)
        #self.gridLayout.addWidget(self.comboBox_preset, 5, 1, 1, 2)
        
        self.button_launch_ui.setText('Launch UI')
        self.button_launch_ui.clicked.connect(self.run_uiScript)
        
        # Get the directory of this file
        self.script_dir = os.path.abspath(os.path.dirname(__file__))  
    
        
        for file in os.listdir(f"{self.script_dir}/automation_presets"):
            file = file[:-7]
            self.comboBox.addItem(file)
        
        if self.comboBox.count() < 2:
            self.comboBox.setItemText(0, 'You do not have any presets')
            self.comboBox.setStyleSheet("background-color: rgb(137, 137, 137)")
    
    def run_uiScript(self):
        self.new_ui = Window()
        self.new_ui.show() 
        if self.comboBox.currentIndex()>0:
            self.new_ui.comboBox_preset.setCurrentText(self.comboBox.currentText())
            self.new_ui.populate_inputs()
        self.close()
         
    def set_background_image(self, image_path):
        self.setStyleSheet(f"QMainWindow {{background-image: url({image_path}); background-repeat: no-repeat; background-position: center;}}")

def main(): 
    # app = QtWidgets.QApplication(sys.argv)
    # ui = LoginWindow()
    # ui.show()
    # sys.exit(app.exec_())
    
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Windows')
    with open('/home/faird/efair/projects/dcan-nn-unet/dcan/util/training_interface/style.qss', 'r') as file:
        stylesheet = file.read()
    app.setStyleSheet(stylesheet)
    ui = LoginWindow()
    ui.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()