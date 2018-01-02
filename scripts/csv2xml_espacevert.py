#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############
###SYNOPSIS####
###############
#
#Auteur : Mingqiang Wang
#
#Date : 02/01/[18]
#
#Mise à jour : 
#
#But : Transformer une fiche espace vert csv en xml
#
#Usage : python3 csv2xml_espacevert.py
#
#Exemple : /
#
#Remarques :  fichier avec  
#							- Nom : 
#							- <autres élèments> :
###############


with open("parcsetjardinsparis2010.csv","r") as f:
	b=f.readline().rstrip().lower().split(";")[0:]
	with open("parcsetjardinsparis2010.xml","w") as fi:
		fi.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n")
		fi.write("<!DOCTYPE EspaceVert SYSTEM \"EspaceVert.dtd\">\n")
		fi.write("<EspaceVert>\n")
		i=0
		b[0]=b[0].replace(" ","_")
		b[1]=b[1].replace(" ","_")
		b[2]=b[2].replace(" ","_")
		b[3]=b[3].replace(" ","_")
		b[4]=b[4].replace(" ","_")
		b[6]=b[6].replace(" ","_")
		b[9]=b[9].rstrip()
		b[9]=b[9].replace(" ","_")
		b[9]=b[9].replace("(m²)","")
		for line in f:
			t=line.rstrip().split(";")[0:]
			if len(t)==12:
				i+=1
				fi.write("<Espacevert id=\"{}\">\n".format(i))
				fi.write("<{}>{}</{}>\n".format(b[0],t[0],b[0]))
				fi.write("<{}>{}</{}>\n".format(b[1],t[1],b[1]))
				fi.write("<{}>{}</{}>\n".format(b[2],t[2],b[2]))
				fi.write("<{}>{}</{}>\n".format(b[3],t[3],b[3]))
				fi.write("<{}>{}</{}>\n".format(b[4],t[4],b[4]))
				fi.write("<{}>{}</{}>\n".format(b[5],t[5],b[5]))
				fi.write("<{}>{}</{}>\n".format(b[6],t[6],b[6]))
				fi.write("<{}>{}</{}>\n".format(b[7],t[7],b[7]))
				fi.write("<{}>{}</{}>\n".format(b[8],t[8],b[8]))
				fi.write("<{}>{}</{}>\n".format(b[9],t[9],b[9]))	
				fi.write("<{}>{}</{}>\n".format(b[10],t[10],b[10]))
				fi.write("<{}>{}</{}>\n".format(b[11],t[11],b[11]))
				fi.write("</Espacevert>")
				fi.write("\n")

		fi.write("</EspaceVert>")
