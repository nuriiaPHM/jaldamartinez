from ventMain import *
from dlgSalir import *
from dlgCalendar import *
from datetime import *
import sys, var, events, clientes, conexion

class FileDialogAbrir(QtWidgets.QFileDialog):
    def __init__(self):
        super(FileDialogAbrir, self).__init__()

class DialogCalendar(QtWidgets.QDialog):
    def __init__(self):
        super(DialogCalendar, self).__init__()
        var.dlgcalendar = Ui_dlgCalendar()
        var.dlgcalendar.setupUi(self)
        dia = datetime.now().day
        mes = datetime.now().month
        ano = datetime.now().year
        var.dlgcalendar.Calendar.setSelectedDate(QtCore.QDate(ano,mes,dia))
        var.dlgcalendar.Calendar.clicked.connect(clientes.Clientes.cargaFecha)

class DialogSalir(QtWidgets.QDialog):
    def __init__(self):
        super(DialogSalir, self).__init__()
        var.avisosalir = Ui_dlgSalir()
        var.avisosalir.setupUi(self)

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_ventMain()
        var.ui.setupUi(self)
        var.avisosalir = DialogSalir()
        var.dlgcalendar = DialogCalendar()
        var.dlgabrir = FileDialogAbrir()

        ''' Listado de eventos de menu '''
        var.ui.actionSalir.triggered.connect(events.Eventos.Salir)
        var.ui.actionSalirBar.triggered.connect(events.Eventos.Salir)
        var.ui.actionCrear_copia_de_seguridad.triggered.connect(events.Eventos.creaBackUp)

        ''' Listado de eventos de cajas '''
        var.ui.txtDni.editingFinished.connect(clientes.Clientes.mostraValidoDni)
        var.ui.txtNombre.editingFinished.connect(events.Eventos.letrasCapital)
        var.ui.txtDircli.editingFinished.connect(events.Eventos.letrasCapital)
        var.ui.txtCar.editingFinished.connect(events.Eventos.letrasCapital)
        var.ui.txtModelo.editingFinished.connect(events.Eventos.letrasCapital)
        var.ui.txtMarca.editingFinished.connect(events.Eventos.letrasCapital)

        ''' Listado de eventos de botones '''
        var.ui.btnGuardaCli.clicked.connect(clientes.Clientes.guardaCli)
        var.ui.btnFechaAltaCli.clicked.connect(events.Eventos.abrirCalendar)
        var.ui.btnLimpiarCli.clicked.connect(clientes.Clientes.limpiaCli)
        '''Llamadas de funciones'''
        conexion.Conexion.conexion()
        '''Llamadas a eventos de combo box'''
        conexion.Conexion.cargarProv()
        var.ui.cmbProvCli.currentIndexChanged.connect(conexion.Conexion.selMuni)


        conexion.Conexion.mostrarTabCarCli(self)
        events.Eventos.resizeTabCarCli(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())
