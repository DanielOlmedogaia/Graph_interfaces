# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imprimeNombreUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 151, 20))
        self.label.setObjectName("label")
        self.lineEditNombre = QtWidgets.QLineEdit(Dialog)
        self.lineEditNombre.setGeometry(QtCore.QRect(170, 30, 141, 25))
        self.lineEditNombre.setObjectName("lineEditNombre")
        self.pushButtonImprime = QtWidgets.QPushButton(Dialog)
        self.pushButtonImprime.setGeometry(QtCore.QRect(140, 90, 89, 25))
        self.pushButtonImprime.setObjectName("pushButtonImprime")
        self.labelOutput = QtWidgets.QLabel(Dialog)
        self.labelOutput.setGeometry(QtCore.QRect(66, 170, 271, 20))
        self.labelOutput.setText("")
        self.labelOutput.setObjectName("labelOutput")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Introduce tu nombre"))
        self.pushButtonImprime.setText(_translate("Dialog", "PushButton"))