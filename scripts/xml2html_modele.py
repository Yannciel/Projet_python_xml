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
#But : PTransformer une fiche fontaine à boire xml en html selon leur modèle
#
#Usage : python3 xml2html_modle.py
#
#Exemple : /
#
#Remarques :  fichier avec  
#                           - Nom : fontaines-a-boire.xml
#                           - <autres élèments> :
###############
from lxml import etree
from collections import defaultdict
import os

file = os.path.join('..','data','XML',"fontaines-a-boire.xml")
tree = etree.parse(file)
modele = tree.xpath("//modele|//a_boire")
modele_dict = defaultdict(list)
modele_list = []


for m in modele:
	modele_list.append(m.text)

for i in range(len(modele_list)):
	if i%2 == 0:
		m = i
	else:
		n = i
		modele_dict[modele_list[m]].append(modele_list[n])

with open(os.path.join('..','web','html','tableau_modele.html'),'w') as f:
    f.write("<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<title>Tableau Fontaine Potable</title>\n\t\t<link rel=\"stylesheet\" type=\"text/css\" href=\"../css/fontaines-a-boire.css\">\n\t</head>\n\t<body>\n\t\t")
    f.write("<table align=\"center\">\n\t\t\t<tr>\n\t\t\t\t")
    f.write("<th>Modèle</th>\n\t\t\t\t")
    f.write("<th>Nombre Potable</th>\n\t\t\t\t")
    f.write("<th>Non Potable</th>\n\t\t\t</tr>\n\t\t\t")
    for mod in modele_dict:
        f.write("<tr>\n\t\t\t\t")
        f.write("<td>{}</td>\n\t\t\t\t".format(mod))
        f.write("<td>{}</td>\n\t\t\t\t".format(modele_dict[mod].count('1')))
        f.write("<td>{}</td>\n\t\t\t".format(modele_dict[mod].count('0')))
        f.write("</tr>\n\t\t\t")
    f.write("</table>\n\t")
    f.write("</body>\n</html>")