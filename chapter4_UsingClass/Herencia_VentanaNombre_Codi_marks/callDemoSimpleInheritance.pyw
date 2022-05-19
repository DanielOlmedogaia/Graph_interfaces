import sys
from unicodedata import name
from PyQt5.QtWidgets import QDialog, QApplication
from demoSimpleInheritance import *
class Student:
    def __init__(self, cod, nom):
        self.codigo = cod
        self.nombre = nom
    def getCode(self):
        return self.codigo
    def getName(self):
        return self.nombre
class Marks(Student):
    def __init__(self,cod,nom,markX,markY):
        Student.__init__(self,cod,nom)
        self.marcaX=markX
        self.marcaY=markY
    def getMarkX(self):
        return self.marcaX
    def getMarkY(self):
        return self.marcaY
class Ventana(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Coordenadas()
        self.ui.setupUi(self)
        self.ui.pushButtonImprime.clicked.connect(self.MuestraMensaje)
        self.show()
    def MuestraMensaje(self):
        objetoMarcas=Marks(self.ui.lineEditCod.text(),self.ui.lineEditName.text(),self.ui.lineEditX.text(),self.ui.lineEditY.text())
        self.ui.labelOutput.setText("nom:"+objetoMarcas.getName()
                                    +",cod: "+objetoMarcas.getCode()
                                    +", x:"+objetoMarcas.getMarkX()
                                    +", y:"+objetoMarcas.getMarkY()
                                    )
if __name__=="__main__":
    applicacion=QApplication(sys.argv)
    Ventana_actual=Ventana()
    Ventana_actual.show()
    sys.exit(applicacion.exec_())
        
    
