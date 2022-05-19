import sys
from PyQt5.QtWidgets import QDialog, QApplication
from LineEditClass import *
""" en este ejercicio se creó una clase Estudiante,el primer metodo recibe como
primer parametro "self" y como segundo name, así un estudiante está definido  unicamente por 
el atributo name.
"""
class Student:
    name = ""
    def __init__(self, nombre):
        # declaramos que el atributo "nombre completo" es el parametro "nombre" 
        self.nombre_completo=nombre
    #Creamos un metodo que devuelva el nombre completo del estudiante
    def printName(self):
        return self.nombre_completo
#Note que ahora la clase "MyForm" es independiente de la clase Student    
class MyForm(QDialog):
    #La clase "MyForm" solo puede mostrar un mensaje(es la unica accion que puede hace)
    # y es por eso que solo tiene un metodo distinto a "init"
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        #Indicamo que, cuando se emita la señal clicked de QpushButton
        self.ui.pushButtonClickMe.clicked.connect(self.dispmessage)
        self.show()
    def dispmessage(self):
        #instanciamos un objeto de la clase "Student"
        studentObj=Student(self.ui.lineEditName.text())
        self.ui.labelResponse.setText("Hello "+studentObj.printName())
"""En resumen: en el metodo init hemos colocado todas las señales y en cada metodo hemos instanciado 
los objetos propios del metodo para así poder utilizar sus atributos como 'Salidas' """
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())