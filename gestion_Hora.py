# Form implementation generated from reading ui file 'gestion_Hora.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 30, 131, 16))
        self.label.setObjectName("label")
        self.calendarWidget = QtWidgets.QCalendarWidget(parent=self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(40, 100, 392, 236))
        self.calendarWidget.setObjectName("calendarWidget")
        self.asignar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.asignar.setGeometry(QtCore.QRect(40, 400, 93, 28))
        self.asignar.setObjectName("Asignar")
        self.eliminar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.eliminar.setGeometry(QtCore.QRect(160, 400, 93, 28))
        self.eliminar.setObjectName("Eliminar")
        self.registros = QtWidgets.QPushButton(parent=self.centralwidget)
        self.registros.setGeometry(QtCore.QRect(290, 400, 131, 28))
        self.registros.setObjectName("Registros")
        self.listadesocios = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.listadesocios.setGeometry(QtCore.QRect(540, 120, 221, 111))
        self.listadesocios.setObjectName("Lista de socios")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(540, 90, 101, 16))
        self.label_2.setObjectName("label_2")
        self.tareas = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.tareas.setGeometry(QtCore.QRect(540, 270, 221, 111))
        self.tareas.setObjectName("Tareas")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(540, 240, 131, 16))
        self.label_3.setObjectName("label_3")
        self.imprimir_horarios = QtWidgets.QPushButton(parent=self.centralwidget)
        self.imprimir_horarios.setGeometry(QtCore.QRect(590, 420, 151, 28))
        self.imprimir_horarios.setObjectName("Imprimir horarios")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Gestion Horarios", "Gestion Horarios"))
        self.label.setText(_translate("MainWindow", "Gestion de horarios"))
        self.asignar.setText(_translate("MainWindow", "Asignar"))
        self.eliminar.setText(_translate("MainWindow", "Eliminar"))
        self.registros.setText(_translate("MainWindow", "Registros anteriores"))
        self.label_2.setText(_translate("MainWindow", "Lista de socios"))
        self.label_3.setText(_translate("MainWindow", "Tareas pendientes"))
        self.imprimir_horarios.setText(_translate("MainWindow", "imprimir  horarios"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())