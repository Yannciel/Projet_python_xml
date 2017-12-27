#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############
###SYNOPSIS####
###############
#
#Auteur : Mingqiang Wang
#
#Date : 21/12/[17]
#
#Mise à jour : 
#
#But : Transformer une fiche tournage de film csv en xml
#
#Usage : python3 csv2xml.py
#
#Exemple : /
#
#Remarques :  fichier avec  
#							- Nom : 
#							- <autres élèments> :
###############


with open("fontaines-a-boire.csv","r") as f:
	b=f.readline().rstrip().lower().split(";")[0:]
	with open("fontaines-a-boire.xml","w") as fi:
		fi.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n")
		fi.write("<!DOCTYPE Root SYSTEM \"Fontaines.dtd\">\n")
		fi.write("<Fontaines>\n")
		i=0
		b[0]=b[0].replace(" ","_")
		for line in f:
			t=line.rstrip().split(";")[0:]
			try:
				i+=1
				fi.write("<fontaine id=\"{}\">\n".format(i))
				fi.write("<{}>{}</{}>\n".format(b[0],t[0],b[0]))
				fi.write("<{}>{}</{}>\n".format(b[2],t[2],b[2]))
				fi.write("<{}>{}</{}>\n".format(b[5],t[5],b[5]))
				fi.write("<{}>{}</{}>\n".format(b[6],t[6],b[6]))
				fi.write("<{}>{}</{}>\n".format(b[8],t[8],b[8]))
				fi.write("<{}>{}</{}>\n".format(b[9],t[9],b[9]))
				fi.write("<{}>{}</{}>\n".format(b[10],t[10],b[10]))
				fi.write("<{}>{}</{}>\n".format(b[14],t[14],b[14]))
				fi.write("<{}>{}</{}>\n".format(b[16],t[16],b[16]))
				fi.write("<{}>{}</{}>\n".format(b[17],t[17],b[17]))	
				fi.write("<{}>{}</{}>\n".format(b[30],t[30],b[30]))
				fi.write("</fontaine>")
				fi.write("\n")
			except IndexError:
				print("La ligne {} n'a pas assez d'intervalles".format(i))		

		fi.write("</Fontaines>")
