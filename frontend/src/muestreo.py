# PyQt5 modules
from PyQt5.QtWidgets import QMainWindow

# Project modules
from src.ui.muestreo import Ui_Muestreo


class Muestreo(QMainWindow, Ui_Muestreo):

    def __init__(self):
        super(Muestreo, self).__init__()
        self.setupUi(self)
