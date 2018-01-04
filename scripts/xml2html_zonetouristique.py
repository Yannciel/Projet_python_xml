#!usr/bin/env python3
#coding=utf-8
###############
###SYNOPSIS####
###############
#
#Auteur : Mingqiang Wang & Guanhua WANG
#
#Date : 30/01/[18]
#
#Mise à jour : 
#
#But : PTransformer une fiche zone touristique xml en html
#
#Usage : python3 xml2html_zonetouristique.py
#
#Exemple : /
#
#Remarques :  fichier avec  
#							- Nom : zones-touristiques-internationales.xml
#							- <autres élèments> :
###############

from lxml import etree
import os

FICHIER = os.path.join('..','data','XML','zones-touristiques-internationales.xml')

tree = etree.parse(FICHIER)
root = tree.getroot()

sortie =''
with open(os.path.join('..','web','html','tableau_zonetouristique.html'),'w') as f:
	sortie += "<!DOCTYPE html>\n<html>\n<head>\n<title>Tableau des espaces verts Paris</title>\n<meta charset=\"utf-8\"/>\n<link rel=\"stylesheet\" type=\"text/css\" href=\"../css/fontaines-a-boire.css\"/>\n</head>\n<body>\n"
	sortie += '<h2>{}</h2>\n<table align=\"center\">\n'.format("Tableau des zones touristiques Paris")
	sortie += '<tr><th>ID</th>'

	# Extraire les balises dans /tournages/tournage/*/name()
	for c in root[0]:
	    if not c.tag == "geo_shape":
	        sortie += '<th>{}</th>\n'.format(c.tag)
	sortie += '</tr>\n'

	# Parcourir chaque tournage, récupère l'id et les informations
	for child in root:
	    sortie += '<tr>\n'
	    sortie += '<td>{}</td>\n'.format(child.attrib['id'])
	    for c in child:
	        if not c.tag == "geo_shape":
	            sortie += '<td>{}</td>\n'.format(c.text)
	    sortie += '</tr>\n'

	sortie += "</table>\n</body>\n</html>"
	f.write(sortie)
