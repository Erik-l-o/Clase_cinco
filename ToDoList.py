from PyQt5 import QtWidgets,uic
from PyQt5.QtWidgets import QMessageBox
class ToDoList(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ToDoList.ui",self)
        self.btnAgregar.clicked.connect(self.AgregarTarea)
        self.btnEliminar.clicked.connect(self.EliminarTarea)
    def AgregarTarea(self):
        tarea=self.edtTarea.text()
        self.lstTareas.addItem(tarea)
        self.edtTarea.clear()
        self.edtTarea.setFocus()
        #TODO AGREGAR LA VALIDACIÓN DE CAMPO NO VACIO
    def EliminarTarea(self):
        indiceTareaBorrar=self.lstTareas.currentRow()
        self.lstTareas.takeItem(indiceTareaBorrar)
    def ActualizarTarea(self):
        indice=self.lstTareas.currentRow()
        texto= self.edtTarea.text()
        if indice >= 0:
            QMessageBox.information(self,"seleccion","seleccionar tarea")
            return
        if texto.strip()=="":
            QMessageBox.information(self,"espacio","campo vacio")
            return
        self.lstTareas.item(indice).setText(texto)
        self.edtTarea.clear()
        self.edtTarea.setFocus()