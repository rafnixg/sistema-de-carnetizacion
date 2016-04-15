#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Sistema de carnetizacion hecho en python y SQLite3
# Desarrollado por Rafnix Guzman @rafnixg 
# http://rafnixg.github.io/

import sys, sqlite3
from PyQt4 import QtCore, QtGui, uic

# Cargando el archivo de la interfaz grafica
form_ver = uic.loadUiType("ver.ui")[0]

# Clase del from Ver
class Ver(QtGui.QWidget,form_ver):
	def __init__(self,parent=None):
		QtGui.QWidget.__init__(self,parent)
		self.setupUi(self)

		# Manejando los eventos click
		self.btn_ver_lista.clicked.connect(self.btn_ver_lista_click)

	def btn_ver_lista_click(self):
		# Abro la conexion a la DB
		self.con = sqlite3.connect('db/carnets.db')
		self.cursor = self.con.cursor()

		# Cargo los datos de la db
		self.cursor.execute("SELECT id, nombre, apellido, cedula, rol, carrera FROM Usuarios")
		
		# Inicializamos las filas de la tabla
		row = 0
		self.lista.setRowCount(0)

		# Recorremos el cursor
		for i in self.cursor:
			
			self.id = i[0]
			self.nombre = i[1]
			self.apellido = i[2]
			self.cedula = i[3]
			self.rol = i[4]
			self.carrera = i[5]

			# Insertamos una nueva fila a la tabla
			self.lista.insertRow(row)

			# Convirtiendo el tipo de dato de las variables
			self.nombre = QtGui.QTableWidgetItem(self.nombre)
			self.apellido = QtGui.QTableWidgetItem(self.apellido)
			self.cedula = QtGui.QTableWidgetItem(self.cedula)
			self.rol = QtGui.QTableWidgetItem(self.rol)
			self.carrera = QtGui.QTableWidgetItem(self.carrera)
			self.id = QtGui.QTableWidgetItem(str(self.id))

			# Insertamos los datos en la tabla
			self.lista.setItem(row,0,self.id)
			self.lista.setItem(row,1,self.nombre)
			self.lista.setItem(row,2,self.apellido)
			self.lista.setItem(row,3,self.cedula)
			self.lista.setItem(row,4,self.rol)
			self.lista.setItem(row,5,self.carrera)

			row+=1
		# Cerramos la conexion a la db
		self.con.commit()
		self.con.close()

	def actualizar(self):
		self.columna = self.lista.currentColumn()
		self.fila = self.lista.currentRow()
		self.id = self.lista.item(self.fila,0).text()