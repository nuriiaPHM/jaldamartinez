from PyQt6 import QtWidgets, QtSql
from ventMain import *
import var

class Conexion():
    def conexion(self = None):
        filedb = 'bbdd.sqlite'
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(filedb)
        if not db.open():
            QtWidgets.QMessageBox.critical(None, 'No se puede abrir la base de datos', 'Conexion no establecida.\n' 'Haga click para cerrar', QtWidgets.QMessageBox.StandardButton.Cancel)
            return False
        else:
            print('Conexion establecida')
        return True

    def cargarProv(self = None):
        try:
            var.ui.cmbProvCli.clear()
            query = QtSql.QSqlQuery()
            query.prepare('select provincia from provincias')
            if query.exec():
                var.ui.cmbProvCli.addItem('')
                while query.next():
                    var.ui.cmbProvCli.addItem(query.value(0))

        except Exception as error:
            print('Error al cargar provincia: ', error)
