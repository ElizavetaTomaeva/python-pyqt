# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_widget.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(331, 208)
        self.loginBtn = QtWidgets.QPushButton(Form)
        self.loginBtn.setGeometry(QtCore.QRect(20, 140, 131, 23))
        self.loginBtn.setObjectName("loginBtn")
        self.exitBtn = QtWidgets.QPushButton(Form)
        self.exitBtn.setGeometry(QtCore.QRect(180, 140, 131, 23))
        self.exitBtn.setObjectName("exitBtn")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 40, 91, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 47, 13))
        self.label_2.setObjectName("label_2")
        self.editLogin = QtWidgets.QLineEdit(Form)
        self.editLogin.setGeometry(QtCore.QRect(142, 40, 151, 20))
        self.editLogin.setObjectName("editLogin")
        self.editPassword = QtWidgets.QLineEdit(Form)
        self.editPassword.setGeometry(QtCore.QRect(142, 90, 151, 20))
        self.editPassword.setObjectName("editPassword")
        self.warning = QtWidgets.QLabel(Form)
        self.warning.setGeometry(QtCore.QRect(90, 10, 141, 16))
        self.warning.setObjectName("warning")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.loginBtn.setText(_translate("Form", "Войти"))
        self.exitBtn.setText(_translate("Form", "Выйти"))
        self.label.setText(_translate("Form", "Пользователь"))
        self.label_2.setText(_translate("Form", "Пароль"))
        self.warning.setText(_translate("Form", "Неверный логин или пароль"))

