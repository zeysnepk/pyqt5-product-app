# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(311, 289)
        Form.setMinimumSize(QtCore.QSize(311, 289))
        Form.setMaximumSize(QtCore.QSize(311, 289))
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(110, 20, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(98, 10, 111, 41))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.lineEdit_name = QtWidgets.QLineEdit(Form)
        self.lineEdit_name.setGeometry(QtCore.QRect(30, 60, 121, 21))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.label_name = QtWidgets.QLabel(Form)
        self.label_name.setGeometry(QtCore.QRect(73, 61, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_name.setFont(font)
        self.label_name.setStyleSheet("color : rgb(175, 177, 177)")
        self.label_name.setScaledContents(False)
        self.label_name.setObjectName("label_name")
        self.lineEdit_surname = QtWidgets.QLineEdit(Form)
        self.lineEdit_surname.setGeometry(QtCore.QRect(160, 60, 121, 21))
        self.lineEdit_surname.setObjectName("lineEdit_surname")
        self.label_surname = QtWidgets.QLabel(Form)
        self.label_surname.setGeometry(QtCore.QRect(200, 61, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_surname.setFont(font)
        self.label_surname.setStyleSheet("color : rgb(175, 177, 177)")
        self.label_surname.setScaledContents(False)
        self.label_surname.setObjectName("label_surname")
        self.comboBox_country = QtWidgets.QComboBox(Form)
        self.comboBox_country.setGeometry(QtCore.QRect(90, 160, 131, 32))
        self.comboBox_country.setDuplicatesEnabled(False)
        self.comboBox_country.setObjectName("comboBox_country")
        self.comboBox_country.addItem("")
        self.comboBox_country.setItemText(0, "Country")
        self.comboBox_country.addItem("")
        self.comboBox_country.addItem("")
        self.comboBox_country.addItem("")
        self.comboBox_country.addItem("")
        self.comboBox_country.addItem("")
        self.comboBox_country.addItem("")
        self.comboBox_country.addItem("")
        self.comboBox_country.addItem("")
        self.comboBox_country.addItem("")
        self.checkBox_confirm = QtWidgets.QCheckBox(Form)
        self.checkBox_confirm.setGeometry(QtCore.QRect(40, 190, 241, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_confirm.setFont(font)
        self.checkBox_confirm.setObjectName("checkBox_confirm")
        self.pushButton_send = QtWidgets.QPushButton(Form)
        self.pushButton_send.setGeometry(QtCore.QRect(100, 210, 100, 32))
        self.pushButton_send.setObjectName("pushButton_send")
        self.lineEdit_username = QtWidgets.QLineEdit(Form)
        self.lineEdit_username.setGeometry(QtCore.QRect(70, 100, 171, 21))
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.label_username = QtWidgets.QLabel(Form)
        self.label_username.setGeometry(QtCore.QRect(130, 100, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_username.setFont(font)
        self.label_username.setStyleSheet("color : rgb(175, 177, 177)")
        self.label_username.setScaledContents(False)
        self.label_username.setObjectName("label_username")
        self.lineEdit_password = QtWidgets.QLineEdit(Form)
        self.lineEdit_password.setGeometry(QtCore.QRect(70, 130, 171, 21))
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.label_password = QtWidgets.QLabel(Form)
        self.label_password.setGeometry(QtCore.QRect(130, 130, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_password.setFont(font)
        self.label_password.setStyleSheet("color : rgb(175, 177, 177)")
        self.label_password.setObjectName("label_password")
        self.label_text = QtWidgets.QLabel(Form)
        self.label_text.setGeometry(QtCore.QRect(40, 250, 241, 16))
        self.label_text.setText("")
        self.label_text.setObjectName("label_text")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(50, 100, 16, 81))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(245, 100, 16, 81))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "REGISTER"))
        self.label_name.setText(_translate("Form", "name"))
        self.label_surname.setText(_translate("Form", "surname"))
        self.comboBox_country.setItemText(1, _translate("Form", "ABD"))
        self.comboBox_country.setItemText(2, _translate("Form", "Belgium"))
        self.comboBox_country.setItemText(3, _translate("Form", "England"))
        self.comboBox_country.setItemText(4, _translate("Form", "France"))
        self.comboBox_country.setItemText(5, _translate("Form", "Germany"))
        self.comboBox_country.setItemText(6, _translate("Form", "Greece"))
        self.comboBox_country.setItemText(7, _translate("Form", "Italy"))
        self.comboBox_country.setItemText(8, _translate("Form", "Poland"))
        self.comboBox_country.setItemText(9, _translate("Form", "Turkey"))
        self.checkBox_confirm.setText(_translate("Form", "I confirm the accuracy of my information"))
        self.pushButton_send.setText(_translate("Form", "SEND"))
        self.label_username.setText(_translate("Form", "username"))
        self.label_password.setText(_translate("Form", "password"))

