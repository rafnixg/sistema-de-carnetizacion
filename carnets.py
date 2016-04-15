#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Sistema de carnetizacion hecho en python y SQLite3
# Desarrollado por Rafnix Guzman @rafnixg 
# http://rafnixg.github.io/

from PIL import Image, ImageDraw, ImageFont

class Carnet:
	"""
		Clase que se encarga de tener la configuracion del carnet
		y el metodo que genera la imagen compuesta.
	"""
	fondo = 'img/carnet.png'
	tam_foto = (250,335)
	pos_foto = (382,303)
	fuente = 'font/OpenSans.ttf'
	pos_nombre = (380,730)
	pos_ci = (380,830)
	pos_vence = (380,950)
	pos_rol = (30,450)
	pos_carrera = (30,495)

	def generar(self,nombre,cedula,foto,rol,carrera,vence):

		# Se abren las imagenes de fondo y la foto del usuario
		img = Image.open(self.fondo).convert('RGBA')
		foto = Image.open(foto).convert('RGBA')

		# Cambio el tamaño de la foto del usuario
		foto = foto.resize(self.tam_foto)

		# Se definen las fuentes y los tamaños
		fnt = ImageFont.truetype(self.fuente,18)
		fnt_rol = ImageFont.truetype(self.fuente,30)
		fnt_carrera = ImageFont.truetype(self.fuente,26)

		# Se combinan las 2 imagenes.
		img.paste(foto,self.pos_foto,foto)

		# Se prepara el area de dibujo
		draw = ImageDraw.Draw(img)

		# Se dibujan los textos
		draw.text(self.pos_nombre,nombre,font=fnt,fill=(60,57,55,255))
		draw.text(self.pos_ci,cedula,font=fnt,fill=(60,57,55,255))
		draw.text(self.pos_vence,vence,font=fnt,fill=(60,57,55,255))
		draw.text(self.pos_rol,rol,font=fnt_rol,fill=(60,57,55,255))
		draw.text(self.pos_carrera,carrera,font=fnt_carrera,fill=(60,57,55,255))

		# Se guarda la imagen final
		img.save("img/carnets/"+nombre+"-"+cedula+".png")