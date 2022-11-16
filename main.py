from ventMain import *
from dlgSalir import *
from dlgCalendar import *
from dlgExportar import *
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
'''
class DialogExportar(QtWidgets.QDialog):
    def __init__(self):
        super(DialogExportar, self).__init__()
        var.dlgexportar = Ui_dlgExportar()
        var.dlgexportar.setupUi(self)
'''
class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_ventMain()
        var.ui.setupUi(self)
        var.avisosalir = DialogSalir()
        var.dlgcalendar = DialogCalendar()
        var.dlgabrir = FileDialogAbrir()
        #var.dlgexportar = DialogExportar()

        ''' Listado de eventos de menu '''
        var.ui.actionSalir.triggered.connect(events.Eventos.Salir)
        var.ui.actionSalirBar.triggered.connect(events.Eventos.Salir)
        var.ui.actionCrear_copia_de_seguridad.triggered.connect(events.Eventos.creaBackup)
        var.ui.actionRestaurar_copia_de_seguridad.triggered.connect(events.Eventos.restauraBackup)
        var.ui.actionCrear_copia_de_seguridadBar.triggered.connect(events.Eventos.creaBackup)
        var.ui.actionRestaurar_copia_de_seguridadBar.triggered.connect(events.Eventos.restauraBackup)
        #var.ui.actionExportar_datos.triggered.connect(events.Eventos.exportarDatos)

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

        '''Llamadas de funciones de conexion'''
        conexion.Conexion.conexion()
        conexion.Conexion.mostrarTabCarCli(self)
        conexion.Conexion.cargarProv()

        '''Llamadas de funciones de tablas'''
        events.Eventos.resizeTabCarCli(self)
        var.ui.tabClientes.clicked.connect(clientes.Clientes.cargaCliente)

        '''Llamadas a eventos de combo box'''
        var.ui.cmbProvCli.currentIndexChanged.connect(conexion.Conexion.selMuni)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())
