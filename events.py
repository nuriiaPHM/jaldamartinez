import sys, var, shutil, os, xlwt, zipfile
from datetime import date, datetime
from PyQt6 import QtSql
import conexion
from ventMain import *
from dlgExportar import *


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

    def abrirExportar(self):
        try:
            var.dlgexportar.show()
        except Exception as error:
            print('Error abrir exportar: ', error)

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
            for i in range(5):
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
            conexion.Conexion.mostrarTabCarCli()

            msg = QtWidgets.QMessageBox()
            msg.setModal(True)
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setText('Copia de seguridad restaurada')
            msg.exec()

        except Exception as error:
            print('Error en restaurar backup: ', error)

    def exportarDatos(self):
        try:
            clientes = False
            coches = False

            var.dlgexportar.show()

            if var.dlgexportar.exec():
                if var.ui.cbClientes.isChecked():
                    clientes = True
                if var.ui.cbCoches.isChecked():
                    coches = True
            else:
                var.dlgexportar.hide()




            fecha = datetime.today()
            fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')

            file = str(fecha)
            if(clientes):
                file += '_Clientes'
            if(coches):
                file += '_Coches'
            file += '.xls'

            directorio, filename = var.dlgabrir.getSaveFileName(None, 'Guardar Datos', file, '.xls')

            wb = xlwt.Workbook()

            if (clientes & coches):
                sheet1 = wb.add_sheet('Clientes_Coches')
                sheet1.write(0, 0, 'DNI')
                sheet1.write(0, 1, 'Nombre')
                sheet1.write(0, 2, 'Fecha Alta')
                sheet1.write(0, 3, 'Direccion')
                sheet1.write(0, 4, 'Provincia')
                sheet1.write(0, 5, 'Municipio')
                sheet1.write(0, 6, 'Forma de pago')
                sheet1.write(0, 7, 'Matricula')
                sheet1.write(0, 8, 'Marca')
                sheet1.write(0, 9, 'Modelo')
                sheet1.write(0, 10, 'Motor')

            elif (clientes):
                sheet1 = wb.add_sheet('Clientes')
                sheet1.write(0, 0, 'DNI')
                sheet1.write(0, 1, 'Nombre')
                sheet1.write(0, 2, 'Fecha Alta')
                sheet1.write(0, 3, 'Direccion')
                sheet1.write(0, 4, 'Provincia')
                sheet1.write(0, 5, 'Municipio')
                sheet1.write(0, 6, 'Forma de pago')

            elif (coches):
                sheet1 = wb.add_sheet('Coches')
                sheet1.write(0, 0, 'Matricula')
                sheet1.write(0, 1, 'Marca')
                sheet1.write(0, 2, 'Modelo')
                sheet1.write(0, 3, 'Motor')



            queryCli = QtSql.QSqlQuery()
            queryCli.prepare('select * from clientes order by dni')

            queryCo = QtSql.QSqlQuery()
            queryCo.prepare('select * from coches order by matricula')

            if (clientes & coches):
                if (clientes & queryCli.exec()):
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

                if (coches & queryCo.exec()):
                    fila = 1
                    while queryCli.next():
                        sheet1.write(fila, 7, str(queryCli.value(7)))
                        sheet1.write(fila, 8, str(queryCli.value(8)))
                        sheet1.write(fila, 9, str(queryCli.value(9)))
                        sheet1.write(fila, 10, str(queryCli.value(10)))

                        fila += 1
            elif (clientes):
                if (clientes & queryCli.exec()):
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
            elif (coches):
                if (coches & queryCo.exec()):
                    fila = 1
                    while queryCli.next():
                        sheet1.write(fila, 0, str(queryCli.value(0)))
                        sheet1.write(fila, 1, str(queryCli.value(1)))
                        sheet1.write(fila, 2, str(queryCli.value(2)))
                        sheet1.write(fila, 3, str(queryCli.value(3)))

                        fila += 1

            wb.save(directorio)

            msg = QtWidgets.QMessageBox()
            msg.setModal(True)
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setText('Datos exportados correctamente')
            msg.exec()

        except Exception as error:
            print('Error al exportar datos: ', error)
