import sys
from PyQt5.QtWidgets import QDialog, QApplication, QLineEdit
from imprimeNombreUI import *
class Ventana(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonImprime.clicked.connect(self.muestraNombre)
        self.ui.lineEditNombre.setEchoMode(QLineEdit.Password)
        self.show()
    def muestraNombre(self):
        self.ui.labelOutput.setText("Hola "
        +self.ui.lineEditNombre.text())
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = Ventana()
    w.show()
    sys.exit(app.exec_())