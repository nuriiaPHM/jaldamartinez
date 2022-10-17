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

    def selMuni(self = None):
        try:
            id = 0
            var.ui.cmbMuniCli.clear()
            prov = var.ui.cmbProvCli.currentText()
            query = QtSql.QSqlQuery()
            query.prepare('select id from provincias where provincia = :prov')
            query.bindValue(':prov', prov)
            if query.exec():
                while query.next():
                    id = query.value(0)
            query1 = QtSql.QSqlQuery()
            query1.prepare('select municipio from municipios where provincia_id = :id')
            query1.bindValue(':id', int(id))
            if query1.exec():
                var.ui.cmbMuniCli.addItem('')
                while query1.next():
                    var.ui.cmbMuniCli.addItem(query1.value(0))
        except Exception as error:
            print("Error al cargar municipio: ", error)
