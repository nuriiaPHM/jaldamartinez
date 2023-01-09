from ventMain import *
import conexion, var

class Servicios:

    def guardarServicio(self=None):
        try:
            newServicio = []

            servicio = [var.ui.txtConcepto, var.ui.txtPrecio]

            for i in servicio:
                newServicio.append(i.text())

            conexion.Conexion.altaServicio(newServicio)
            print(newServicio)

            var.ui.txtCodigo.setText('')
            var.ui.txtConcepto.setText('')
            var.ui.txtPrecio.setText('')

        except Exception as error:
            print('Error en Servicios.guardarServicio: ', error)

    def cargaServicio(self=None):
        try:
            '''Servicios.limpiaCli()'''
            fila = var.ui.tabServicios.selectedItems()
            datos = [var.ui.txtCodigo, var.ui.txtConcepto, var.ui.txtPrecio]
            row = [dato.text() for dato in fila]

            for i, dato in enumerate(datos):
                dato.setText(row[i])

            registro = conexion.Conexion.selectServicio(row[0])

            var.ui.txtCodigo.setText(row[0])
            var.ui.txtConcepto.setText(registro[0])
            var.ui.txtPrecio.setText(registro[1])

        except Exception as error:
            print('Error en Servicios.cargarServicio: ', error)


    def borrarServicio(self=None):
        try:
            codigo = var.ui.txtCodigo.text()
            conexion.Conexion.borrarServicio(codigo)
            conexion.Conexion.mostrarTabServicios()

            var.ui.txtCodigo.setText('')
            var.ui.txtConcepto.setText('')
            var.ui.txtPrecio.setText('')

        except Exception as error:
            print('Error en Servicios.borrarServicio: ',error)

    def modificarServicio(self=None):
        try:
            modServicio = []

            servicio = [var.ui.txtCodigo, var.ui.txtConcepto, var.ui.txtPrecio]
            for i in servicio:
                modServicio.append(i.text())

            conexion.Conexion.modificarServicio(modServicio)
            conexion.Conexion.mostrarTabServicios()

        except Exception as error:
            print('Error en Servicios.modificarServicio: ', error)

    def buscarServicio(self=None):
        try:
            nombre = var.ui.txtBuscarServicio.text()

            registro = conexion.Conexion.buscarServicio(nombre)
            print(registro)

            var.ui.txtCodigo.setText(str(registro[0]))
            var.ui.txtConcepto.setText(registro[1])
            var.ui.txtPrecio.setText(registro[2])

        except Exception as error:
            print('Error en Servicios.buscarServicio: ', error)