# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QRadioButton.ui'
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
        self.radioButtonMelon = QtWidgets.QRadioButton(Dialog)
        self.radioButtonMelon.setGeometry(QtCore.QRect(50, 59, 112, 23))
        self.radioButtonMelon.setObjectName("radioButtonMelon")
        self.radioButtonPapaya = QtWidgets.QRadioButton(Dialog)
        self.radioButtonPapaya.setGeometry(QtCore.QRect(50, 217, 112, 23))
        self.radioButtonPapaya.setObjectName("radioButtonPapaya")
        self.radioButtonSandia = QtWidgets.QRadioButton(Dialog)
        self.radioButtonSandia.setGeometry(QtCore.QRect(50, 138, 112, 23))
        self.radioButtonSandia.setObjectName("radioButtonSandia")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(110, 20, 171, 20))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.labelOutput = QtWidgets.QLabel(Dialog)
        self.labelOutput.setGeometry(QtCore.QRect(160, 250, 171, 17))
        self.labelOutput.setObjectName("labelOutput")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.radioButtonMelon.setText(_translate("Dialog", "Melon"))
        self.radioButtonPapaya.setText(_translate("Dialog", "Papaya"))
        self.radioButtonSandia.setText(_translate("Dialog", "Sandia"))
        self.label.setText(_translate("Dialog", "Escoja solo una fruta"))
        self.labelOutput.setText(_translate("Dialog", "TextLabel"))
