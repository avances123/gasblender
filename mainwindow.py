# This Python file uses the following encoding: utf-8
from pathlib import Path
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import QFile, QCoreApplication, Qt
from PySide6.QtUiTools import QUiLoader

from algoritmos import aire,pp,calculo_costes

ALGORITMOS = {
    'Aire': aire,
    'Presiones Parciales' : pp,
}

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.load_ui()

    def load_ui(self):
        loader = QUiLoader()
        path = Path(__file__).resolve().parent / "form.ui"
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        self.window = loader.load(ui_file)
        self.window.setWindowTitle("Calculadora para blenders caseros")
        ui_file.close()

    def show(self):
        self.window.show()



    def inicializar_ui(self):
        # datos iniciales
        self.window.comboBox.addItems(ALGORITMOS.keys())

        # Status bar
        #self.window.statusbar.showMessage("Creado por Fabio Rueda")
        label_status = QLabel()
        label_status.setOpenExternalLinks(True)
        #< font      face = verdana      size = 12        color = black >
        label_status.setText("<a href='https://diving.fabio.xyz'>< font face = verdana size = 2 color = black >Creado por Avances123</a>")
        self.window.statusbar.addPermanentWidget(label_status)

        # señales
        self.window.doubleSpinBoxvol.valueChanged.connect(self.calcular_plan)
        self.window.comboBox.currentIndexChanged.connect(self.calcular_plan)

        self.window.spinBox_2.valueChanged.connect(self.calcular_plan)
        self.window.spinBox_5.valueChanged.connect(self.calcular_plan)
        self.window.spinBox_3.valueChanged.connect(self.calcular_plan)
        self.window.spinBox_6.valueChanged.connect(self.calcular_plan)
        self.window.spinBox_4.valueChanged.connect(self.calcular_plan)
        self.window.spinBox_7.valueChanged.connect(self.calcular_plan)

        self.window.doubleSpinBox.valueChanged.connect(self.calcular_plan)
        self.window.doubleSpinBox_2.valueChanged.connect(self.calcular_plan)
        self.window.doubleSpinBox_3.valueChanged.connect(self.calcular_plan)

        # Señales al cambiar metodo (en aire quito el o2 y el he finales)
        self.window.comboBox.currentTextChanged.connect(self.cambio_metodo)
        self.cambio_metodo(next(iter(ALGORITMOS)))

    def cambio_metodo(self,metodo):
        if metodo == 'Aire':
            self.window.spinBox_6.setDisabled(True)
            self.window.spinBox_7.setDisabled(True)
        else:
            self.window.spinBox_6.setDisabled(False)


    def calcular_plan(self):
        volumen_botella = self.window.doubleSpinBoxvol.value()
        nombre_algoritmo = self.window.comboBox.currentText()

        bares_iniciales = self.window.spinBox_2.value()
        bares_finales = self.window.spinBox_5.value()
        porcentaje_inicial_o2 = self.window.spinBox_3.value()
        porcentaje_final_o2 = self.window.spinBox_6.value()
        porcentaje_inicial_he = self.window.spinBox_4.value()
        porcentaje_final_he = self.window.spinBox_7.value()

        precio_O2 = self.window.doubleSpinBox.value()
        precio_He = self.window.doubleSpinBox_2.value()
        precio_aire = self.window.doubleSpinBox_3.value()

        algoritmo = ALGORITMOS[nombre_algoritmo]
        resultado = algoritmo(bares_iniciales=bares_iniciales, bares_finales=bares_finales, porcentaje_inicial_o2=porcentaje_inicial_o2,
                              porcentaje_final_o2=porcentaje_final_o2, porcentaje_inicial_he=porcentaje_inicial_he, porcentaje_final_he=porcentaje_final_he)
        costes = calculo_costes(volumen_botella,resultado['bares_aire'],resultado['bares_o2'], resultado['bares_he'], precio_aire=precio_aire)


        # Pinto Resultado
        self.window.label_11.setText(f"{resultado['porcentaje_o2']:.1f}/{resultado['porcentaje_he']:.1f}")
        self.window.lcdNumber_3.display(resultado['bares_aire'])
        if nombre_algoritmo == 'Aire':
            self.window.spinBox_6.setValue(resultado['porcentaje_o2'])
            self.window.spinBox_7.setValue(resultado['porcentaje_he'])


        # Pinto Costes
        self.window.label_10.setText(costes['aire'])
        self.window.label_5.setText(costes['o2'])
        self.window.label_9.setText(costes['he'])
        self.window.label_12.setText(costes['total'])




if __name__ == "__main__":
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.inicializar_ui()
    widget.calcular_plan()
    widget.show()
    sys.exit(app.exec())
