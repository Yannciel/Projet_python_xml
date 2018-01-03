#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############
###SYNOPSIS####
###############
#
#Auteur : Mingqiang Wang & Guanhua WANG
#
#Date : 01/01/[18]
#
#Mise à jour : 
#
#But : Projeter des fontaines et espaces verts dans une cartes
#
#Usage : python3 XML2HTML.py
#
#Exemple : /
#
#Remarques :  fichier avec  
#                           - Nom : 
#                           - <autres élèments> :
###############
from lxml import etree as ET
import folium
import os
import json

parcsetjardinsparis2010 = os.path.join('..','data','JSON', 'parcsetjardinsparis2010.geojson')
zones_touristiques_internationales = os.path.join('..','data','JSON', 'zones-touristiques-internationales.geojson')
fontaines_a_boire=os.path.join('..','data','XML','fontaines-a-boire.xml')
carte_zonestouristiques_fontaines=os.path.join('..','web','html','carte_zonestouristiques_fontaines.html')
carte_espacesverts_fontaines=os.path.join('..','web','html','carte_espacesverts_fontaines.html')
def mark_touristes(nomfichier):
    """
    Projection des monuments dans la carte
    Arg: fichier XML de coordonnés des zones touristes
    Retourne: une carte OpenStreetMap
    """
    m = folium.Map(location=[48.87, 2.33],zoom_start=13)

    folium.GeoJson(
        nomfichier,
     name='geojson'
    ).add_to(m)

    folium.LayerControl().add_to(m)
    return  m 



def mark_fontaine(carte,nomfichier):
    """
    Projection de tournages dans une carte OpenStreetMap
    Arg: la carte OpenStreetMap qui a déjà marqué zones touristes, et le fichier XML des fontaines
    """
    tree = ET.parse(nomfichier)
    for elem in tree.xpath('//geo_point'):
        coor = elem.text.rstrip()
        coordinates = coor.split(", ")
        lat = float(coordinates[0])
        lgt = float(coordinates[1])
<<<<<<< HEAD:scripts/geojson_RUN.py
        folium.CircleMarker(location=[lat,lgt],radius=1).add_to(carte)
=======
        fill_color='YlGn'
        folium.CircleMarker(location=[lat, lgt],radius=0.5).add_to(carte)
>>>>>>> 661f44c8c85e00dbe2a6ca0cd4652477ba6f9563:scripts/Projet_carte_Geojson.py
    return carte



print("Projection des zones touristes et toutes les fontaines dans une carte...")
carte_touristesfontaines= mark_fontaine(mark_touristes(zones_touristiques_internationales),fontaines_a_boire)
print("Réussir à créer la carte!")
carte_touristesfontaines.save(carte_zonestouristiques_fontaines)
print("Fin")

print("Projection des zones touristes et toutes les espaces verts dans une carte...")
carte_espacesfontaines= mark_fontaine(mark_touristes(parcsetjardinsparis2010),fontaines_a_boire)
print("Réussir à créer la carte!")
carte_espacesfontaines.save(carte_espacesverts_fontaines)
print("Fin")


