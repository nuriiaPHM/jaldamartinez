# Form implementation generated from reading ui file 'dlgCalendar.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_dlgCalendar(object):
    def setupUi(self, dlgCalendar):
        dlgCalendar.setObjectName("dlgCalendar")
        dlgCalendar.resize(320, 240)
        dlgCalendar.setMinimumSize(QtCore.QSize(320, 240))
        dlgCalendar.setMaximumSize(QtCore.QSize(320, 240))
        self.Calendar = QtWidgets.QCalendarWidget(dlgCalendar)
        self.Calendar.setGeometry(QtCore.QRect(0, 0, 320, 230))
        self.Calendar.setMinimumSize(QtCore.QSize(320, 230))
        self.Calendar.setMaximumSize(QtCore.QSize(320, 230))
        self.Calendar.setObjectName("Calendar")

        self.retranslateUi(dlgCalendar)
        QtCore.QMetaObject.connectSlotsByName(dlgCalendar)

    def retranslateUi(self, dlgCalendar):
        _translate = QtCore.QCoreApplication.translate
        dlgCalendar.setWindowTitle(_translate("dlgCalendar", "Fecha Alta"))
