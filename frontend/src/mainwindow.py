# PyQt5 modules
from PyQt5.QtWidgets import QMainWindow

# Project modules
from src.ui.mainwindow import Ui_Muestreo

# Utilities
from matplotlib.backends.backend_qt5agg import (FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure

class MainWindow(QMainWindow, Ui_Muestreo):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.pushButton_actualizar.clicked.connect(self.Update_clicked)
        self.pushButton_actualizar.setStyleSheet("QPushButton"
                                         "{"
                                         "background-color : grey;"
                                         "}"
                                         "QPushButton::pressed"
                                         "{"
                                         "background-color : lightblue;"
                                         "}"
                                         )

        self.figure_tiempo = Figure()  #Creo widget Figura
        self.canvas_tiempo = FigureCanvas(self.figure_tiempo) #le pongo un canvas
        self.toolbar_tiempo = NavigationToolbar(self.canvas_tiempo, self) #creo widget toolbar
        self.Layout_tiempo.addWidget(self.toolbar_tiempo) #meto los widgets en el layout
        self.Layout_tiempo.addWidget(self.canvas_tiempo)

        self.figure_frec = Figure()
        self.canvas_frec = FigureCanvas(self.figure_frec)
        self.toolbar_frec = NavigationToolbar(self.canvas_frec, self)
        self.Layout_frec.addWidget(self.toolbar_frec)
        self.Layout_frec.addWidget(self.canvas_frec)

        self.ax_tiempo = self.figure_tiempo.subplots()
        self.figure_tiempo.subplots_adjust(bottom=0.2)
        self.ax_tiempo.grid(which="both")
        self.ax_tiempo.set_xscale("log")
        self.ax_tiempo.set_title("Osciloscopio", fontsize=10)
        self.ax_tiempo.set_ylabel("Amplitud [V]", fontsize=10)
        self.ax_tiempo.set_xlabel("Tiempo [s]", fontsize=10)

        self.ax_frec = self.figure_frec.subplots()
        self.figure_frec.subplots_adjust(bottom=0.2)
        self.ax_frec.grid(which="both")
        self.ax_frec.set_xscale("log")
        self.ax_frec.set_title("Analizador de espectros", fontsize=10)
        self.ax_frec.set_ylabel("Amplitud [V]", fontsize=10)
        self.ax_frec.set_xlabel("Frecuencia [Hz]", fontsize=10)


    def Update_clicked(self):
        #Grafica las cosas
        pass
