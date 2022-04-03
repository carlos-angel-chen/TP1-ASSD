# PyQt5 modules
from PyQt5.QtWidgets import QMainWindow

# Project modules
from src.ui.mainwindow import Ui_Muestreo


class MainWindow(QMainWindow, Ui_Muestreo):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
