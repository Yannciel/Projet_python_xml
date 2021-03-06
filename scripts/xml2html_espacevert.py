#!usr/bin/env python3
#coding=utf-8
###############
###SYNOPSIS####
###############
#
#Auteur : Mingqiang Wang & Guanhua WANG
#
#Date : 31/12/[17]
#
#Mise à jour : 
#
#But : PTransformer une fiche espace vert xml en html
#
#Usage : python3 xml2html_espacevert.py
#
#Exemple : /
#
#Remarques :  fichier avec  
#							- Nom : parcsetjardinsparis2010.xml
#							- <autres élèments> :
###############

from lxml import etree
import os

FICHIER = os.path.join('..','data','XML','parcsetjardinsparis2010.xml')

tree = etree.parse(FICHIER)
root = tree.getroot()

sortie =''
with open(os.path.join('..','web','html','tableau_espacevert.html'),'w') as f:
	sortie += "<!DOCTYPE html>\n<html>\n<head>\n<title>Tableau des espaces verts Paris</title>\n<meta charset=\"utf-8\"/>\n<link rel=\"stylesheet\" type=\"text/css\" href=\"../css/fontaines-a-boire.css\"/>\n</head>\n<body>\n"
	sortie += '<h2>{}</h2>\n<table align=\"center\">\n'.format("Tableau des espaces verts Paris")
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
