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
#							- Nom : 
#							- <autres élèments> :
###############

from lxml import etree as ET
import folium

def mark_touristes(nomfichier):
    """
    Projection des monuments dans la carte
    Arg: fichier XML de coordonnés des zones touristes
    Retourne: une carte OpenStreetMap
    """
    carte_touristes = folium.Map(location=[48.87, 2.33],zoom_start=13)
    tree = ET.parse(nomfichier)

    for elem in tree.iter(tag='zone'):
        name = elem.find('name').text
        coor= elem.find('geo_point').text
        folium.CircleMarker(location=[coor],radius=200,fill_color='#3186cc',popup=name).add_to(carte_touristes)
    return carte_touristes


def mark_fontaine(carte,nomfichier):
    """
    Projection de tournages dans une carte OpenStreetMap
    Arg: la carte OpenStreetMap qui a déjà marqué zones touristes, et le fichier XML des fontaines
    """
    tree = ET.parse(nomfichier)
    for elem in tree.iter(tag = 'fontaine'):
        coor = elem.find('geo_point').text
        folium.CircleMarker(location=[coor],radius=1).add_to(carte)
    return carte


print("Projection des zones touristes et toutes les fontaines dans une carte...")
carte_touristesfontaines= mark_fontaine(mark_touristes("../xml/zones-touristiques-internationales.xml"),"../xml/fontaines-a-boire.xml")
print("Réussir à créer la carte!")
carte_touristesfontaines.save('../cartes/carte_zonestouristiques_fontaines.html')
print("Fin")
