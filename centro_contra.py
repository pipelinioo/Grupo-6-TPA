# Form implementation generated from reading ui file 'centro_contra.ui'
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
        self.label.setGeometry(QtCore.QRect(30, 20, 181, 16))
        self.label.setObjectName("label")
        self.Nombre = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Nombre.setGeometry(QtCore.QRect(20, 100, 113, 22))
        self.Nombre.setObjectName("Nombre")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 55, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 140, 101, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 230, 111, 16))
        self.label_4.setObjectName("label_4")
        self.apellido_P = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.apellido_P.setGeometry(QtCore.QRect(20, 170, 113, 22))
        self.apellido_P.setObjectName("Apellido Paterno")
        self.apellido_M = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.apellido_M.setGeometry(QtCore.QRect(20, 270, 113, 22))
        self.apellido_M.setObjectName("Apellido Materno")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 320, 55, 16))
        self.label_5.setObjectName("label_5")
        self.rut = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.rut.setGeometry(QtCore.QRect(20, 350, 113, 22))
        self.rut.setObjectName("Rut")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(510, 70, 55, 16))
        self.label_6.setObjectName("label_6")
        self.direccion = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.direccion.setGeometry(QtCore.QRect(500, 100, 113, 22))
        self.direccion.setObjectName("Dirección")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(510, 150, 151, 16))
        self.label_7.setObjectName("label_7")
        self.dep = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.dep.setGeometry(QtCore.QRect(500, 190, 113, 22))
        self.dep.setObjectName("Departamento")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(510, 250, 55, 16))
        self.label_8.setObjectName("label_8")
        self.cargo = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.cargo.setGeometry(QtCore.QRect(510, 280, 113, 22))
        self.cargo.setObjectName("Cargo")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(320, 420, 93, 28))
        self.pushButton.setObjectName("pushButton")
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
        MainWindow.setWindowTitle(_translate("Centro de Contratacion", "Centro de Contratacion"))
        self.label.setText(_translate("MainWindow", "Centro de contratación"))
        self.label_2.setText(_translate("MainWindow", "Nombre"))
        self.label_3.setText(_translate("MainWindow", "Apellido paterno"))
        self.label_4.setText(_translate("MainWindow", "Apellido materno"))
        self.label_5.setText(_translate("MainWindow", "Rut"))
        self.label_6.setText(_translate("MainWindow", "Direccion"))
        self.label_7.setText(_translate("MainWindow", "Departamento a asignar"))
        self.label_8.setText(_translate("MainWindow", "Cargo"))
        self.pushButton.setText(_translate("MainWindow", "Agregar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
