#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############
###SYNOPSIS####
###############
#
#Auteur : Mingqiang Wang
#
#Date : 31/12/[17]
#
#Mise à jour : 
#
#But : Transformer une fiche fontaine à boire xml en html
#
#Usage : python3 carte.py
#
#Exemple : /
#
#Remarques :  fichier avec  
#							- Nom : 
#							- <autres élèments> :
###############
from lxml import etree
FICHIER = 'fontaines-a-boire.xml'
tree = etree.parse(FICHIER)
geo=tree.xpath("//geo_point")
geo_list=[]
for i in geo:
	geo_list.append(i.text)
sortie=""
with open('carte_nombrefontaines.html','w') as f:
	sortie += "<!DOCTYPE html>\n<html>\n<head>\n"
	sortie += "<meta name=\"viewport\" content=\"initial-scale=1.0, user-scalable=no\">\n"
	sortie += "<meta charset=\"utf-8\">\n"
	sortie += "<title>Cartes -- Fontaines à Paris</title>\n"
	sortie += "<style>#map {height: 100%;}html, body {height: 100%; margin: 0; padding: 0;} </style>\n"
	sortie += "</head>\n<body> \n <div id=\"map\"></div> \n"
	sortie += "<script> function initMap() {\n"
	sortie += "var map = new google.maps.Map(document.getElementById(\'map\'), {\n zoom: 12,\n  center: {lat: 48.872, lng: 2.2999}\n"
	sortie += "});\n"
	sortie += "var labels = \'ABCDEFGHIJKLMNOPQRSTUVWXYZ\';\n"
	sortie += "var markers = locations.map(function(location, i) {\n"
	sortie += "return new google.maps.Marker({ \n"
	sortie += "position: location,\n  label: labels[i % labels.length] \n });\n });\n"
	sortie += "var markerCluster = new MarkerClusterer(map, markers,\n"
	sortie += " {imagePath: \'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m\'});\n}\n"

	with open('fontaines-a-boire.xml','r') as file:
		sortie += "var locations = [\n"
		for g in geo_list:
			lat,lng=g.split(",")
			sortie += "{lat: %s, lng: %s},\n" %(lat,lng)
	sortie += "]\n</script>\n"
	sortie += "<script src=\"https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/markerclusterer.js\">\n</script>\n"
	sortie += "</script>\n<script async defer\n"
	sortie += "src=\"https://maps.googleapis.com/maps/api/js?key=AIzaSyCUOQCIU1RWnaSlI93bCFQK47yR4yUKAww&callback=initMap\">\n"
	sortie += "</script>\n</body>\n</html>" 
	f.write(sortie)

		