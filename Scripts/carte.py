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
import MY_KEY
FICHIER = 'fontaines-a-boire.xml'
tree = etree.parse(FICHIER)
geo=tree.xpath("//geo_point")
geo_list=[]
for i in geo:
    geo_list.append(i.text)

my_key=mykey.get_key()

with open('carte.html','w') as f:
    f.write("<!DOCTYPE html>\n<html>\n<head>\n<meta name=\"viewport\" content=\"initial-scale=1.0, user-scalable=no\">\n<meta charset=\"utf-8\">\n<title>Cartes -- Fontaines à Paris</title>\n<style>#map {height: 100%;}html, body {height: 100%; margin: 0; padding: 0;} </style>\n</head>\n<body> \n <div id=\"map\"></div> \n<script> function initMap() {\n  var map = new google.maps.Map(document.getElementById(\'map\'), {\n zoom: 12,\n  center: {lat: 48.872, lng: 2.2999} }\n);\n var labels = \'ABCDEFGHIJKLMNOPQRSTUVWXYZ\';\n  var markers = locations.map(function(location, i) {\n  return new google.maps.Marker({ \n  position: location,\n  label: labels[i % labels.length] \n });\n });\n var markerCluster = new MarkerClusterer(map, markers,\n {imagePath: \'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m\'});\n}\n")
    with open('fontaines-a-boire.xml','r') as file:
        f.write("var locations = [\n")
        for g in geo_list:
            lat,lng=g.split(",")
            f.write("{lat: %s, lng: %s},\n" %(lat,lng)) 
    f.write("]\n</script>")
    f.write(" \n<script src=\"https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/markerclusterer.js\">\n</script>\n</script>\n<script async defer\n src=\"https://maps.googleapis.com/maps/api/js?key=%s&callback=initMap\">\n</script>\n</body>\n</html>" %(my_key))