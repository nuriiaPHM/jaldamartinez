import sys, var, shutil, os, xlwt, zipfile, xlrd
from datetime import datetime
from PyQt6 import QtSql

import clientes
import conexion
from dlgExportar import *
from dlgImportar import *
from ventMain import *


class Eventos:
    def Salir(self):
        try:
            var.avisosalir.show()
            if var.avisosalir.exec():
                sys.exit()
            else:
                var.avisosalir.hide()
        except Exception as error:
            print('Error en funcion salir %s', str(error))

    def abrirCalendar(self):
        try:
            var.dlgcalendar.show()
        except Exception as error:
            print('Error abrir calendario: ', error)

    def letrasCapital(self=None):
        try:
            var.ui.txtNombre.setText(var.ui.txtNombre.text().title())
            var.ui.txtDircli.setText(var.ui.txtDircli.text().title())
            var.ui.txtCar.setText(var.ui.txtCar.text().upper())
            var.ui.txtMarca.setText(var.ui.txtMarca.text().upper())
            var.ui.txtModelo.setText(var.ui.txtModelo.text().title())

        except Exception as error:
            print('Error en letras capital: ', error)

    def resizeTabCarCli(self):
        try:
            header = var.ui.tabClientes.horizontalHeader()
            for i in range(6):
                header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)
                if i == 0 or i == 1:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)

        except Exception as error:
            print('Error en resize')

    def creaBackup(self):
        try:
            # var.dlgabrir.show()

            fecha = datetime.today()
            fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')
            copia = (str(fecha) + '_backup.zip')

            directorio, filename = var.dlgabrir.getSaveFileName(None, 'Guardar copia', copia, '.zip')

            if var.dlgabrir.accept and filename != '':
                fichzip = zipfile.ZipFile(copia, 'w')
                fichzip.write(var.bbdd, os.path.basename(var.bbdd), zipfile.ZIP_DEFLATED)
                fichzip.close()
                shutil.move(str(copia), str(directorio))

                msg = QtWidgets.QMessageBox()
                msg.setModal(True)
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText('Copia de seguridad creada')
                msg.exec()

        except Exception as error:
            print('Error en crear backup: ', error)

    def restauraBackup(self):
        try:
            filename = var.dlgabrir.getOpenFileName(None, 'Restaurar Copia Seguridad', '', '*.zip;;All Files (*)')

            if var.dlgabrir.accept and filename != '':
                file = filename[0]
                with zipfile.ZipFile(str(file), 'r') as bbdd:
                    bbdd.extractall(pwd=None)
                bbdd.close()

            conexion.Conexion.conexion()
            conexion.Conexion.mostrarTab()

            msg = QtWidgets.QMessageBox()
            msg.setModal(True)
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setText('Copia de seguridad restaurada')
            msg.exec()

        except Exception as error:
            print('Error en restaurar backup: ', error)

    def abrirImportar(self=None):
        try:
            var.dlgimportar.show()
            if var.dlgimportar.exec():
                pass

        except Exception as error:
            print('Error en abrir exportar: ', error)

    def importarDatos(self):
        try:
            filename = var.dlgabrir.getOpenFileName(None, 'Importar datos', '', '*.xls;;All Files (*)')

            if var.dlgabrir.accept and filename != '':
                file = filename[0]
                documento = xlrd.open_workbook(file)
                datos = documento.sheet_by_index(0)

                filas = datos.nrows
                columnas = datos.ncols

                new = []
                for i in range(filas):
                    if i == 0:
                        pass
                    else:
                        new = []
                        for j in range(columnas):
                            new.append(str(datos.cell_value(i, j)))
                        if clientes.Clientes.validarDni(str(new[0])):
                            if var.stateCliImportar == 2:
                                conexion.Conexion.altaExcelCli(new)

                        if clientes.Clientes.validarDni(str(new[1])):
                            if var.stateCarImportar == 2:
                                conexion.Conexion.altaExcelCoche(new)

                conexion.Conexion.mostrarTab()

                msg = QtWidgets.QMessageBox()
                msg.setModal(True)
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText('Importacion de datos realizada')
                msg.exec()

        except Exception as error:
            print('Error en importar datos: ', error)

    def abrirExportar(self=None):
        try:
            var.dlgexportar.show()
            if var.dlgexportar.exec():
                pass

        except Exception as error:
            print('Error en abrir exportar: ', error)

    def exportarDatos(self):
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')

            file = str(fecha)

            if var.stateCliExportar == 2 & var.stateCarExportar == 2:
                file += '_Clientes_Coches.xls'
                directorio, filename = var.dlgabrir.getSaveFileName(None, 'Guardar datos de clientes', file, '.xls')
                wb = xlwt.Workbook()
                Eventos.exportarClientesCoches(wb, directorio)
            elif var.stateCliExportar == 2:
                file += '_Clientes.xls'
                directorio, filename = var.dlgabrir.getSaveFileName(None, 'Guardar datos de clientes', file, '.xls')
                wb = xlwt.Workbook()
                Eventos.exportarClientes(wb, directorio)
            elif var.stateCarExportar == 2:
                file += '_Coches.xls'
                directorio, filename = var.dlgabrir.getSaveFileName(None, 'Guardar datos de clientes', file, '.xls')
                wb = xlwt.Workbook()
                Eventos.exportarCoches(wb, directorio)

        except Exception as error:
            print('Error al exportar datos: ', error)

    def exportarClientes(wb, directorio):
        try:

            sheet1 = wb.add_sheet('Clientes')
            sheet1.write(0, 0, 'DNI')
            sheet1.write(0, 1, 'Nombre')
            sheet1.write(0, 2, 'Fecha Alta')
            sheet1.write(0, 3, 'Direccion')
            sheet1.write(0, 4, 'Provincia')
            sheet1.write(0, 5, 'Municipio')
            sheet1.write(0, 6, 'Forma de pago')

            queryCli = QtSql.QSqlQuery()
            queryCli.prepare('select * from clientes order by dni')

            if (queryCli.exec()):
                fila = 1
                while queryCli.next():
                    sheet1.write(fila, 0, str(queryCli.value(0)))
                    sheet1.write(fila, 1, str(queryCli.value(1)))
                    sheet1.write(fila, 2, str(queryCli.value(2)))
                    sheet1.write(fila, 3, str(queryCli.value(3)))
                    sheet1.write(fila, 4, str(queryCli.value(4)))
                    sheet1.write(fila, 5, str(queryCli.value(5)))
                    sheet1.write(fila, 6, str(queryCli.value(6)))

                    fila += 1

            wb.save(directorio)

            msg = QtWidgets.QMessageBox()
            msg.setModal(True)
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setText('Datos de clientes exportados correctamente')
            msg.exec()

        except Exception as error:
            print('Error al exportar datos de clientes: ', error)


    def exportarCoches(wb, directorio):
        try:

            sheet1 = wb.add_sheet('Coches')
            sheet1.write(0, 0, 'Matricula')
            sheet1.write(0, 1, 'Marca')
            sheet1.write(0, 2, 'Modelo')
            sheet1.write(0, 3, 'Motor')

            queryCo = QtSql.QSqlQuery()
            queryCo.prepare('select * from coches order by matricula')


            if (queryCo.exec()):
                fila = 1
                while queryCo.next():
                    sheet1.write(fila, 0, str(queryCo.value(0)))
                    sheet1.write(fila, 1, str(queryCo.value(2)))
                    sheet1.write(fila, 2, str(queryCo.value(3)))
                    sheet1.write(fila, 3, str(queryCo.value(4)))

                    fila += 1

            wb.save(directorio)

            msg = QtWidgets.QMessageBox()
            msg.setModal(True)
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setText('Datos de coches exportados correctamente')
            msg.exec()

        except Exception as error:
            print('Error al exportar datos de coches: ', error)

    def exportarClientesCoches(wb, directorio):
        try:
            sheet1 = wb.add_sheet('Clientes')
            sheet1.write(0, 0, 'DNI')
            sheet1.write(0, 1, 'Nombre')
            sheet1.write(0, 2, 'Fecha Alta')
            sheet1.write(0, 3, 'Direccion')
            sheet1.write(0, 4, 'Provincia')
            sheet1.write(0, 5, 'Municipio')
            sheet1.write(0, 6, 'Forma de pago')

            queryCli = QtSql.QSqlQuery()
            queryCli.prepare('select * from clientes order by dni')

            if (queryCli.exec()):
                fila = 1
                while queryCli.next():
                    sheet1.write(fila, 0, str(queryCli.value(0)))
                    sheet1.write(fila, 1, str(queryCli.value(1)))
                    sheet1.write(fila, 2, str(queryCli.value(2)))
                    sheet1.write(fila, 3, str(queryCli.value(3)))
                    sheet1.write(fila, 4, str(queryCli.value(4)))
                    sheet1.write(fila, 5, str(queryCli.value(5)))
                    sheet1.write(fila, 6, str(queryCli.value(6)))

                    fila += 1

            sheet2 = wb.add_sheet('Coches')
            sheet2.write(0, 0, 'Matricula')
            sheet2.write(0, 1, 'Marca')
            sheet2.write(0, 2, 'Modelo')
            sheet2.write(0, 3, 'Motor')

            queryCo = QtSql.QSqlQuery()
            queryCo.prepare('select * from coches order by matricula')

            if (queryCo.exec()):
                fila = 1
                while queryCo.next():
                    sheet2.write(fila, 0, str(queryCo.value(0)))
                    sheet2.write(fila, 1, str(queryCo.value(2)))
                    sheet2.write(fila, 2, str(queryCo.value(3)))
                    sheet2.write(fila, 3, str(queryCo.value(4)))

                    fila += 1

            wb.save(directorio)

            msg = QtWidgets.QMessageBox()
            msg.setModal(True)
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setText('Datos de clientes exportados correctamente')
            msg.exec()

        except Exception as error:
            print('error al exportar datos de coches y clientes: ', error)