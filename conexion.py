from datetime import datetime

from PyQt6 import QtWidgets, QtSql

import clientes
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

    def altaExcelCoche(new):
        try:
            query1 = QtSql.QSqlQuery()
            query1.prepare('insert into coches(matricula, dnicli, marca, modelo, motor) '
                           'values (:matricula, :dnicli, :marca, :modelo, :motor)')

            query1.bindValue(':matricula', str(new[0]))
            query1.bindValue(':dnicli', str(new[1]))
            query1.bindValue(':marca', str(new[2]))
            query1.bindValue(':modelo', str(new[3]))
            query1.bindValue(':motor', str(new[4]))

            if query1.exec():
                pass

            conexion.Conexion.mostrarTabCarCli(None)

        except Exception as error:
            print('Error en alta excel coche: ', error)

    def altaExcelCli(new):
        try:
            query1 = QtSql.QSqlQuery()
            query1.prepare('insert into clientes(dni, nombre, alta, direccion, provincia, municipio, pago) '
                           'values (:dni, :nombre, :alta, :direccion, :provincia, :municipio, :pago)')

            query1.bindValue(':dni', str(new[0]))
            query1.bindValue(':nombre', str(new[1]))
            query1.bindValue(':alta', str(new[2]))
            query1.bindValue(':direccion', str(new[3]))
            query1.bindValue(':provincia', str(new[4]))
            query1.bindValue(':municipio', str(new[5]))
            query1.bindValue(':pago', str(new[6]))

            if query1.exec():
                pass

            conexion.Conexion.mostrarTabCarCli(None)

        except Exception as error:
            print('Error en alta excel clientes: ', error)

    def mostrarTabCarCli(self=None):
        try:
            index = 0
            query = QtSql.QSqlQuery()
            query.prepare('select matricula, dnicli, marca, modelo, motor from coches where fechabajacar is null order by marca, modelo')
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

                    var.ui.tabClientes.setStyleSheet("QTableView::item:alternate { background-color: #b5b5b5; } QTableView::item { background-color: #f3eeed; }")

                    index += 1

        except Exception as error:
            print('Error al mostrar tabla coches clientes: ', error)

    def oneCli(dni):
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare('select nombre, alta, direccion, provincia, municipio, pago from clientes where dni = :dni')

            query.bindValue(':dni', str(dni))
            if query.exec():
                while query.next():
                    for i in range(6):
                        registro.append(query.value(i))
            return registro

        except Exception as error:
            print('Error en oneCli: ', error)

    def borraCli(dni):
        try:

            fecha = datetime.today()
            fecha = fecha.strftime('%d.%m.%Y.%H.%M.%S')

            query1 = QtSql.QSqlQuery()
            query1.prepare('update clientes set fechabajacli = :fecha where dni = :dni')
            query1.bindValue(':fecha', str(fecha))
            query1.bindValue(':dni', str(dni))

            if query1.exec():
                pass

            query = QtSql.QSqlQuery()
            query.prepare('update coches set fechabajacar = :fecha where dnicli = :dni')
            query.bindValue(':fecha', str(fecha))
            query.bindValue(':dni', str(dni))


            if query.exec():
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText('Cliente dado de baja')
                msg.exec()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                msg.setText(query.lastError().text())
                msg.exec()

            '''
            query1 = QtSql.QSqlQuery()
            query1.prepare('delete from coches where dnicli = :dni')
            query1.bindValue(':dni', str(dni))

            if query1.exec():
                pass

            query = QtSql.QSqlQuery()
            query.prepare('delete from clientes where dni = :dni')
            query.bindValue(':dni',str(dni))

            if query.exec():
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText('Cliente dado de baja')
                msg.exec()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                msg.setText(query.lastError().text())
                msg.exec()
            '''
        except Exception as error:
            print('Error en conexion borrar clientes: ', error)

    def modificaCli(modcli, modcar):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('update clientes set nombre = :nombre, alta = :alta, direccion = :direccion, provincia = :provincia, municipio = :municipio, pago = :pago where dni = :dni')

            query.bindValue(':dni', str(modcli[0]))
            query.bindValue(':nombre', str(modcli[1]))
            query.bindValue(':alta', str(modcli[2]))
            query.bindValue(':direccion', str(modcli[3]))
            query.bindValue(':provincia', str(modcli[4]))
            query.bindValue(':municipio', str(modcli[5]))
            query.bindValue(':pago', str(modcli[6]))

            if query.exec():
                pass

            query1 = QtSql.QSqlQuery()
            query1.prepare('update coches set dnicli = :dnicli, marca = :marca, modelo = :modelo, motor = :motor where matricula = :matricula')

            query1.bindValue(':matricula', str(modcar[0]))
            query1.bindValue(':dnicli', str(modcli[0]))
            query1.bindValue(':marca', str(modcar[1]))
            query1.bindValue(':modelo', str(modcar[2]))
            query1.bindValue(':motor', str(modcar[3]))

            if query1.exec():
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText('Datos modificados correctamente')
                msg.exec()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                msg.setText(query.lastError().text())
                msg.exec()


        except Exception as error:
            print('Error en modificar clientes en conexion: ', error)