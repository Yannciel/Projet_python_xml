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
#But : Transformer le fichier fontaines-a-boire.csv en xml
#
#Usage : python3 csv2xml.py
#
#Exemple : /
#
#Remarques :  fichier avec  
#							- Nom : 
#							- <autres élèments> :
###############


with open("../Data/CSV/zones-touristiques-internationales.csv","r") as f:
	b=f.readline().rstrip().lower().split(";")[0:]
	with open("zones-touristiques-internationales.xml","w") as fi:
		fi.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n")
		fi.write("<!DOCTYPE ZONES SYSTEM \"Zones.dtd\">\n")
		fi.write("<ZONES>\n")
		i=0
		b[0]=b[0].replace(" ","_")
		b[1]=b[1].replace(" ","_")
		for line in f:
			t=line.rstrip().split(";")[0:]
			if len(t)==len(b):
				i+=1
				fi.write("<zone id=\"{}\">\n".format(i))
				fi.write("<{}>{}</{}>\n".format(b[0],t[0],b[0]))
				fi.write("<{}>{}</{}>\n".format(b[1],t[1],b[1]))
				fi.write("<{}>{}</{}>\n".format(b[3],t[3],b[3]))
				fi.write("<{}>{}</{}>\n".format(b[7],t[7],b[7]))
				fi.write("<{}>{}</{}>\n".format(b[10],t[10],b[10]))
				fi.write("</zone>")
				fi.write("\n")

		fi.write("</ZONES>")
