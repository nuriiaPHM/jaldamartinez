import clientes
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

    def mostraValidoDni(self=None):
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

    def selMotor(self=None):
        try:
            var.motor = (var.ui.rbtGasolina, var.ui.rbtDiesel, var.ui.rbtHibrido, var.ui.rbtElectrico)
            for i in var.motor:
                i.toggled.connect(Clientes.checkMotor)
        except Exception as error:
            print('Error seleccion motor: ', error)

    def checkMotor(self=None):
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

    def guardaCli(self=None):
        try:
            newcli = []
            newcar = []
            pagos = []

            cliente = [var.ui.txtDni, var.ui.txtNombre, var.ui.txtFechaAltaCli, var.ui.txtDircli]
            car = [var.ui.txtCar, var.ui.txtMarca, var.ui.txtModelo]

            for i in cliente:
                newcli.append(i.text())
            for i in car:
                newcar.append(i.text())

            prov = var.ui.cmbProvCli.currentText()
            muni = var.ui.cmbMuniCli.currentText()
            motor = Clientes.checkMotor()

            newcli.append(prov)
            newcli.append(muni)
            newcar.append(motor)

            if var.ui.chkTarjeta.isChecked():
                pagos.append('Tarjeta')

            if var.ui.chkEfectivo.isChecked():
                pagos.append('Efectivo')

            if var.ui.chkTransferencia.isChecked():
                pagos.append('Transeferencia')

            pagos = set(pagos)  # evita duplicados
            newcli.append('; '.join(pagos))

            conexion.Conexion.altaCli(newcli, newcar)
            print(newcli)
            print(newcar)

            var.ui.txtDni.setStyleSheet("background-color: rgb(255, 243, 181);")
            var.ui.lblValidarDni.setText('')


        except Exception as error:
            print('Error en guardaCli: ', error)

    def cargaFecha(qDate):
        try:
            data = ('{0}/{1}/{2}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.txtFechaAltaCli.setText(str(data))
            var.dlgcalendar.hide()
        except Exception as error:
            print('Error en cargar fecha: ', error)

    def limpiaCli(self=None):
        try:
            cliente = [var.ui.txtDni, var.ui.txtNombre, var.ui.txtFechaAltaCli, var.ui.txtDircli, var.ui.txtCar,
                       var.ui.txtMarca, var.ui.txtModelo]
            for i in cliente:
                i.setText('')

            var.ui.cmbProvCli.setCurrentText('')
            var.ui.cmbMuniCli.setCurrentText('')

            checks = [var.ui.chkTarjeta, var.ui.chkEfectivo, var.ui.chkTransferencia]
            for i in checks:
                i.setChecked(False)


            var.ui.txtDni.setStyleSheet("background-color: rgb(255, 243, 181);")
            var.ui.lblValidarDni.setText('')

        except Exception as error:
            print('Error limpiar cliente: ', error)

    def cargaCliente(self=None):
        try:
            Clientes.limpiaCli()
            fila = var.ui.tabClientes.selectedItems()
            datos = [var.ui.txtDni, var.ui.txtCar, var.ui.txtMarca, var.ui.txtModelo]
            row = [dato.text() for dato in fila]

            for i, dato in enumerate(datos):
                dato.setText(row[i])

            if row[4] == 'Gasolina':
                var.ui.rbtGasolina.setChecked(True)
            elif row[4] == 'Diesel':
                var.ui.rbtDiesel.setChecked(True)
            elif row[4] == 'Hibrido':
                var.ui.rbtHibrido.setChecked(True)
            elif row[4] == 'Electrico':
                var.ui.rbtElectrico.setChecked(True)

            registro = conexion.Conexion.oneCli(row[0])

            var.ui.txtNombre.setText(registro[0])
            var.ui.txtFechaAltaCli.setText(registro[1])
            var.ui.txtDircli.setText(registro[2])
            var.ui.cmbProvCli.setCurrentText(registro[3])
            var.ui.cmbMuniCli.setCurrentText(registro[4])

            if 'Efectivo' in registro[5]:
                var.ui.chkEfectivo.setChecked(True)
            if 'Tarjeta' in registro[5]:
                var.ui.chkTarjeta.setChecked(True)
            if 'Transferencia' in registro[5]:
                var.ui.chkTransferencia.setChecked(True)


        except Exception as error:
            print('Error al cargar cliente: ', error)

    def borraCli(self):
        try:
            dni = var.ui.txtDni.text()
            conexion.Conexion.borraCli(dni)
            conexion.Conexion.mostrarTab(self)

        except Exception as error:
            print('Error en borra clientes: ',error)

    def modifCli(self):
        try:
            modcli = []
            modcar = []

            cliente = [var.ui.txtDni, var.ui.txtNombre, var.ui.txtFechaAltaCli, var.ui.txtDircli]
            for i in cliente:
                modcli.append(i.text())

            prov = var.ui.cmbProvCli.currentText()
            modcli.append(prov)

            muni = var.ui.cmbMuniCli.currentText()
            modcli.append(muni)

            pagos = []
            if var.ui.chkEfectivo.isChecked():
                pagos.append('Efectivo')
            if var.ui.chkTarjeta.isChecked():
                pagos.append('Tarjeta')
            if var.ui.chkTransferencia.isChecked():
                pagos.append('Transferencia')
            pagos = set(pagos)
            modcli.append('; '.join(pagos))

            car = [var.ui.txtCar, var.ui.txtMarca, var.ui.txtModelo]
            for i in car:
                modcar.append(i.text())
            motor = Clientes.checkMotor()
            modcar.append(motor)

            conexion.Conexion.modificarDatos(modcli, modcar)

            conexion.Conexion.mostrarTab()

        except Exception as error:
            print('Error al modificar cliente: ', error)