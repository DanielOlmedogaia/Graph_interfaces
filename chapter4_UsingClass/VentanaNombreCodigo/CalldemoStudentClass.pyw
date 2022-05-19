import sys
from PyQt5.QtWidgets import QDialog, QApplication
from prompt_toolkit import Application 
from demoStudentClass import *
class Student:
    def __init__(self,nom,cod):
        self.nombre=nom
        self.codigo=cod
    def getName(self):
        return self.nombre
    def getCode(self):
        return self.codigo
class Ventana(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonClick.clicked.connect(self.MuestraMensaje)
        self.show()
    def MuestraMensaje(self):
        objetoEstudiante=Student(nom=self.ui.lineEditName.text(),cod=self.ui.lineEditCod.text())
        self.ui.labelOutput.setText("el estudiante "+objetoEstudiante.getName()+"Tiene codigo "+objetoEstudiante.getCode())
if __name__=="__main__":
    app=QApplication(sys.argv)
    w=Ventana()
    w.show()
    sys.exit(app.exec_())