#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Sistema de carnetizacion hecho en python y SQLite3
# Desarrollado por Rafnix Guzman @rafnixg 
# http://rafnixg.github.io/

import sys, sqlite3
from PyQt4 import QtCore, QtGui, uic
from registrar import Registrar
from ver import Ver
from carnets import Carnet

# Cargo los UI de cada uno de los forms
form_principal = uic.loadUiType("principal.ui")[0]

# Creo la clase del from principal
class Principal(QtGui.QMainWindow, form_principal):
	
	def __init__(self,parent=None):
		QtGui.QMainWindow.__init__(self,parent)
		self.setupUi(self)
		
		# Creacion y vinculacion del widget Registrar
		self.registrar_w = Registrar(self)
		self.action_Registrar.triggered.connect(self.menuRegistrar)
		self.central_widget.addWidget(self.registrar_w)

		# Creacion y vinculacion del widget Ver
		self.ver_w = Ver(self)
		self.action_Ver_Todos.triggered.connect(self.menuVer)
		self.central_widget.addWidget(self.ver_w)

		# Vinculacion del boton Generar
		self.action_Generar_Todos.triggered.connect(self.menuGenerar)

		# Mensajes del status bar
		self.statusBar().showMessage(u"Bienvenid@ al Sistema de Carnetización")
		self.action_Generar_Todos.setStatusTip(u"Generar todos los carnets")
		self.action_Ver_Todos.setStatusTip(u"Ver todos los registrados")
		self.action_Registrar.setStatusTip(u"Registrar nuevos usuarios")
		self.registrar_w.btn_cargar_foto.setStatusTip(u"Cargar foto el usuario")
		self.registrar_w.btn_registrar.setStatusTip(u"Guardar el usuario en la base de datos")

		self.inicio()

	# Inicializando la db
	def inicio(self):
		self.con = sqlite3.connect('db/carnets.db')
		self.cursor = self.con.cursor()
		self.cursor.execute(""" CREATE TABLE IF NOT EXISTS Usuarios(id	INTEGER PRIMARY KEY AUTOINCREMENT,nombre	TEXT NOT NULL,apellido	TEXT NOT NULL,cedula	TEXT NOT NULL,carrera	TEXT NOT NULL,foto	TEXT NOT NULL,rol TEXT NOT NULL) """)
		self.con.commit()

	# Manejador del evento click para el item del menu (registrar)
	def menuRegistrar(self):
		self.central_widget.setCurrentWidget(self.registrar_w)

	# Manejador del evento click para el item del menu (Ver)
	def menuVer(self):
		self.central_widget.setCurrentWidget(self.ver_w)

	# Manejador del evento click para el item del menu (Generar)
	def menuGenerar(self):
		self.carnet = Carnet()
		self.con = sqlite3.connect('db/carnets.db')
		self.cursor = self.con.cursor() 

		# Cargo los datos de la db
		self.cursor.execute("SELECT id, nombre, apellido, cedula, rol, carrera, foto FROM Usuarios")

		for i in self.cursor:
			
			self.id = i[0]
			self.nombre = i[1]
			self.apellido = i[2]
			self.cedula = i[3]
			self.rol = i[4]
			self.carrera = i[5]
			self.foto = i[6]

			self.carnet.generar(self.nombre+" "+self.apellido,self.cedula,self.foto,self.rol,self.carrera,"Feb del 2016")

		print 'Genero las imagenes'

if __name__ == '__main__':
	app = QtGui.QApplication([])
	window = Principal()
	window.show()
	app.exec_()