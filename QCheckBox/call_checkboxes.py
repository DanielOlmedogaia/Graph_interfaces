import sys
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from QcheckBoxes_UI import *
class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        ##### Señales de CheckBoxes ####
        
        self.ui.checkBox_Peperoni.stateChanged.connect(self.Sabor)
        self.ui.checkBox_Pina.stateChanged.connect(self.Sabor)
        self.ui.checkBoxQueso.stateChanged.connect(self.Sabor)
        
        ###### señales de Ratio Buttons ######
        
        self.ui.radioButtonCh.toggled.connect(self.Tama)
        self.ui.radioButtonGra.toggled.connect(self.Tama)
        self.ui.radioButtonMed.toggled.connect(self.Tama)
        
    def Sabor(self):
        
        ingredientes=""
        if self.ui.checkBox_Peperoni.isChecked()==True:
            ingredientes=ingredientes+"peperoni"            
        if self.ui.checkBox_Pina.isChecked()==True:
            ingredientes=ingredientes+"piña"
        if self.ui.checkBoxQueso.isChecked()==True:
            ingredientes=ingredientes+"Queso"
        self.ui.labelOutput.setText("Pizza de"+str(ingredientes))

        return ingredientes
            
    def Tama(self):
        tamano=""
        if self.ui.radioButtonCh.isChecked()==True:
            tamano="Pizza Chica"
        if self.ui.radioButtonMed.isChecked()==True:
            tamano="Pizza Mediana"
        if self.ui.radioButtonGra.isChecked()==True:
            tamano="Pizza Grande"
        self.ui.labelOutput.setText(tamano)
        return tamano
        
    
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())