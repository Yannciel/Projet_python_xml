#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############
###SYNOPSIS####
###############
#
#Auteur : Mingqiang Wang & Guanhua WANG
#
#Date : 02/01/[18]
#
#Mise à jour : 
#
#But : Transformer une fiche zone touristique csv en xml
#
#Usage : python3 csv2xml_zonetouristiques.py
#
#Exemple : /
#
#Remarques :  fichier avec  
#							- Nom : zones-touristiques-internationales.csv
#							- <autres élèments> :
###############
import os 

with open(os.path.join('..','data','CSV',"zones-touristiques-internationales.csv"),"r") as f:
	b=f.readline().rstrip().lower().split(";")[0:]
	with open(os.path.join('..','data','XML',"zones-touristiques-internationales.xml"),"w") as fi:
		fi.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n")
		fi.write("<!DOCTYPE ZONES SYSTEM \"zones-touristiques-internationales.dtd\">\n")
		fi.write("<ZONES>\n")
		i=0
		b[0]=b[0].replace(" ","_")
		b[1]=b[1].replace(" ","_")
		for line in f:
			t=line.rstrip().split(";")[0:]
			if len(t)==12:
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
