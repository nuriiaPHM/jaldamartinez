from PyQt6 import QtWidgets, QtSql

import conexion
from ventMain import *
import var

class Conexion():
    def conexion(self = None):
        filedb = 'bbdd.sqlite'
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(filedb)
        var.bbdd = 'bbdd.sqlite'
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

    def altaCli(newcli, newcar):
        try:
            query = QtSql.QSqlQuery()
            queryCli = QtSql.QSqlQuery()

            query.prepare('insert into clientes (dni, nombre, alta, direccion, provincia, municipio, pago) '
                          'values (:dni, :nombre, :alta, :direccion, :provincia, :municipio, :pago)')
            queryCli.prepare('select dni from clientes where dni = :dni')

            queryCli.bindValue(':dni', str(newcli[0]))
            query.bindValue(':dni', str(newcli[0]))
            query.bindValue(':nombre', str(newcli[1]))
            query.bindValue(':alta', str(newcli[2]))
            query.bindValue(':direccion', str(newcli[3]))
            query.bindValue(':provincia', str(newcli[4]))
            query.bindValue(':municipio', str(newcli[5]))
            query.bindValue(':pago', str(newcli[6]))

            if query.exec():
                pass
            
            query1 = QtSql.QSqlQuery()
            query1.prepare('insert into coches(matricula, dnicli, marca, modelo, motor) '
                           'values (:matricula, :dnicli, :marca, :modelo, :motor)')

            query1.bindValue(':matricula', str(newcar[0]))
            query1.bindValue(':dnicli', str(newcli[0]))
            query1.bindValue(':marca', str(newcar[1]))
            query1.bindValue(':modelo', str(newcar[2]))
            query1.bindValue(':motor', str(newcar[3]))

            if query1.exec():
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText('Coche dado de alta')
                msg.exec()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                msg.setText(query1.lastError().text())
                msg.exec()

            conexion.Conexion.mostrarTabCarCli(None)

        except Exception as error:
            print('Error en alta cliente: ', error)

    def mostrarTabCarCli(self=None):
        try:
            index = 0
            query = QtSql.QSqlQuery()
            query.prepare('select matricula, dnicli, marca, modelo, motor from coches order by marca, modelo')
            if query.exec():
                while query.next():
                    var.ui.tabClientes.setRowCount(index+1)

                    var.ui.tabClientes.setItem(index, 0, QtWidgets.QTableWidgetItem(str(query.value(1))))
                    var.ui.tabClientes.setItem(index, 1, QtWidgets.QTableWidgetItem(str(query.value(0))))
                    var.ui.tabClientes.setItem(index, 2, QtWidgets.QTableWidgetItem(str(query.value(2))))
                    var.ui.tabClientes.setItem(index, 3, QtWidgets.QTableWidgetItem(str(query.value(3))))
                    var.ui.tabClientes.setItem(index, 4, QtWidgets.QTableWidgetItem(str(query.value(4))))

                    var.ui.tabClientes.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tabClientes.item(index, 2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tabClientes.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tabClientes.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

                    var.ui.tabClientes.setStyleSheet("QTableView::item:alternate { background-color: #f3eeed; } QTableView::item { background-color: #d1c8c6; }")

                    index += 1

        except Exception as error:
            print('Error al mostrar tabla coches clientes: ', error)