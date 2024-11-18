from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Sistema(object):
    def setupUi(self, Sistema, user_role):
        Sistema.setObjectName("Sistema")
        Sistema.resize(800, 600)

        # Configuración de la paleta de colores
        palette = QtGui.QPalette()
        colors = [
            (QtGui.QPalette.WindowText, QtGui.QColor(0, 0, 0)),
            (QtGui.QPalette.Button, QtGui.QColor(85, 170, 255)),
            (QtGui.QPalette.Light, QtGui.QColor(212, 234, 255)),
            (QtGui.QPalette.Midlight, QtGui.QColor(148, 202, 255)),
            (QtGui.QPalette.Dark, QtGui.QColor(42, 85, 127)),
            (QtGui.QPalette.Mid, QtGui.QColor(57, 113, 170)),
            (QtGui.QPalette.Text, QtGui.QColor(0, 0, 0)),
            (QtGui.QPalette.BrightText, QtGui.QColor(255, 255, 255)),
            (QtGui.QPalette.ButtonText, QtGui.QColor(0, 0, 0)),
            (QtGui.QPalette.Base, QtGui.QColor(255, 255, 255)),
            (QtGui.QPalette.Window, QtGui.QColor(85, 170, 255)),
            (QtGui.QPalette.AlternateBase, QtGui.QColor(170, 212, 255)),
            (QtGui.QPalette.ToolTipBase, QtGui.QColor(255, 255, 220)),
            (QtGui.QPalette.ToolTipText, QtGui.QColor(0, 0, 0)),
            (QtGui.QPalette.PlaceholderText, QtGui.QColor(0, 0, 0, 127)),
        ]
        for role, color in colors:
            brush = QtGui.QBrush(color)
            palette.setBrush(QtGui.QPalette.Active, role, brush)
            palette.setBrush(QtGui.QPalette.Inactive, role, brush)
            if role != QtGui.QPalette.Text:  # Ejemplo: personalizar deshabilitado
                palette.setBrush(QtGui.QPalette.Disabled, role, brush)

        Sistema.setPalette(palette)

        # Configuración del widget central y la barra de menú
        self.centralwidget = QtWidgets.QWidget(Sistema)
        Sistema.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Sistema)
        Sistema.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Sistema)
        Sistema.setStatusBar(self.statusbar)

        # Creación de menús
        self.Registro = QtWidgets.QMenu(self.menubar)
        self.menuConsulta = QtWidgets.QMenu(self.menubar)
        self.menuReporte = QtWidgets.QMenu(self.menubar)
        self.menuSesion = QtWidgets.QMenu(self.menubar)

        # Creación de acciones
        actions = [
            "Evaluaciones Históricas", "Detalles Carrera",
            "Evaluaciones Realizadas", "Resultados",
            "Evaluación", "Criterio",
            "Resumen Resultados", "Evaluaciones por Fecha", "Salir"
        ]
        self.actions = {name: QtWidgets.QAction(Sistema) for name in actions}

        # Definir permisos por rol
        role_permissions = {
            'admin': ["Evaluaciones Históricas", "Detalles Carrera", "Evaluaciones Realizadas", "Resultados", 
                      "Evaluación", "Criterio", "Resumen Resultados", "Evaluaciones por Fecha", "Salir"],
            'user': ["Detalles Carrera", "Resultados", "Salir"]
        }

        # Configuración de acciones
        self.configureActions(user_role, role_permissions)

        # Añadir menús a la barra de menú
        self.menubar.addAction(self.Registro.menuAction())
        self.menubar.addAction(self.menuConsulta.menuAction())
        self.menubar.addAction(self.menuReporte.menuAction())
        self.menubar.addAction(self.menuSesion.menuAction())

        self.retranslateUi(Sistema)
        QtCore.QMetaObject.connectSlotsByName(Sistema)

        # Conectar acción salir
        self.actions["Salir"].triggered.connect(self.salir)

    def configureActions(self, user_role, role_permissions):
        """Configura las acciones según el rol."""
        for name, action in self.actions.items():
            action.setObjectName(name.replace(" ", "_"))
            action.setEnabled(name in role_permissions.get(user_role, []))

        # Asignar acciones a menús
        self.menuSesion.addAction(self.actions["Salir"])
        self.menuConsulta.addAction(self.actions["Resultados"])
        self.menuConsulta.addAction(self.actions["Detalles Carrera"])

        if user_role == "admin":
            self.Registro.addAction(self.actions["Evaluación"])
            self.Registro.addAction(self.actions["Criterio"])
            self.menuConsulta.addAction(self.actions["Evaluaciones Históricas"])
            self.menuConsulta.addAction(self.actions["Evaluaciones Realizadas"])
            self.menuReporte.addAction(self.actions["Evaluaciones por Fecha"])
            self.menuReporte.addAction(self.actions["Resumen Resultados"])

    def retranslateUi(self, Sistema):
        _translate = QtCore.QCoreApplication.translate
        Sistema.setWindowTitle(_translate("Sistema", "Sistema"))
        self.Registro.setTitle(_translate("Sistema", "Registro"))
        self.menuConsulta.setTitle(_translate("Sistema", "Consulta"))
        self.menuReporte.setTitle(_translate("Sistema", "Reporte"))
        self.menuSesion.setTitle(_translate("Sistema", "Sesión"))
        for name, action in self.actions.items():
            action.setText(_translate("Sistema", name))

    def salir(self):
        """Maneja la acción de salir."""
        QtWidgets.QApplication.quit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Sistema = QtWidgets.QMainWindow()
    ui = Ui_Sistema()
    ui.setupUi(Sistema, user_role='admin')  # Cambia 'admin' según el rol
    Sistema.show()
    sys.exit(app.exec_())
