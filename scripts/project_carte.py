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

from lxml import etree
import folium
FICHIER = '../XML/fontaines-a-boire.xml'
tree = etree.parse(FICHIER)

def mark_fontaine(carte,nomfichier):
    """
    Projection de tournages dans une carte OpenStreetMap
    Arg: la carte OpenStreetMap qui a déjà marqué les monuments, et le fichier XML des films
    """
    tree = ET.parse(nomfichier)
    for elem in tree.iter(tag = 'fontaine'):
        coor = elem.find('geo_point').text
        folium.CircleMarker(location=[coor],radius=1).add_to(carte)
    return carte

    