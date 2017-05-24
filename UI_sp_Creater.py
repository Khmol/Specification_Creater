# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_sp_Creater.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_sp_Creator(object):
    def setupUi(self, sp_Creator):
        sp_Creator.setObjectName("sp_Creator")
        sp_Creator.resize(415, 220)
        sp_Creator.setMinimumSize(QtCore.QSize(415, 220))
        sp_Creator.setMaximumSize(QtCore.QSize(5000, 220))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("11.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("11.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        sp_Creator.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(sp_Creator)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_Choice_File = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Choice_File.setEnabled(True)
        self.pushButton_Choice_File.setGeometry(QtCore.QRect(5, 30, 171, 23))
        self.pushButton_Choice_File.setObjectName("pushButton_Choice_File")
        self.label_File_Name = QtWidgets.QLabel(self.centralwidget)
        self.label_File_Name.setGeometry(QtCore.QRect(10, 10, 401, 16))
        self.label_File_Name.setObjectName("label_File_Name")
        self.pushButton_Create = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Create.setEnabled(False)
        self.pushButton_Create.setGeometry(QtCore.QRect(180, 30, 231, 23))
        self.pushButton_Create.setObjectName("pushButton_Create")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(10, 95, 171, 16))
        self.label_1.setObjectName("label_1")
        self.spinBox_Name = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_Name.setGeometry(QtCore.QRect(180, 90, 42, 22))
        self.spinBox_Name.setObjectName("spinBox_Name")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 65, 171, 16))
        self.label_2.setObjectName("label_2")
        self.spinBox_Pos = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_Pos.setGeometry(QtCore.QRect(180, 60, 42, 22))
        self.spinBox_Pos.setObjectName("spinBox_Pos")
        self.spinBox_Count = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_Count.setGeometry(QtCore.QRect(180, 120, 42, 22))
        self.spinBox_Count.setObjectName("spinBox_Count")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 125, 171, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 155, 171, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_Page_Name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Page_Name.setGeometry(QtCore.QRect(180, 155, 171, 20))
        self.lineEdit_Page_Name.setObjectName("lineEdit_Page_Name")
        sp_Creator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(sp_Creator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 415, 18))
        self.menubar.setObjectName("menubar")
        sp_Creator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(sp_Creator)
        self.statusbar.setObjectName("statusbar")
        sp_Creator.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(sp_Creator)
        self.action.setObjectName("action")

        self.retranslateUi(sp_Creator)
        QtCore.QMetaObject.connectSlotsByName(sp_Creator)

    def retranslateUi(self, sp_Creator):
        _translate = QtCore.QCoreApplication.translate
        sp_Creator.setWindowTitle(_translate("sp_Creator", "Формирователь спецификации"))
        self.pushButton_Choice_File.setText(_translate("sp_Creator", "Выбрать файл"))
        self.label_File_Name.setText(_translate("sp_Creator", "Файл:"))
        self.pushButton_Create.setText(_translate("sp_Creator", "Сформировать спецификацию"))
        self.label_1.setText(_translate("sp_Creator", "№ столбца \"Наименование\""))
        self.label_2.setText(_translate("sp_Creator", "№ столбца \"Поз. обозначение\""))
        self.label_3.setText(_translate("sp_Creator", "№ столбца \"Количество\""))
        self.label_4.setText(_translate("sp_Creator", "Название страницы"))
        self.action.setText(_translate("sp_Creator", "Закрыть"))

