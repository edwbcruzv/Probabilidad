# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Interfaz_Prob.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1316, 867)
        self.groupBox_Integral1 = QtWidgets.QGroupBox(Form)
        self.groupBox_Integral1.setGeometry(QtCore.QRect(40, 20, 1241, 381))
        font = QtGui.QFont()
        font.setFamily("Microsoft New Tai Lue")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.groupBox_Integral1.setFont(font)
        self.groupBox_Integral1.setMouseTracking(False)
        self.groupBox_Integral1.setObjectName("groupBox_Integral1")
        self.doubleSpinBox_a = QtWidgets.QDoubleSpinBox(self.groupBox_Integral1)
        self.doubleSpinBox_a.setGeometry(QtCore.QRect(60, 30, 251, 22))
        self.doubleSpinBox_a.setMinimumSize(QtCore.QSize(42, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.doubleSpinBox_a.setFont(font)
        self.doubleSpinBox_a.setMouseTracking(False)
        self.doubleSpinBox_a.setTabletTracking(False)
        self.doubleSpinBox_a.setStyleSheet("")
        self.doubleSpinBox_a.setReadOnly(False)
        self.doubleSpinBox_a.setAccelerated(False)
        self.doubleSpinBox_a.setDecimals(10)
        self.doubleSpinBox_a.setMinimum(-999999999.9)
        self.doubleSpinBox_a.setMaximum(999999999.9)
        self.doubleSpinBox_a.setObjectName("doubleSpinBox_a")
        self.label = QtWidgets.QLabel(self.groupBox_Integral1)
        self.label.setGeometry(QtCore.QRect(30, 30, 21, 16))
        self.label.setMouseTracking(False)
        self.label.setAcceptDrops(False)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_Integral1)
        self.label_2.setGeometry(QtCore.QRect(430, 30, 31, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_Integral1)
        self.label_3.setGeometry(QtCore.QRect(30, 80, 31, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_Integral1)
        self.label_4.setGeometry(QtCore.QRect(430, 70, 21, 20))
        self.label_4.setObjectName("label_4")
        self.doubleSpinBox_b = QtWidgets.QDoubleSpinBox(self.groupBox_Integral1)
        self.doubleSpinBox_b.setGeometry(QtCore.QRect(470, 30, 251, 22))
        self.doubleSpinBox_b.setMinimumSize(QtCore.QSize(42, 22))
        self.doubleSpinBox_b.setMouseTracking(False)
        self.doubleSpinBox_b.setTabletTracking(False)
        self.doubleSpinBox_b.setStyleSheet("")
        self.doubleSpinBox_b.setReadOnly(False)
        self.doubleSpinBox_b.setAccelerated(False)
        self.doubleSpinBox_b.setDecimals(10)
        self.doubleSpinBox_b.setMinimum(-999999999.9)
        self.doubleSpinBox_b.setMaximum(999999999.9)
        self.doubleSpinBox_b.setObjectName("doubleSpinBox_b")
        self.doubleSpinBox_sigma = QtWidgets.QDoubleSpinBox(self.groupBox_Integral1)
        self.doubleSpinBox_sigma.setGeometry(QtCore.QRect(60, 80, 251, 22))
        self.doubleSpinBox_sigma.setMinimumSize(QtCore.QSize(42, 22))
        self.doubleSpinBox_sigma.setMouseTracking(False)
        self.doubleSpinBox_sigma.setTabletTracking(False)
        self.doubleSpinBox_sigma.setStyleSheet("")
        self.doubleSpinBox_sigma.setReadOnly(False)
        self.doubleSpinBox_sigma.setAccelerated(False)
        self.doubleSpinBox_sigma.setDecimals(6)
        self.doubleSpinBox_sigma.setMinimum(1e-06)
        self.doubleSpinBox_sigma.setMaximum(999999999.9)
        self.doubleSpinBox_sigma.setProperty("value", 1e-06)
        self.doubleSpinBox_sigma.setObjectName("doubleSpinBox_sigma")
        self.doubleSpinBox_media = QtWidgets.QDoubleSpinBox(self.groupBox_Integral1)
        self.doubleSpinBox_media.setGeometry(QtCore.QRect(470, 70, 251, 22))
        self.doubleSpinBox_media.setMinimumSize(QtCore.QSize(42, 22))
        self.doubleSpinBox_media.setMouseTracking(False)
        self.doubleSpinBox_media.setTabletTracking(False)
        self.doubleSpinBox_media.setStyleSheet("")
        self.doubleSpinBox_media.setReadOnly(False)
        self.doubleSpinBox_media.setAccelerated(False)
        self.doubleSpinBox_media.setDecimals(10)
        self.doubleSpinBox_media.setMinimum(-999999999.9)
        self.doubleSpinBox_media.setMaximum(999999999.9)
        self.doubleSpinBox_media.setObjectName("doubleSpinBox_media")
        self.label_5 = QtWidgets.QLabel(self.groupBox_Integral1)
        self.label_5.setGeometry(QtCore.QRect(30, 130, 21, 16))
        self.label_5.setObjectName("label_5")
        self.spinBox_n = QtWidgets.QSpinBox(self.groupBox_Integral1)
        self.spinBox_n.setGeometry(QtCore.QRect(60, 130, 251, 22))
        self.spinBox_n.setMinimum(1)
        self.spinBox_n.setMaximum(50)
        self.spinBox_n.setObjectName("spinBox_n")
        self.textEdit_ResultadoIntegral1 = QtWidgets.QTextEdit(self.groupBox_Integral1)
        self.textEdit_ResultadoIntegral1.setEnabled(True)
        self.textEdit_ResultadoIntegral1.setGeometry(QtCore.QRect(30, 240, 691, 111))
        self.textEdit_ResultadoIntegral1.setMouseTracking(False)
        self.textEdit_ResultadoIntegral1.setTabletTracking(False)
        self.textEdit_ResultadoIntegral1.setToolTip("")
        self.textEdit_ResultadoIntegral1.setObjectName("textEdit_ResultadoIntegral1")
        self.pushButton_CalcularIntegral1 = QtWidgets.QPushButton(self.groupBox_Integral1)
        self.pushButton_CalcularIntegral1.setGeometry(QtCore.QRect(60, 180, 201, 41))
        self.pushButton_CalcularIntegral1.setObjectName("pushButton_CalcularIntegral1")
        self.label_9 = QtWidgets.QLabel(self.groupBox_Integral1)
        self.label_9.setGeometry(QtCore.QRect(760, 180, 461, 151))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("Integral1.jpeg"))
        self.label_9.setScaledContents(True)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.label_12 = QtWidgets.QLabel(self.groupBox_Integral1)
        self.label_12.setGeometry(QtCore.QRect(350, 120, 851, 16))
        self.label_12.setObjectName("label_12")
        self.progressBar_Integral1 = QtWidgets.QProgressBar(self.groupBox_Integral1)
        self.progressBar_Integral1.setGeometry(QtCore.QRect(340, 160, 171, 23))
        self.progressBar_Integral1.setProperty("value", 0)
        self.progressBar_Integral1.setObjectName("progressBar_Integral1")
        self.groupBox_Integral1_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_Integral1_2.setGeometry(QtCore.QRect(30, 420, 1251, 371))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Typewriter")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_Integral1_2.setFont(font)
        self.groupBox_Integral1_2.setObjectName("groupBox_Integral1_2")
        self.label_6 = QtWidgets.QLabel(self.groupBox_Integral1_2)
        self.label_6.setGeometry(QtCore.QRect(40, 40, 21, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_Integral1_2)
        self.label_7.setGeometry(QtCore.QRect(40, 90, 31, 16))
        self.label_7.setObjectName("label_7")
        self.doubleSpinBox_b0 = QtWidgets.QDoubleSpinBox(self.groupBox_Integral1_2)
        self.doubleSpinBox_b0.setGeometry(QtCore.QRect(70, 40, 251, 22))
        self.doubleSpinBox_b0.setMinimumSize(QtCore.QSize(42, 22))
        self.doubleSpinBox_b0.setMouseTracking(False)
        self.doubleSpinBox_b0.setTabletTracking(False)
        self.doubleSpinBox_b0.setStyleSheet("")
        self.doubleSpinBox_b0.setReadOnly(False)
        self.doubleSpinBox_b0.setAccelerated(False)
        self.doubleSpinBox_b0.setDecimals(10)
        self.doubleSpinBox_b0.setMinimum(-999999999.9)
        self.doubleSpinBox_b0.setMaximum(999999999.9)
        self.doubleSpinBox_b0.setObjectName("doubleSpinBox_b0")
        self.doubleSpinBox_bf = QtWidgets.QDoubleSpinBox(self.groupBox_Integral1_2)
        self.doubleSpinBox_bf.setGeometry(QtCore.QRect(70, 90, 251, 22))
        self.doubleSpinBox_bf.setMinimumSize(QtCore.QSize(42, 22))
        self.doubleSpinBox_bf.setMouseTracking(False)
        self.doubleSpinBox_bf.setTabletTracking(False)
        self.doubleSpinBox_bf.setStyleSheet("")
        self.doubleSpinBox_bf.setReadOnly(False)
        self.doubleSpinBox_bf.setAccelerated(False)
        self.doubleSpinBox_bf.setDecimals(10)
        self.doubleSpinBox_bf.setMinimum(-999999999.9)
        self.doubleSpinBox_bf.setMaximum(999999999.9)
        self.doubleSpinBox_bf.setObjectName("doubleSpinBox_bf")
        self.doubleSpinBox_delta = QtWidgets.QDoubleSpinBox(self.groupBox_Integral1_2)
        self.doubleSpinBox_delta.setGeometry(QtCore.QRect(70, 140, 251, 22))
        self.doubleSpinBox_delta.setMinimum(0.02)
        self.doubleSpinBox_delta.setMaximum(1000.0)
        self.doubleSpinBox_delta.setObjectName("doubleSpinBox_delta")
        self.label_8 = QtWidgets.QLabel(self.groupBox_Integral1_2)
        self.label_8.setGeometry(QtCore.QRect(20, 140, 55, 16))
        self.label_8.setObjectName("label_8")
        self.pushButton_CalcularIntegral2 = QtWidgets.QPushButton(self.groupBox_Integral1_2)
        self.pushButton_CalcularIntegral2.setGeometry(QtCore.QRect(20, 190, 181, 41))
        self.pushButton_CalcularIntegral2.setObjectName("pushButton_CalcularIntegral2")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_Integral1_2)
        self.tableWidget.setGeometry(QtCore.QRect(350, 30, 441, 311))
        font = QtGui.QFont()
        font.setItalic(True)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.textEdit_ResultadoIntegral2 = QtWidgets.QTextEdit(self.groupBox_Integral1_2)
        self.textEdit_ResultadoIntegral2.setGeometry(QtCore.QRect(20, 260, 321, 87))
        self.textEdit_ResultadoIntegral2.setObjectName("textEdit_ResultadoIntegral2")
        self.label_10 = QtWidgets.QLabel(self.groupBox_Integral1_2)
        self.label_10.setGeometry(QtCore.QRect(820, 170, 401, 141))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("Integral2.jpeg"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.progressBar_Integral2 = QtWidgets.QProgressBar(self.groupBox_Integral1_2)
        self.progressBar_Integral2.setGeometry(QtCore.QRect(230, 200, 101, 23))
        self.progressBar_Integral2.setProperty("value", 0)
        self.progressBar_Integral2.setObjectName("progressBar_Integral2")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(120, 810, 1061, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")

        self.retranslateUi(Form)
        self.doubleSpinBox_a.valueChanged['double'].connect(self.textEdit_ResultadoIntegral1.clear) # type: ignore
        self.doubleSpinBox_b.editingFinished.connect(self.textEdit_ResultadoIntegral1.clear) # type: ignore
        self.doubleSpinBox_sigma.editingFinished.connect(self.textEdit_ResultadoIntegral1.clear) # type: ignore
        self.doubleSpinBox_media.editingFinished.connect(self.textEdit_ResultadoIntegral1.clear) # type: ignore
        self.spinBox_n.editingFinished.connect(self.textEdit_ResultadoIntegral1.clear) # type: ignore
        self.doubleSpinBox_b0.editingFinished.connect(self.tableWidget.reset) # type: ignore
        self.doubleSpinBox_bf.editingFinished.connect(self.tableWidget.clear) # type: ignore
        self.doubleSpinBox_delta.editingFinished.connect(self.tableWidget.clear) # type: ignore
        self.spinBox_n.editingFinished.connect(self.progressBar_Integral1.reset) # type: ignore
        self.doubleSpinBox_sigma.editingFinished.connect(self.progressBar_Integral1.reset) # type: ignore
        self.doubleSpinBox_a.editingFinished.connect(self.progressBar_Integral1.reset) # type: ignore
        self.doubleSpinBox_b.editingFinished.connect(self.progressBar_Integral1.reset) # type: ignore
        self.doubleSpinBox_media.editingFinished.connect(self.progressBar_Integral1.reset) # type: ignore
        self.doubleSpinBox_b0.editingFinished.connect(self.progressBar_Integral2.reset) # type: ignore
        self.doubleSpinBox_bf.editingFinished.connect(self.progressBar_Integral2.reset) # type: ignore
        self.doubleSpinBox_delta.editingFinished.connect(self.progressBar_Integral2.reset) # type: ignore
        self.doubleSpinBox_b0.editingFinished.connect(self.textEdit_ResultadoIntegral2.clear) # type: ignore
        self.doubleSpinBox_bf.editingFinished.connect(self.textEdit_ResultadoIntegral2.clear) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox_Integral1.setTitle(_translate("Form", "Integral 1"))
        self.label.setText(_translate("Form", "a ="))
        self.label_2.setText(_translate("Form", "b ="))
        self.label_3.setText(_translate("Form", "σ ="))
        self.label_4.setText(_translate("Form", " μ ="))
        self.label_5.setText(_translate("Form", "n ="))
        self.pushButton_CalcularIntegral1.setText(_translate("Form", "Calcular"))
        self.label_12.setText(_translate("Form", "Nota: entre mas alto sea n mas tardara el programa en obtener el resultado, no preocuparse"))
        self.groupBox_Integral1_2.setTitle(_translate("Form", "Integral 2"))
        self.label_6.setText(_translate("Form", "b0 ="))
        self.label_7.setText(_translate("Form", "bf ="))
        self.label_8.setText(_translate("Form", "delta ="))
        self.pushButton_CalcularIntegral2.setText(_translate("Form", "Calcular"))
        self.label_11.setText(_translate("Form", "Elaborado por Edwin Bernardo Cruz villalba, Prob y Estadistica 2CV16. PD: Evite Romperlo Profe :)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())