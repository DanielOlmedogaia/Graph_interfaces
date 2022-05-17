#Se construye a continuacion una ventana en donde se puede elegir la talla y el color de una playera
#No olvide que se deben asignar grupos en Qt designer para que los grupos sean mutuamente excluyentes
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from RatioButtonGROUP_UI import *
class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.radioButtonMed.toggled.connect(self.dispSelected)
        self.ui.radioButtonChica.toggled.connect(self.dispSelected)
        self.ui.radioButtonGra.toggled.connect(self.dispSelected)
        self.ui.radioButtonAzul.toggled.connect(self.dispSelected)
        self.ui.radioButtonNegra.toggled.connect(self.dispSelected)
        self.ui.radioButtonRoja.toggled.connect(self.dispSelected)
        self.show()

    def dispSelected(self):
        selected1=""
        selected2=""
        if self.ui.radioButtonMed.isChecked()==True:
            selected1="Mediana"
        if self.ui.radioButtonChica.isChecked()==True:
            selected1="Chica"
        if self.ui.radioButtonGra.isChecked()==True:
            selected1="Grande"
        if self.ui.radioButtonNegra.isChecked()==True:
            selected2="color Negra"
        if self.ui.radioButtonRoja.isChecked()==True:
            selected2="Color Roja"
        if self.ui.radioButtonAzul.isChecked()==True:
            selected2="Color Azul"
        self.ui.labelOutput.setText("playera "+selected1+" de " + selected2)
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
