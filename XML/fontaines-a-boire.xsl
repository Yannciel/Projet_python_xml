<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    exclude-result-prefixes="xs"
    version="2.0">
    <xsl:template match="/">
        <html>
            <head>
                <title>Fontaines Potables A Paris</title>
                <meta charset="utf-8"/>
                <link rel="stylesheet" type="text/css" href="fontaines-a-boire.css"></link>
            </head>
            <body>
                <div>
                    <h2>Données brutes utilisées dans ce projet</h2>
                    <table align="center">
                        <tr>
                            <th>Fontaines</th>
                            <th>Géo-point de fontaines</th>
                            <th>Id de fontaines</th>
                            <th>Localisation</th>
                            <th>Adresse</th>
                            <th>Arrondissement</th>
                            <th>Modèle</th>
                            <th>Nombre de fontaines</th>
                            <th>Ouverture en hiver</th>
                            <th>En service</th>
                            <th>Commentaire</th>
                            <th>Potable</th>
                        </tr>
                        <xsl:for-each select="Fontaines/fontaine">
                            <tr>
                                <td>
                                    <xsl:value-of select="./@id"/>
                                </td>
                                <td>
                                    <xsl:value-of select="geo_point"/>
                                </td>
                                <td>
                                    <xsl:value-of select="id"/>
                                </td>
                                <td>
                                    <xsl:value-of select="localisati"/>
                                </td>
                                <td>
                                    <xsl:value-of select="adr_s"/>
                                </td>
                                <td>
                                    <xsl:value-of select="arro"/>
                                </td>
                                <td>
                                    <xsl:value-of select="modele"/>
                                </td>
                                <td>
                                    <xsl:value-of select="nb"/>
                                </td>
                                <td>
                                    <xsl:value-of select="ouv_hiver"/>
                                </td>
                                <td>
                                    <xsl:value-of select="en_service"/>
                                </td>
                                <td>
                                    <xsl:value-of select="comm"/>
                                </td>
                                <td>
                                    <xsl:if test="./a_boire/text()=1">
                                        Oui
                                    </xsl:if>
                                    <xsl:if test="./a_boire/text()=0">
                                        Non
                                    </xsl:if>
                                </td>
                            </tr>
                        </xsl:for-each>
                    </table>
                </div>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>