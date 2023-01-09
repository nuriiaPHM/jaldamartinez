import os, var
from reportlab.pdfgen import canvas
from datetime import datetime

class Informes:
    def listClientes(self):
        try:
            var.report = canvas.Canvas('informes/listadoClientes.pdf')
            titulo = 'LISTADO CLIENTES'

            var.report.drawString(100,750, str(titulo))
            Informes.pieInforme(titulo)
            var.report.save()

            rootPath = '.\\informes'
            for file in os.listdir(rootPath):
                if file.endswith('Clientes.pdf'):
                    os.startfile('%s\%s' % (rootPath, file))

        except Exception as error:
            print('Error en Informes.listClientes(): ', error)

    def listCoches(self):
        try:
            var.report = canvas.Canvas('informes/listadoCoches.pdf')
            titulo = 'LISTADO VEHÍCULOS'

            var.report.drawString(100, 750, str(titulo))
            Informes.pieInforme(titulo)
            var.report.save()

            rootPath = '.\\informes'
            for file in os.listdir(rootPath):
                if file.endswith('Coches.pdf'):
                    os.startfile('%s\%s' % (rootPath, file))

        except Exception as error:
            print('Error en Informes.listCoches(): ', error)

    def pieInforme(titulo):
        try:
            var.report.line(50,50,540,50)

            fecha = datetime.today().strftime('%d/%m/%Y %H:%M:%S')
            var.report.setFont('Helvetica-Oblique', size = 7)
            var.report.drawString(60,40, str(fecha))

            var.report.drawString(270,40, str(titulo))

            var.report.drawString(500,40, str('Pagina %s' % var.report.getPageNumber()))

        except Exception as error:
            print('Error en Informes.pieInforme(): ', error)


