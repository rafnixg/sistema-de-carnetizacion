#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Sistema de carnetizacion hecho en python y SQLite3
# Desarrollado por Rafnix Guzman @rafnixg 
# http://rafnixg.github.io/

import sys, sqlite3
from PyQt4 import QtCore, QtGui, uic

# Cargando el archivo de la interfaz grafica
form_registrar = uic.loadUiType("registrar.ui")[0]

# Clase del form Registrar
class Registrar(QtGui.QWidget,form_registrar):
	def __init__(self,parent=None):
		QtGui.QWidget.__init__(self,parent)
		self.setupUi(self)
		self.imagen =''

		# Manejando los eventos click
		self.btn_registrar.clicked.connect(self.btn_registrar_click)
		self.btn_cargar_foto.clicked.connect(self.btn_cargar_click)

	def btn_registrar_click(self):
		# Abro la conexion a la DB
		self.con = sqlite3.connect('db/carnets.db')
		self.cursor = self.con.cursor()

		# Obtencion de datos
		self.nombre = unicode(self.txt_nombre.text())
		self.apellido = unicode(self.txt_apellido.text())
		self.cedula = str(self.txt_cedula.text())
		self.rol = str(self.comb_rol.currentText())
		self.carrera = unicode(self.comb_carrera.currentText())

		# Validacion de los datos
		if self.nombre == "":
			self.txt_nombre.setStyleSheet("border: 2px solid rgba(255,0,0,120);")
			return False
		else:
			self.txt_nombre.setStyleSheet("border: 2px solid rgba(0,255,0,120);")

		if self.apellido == "":
			self.txt_apellido.setStyleSheet("border: 2px solid rgba(255,0,0,120);")
			return False
		else:
			self.txt_apellido.setStyleSheet("border: 2px solid rgba(0,255,0,120);")

		if self.cedula == "":
			self.txt_cedula.setStyleSheet("border: 2px solid rgba(255,0,0,120);")
			return False
		else:
			self.txt_cedula.setStyleSheet("border: 2px solid rgba(0,255,0,120);")
		
		if self.imagen == "":
			print "mensaje"
			return False

		self.guardarImagen(self.imagen,self.cedula)

		self.datos = (self.nombre, self.apellido, self.cedula, self.carrera, self.rol, "img/fotos/"+self.cedula+".png")
		
		# Insertando los datos en la DB
		self.cursor.execute("INSERT INTO Usuarios(nombre,apellido,cedula,carrera,rol,foto) VALUES (?,?,?,?,?,?)",self.datos)
		self.con.commit()

		# Limpiamos las cajas de texto y devolvemos los estilos
		self.txt_nombre.setStyleSheet("border: 2px solid rgba(0,0,0,80);")
		self.txt_apellido.setStyleSheet("border: 2px solid rgba(0,0,0,80);")
		self.txt_cedula.setStyleSheet("border: 2px solid rgba(0,0,0,80);")

		self.txt_cedula.setText("")
		self.txt_apellido.setText("")
		self.txt_nombre.setText("")
		self.l_img.clear()

		# Cerrando la conexion
		self.con.close()

	def btn_cargar_click(self):
		# Cargamos la foto
		self.filename = QtGui.QFileDialog.getOpenFileName(self,'Abrir Imagen','.','Archivos de Imagenes (*.jpg *.png *.bmp)')
		if self.filename == "":
			return False
		self.img = QtGui.QPixmap(self.filename)
		self.l_img.setPixmap(self.img.scaled(140,170,2))
		self.imagen = self.filename

	def guardarImagen(self,ruta,nombre):
		# Guardamos la imagen
		self.imgOriginal = open(ruta)
		self.imgCopia = open('img/fotos/'+nombre+'.png','w')
		self.imgCopia.write(self.imgOriginal.read())
		self.imgOriginal.close()
		self.imgCopia.close()
