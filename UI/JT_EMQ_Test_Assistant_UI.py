# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'JT_EMQ_Test_Assistant_UI.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_JT_EMQ_Test_Assistant(object):
    def setupUi(self, JT_EMQ_Test_Assistant):
        JT_EMQ_Test_Assistant.setObjectName("JT_EMQ_Test_Assistant")
        JT_EMQ_Test_Assistant.resize(1222, 914)
        self.centralwidget = QtWidgets.QWidget(JT_EMQ_Test_Assistant)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 381, 21))
        self.label.setObjectName("label")
        self.Connect_EMQ_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Connect_EMQ_Button.setGeometry(QtCore.QRect(30, 60, 201, 51))
        self.Connect_EMQ_Button.setObjectName("Connect_EMQ_Button")
        self.Emq_connect_lable = QtWidgets.QLabel(self.centralwidget)
        self.Emq_connect_lable.setGeometry(QtCore.QRect(260, 70, 251, 31))
        self.Emq_connect_lable.setObjectName("Emq_connect_lable")
        self.Send_EMQ_Bowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.Send_EMQ_Bowser.setGeometry(QtCore.QRect(630, 590, 411, 201))
        self.Send_EMQ_Bowser.setObjectName("Send_EMQ_Bowser")
        self.Receive_label = QtWidgets.QLabel(self.centralwidget)
        self.Receive_label.setGeometry(QtCore.QRect(50, 200, 141, 16))
        self.Receive_label.setObjectName("Receive_label")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(470, 190, 91, 19))
        self.checkBox.setObjectName("checkBox")
        self.Send_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.Send_label_2.setGeometry(QtCore.QRect(640, 570, 141, 16))
        self.Send_label_2.setObjectName("Send_label_2")
        self.Rec_Data_Clean_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Rec_Data_Clean_Button.setGeometry(QtCore.QRect(470, 800, 93, 28))
        self.Rec_Data_Clean_Button.setObjectName("Rec_Data_Clean_Button")
        self.Send_Data_Clean_Button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Send_Data_Clean_Button_2.setGeometry(QtCore.QRect(950, 800, 93, 28))
        self.Send_Data_Clean_Button_2.setObjectName("Send_Data_Clean_Button_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(620, 60, 521, 501))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.Cpmmand_labe = QtWidgets.QLabel(self.centralwidget)
        self.Cpmmand_labe.setGeometry(QtCore.QRect(630, 30, 141, 16))
        self.Cpmmand_labe.setObjectName("Cpmmand_labe")
        self.Receive_EMQ_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.Receive_EMQ_textEdit.setGeometry(QtCore.QRect(40, 220, 521, 571))
        self.Receive_EMQ_textEdit.setObjectName("Receive_EMQ_textEdit")
        JT_EMQ_Test_Assistant.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(JT_EMQ_Test_Assistant)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1222, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        JT_EMQ_Test_Assistant.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(JT_EMQ_Test_Assistant)
        self.statusbar.setObjectName("statusbar")
        JT_EMQ_Test_Assistant.setStatusBar(self.statusbar)
        self.actionImport_configuration_file = QtWidgets.QAction(JT_EMQ_Test_Assistant)
        self.actionImport_configuration_file.setShortcut("")
        self.actionImport_configuration_file.setObjectName("actionImport_configuration_file")
        self.actionEMQ = QtWidgets.QAction(JT_EMQ_Test_Assistant)
        self.actionEMQ.setObjectName("actionEMQ")
        self.actionConnect_EMQ_Button = QtWidgets.QAction(JT_EMQ_Test_Assistant)
        self.actionConnect_EMQ_Button.setObjectName("actionConnect_EMQ_Button")
        self.menuFile.addAction(self.actionImport_configuration_file)
        self.menuSetting.addAction(self.actionEMQ)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())

        self.retranslateUi(JT_EMQ_Test_Assistant)
        QtCore.QMetaObject.connectSlotsByName(JT_EMQ_Test_Assistant)

    def retranslateUi(self, JT_EMQ_Test_Assistant):
        _translate = QtCore.QCoreApplication.translate
        JT_EMQ_Test_Assistant.setWindowTitle(_translate("JT_EMQ_Test_Assistant", "MainWindow"))
        self.label.setText(_translate("JT_EMQ_Test_Assistant", "Before you use pls check the setting "))
        self.Connect_EMQ_Button.setStatusTip(_translate("JT_EMQ_Test_Assistant", "Connect to EMQ accroding to setting"))
        self.Connect_EMQ_Button.setText(_translate("JT_EMQ_Test_Assistant", "Connect to EMQ"))
        self.Emq_connect_lable.setText(_translate("JT_EMQ_Test_Assistant", "EMQ Disconnect"))
        self.Receive_label.setText(_translate("JT_EMQ_Test_Assistant", "Receive Data"))
        self.checkBox.setText(_translate("JT_EMQ_Test_Assistant", "Save log"))
        self.Send_label_2.setText(_translate("JT_EMQ_Test_Assistant", "Send Data"))
        self.Rec_Data_Clean_Button.setText(_translate("JT_EMQ_Test_Assistant", "Clean"))
        self.Send_Data_Clean_Button_2.setText(_translate("JT_EMQ_Test_Assistant", "Clean"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("JT_EMQ_Test_Assistant", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("JT_EMQ_Test_Assistant", "2"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("JT_EMQ_Test_Assistant", "Command Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("JT_EMQ_Test_Assistant", "Data"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("JT_EMQ_Test_Assistant", "Time"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("JT_EMQ_Test_Assistant", "Activate"))
        self.Cpmmand_labe.setText(_translate("JT_EMQ_Test_Assistant", "Command List"))
        self.menuFile.setTitle(_translate("JT_EMQ_Test_Assistant", "File(&F)"))
        self.menuSetting.setTitle(_translate("JT_EMQ_Test_Assistant", "Setting(&S)"))
        self.actionImport_configuration_file.setText(_translate("JT_EMQ_Test_Assistant", "Import Configuration file"))
        self.actionEMQ.setText(_translate("JT_EMQ_Test_Assistant", "EMQ"))
        self.actionEMQ.setStatusTip(_translate("JT_EMQ_Test_Assistant", "EMQ Setting"))
        self.actionEMQ.setShortcut(_translate("JT_EMQ_Test_Assistant", "Ctrl+S"))
        self.actionConnect_EMQ_Button.setText(_translate("JT_EMQ_Test_Assistant", "actionConnect_EMQ_Button"))
