#!usr/bin/env python3
#coding=utf-8
from lxml import etree

FICHIER = '../XML/zones-touristiques-internationales.xml'

tree = etree.parse(FICHIER)
root = tree.getroot()

print("<!DOCTYPE html>\n<html>\n<head>\n<title>Tableau des Zones touristiques Paris</title>\n<meta charset=\"utf-8\"/>\n<link rel=\"stylesheet\" type=\"text/css\" href=\"../css/fontaines-a-boire.css\"/>\n</head>\n<body>\n")
print('<h2>{}</h2>\n<table align=\"center\">\n'.format("Tableau des Zones touristiques Paris"))
print('<tr><th>ID</th>')

# Extraire les balises dans /tournages/tournage/*/name()
for c in root[0]:
    if not c.tag == "geo_shape":
        print('<th>{}</th>\n'.format(c.tag))
print('</tr>\n')

# Parcourir chaque tournage, récupère l'id et les informations
for child in root:
    print('<tr>\n')
    print('<td>{}</td>\n'.format(child.attrib['id']))
    for c in child:
        if not c.tag == "geo_shape":
            print('<td>{}</td>\n'.format(c.text))
    print('</tr>\n')

print("</table>\n</body>\n</html>")