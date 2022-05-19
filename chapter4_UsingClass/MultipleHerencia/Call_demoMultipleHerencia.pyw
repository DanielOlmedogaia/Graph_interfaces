import sys
from PyQt5.QtWidgets import QDialog, QApplication
from  demoMultipleInheritance import *
class Student:
    def __init__(self, code, name):
        self.code = code
        self.name = name
    def getCode(self):
        return self.code
    def getName(self):
        return self.name
class Peso:
    def __init__(self, kgcafe, kgmaiz):
        self.kgcafe= kgcafe
        self.kgmaiz =kgmaiz 
    def getkgMaiz(self):
        self.kgmaiz
    def getkgCafe(self):
        return self.kgcafe
class Result(Student, Peso):
    def __init__(self, code, name, kgmaiz,
        kgcafe):
        Student.__init__(self, code, name)
        Peso.__init__(self,kgcafe, kgmaiz)
        self.totalKilos= kgcafe + kgmaiz
        self.razon = kgmaiz/kgcafe
    def getTotalCafe(self):
        return self.totalKilos
    def getRazonCafe(self):
        return self.razon
class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.MuestraMensaje)
        self.show()
    def MuestraMensaje(self):
        resultObj=Result(self.ui.lineEditCode.text(),
        self.ui.lineEditName.text(),
        int(self.ui.lineEditkgCafe.text()),
        int(self.ui.lineEditkgMaiz.text()))
        self.ui.lineEditkgTotal.setText(str(resultObj.getTotalCafe()))
        self.ui.lineEditRazon.setText(str(resultObj.getRazonCafe()))
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
        