# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'note_edit_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(564, 313)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(210, 270, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 10, 541, 261))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.titleEdit = QtWidgets.QLineEdit(self.widget)
        self.titleEdit.setObjectName("titleEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.titleEdit)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.contentEdit = QtWidgets.QPlainTextEdit(self.widget)
        self.contentEdit.setObjectName("contentEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.contentEdit)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.plannedDateTimeEdit = QtWidgets.QDateTimeEdit(self.widget)
        self.plannedDateTimeEdit.setObjectName("plannedDateTimeEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.plannedDateTimeEdit)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Новая заметка"))
        self.label.setText(_translate("Dialog", "Наименование"))
        self.label_2.setText(_translate("Dialog", "Текст"))
        self.label_3.setText(_translate("Dialog", "Дата"))

