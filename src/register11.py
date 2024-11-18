
from PyQt5 import QtCore, QtGui, QtWidgets


class register11(object):
    def setupUi(self, RegistrarEvaluacion):
        RegistrarEvaluacion.setObjectName("RegistrarEvaluacion")
        RegistrarEvaluacion.resize(392, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(RegistrarEvaluacion)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(RegistrarEvaluacion)
        self.label.setGeometry(QtCore.QRect(20, 30, 91, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(RegistrarEvaluacion)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 91, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(RegistrarEvaluacion)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 101, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(RegistrarEvaluacion)
        self.label_4.setGeometry(QtCore.QRect(20, 150, 101, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(RegistrarEvaluacion)
        self.lineEdit.setGeometry(QtCore.QRect(130, 30, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(RegistrarEvaluacion)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 70, 113, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(RegistrarEvaluacion)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 110, 113, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(RegistrarEvaluacion)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 150, 113, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.retranslateUi(RegistrarEvaluacion)
        self.buttonBox.accepted.connect(RegistrarEvaluacion.accept) # type: ignore
        self.buttonBox.rejected.connect(RegistrarEvaluacion.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(RegistrarEvaluacion)

    def retranslateUi(self, RegistrarEvaluacion):
        _translate = QtCore.QCoreApplication.translate
        RegistrarEvaluacion.setWindowTitle(_translate("RegistrarEvaluacion", "Registrar Evaluacion"))
        self.label.setText(_translate("RegistrarEvaluacion", "ID Evaluación:"))
        self.label_2.setText(_translate("RegistrarEvaluacion", "Fecha:"))
        self.label_3.setText(_translate("RegistrarEvaluacion", "Evaluador:"))
        self.label_4.setText(_translate("RegistrarEvaluacion", "Informe Final:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RegistrarEvaluacion = QtWidgets.QDialog()
    ui = register11()
    ui.setupUi(RegistrarEvaluacion)
    RegistrarEvaluacion.show()
    sys.exit(app.exec_())
