from PyQt5 import QtCore, QtGui, QtWidgets

from register11 import register11
from register12 import register12
from consulta11 import consulta11
from consulta12 import consulta12
from consulta13 import consulta13
from consulta14 import consulta14
from update1 import update11
from update2 import update12


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
        self.menuActualizar = QtWidgets.QMenu(self.menubar)
        self.menuSesion = QtWidgets.QMenu(self.menubar)

        # Creación de acciones
        actions = [
            "Evaluaciones Históricas", "Detalles Carrera",
            "Resultados",
            "Evaluación", "Criterio",
            "Resumen Resultados", "Evaluaciones por Fecha",
            "Actualizar Contraseña", "Actualizar Evaluación", "Salir"
        ]
        self.actions = {name: QtWidgets.QAction(Sistema) for name in actions}

        # Definir permisos por rol
        role_permissions = {
            'admin': ["Evaluaciones Históricas", "Detalles Carrera","Resultados", 
                      "Evaluación", "Criterio", "Resumen Resultados", "Evaluaciones por Fecha", 
                      "Actualizar Contraseña", "Actualizar Evaluación", "Salir"],
            'user': ["Detalles Carrera", "Resultados", "Actualizar Contraseña", "Salir"]
        }

        # Configuración de acciones
        self.configureActions(user_role, role_permissions)

        # Añadir menús a la barra de menú
        self.menubar.addAction(self.Registro.menuAction())
        self.menubar.addAction(self.menuConsulta.menuAction())
        self.menubar.addAction(self.menuReporte.menuAction())
        self.menubar.addAction(self.menuActualizar.menuAction())
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
        self.actions["Resultados"].triggered.connect(self.abrirResultados)
        self.menuConsulta.addAction(self.actions["Detalles Carrera"])
        self.actions["Detalles Carrera"].triggered.connect(self.abrirDetallesCarrera)

        if user_role == "admin":
            self.Registro.addAction(self.actions["Evaluación"])
            self.actions["Evaluación"].triggered.connect(self.abrirRegistrarEvaluacion)
            self.Registro.addAction(self.actions["Criterio"])
            self.actions["Criterio"].triggered.connect(self.abrirRegistrarCriterio)
            self.menuConsulta.addAction(self.actions["Evaluaciones Históricas"])
            self.actions["Evaluaciones Históricas"].triggered.connect(self.abrirConsultaHistorica)
            self.menuReporte.addAction(self.actions["Evaluaciones por Fecha"])
            self.actions["Evaluaciones por Fecha"].triggered.connect(self.abrirEvaluacionesPorFecha)
            self.menuReporte.addAction(self.actions["Resumen Resultados"])
            self.menuActualizar.addAction(self.actions["Actualizar Contraseña"])
            self.actions["Actualizar Contraseña"].triggered.connect(self.abrirActualizarContrasena)
            self.menuActualizar.addAction(self.actions["Actualizar Evaluación"])
            self.actions["Actualizar Evaluación"].triggered.connect(self.abrirActualizarEvaluacion)

#Métodos para abrir ventanas:
    #Registro
    def abrirRegistrarEvaluacion(self):
        """Abre la ventana de Registrar Evaluación."""
        self.registrar_evaluacion = QtWidgets.QDialog()  # Crear diálogo
        self.ui_registro = register11()  # Crear instancia de la clase de la ventana
        self.ui_registro.setupUi(self.registrar_evaluacion)  # Configurar UI en el diálogo
        self.registrar_evaluacion.exec_()  # Mostrar ventana en modo modal

    def abrirRegistrarCriterio(self):
        """Abre la ventana de Registrar Criterio Evaluación."""
        self.registrar_criterio = QtWidgets.QDialog()
        self.ui_criterio = register12() 
        self.ui_criterio.setupUi(self.registrar_criterio)
        self.registrar_criterio.exec_()

    #Consulta
    def abrirConsultaHistorica(self):
        """Abre la ventana de Consulta Evaluaciones Históricas."""
        self.consulta_historica = QtWidgets.QDialog() 
        self.ui_consulta = consulta11() 
        self.ui_consulta.setupUi(self.consulta_historica) 
        self.consulta_historica.exec_()  

    def abrirDetallesCarrera(self):
        """Abre la ventana de Consultar Detalles de Carrera."""
        self.detalles_carrera = QtWidgets.QDialog()  
        self.ui_detalles = consulta12()  
        self.ui_detalles.setupUi(self.detalles_carrera)  
        self.detalles_carrera.exec_()  

    def abrirEvaluacionesPorFecha(self):
        """Abre la ventana de Consultar Evaluaciones por Fecha."""
        self.evaluaciones_fecha = QtWidgets.QDialog() 
        self.ui_evaluaciones_fecha = consulta13()  
        self.ui_evaluaciones_fecha.setupUi(self.evaluaciones_fecha)  
        self.evaluaciones_fecha.exec_()  

    def abrirResultados(self):
        """Abre la ventana de Consultar Resultados."""
        self.resultados = QtWidgets.QDialog()  
        self.ui_resultados = consulta14()  
        self.ui_resultados.setupUi(self.resultados)  
        self.resultados.exec_()  

    #Actualizar
    def abrirActualizarEvaluacion(self):
        """Abre la ventana para actualizar evaluación."""
        self.actualizar_evaluacion = QtWidgets.QDialog()
        self.ui_update12 = update12()
        self.ui_update12.setupUi(self.actualizar_evaluacion)
        self.actualizar_evaluacion.exec_() 
    
    def abrirActualizarContrasena(self):
        """Abre la ventana para actualizar contraseña."""
        self.actualizar_contrasena = QtWidgets.QDialog()
        self.ui_update11 = update11()
        self.ui_update11.setupUi(self.actualizar_contrasena)
        self.actualizar_contrasena.exec_()


    #Reportes
    
    
    def retranslateUi(self, Sistema):
        _translate = QtCore.QCoreApplication.translate
        Sistema.setWindowTitle(_translate("Sistema", "Sistema"))
        self.Registro.setTitle(_translate("Sistema", "Registro"))
        self.menuConsulta.setTitle(_translate("Sistema", "Consulta"))
        self.menuReporte.setTitle(_translate("Sistema", "Reporte"))
        self.menuActualizar.setTitle(_translate("Sistema", "Actualizar"))
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
