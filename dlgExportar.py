# Form implementation generated from reading ui file 'dlgExportar.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_dlgExportar(object):
    def setupUi(self, dlgExportar):
        dlgExportar.setObjectName("dlgExportar")
        dlgExportar.resize(260, 130)
        dlgExportar.setMinimumSize(QtCore.QSize(260, 130))
        dlgExportar.setMaximumSize(QtCore.QSize(260, 130))
        self.label = QtWidgets.QLabel(dlgExportar)
        self.label.setGeometry(QtCore.QRect(30, 20, 151, 21))
        self.label.setObjectName("label")
        self.layoutWidget_4 = QtWidgets.QWidget(dlgExportar)
        self.layoutWidget_4.setGeometry(QtCore.QRect(30, 50, 179, 22))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.cbClientes = QtWidgets.QCheckBox(self.layoutWidget_4)
        self.cbClientes.setMinimumSize(QtCore.QSize(80, 20))
        self.cbClientes.setMaximumSize(QtCore.QSize(80, 20))
        self.cbClientes.setObjectName("cbClientes")
        self.horizontalLayout_6.addWidget(self.cbClientes)
        self.cbCoches = QtWidgets.QCheckBox(self.layoutWidget_4)
        self.cbCoches.setMinimumSize(QtCore.QSize(80, 20))
        self.cbCoches.setMaximumSize(QtCore.QSize(80, 20))
        self.cbCoches.setObjectName("cbCoches")
        self.horizontalLayout_6.addWidget(self.cbCoches)
        self.btnAceptar = QtWidgets.QPushButton(dlgExportar)
        self.btnAceptar.setGeometry(QtCore.QRect(150, 90, 75, 23))
        self.btnAceptar.setObjectName("btnAceptar")

        self.retranslateUi(dlgExportar)
        QtCore.QMetaObject.connectSlotsByName(dlgExportar)

    def retranslateUi(self, dlgExportar):
        _translate = QtCore.QCoreApplication.translate
        dlgExportar.setWindowTitle(_translate("dlgExportar", "Dialog"))
        self.label.setText(_translate("dlgExportar", "¿Qué datos quiere exportar?"))
        self.cbClientes.setText(_translate("dlgExportar", "Clientes"))
        self.cbCoches.setText(_translate("dlgExportar", "Coches"))
        self.btnAceptar.setText(_translate("dlgExportar", "Aceptar"))
