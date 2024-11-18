from PyQt5 import QtCore, QtGui, QtWidgets
from menu import Ui_Sistema  # Importa el menú

class Ui_Ingreso(object):
    def setupUi(self, Ingreso):
        Ingreso.setObjectName("Ingreso")
        Ingreso.resize(737, 314)
        self.centralwidget = QtWidgets.QWidget(Ingreso)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 80, 71, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 120, 101, 41))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(250, 90, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 130, 113, 22))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 170, 75, 24))
        self.pushButton.setObjectName("pushButton")
        Ingreso.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Ingreso)
        self.statusbar.setObjectName("statusbar")
        Ingreso.setStatusBar(self.statusbar)

        self.retranslateUi(Ingreso)
        self.pushButton.clicked.connect(self.openSistema)  # Conecta el botón
        QtCore.QMetaObject.connectSlotsByName(Ingreso)

    def retranslateUi(self, Ingreso):
        _translate = QtCore.QCoreApplication.translate
        Ingreso.setWindowTitle(_translate("Ingreso", "Ingreso al Sistema"))
        self.label.setText(_translate("Ingreso", "Usuario:"))
        self.label_2.setText(_translate("Ingreso", "Contraseña:"))
        self.pushButton.setText(_translate("Ingreso", "Ingresar"))

    def openSistema(self):
        usuario = self.lineEdit.text()
        contraseña = self.lineEdit_2.text()

        if usuario == "admin" and contraseña == "1234":
            self.showSistema("admin")
        elif usuario == "user" and contraseña == "abcd":
            self.showSistema("user")
        else:
            QtWidgets.QMessageBox.warning(None, "Error", "Usuario o contraseña incorrectos")

    def showSistema(self, role):
        self.window = QtWidgets.QMainWindow()  # Mantén esta referencia
        self.ui = Ui_Sistema()
        self.ui.setupUi(self.window, role)  # Pasa el rol al menú
        self.window.show()
        QtWidgets.QApplication.instance().activeWindow().hide()  # Esconde la ventana de ingreso


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ingreso = QtWidgets.QMainWindow()
    ui = Ui_Ingreso()
    ui.setupUi(Ingreso)
    Ingreso.show()
    sys.exit(app.exec_())
