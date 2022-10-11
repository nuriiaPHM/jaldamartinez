import sys, var

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

    def letrasCapital(self = None):
        try:
            var.ui.txtNombre.setText(var.ui.txtNombre.text().title())
            var.ui.txtDircli.setText(var.ui.txtDircli.text().title())
            var.ui.txtCar.setText(var.ui.txtCar.text().upper())
            var.ui.txtMarca.setText(var.ui.txtMarca.text().upper())
            var.ui.txtModelo.setText(var.ui.txtModelo.text().title())

        except Exception as error:
            print('Error en letras capital: ', error)