import sys
from PyQt5.QtWidgets import QDialog, QApplication
from QRadioButtonUI import *
class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.radioButtonMelon.toggled.connect(self.MuestraPrecio)
        self.ui.radioButtonPapaya.toggled.connect(self.MuestraPrecio)
        self.ui.radioButtonSandia.toggled.connect(self.MuestraPrecio)
        self.show()
    def MuestraPrecio(self):
        fare=0
        if self.ui.radioButtonMelon.isChecked()==True:
            fare=150
        if self.ui.radioButtonPapaya.isChecked()==True:
            fare=125
        if self.ui.radioButtonSandia.isChecked()==True:
            fare=100
        self.ui.labelOutput.setText("la fruta cuesta "+str(fare)+" Pesos")
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
