import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from k_login import Ui_LoginWindow  # Generated from your .ui file
import subprocess


class MainWindow(Ui_LoginWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
    
        # super(MainWindow, self).__init__(parent)
        # self.setupUi(self)
        # self.pushButton.clicked.connect(self.on_clicked)
    def setupUi(self,MainWindow):
        super().setupUi(MainWindow)
        
        self.button_launch_ui.setText('Launch UI')
        self.button_launch_ui.clicked.connect(self.run_uiScript)
    def run_uiScript(self):
        
        if self.comboBox.currentIndex()>0:
            subprocess.run(['python', 'pyqt_test.py','--preset', self.comboBox.currentText()])
        else:
            subprocess.run(['python', 'pyqt_test.py'])
         
    def set_background_image(self, image_path):
        self.setStyleSheet(f"QMainWindow {{background-image: url({image_path}); background-repeat: no-repeat; background-position: center;}}")
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow() 
    ui = MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()