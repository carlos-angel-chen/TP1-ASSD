# PyQt5 modules
from PyQt5.QtWidgets import QMainWindow

# Project modules
from src.ui.mainwindow import Ui_Muestreo

# Utilities
from matplotlib.backends.backend_qt5agg import (FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
import backend.recive as RCV

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
        signal = self.comboBox_signal.currentText()
        Av = self.doubleSpinBox_Av.value()
        frec = self.doubleSpinBox_frec.value()
        theta = self.doubleSpinBox_theta.value()
        frec_unit = self.comboBox_frec.currentText()
        periodo = self.doubleSpinBox_T_muestreo.value()
        periodo_unit = self.comboBox_T_muestreo.currentText()
        DC = self.doubleSpinBox_DC.value()

        if (frec_unit == "KHz"):
            frec *= 1000
        if (periodo_unit == "µs"):
            periodo *= 10**(-6)
        elif (periodo_unit == "ms"):
            periodo *= 10 ** (-3)

        entrada_Plot = self.checkBox_Plot_input.isChecked()
        FAA_Plot = self.checkBox_Plot_FAA.isChecked()
        SyH_Plot = self.checkBox_Plot_SyH.isChecked()
        Llave_Plot = self.checkBox_Plot_Llave.isChecked()
        FR_Plot = self.checkBox_Plot_FR.isChecked()


        FAA_ON = self.checkBox_ON_FAA.isChecked()
        SyH_ON = self.checkBox_ON_SyH.isChecked()
        Llave_ON = self.checkBox_ON_Llave.isChecked()
        FR_ON = self.checkBox_ON_FR.isChecked()

        MT, MF_x, MF_y = RCV.Recieve(signal, Av, frec, theta, periodo, DC, FAA_ON, SyH_ON, Llave_ON, FR_ON)
        self.Plot(MT,MF_x,MF_y, entrada_Plot, FAA_Plot, SyH_Plot, Llave_Plot, FR_Plot)
        pass

    def Plot(self, MT, MF_x, MF_y, entrada_Plot, FAA_Plot, SyH_Plot, Llave_Plot, FR_Plot):
        #limpar graficos

        self.ax_tiempo.cla()

        self.figure_tiempo.subplots_adjust(bottom=0.2)
        self.ax_tiempo.grid(which="both")
        self.ax_tiempo.set_title("Osciloscopio", fontsize=10)
        self.ax_tiempo.set_ylabel("Amplitud [V]", fontsize=10)
        self.ax_tiempo.set_xlabel("Tiempo [s]", fontsize=10)

        self.ax_frec.cla()

        self.figure_frec.subplots_adjust(bottom=0.2)
        self.ax_frec.grid(which="both")
        self.ax_frec.set_xscale("log")
        self.ax_frec.set_title("Analizador de espectros", fontsize=10)
        self.ax_frec.set_ylabel("Amplitud [V]", fontsize=10)
        self.ax_frec.set_xlabel("Frecuencia [Hz]", fontsize=10)

        #OSCILOSCOPIO
        #verifico que graficar
        if (entrada_Plot):
            #grafico
            self.ax_tiempo.plot(MT[0],MT[1],label="Input")
            self.ax_frec.plot(MF_x[0], MF_y[0], label="Input")
        if (FAA_Plot):
            self.ax_tiempo.plot(MT[0], MT[2], label="Output FAA")
            self.ax_frec.plot(MF_x[1], MF_y[1], label="Output FAA")
        if (SyH_Plot):
            self.ax_tiempo.plot(MT[0], MT[3], label="Output SyH")
            self.ax_frec.plot(MF_x[2], MF_y[2], label="Output SyH")
        if (Llave_Plot):
            self.ax_tiempo.plot(MT[0], MT[4], label="Output Llave")
            self.ax_frec.plot(MF_x[3], MF_y[3], label="Output Llave")
        if (FR_Plot):
            self.ax_tiempo.plot(MT[0], MT[5], label="Output FR")
            self.ax_frec.plot(MF_x[4], MF_y[4], label="Output FR")

        self.ax_frec.legend(prop={"size":7})
        self.ax_tiempo.legend(prop={"size":7})
        self.canvas_tiempo.draw()
        self.canvas_frec.draw()
