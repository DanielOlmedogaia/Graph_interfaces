# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RatioButtonGroup.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(490, 349)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(90, 10, 211, 17))
        self.label.setObjectName("label")
        self.radioButtonChica = QtWidgets.QRadioButton(Dialog)
        self.radioButtonChica.setGeometry(QtCore.QRect(40, 40, 112, 23))
        self.radioButtonChica.setObjectName("radioButtonChica")
        self.buttonGroupTAM = QtWidgets.QButtonGroup(Dialog)
        self.buttonGroupTAM.setObjectName("buttonGroupTAM")
        self.buttonGroupTAM.addButton(self.radioButtonChica)
        self.radioButtonMed = QtWidgets.QRadioButton(Dialog)
        self.radioButtonMed.setGeometry(QtCore.QRect(40, 70, 112, 23))
        self.radioButtonMed.setObjectName("radioButtonMed")
        self.buttonGroupTAM.addButton(self.radioButtonMed)
        self.radioButtonGra = QtWidgets.QRadioButton(Dialog)
        self.radioButtonGra.setGeometry(QtCore.QRect(40, 100, 112, 23))
        self.radioButtonGra.setObjectName("radioButtonGra")
        self.buttonGroupTAM.addButton(self.radioButtonGra)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(90, 150, 201, 17))
        self.label_2.setObjectName("label_2")
        self.radioButtonRoja = QtWidgets.QRadioButton(Dialog)
        self.radioButtonRoja.setGeometry(QtCore.QRect(40, 190, 112, 23))
        self.radioButtonRoja.setObjectName("radioButtonRoja")
        self.buttonGroupCOLOR = QtWidgets.QButtonGroup(Dialog)
        self.buttonGroupCOLOR.setObjectName("buttonGroupCOLOR")
        self.buttonGroupCOLOR.addButton(self.radioButtonRoja)
        self.radioButtonAzul = QtWidgets.QRadioButton(Dialog)
        self.radioButtonAzul.setGeometry(QtCore.QRect(40, 220, 112, 23))
        self.radioButtonAzul.setObjectName("radioButtonAzul")
        self.buttonGroupCOLOR.addButton(self.radioButtonAzul)
        self.radioButtonNegra = QtWidgets.QRadioButton(Dialog)
        self.radioButtonNegra.setGeometry(QtCore.QRect(40, 250, 112, 23))
        self.radioButtonNegra.setObjectName("radioButtonNegra")
        self.buttonGroupCOLOR.addButton(self.radioButtonNegra)
        self.labelOutput = QtWidgets.QLabel(Dialog)
        self.labelOutput.setGeometry(QtCore.QRect(100, 290, 321, 20))
        self.labelOutput.setObjectName("labelOutput")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Escoje un tamaño de playera"))
        self.radioButtonChica.setText(_translate("Dialog", "Chica"))
        self.radioButtonMed.setText(_translate("Dialog", "Mediana"))
        self.radioButtonGra.setText(_translate("Dialog", "Grande"))
        self.label_2.setText(_translate("Dialog", "Escoje el color de tu playera"))
        self.radioButtonRoja.setText(_translate("Dialog", "Roja"))
        self.radioButtonAzul.setText(_translate("Dialog", "Azul"))
        self.radioButtonNegra.setText(_translate("Dialog", "Negra"))
        self.labelOutput.setText(_translate("Dialog", "TextLabel"))
