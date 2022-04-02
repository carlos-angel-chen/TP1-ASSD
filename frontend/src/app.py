# PyQt5 modules
from PyQt5 import QtWidgets

# Python modules
import sys

# Main window ui import
from src.muestreo import Muestreo


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Muestreo()
    window.show()
    sys.exit(app.exec())
