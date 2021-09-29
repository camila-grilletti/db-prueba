import sys
from PyQt5 import QtWidgets
import psycopg2
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from PyQt5.uic import loadUi

class ingresar(QMainWindow):
    def __init__(self):
        super(ingresar, self).__init__()
        loadUi("botones.ui", self)
        self.ingresarboton.clicked.connect(self.ingresarfuncion)
    
    def ingresarfuncion(self):
        ingresarfuncion=login()
        widget.addWidget(ingresarfuncion)
        widget.setCurrentIndex(widget.currentIndex()+1)

class login(QMainWindow):
    def __init__(self):
        super(login, self).__init__()
        loadUi("ingresar2.ui", self)
        self.guardar.clicked.connect(self.db)
    def db(self):
        nombre = self.nombre.text()
        apellido = self.apellido.text()
        conexion = psycopg2.connect(database = "prueba", user = "postgres", password = "649785")
        cursor = conexion.cursor()
        insertar = "insert into public.usuarios (nombre, apellido) values (%s, %s);"

        parametros = (nombre, apellido)
        cursor.execute(insertar, parametros)
        conexion.commit()

app=QApplication(sys.argv)
mainwindow=ingresar()
widget =QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(480)
widget.setFixedHeight(620)
widget.show()
app.exec_()
