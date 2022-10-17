import conexion
from ventMain import *
import var

class Clientes():
    def validarDni(dni):
        '''
        Modulo para la validacion del DNI
        :return: booleano
        '''

        try:
            tabla = 'TRWAGMYFPDXBNJZSQVHLCKE'
            dig_ext = 'XYZ'
            reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
            numeros = '1234567890'
            dni = dni.upper()
            if len(dni) == 9:
                dig_control = dni[8]
                dni = dni[:8]
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                return len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control
            return False

        except Exception as error:
            print('Error al validar DNI', error)

    def mostraValidoDni(self = None):
        try:
            dni = var.ui.txtDni.text()
            if Clientes.validarDni(dni):
                var.ui.lblValidarDni.setStyleSheet('color: green')
                var.ui.lblValidarDni.setText('V')
                var.ui.txtDni.setText(dni.upper())
                var.ui.txtDni.setStyleSheet('background-color: white;')
            else:
                var.ui.lblValidarDni.setStyleSheet('color: red')
                var.ui.lblValidarDni.setText('X')
                var.ui.txtDni.setText(dni.upper())
                var.ui.txtDni.setStyleSheet('background-color: pink;')
        except Exception as error:
            print('Error mostrar marcado validez DNI: ', error)

    def selMotor(self = None):
        try:
            var.motor = (var.ui.rbtGasolina, var.ui.rbtDiesel, var.ui.rbtHibrido, var.ui.rbtElectrico)
            for i in var.motor:
                i.toggled.connect(Clientes.checkMotor)
        except Exception as error:
            print('Error seleccion motor: ', error)

    def checkMotor(self = None):
        try:
            if var.ui.rbtGasolina.isChecked():
                motor = 'Gasolina'
            elif var.ui.rbtDiesel.isChecked():
                motor = 'Diesel'
            elif var.ui.rbtHibrido.isChecked():
                motor = 'Hibrido'
            elif var.ui.rbtElectrico.isChecked():
                motor = 'Electrico'
            else:
                pass
            return motor
        except Exception as error:
            print('Error check motor: ', error)

    def guardaCli(self = None):
        try:
            newcli = []
            cliente = [var.ui.txtDni, var.ui.txtNombre, var.ui.txtFechaAltaCli, var.ui.txtDircli]
            for i in cliente:
                newcli.append(i.text())
            prov = var.ui.cmbProvCli.currentText()
            newcli.append(prov)
            muni = var.ui.cmbMuniCli.currentText()
            newcli.append(muni)

            print(newcli)







            '''
            motor = Clientes.checkMotor()
            newcli.append(motor)
            row = 0
            column = 0
            var.ui.tabClientes.insertRow(row)
            for registro in newcli:
                cell = QtWidgets.QTableWidgetItem(registro)
                var.ui.tabClientes.setItem(row, column, cell)
                column += 1'''

        except Exception as error:
            print('Error en guardaCli: ', error)

    def cargaFecha(qDate):
        try:
            data = ('{0}/{1}/{2}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.txtFechaAltaCli.setText(str(data))
            var.dlgcalendar.hide()
        except Exception as error:
            print('Error en cargar fecha: ', error)

    def limpiaCli(self = None):
        try:
            cliente = [var.ui.txtDni, var.ui.txtNombre, var.ui.txtFechaAltaCli, var.ui.txtDircli, var.ui.txtCar, var.ui.txtMarca, var.ui.txtModelo]
            for i in cliente:
                i.setText('')

            for i in var.ui.btnGroupPago.buttons():
                i.setChecked(False)

            conexion.Conexion.cargarProv()

        except Exception as error:
            print('Error limpiar cliente: ', error)

