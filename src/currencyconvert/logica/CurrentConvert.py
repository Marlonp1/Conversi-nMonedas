import sys
import os

from PyQt6.QtWidgets import QApplication, QDialog
from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox

class Dialogo(QDialog):

    AusInUS = 1.5
    UKInUS = 1.27
    YENInUS = 0.0063
    PENInUS = 0.26

    def __init__(self):
        ruta = os.path.dirname(os.path.abspath(__file__)) + r"\..\vista\CurrencyConvert.ui"
        super().__init__()
        uic.loadUi(ruta, self)

        self.pbConvert.clicked.connect(self.calculate_convert)
        self.pbExit.clicked.connect(self.exit_app)

    def calculate_convert(self):
        initial = float(self.ltAmount.text())
        converted = initial


        if self.brFromUK.isChecked():
            converted *= self.UKInUS
        elif self.brFromAUS.isChecked():
            converted *= self.AusInUS
        elif self.brFromYEN.isChecked():
            converted *= self.YENInUS
        elif self.brFromPEN.isChecked():
            converted *= self.PENInUS

        if self.brToUK.isChecked():
            converted /= self.UKInUS
        elif self.brToAUS.isChecked():
            converted /= self.AusInUS
        elif self.brToYEN.isChecked():
            converted /= self.YENInUS
        elif self.brToPEN.isChecked():
            converted /= self.PENInUS

        self.lbResult.setText(f"{converted:.2f}")

    def exit_app(self):
        resultado = QMessageBox.question(self, "Salir", "¿Está seguro que desea salir?", QMessageBox.StandardButtons(QMessageBox.Yes | QMessageBox.No))
        if resultado == QMessageBox.StandardButton.Yes:
            sys.exit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialogo = Dialogo()
    dialogo.show()
    sys.exit(app.exec())
