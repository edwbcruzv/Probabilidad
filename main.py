##conexion con la interfaz grafica comando>   pyuic5 -x Interfaz_Prob.ui -o Interfaz_Prob.py 
import sys
import os
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from Interfaz_Prob.Interfaz_Prob import Ui_Form
from Integral1 import *
from Integral2 import *



class Ventana(QtWidgets.QWidget):
    

    def __init__(self,parent=None):
        super(Ventana,self).__init__(parent)
        self.ui=Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton_CalcularIntegral1.clicked.connect(self.Integral1_Operacion)
        self.ui.pushButton_CalcularIntegral2.clicked.connect(self.Integral2_Operacion)

    
    def Integral1_Operacion(self):
        self.ui.progressBar_Integral1.setValue(10)
        a=self.ui.doubleSpinBox_a.value()
        b=self.ui.doubleSpinBox_b.value()
        n=self.ui.spinBox_n.value()
        u=self.ui.doubleSpinBox_media.value()
        sigma=self.ui.doubleSpinBox_sigma.value()
        self.ui.progressBar_Integral1.setValue(30)

        res=integral_1(a,b,sigma,u,n)
        self.ui.progressBar_Integral1.setValue(80)
        self.ui.textEdit_ResultadoIntegral1.setText(str(res))
        self.ui.progressBar_Integral1.setValue(100)

    def Integral2_Operacion(self):
        self.ui.progressBar_Integral2.setValue(10)

        b0=self.ui.doubleSpinBox_b0.value()
        bf=self.ui.doubleSpinBox_bf.value()
        delta=self.ui.doubleSpinBox_delta.value()
        self.ui.progressBar_Integral2.setValue(20)
        res_list=integral_2(b0,bf,delta)
        self.ui.progressBar_Integral2.setValue(50)

        self.Tabla_Integral2(res_list)
        self.ui.progressBar_Integral2.setValue(80)
        elem0=res_list[0][1]
        elemN=res_list[len(res_list)-1][1]
        resta=elem0-elemN
        self.ui.textEdit_ResultadoIntegral2.setText(str(resta))
        self.ui.progressBar_Integral2.setValue(100)


    def Tabla_Integral2(self,res_list):

        _translate = QtCore.QCoreApplication.translate

        tam_list=len(res_list)
        # definiendo numero de columnas
        self.ui.tableWidget.setColumnCount(2)
        # definiendo numero de filas (usando numero de automatas en la lista)
        self.ui.tableWidget.setRowCount(tam_list)

        
        #definiendo los numeros de las filas
        for f in range(tam_list):
            item = QtWidgets.QTableWidgetItem()
            self.ui.tableWidget.setVerticalHeaderItem(f, item)

        #definiendo las columnas y la cabecera
        for c in range(2):
            item = QtWidgets.QTableWidgetItem()
            self.ui.tableWidget.setHorizontalHeaderItem(c, item)

        ##definiendo los cuadros de las tabla (matriz)
        for f in range(tam_list):
            for c in range(2):
                item = QtWidgets.QTableWidgetItem()
                self.ui.tableWidget.setItem(f, c, item)

        
        #indicador de las filas
        
        for i in range(tam_list):
            item = self.ui.tableWidget.verticalHeaderItem(i)
            item.setText(_translate("Form", "b ="))
        
        #Cabecera de la tabla
        item = self.ui.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "b"))
        item = self.ui.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Integral"))

        __sortingEnabled = self.ui.tableWidget.isSortingEnabled()
        self.ui.tableWidget.setSortingEnabled(False)


        #llenado de la tabla
        for i in range(tam_list):
            item = self.ui.tableWidget.item(i, 0)
            item.setText(_translate("Form", str(res_list[i][0])))
            item = self.ui.tableWidget.item(i, 1)
            item.setText(_translate("Form", str(res_list[i][1])))

        self.ui.tableWidget.setSortingEnabled(__sortingEnabled)

##*****INICIO DE TODO EL PROGRAMA
if __name__=='__main__':
    app=QtWidgets.QApplication(sys.argv)
    myapp=Ventana()
    myapp.show()
    sys.exit(app.exec_())