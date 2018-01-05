#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############
###SYNOPSIS####
###############
#
#Auteur :  Mingqiang Wang & Guanhua WANG
#
#Date : 01/01/[18]
#
#Mise à jour : 
#
#But : Transformer une fiche fontaine à boire xml en html selon l'arrodissment
#
#Usage : python3 xml2html_arro.py
#
#Exemple : /
#
#Remarques :  fichier avec  
#							- Nom : fontaines-a-boire.xml
#							- <autres élèments> :
###############

from lxml import etree
from collections import defaultdict
import os 

FICHIER = os.path.join('..','data','XML','fontaines-a-boire.xml')
tree = etree.parse(FICHIER)

Aroo_Aboire= tree.xpath("//arro|//a_boire")

Aroo_Aboiredict=defaultdict(list)

Aroo_Aboirelist=[]
for c in Aroo_Aboire:
    Aroo_Aboirelist.append(c.text)
    
for i in range(len(Aroo_Aboirelist)):
    if i%2==0:
        c=i
    else:
        b=i
        Aroo_Aboiredict[Aroo_Aboirelist[c]].append(Aroo_Aboirelist[b])

with open(os.path.join('..','web','html','tableau_fontaine_arro.html'),'w') as f:
    f.write("<!DOCTYPE html><html><head><title>Tableau Fontaine Potable</title><link rel=\"stylesheet\" type=\"text/css\" href=\"../css/fontaines-a-boire.css\"></head><body>")
    f.write("<body><table border=\"1\" align=\"center\"><tr>")
    f.write("<th class=\"cat\" style=\"font-size:20px\">Arroddisment</th>")
    f.write("<th class=\"cat\" style=\"font-size:20px\">Nombre Potable</th>")
    f.write("<th class=\"cat\" style=\"font-size:20px\">Non Potable</th>")
    f.write("<th class=\"cat\" style=\"font-size:20px\">Nombre total</th></tr>")
    for arr in sorted(Aroo_Aboiredict.keys()):
        f.write("<tr>")
        f.write("<td align=\"center\">{}</td>".format(arr))
        f.write("<td align=\"center\">{}</td>".format(Aroo_Aboiredict[arr].count('1')))
        f.write("<td align=\"center\">{}</td>".format(Aroo_Aboiredict[arr].count('0')))
        f.write("<td align=\"center\">{}</td>".format(Aroo_Aboiredict[arr].count('0')+Aroo_Aboiredict[arr].count('1')))
        f.write("</tr>")
    f.write("</table>")
    f.write("</body></html>")


