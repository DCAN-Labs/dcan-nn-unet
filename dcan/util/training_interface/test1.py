# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QCompleter, QComboBox, QCheckBox
import PyQt5_stylesheets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(892, 749) 
        
        MainWindow.setStyleSheet(PyQt5_stylesheets.load_stylesheet_pyqt5(style="style_Dark"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.line_dcan_path = QtWidgets.QLineEdit(self.centralwidget)
        self.line_dcan_path.setObjectName("line_dcan_path")
        self.gridLayout.addWidget(self.line_dcan_path, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 18, 0, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 4, 1, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        self.button_clear= QtWidgets.QPushButton(self.centralwidget)
        self.button_clear.setObjectName("button_clear")
        self.gridLayout.addWidget(self.button_clear, 18, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        self.button_save= QtWidgets.QPushButton(self.centralwidget)
        self.button_save.setObjectName("button_save")
        self.gridLayout.addWidget(self.button_save, 0, 1, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        self.button_remove= QtWidgets.QPushButton(self.centralwidget)
        self.button_remove.setObjectName("button_remove")
        self.gridLayout.addWidget(self.button_remove, 2, 1, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        self.button_select_all=QtWidgets.QPushButton(self.centralwidget)
        self.button_select_all.setObjectName("button_select_all")
        #self.gridLayout.addWidget(self.button_select_all, 15, 1, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        self.button_select_all.setGeometry(QtCore.QRect(510, 490, 120, 26))

        self.check_overwrite = QtWidgets.QCheckBox(self.centralwidget)
        self.check_overwrite.setObjectName("check_overwrite")
        self.gridLayout.addWidget(self.check_overwrite, 0, 1, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.line_save_preset = QtWidgets.QLineEdit(self.centralwidget)
        self.line_save_preset.setObjectName("line_save_preset")
        self.gridLayout.addWidget(self.line_save_preset, 1, 1, 1, 2)
        # self.line_remove_preset = QtWidgets.QLineEdit(self.centralwidget)
        # self.line_remove_preset.setObjectName("line_remove_preset")
        # self.gridLayout.addWidget(self.line_remove_preset, 3, 1, 1, 2)
        
        #self.comboBox_remove_preset = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_remove_preset = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_remove_preset.setObjectName("comboBox_remove_preset")
        self.comboBox_remove_preset.setFixedSize(200, 30)  # Set fixed size
        self.gridLayout.addWidget(self.comboBox_remove_preset, 3, 1, 1, 2)
        self.comboBox_remove_preset.addItem('-- Remove Preset --')
        
        # self.line_set_preset = QtWidgets.QLineEdit(self.centralwidget)
        # self.line_set_preset.setObjectName("line_set_preset")
        # self.gridLayout.addWidget(self.line_set_preset, 5, 1, 1, 2)
        #'''
        self.comboBox_preset = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_preset.setObjectName("comboBox_preset")
        self.comboBox_preset.setFixedSize(200, 30)  # Set fixed size
        self.gridLayout.addWidget(self.comboBox_preset, 5, 1, 1, 2)
        
        
        
        self.comboBox_preset.setEditable(True) 
        self.comboBox_preset.completer().setCompletionMode(QtWidgets.QCompleter.PopupCompletion) 
        self.comboBox_preset.setInsertPolicy(QComboBox.NoInsert) 
        
     #
        
        self.comboBox_remove_preset.setEditable(True) 
        self.comboBox_remove_preset.completer().setCompletionMode(QtWidgets.QCompleter.PopupCompletion) 
        self.comboBox_remove_preset.setInsertPolicy(QComboBox.NoInsert) 

        self.checkBoxes = []  # Store references to checkboxes
        run_list = ['Resize Images', 'Mins/Maxs', 'SynthSeg Image Creation', 'Copying SynthSeg Images Over', 'Create JSON File','Plan and Preprocess','Training the Model', 'Running Inference']
        for i in range(8):
            self.checkBox = QCheckBox(run_list[i], self.centralwidget)
            self.checkBox.setObjectName(f'checkBox_{i}')
            self.gridLayout.addWidget(self.checkBox, i+7, 1, 1, 1)
            self.checkBoxes.append(self.checkBox)

        self.label_i = QtWidgets.QLabel(self.centralwidget)
        self.label_i.setObjectName("label_i")
        self.gridLayout.addWidget(self.label_i, 6, 1, 1, 1)


        #'''
        self.label_overwrite = QtWidgets.QLabel(self.centralwidget)
        self.label_overwrite.setMaximumSize(QtCore.QSize(150, 20))
        self.label_overwrite.setObjectName("label_overwrite")
        self.gridLayout.addWidget(self.label_overwrite, 0, 2, 1, 1)
        self.label_raw_data_base_path = QtWidgets.QLabel(self.centralwidget)
        self.label_raw_data_base_path.setMaximumSize(QtCore.QSize(150, 20))
        self.label_raw_data_base_path.setObjectName("label_raw_data_base_path")
        self.gridLayout.addWidget(self.label_raw_data_base_path, 6, 0, 1, 1)
        self.label_distribution = QtWidgets.QLabel(self.centralwidget)
        self.label_distribution.setMaximumSize(QtCore.QSize(150, 20))
        self.label_distribution.setObjectName("label_distribution")
        self.gridLayout.addWidget(self.label_distribution, 12, 0, 1, 1)
        self.line_synth_path = QtWidgets.QLineEdit(self.centralwidget)
        self.line_synth_path.setObjectName("line_synth_path")
        self.gridLayout.addWidget(self.line_synth_path, 5, 0, 1, 1)
        self.label_task_number = QtWidgets.QLabel(self.centralwidget)
        self.label_task_number.setMaximumSize(QtCore.QSize(150, 20))
        self.label_task_number.setObjectName("label_task_number")
        self.gridLayout.addWidget(self.label_task_number, 10, 0, 1, 1)
        self.line_synth_img_amt = QtWidgets.QLineEdit(self.centralwidget)
        self.line_synth_img_amt.setObjectName("line_synth_img_amt")
        self.gridLayout.addWidget(self.line_synth_img_amt, 15, 0, 1, 1, QtCore.Qt.AlignTop)
       # self.line_slurm_scripts_path = QtWidgets.QLineEdit(self.centralwidget)
       # self.line_slurm_scripts_path.setObjectName("line_slurm_scripts_path")
       # self.gridLayout.addWidget(self.line_slurm_scripts_path, 17, 0, 1, 1, QtCore.Qt.AlignTop)
        self.line_modality = QtWidgets.QLineEdit(self.centralwidget)
        self.line_modality.setObjectName("line_modality")
        self.gridLayout.addWidget(self.line_modality, 9, 0, 1, 1)
        self.label_synth_img_amt = QtWidgets.QLabel(self.centralwidget)
        self.label_synth_img_amt.setMaximumSize(QtCore.QSize(300, 20))
        self.label_synth_img_amt.setObjectName("label_synth_img_amt")
        self.gridLayout.addWidget(self.label_synth_img_amt, 14, 0, 1, 1)
        #self.label_slurm_scripts_path = QtWidgets.QLabel(self.centralwidget)
        #self.label_slurm_scripts_path.setMaximumSize(QtCore.QSize(300, 20))
       # self.label_slurm_scripts_path.setObjectName("label_slurm_scripts_path")
        #self.gridLayout.addWidget(self.label_slurm_scripts_path, 16, 0, 1, 1)
        self.label_task_path = QtWidgets.QLabel(self.centralwidget)
        self.label_task_path.setMaximumSize(QtCore.QSize(300, 20))
        self.label_task_path.setObjectName("label_task_path")
        self.gridLayout.addWidget(self.label_task_path, 2, 0, 1, 1)
        self.label_dcan_path = QtWidgets.QLabel(self.centralwidget)
        self.label_dcan_path.setMaximumSize(QtCore.QSize(150, 20))
        self.label_dcan_path.setObjectName("label_dcan_path")
        self.gridLayout.addWidget(self.label_dcan_path, 0, 0, 1, 1)
        self.label_modality = QtWidgets.QLabel(self.centralwidget)
        self.label_modality.setMaximumSize(QtCore.QSize(150, 20))
        self.label_modality.setObjectName("label_modality")
        self.gridLayout.addWidget(self.label_modality, 8, 0, 1, 1)
        self.line_raw_data_base_path = QtWidgets.QLineEdit(self.centralwidget)
        self.line_raw_data_base_path.setObjectName("line_raw_data_base_path")
        self.gridLayout.addWidget(self.line_raw_data_base_path, 7, 0, 1, 1)
        self.line_task_path = QtWidgets.QLineEdit(self.centralwidget)
        self.line_task_path.setObjectName("line_task_path")
        self.gridLayout.addWidget(self.line_task_path, 3, 0, 1, 1)
        self.line_task_number = QtWidgets.QLineEdit(self.centralwidget)
        self.line_task_number.setObjectName("line_task_number")
        self.gridLayout.addWidget(self.line_task_number, 11, 0, 1, 1)
        self.label_synth_path = QtWidgets.QLabel(self.centralwidget)
        self.label_synth_path.setMaximumSize(QtCore.QSize(150, 20))
        self.label_synth_path.setObjectName("label_synth_path")
        self.gridLayout.addWidget(self.label_synth_path, 4, 0, 1, 1)
        self.line_distribution = QtWidgets.QLineEdit(self.centralwidget)
        self.line_distribution.setObjectName("line_distribution")
        self.gridLayout.addWidget(self.line_distribution, 13, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 892, 26))
        self.menubar.setObjectName("menubar")
        self.menuiuhwuaibfa = QtWidgets.QMenu(self.menubar)
        self.menuiuhwuaibfa.setObjectName("menuiuhwuaibfa")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuiuhwuaibfa.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton_2"))
        self.button_clear.setText(_translate("MainWindow", "clear"))
        self.button_save.setText(_translate("MainWindow", "Save Preset"))
        self.button_remove.setText(_translate("MainWindow", "Remove Preset"))
        self.label_overwrite.setText(_translate("MainWindow", "Overwrite Save?"))
        self.label_raw_data_base_path.setText(_translate("MainWindow", "Raw Data Base Path"))
        self.label_distribution.setText(_translate("MainWindow", "Distribution (uniform, normal)"))
        self.label_task_number.setText(_translate("MainWindow", "Task Number"))
        self.label_synth_img_amt.setText(_translate("MainWindow", "Number of SynthSeg Generated Images"))
        self.label_task_path.setText(_translate("MainWindow", "Task Path"))
        self.label_dcan_path.setText(_translate("MainWindow", "Dcan-nn-unet Path"))
        self.label_modality.setText(_translate("MainWindow", "Modality (t1, t2, t1t2)"))
        self.label_synth_path.setText(_translate("MainWindow", "SynthSeg Path"))
        self.button_select_all.setText(_translate("MainWindow", "Select All Boxes"))
        #self.label_slurm_scripts_path.setText(_translate("MainWindow", "Slurm Scripts Path"))
        self.menuiuhwuaibfa.setTitle(_translate("MainWindow", "iuhwuaibfa"))
        
        self.label_i.setText(_translate("MainWindow", "Select Which Features You Would Like to Run"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
