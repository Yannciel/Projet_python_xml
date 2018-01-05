<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    exclude-result-prefixes="xs"
    version="2.0">
    <xsl:template match="/">
        <html>
            <head>
                <title>Projet XML</title>
                <meta charset="UTF-8"/>
                <meta name="viewport" content="width=device-width, initial-scale=1" />
                <link rel="stylesheet" href="../css/main.css"/>
                <link href="https://fonts.googleapis.com/css?family=Nunito:700" rel="stylesheet"/>
            </head>
            <body>
                <!-- Sidebar -->
                <section id="sidebar">
                    <div class="inner">
                        <nav>
                            <ul>
                                <li><a href="#intro">PROJET</a></li>
                                <li><a href="#one">PRÉSENTATION</a></li>
                                <li><a href="#two">Méthodes &amp; Étapes</a></li>
                                <li><a href="#three">Analyse</a></li>
                            </ul>
                        </nav>
                    </div>
                </section>
                
                <!-- Wrapper -->
                <div id="wrapper">
                    
                    <!-- Intro -->
                    <section id="intro" class="wrapper style1 fullscreen fade-up">
                        <div class="inner">
                            <h1>Projet XML</h1>
                            <p><xsl:value-of select="PROJET/sujet"/></p>
                        </div>
                    </section>
                    
                    <!-- One -->
                    <section id="one" class="wrapper style2 spotlights">
                        <section>
                            <img src="../images/pic01.jpg" alt="" data-position="center center" />
                            <div class="content">
                                <div class="inner">
                                    <xsl:apply-templates select="PROJET/presentation"/>
                                </div>
                            </div>
                        </section>
                    </section>
                    
                    <!-- Two -->
                    <section id="two" class="wrapper style3 fade-up">
                        <div class="inner">
                            <xsl:apply-templates select="PROJET/etapes"/>
                        </div>
                    </section>
                    
                    <!-- Three -->
                    <section id="three" class="wrapper style1 fade-up">
                        <div class="inner">
                            <xsl:apply-templates select="PROJET/analyse"/>
                        </div>
                    </section>
                    
                </div>
                
                <!-- Footer -->
                <footer id="footer" class="wrapper style1-alt">
                    <div class="inner">
                        <ul class="menu">
                            <li>Projet XML. All rights reserved @ INALCO M2 TAL IM</li><li>Guanhua WANG &amp; Mingqiang WANG</li>
                        </ul>
                    </div>
                </footer>
                
                <!-- Scripts -->
                <script src="../js/jquery.min.js"></script>
                <script src="../js/jquery.scrollex.min.js"></script>
                <script src="../js/jquery.scrolly.min.js"></script>
                <script src="../js/skel.min.js"></script>
                <script src="../js/util.js"></script>
                <!--[if lte IE 8]><script src="assets/js/ie/respond.min.js"></script><![endif]-->
                <script src="../js/main.js"></script>
                
            </body>
        </html>
    </xsl:template>
    <xsl:template match="PROJET/presentation">
        <h2>
            <xsl:value-of select="titre"/>
        </h2>
        <xsl:for-each select="introduction">
            <p>
                <xsl:value-of select="."/>
            </p>
        </xsl:for-each>
    </xsl:template>
    <xsl:template match="PROJET/etapes">
        <h2><xsl:value-of select="titre"/></h2>
        <p><xsl:value-of select="intro"/></p>
        <xsl:apply-templates select="structuration"/>
        <xsl:apply-templates select="modelisation"/>
        <xsl:apply-templates select="grammaires"/>
        <xsl:apply-templates select="trans_tablo"/>
        <xsl:apply-templates select="carte"/>
    </xsl:template>
        <xsl:template match="structuration">
            <p class="sous-titre">1. <xsl:value-of select="intro"/></p>
            <p><xsl:value-of select="creation_env"/></p>
            <xsl:apply-templates select="recuperation"/>
            <p><xsl:value-of select="nettoyage"/></p>
        </xsl:template>
            <xsl:template match="recuperation">
                <p><xsl:value-of select="intro"/></p>
                <xsl:apply-templates select="donnees"/>
            </xsl:template>
                <xsl:template match="donnees">
                    <xsl:apply-templates select="origine"/>
                    <xsl:apply-templates select="info_donnees"/>
                </xsl:template>
                    <xsl:template match="origine">
                        <p>
                            <xsl:apply-templates/>
                        </p>
                    </xsl:template>
                        <xsl:template match="origine//*">
                            <xsl:copy>
                                <xsl:copy-of select="@*" />
                                <xsl:apply-templates />
                            </xsl:copy>
                        </xsl:template>
                        <xsl:template match="origine//link">
                            <a href="{@url}"><xsl:apply-templates/></a>
                        </xsl:template>
                        <xsl:template match="text()"/>
                        <xsl:template match="origine//text()">
                            <xsl:copy-of select="." />
                        </xsl:template>
                    <xsl:template match="info_donnees">
                        <p><xsl:value-of select="liste"/></p>
                        <ul class="content">
                            <xsl:for-each select="info">
                                <li><xsl:value-of select="."/></li>
                            </xsl:for-each>
                        </ul>
                    </xsl:template>
        <xsl:template match="modelisation">
            <p class="sous-titre">2. <xsl:value-of select="intro"/></p>
            <p><xsl:value-of select="csv2xml"/></p>
            <xsl:apply-templates select="fichiers"/>
        </xsl:template>
            <xsl:template match="fichiers">
                <ul class="content">
                    <xsl:for-each select="fichier/link">
                        <li><a href="{@url}"><xsl:value-of select="."/></a></li>
                    </xsl:for-each>
                </ul>
            </xsl:template>
        <xsl:template match="grammaires">
            <p class="sous-titre">3. <xsl:value-of select="liste"/></p>
            <ul class="content">
                <xsl:for-each select="fichier">
                    <li><xsl:apply-templates/></li>
                </xsl:for-each>
            </ul>
        </xsl:template>
            <xsl:template match="fichier//*">
                <xsl:copy>
                    <xsl:copy-of select="@*" />
                    <xsl:apply-templates />
                </xsl:copy>
            </xsl:template>
            <xsl:template match="fichier//link">
                <a href="{@url}"><xsl:apply-templates/></a>
            </xsl:template>
            <xsl:template match="text()"/>
            <xsl:template match="fichier//text()">
                <xsl:copy-of select="."/>
            </xsl:template>
        <xsl:template match="trans_tablo">
            <p class="sous-titre">4. <xsl:value-of select="liste"/></p>
            <xsl:apply-templates select="xml2html"/>
            <xsl:apply-templates select="tableaux"/>
        </xsl:template>
            <xsl:template match="xml2html">
                <p><xsl:value-of select="intro"/></p>
                <ul class="content">
                    <xsl:for-each select="fichier">
                        <li><xsl:apply-templates/></li>
                    </xsl:for-each>
                </ul>
            </xsl:template>
        <xsl:template match="tableaux">
            <ul class="content">
                <xsl:for-each select="tablo">
                    <li><xsl:apply-templates/></li>
                </xsl:for-each>
            </ul>
        </xsl:template>
            <xsl:template match="tablo//*">
                <xsl:copy>
                    <xsl:copy-of select="@*" />
                    <xsl:apply-templates />
                </xsl:copy>
            </xsl:template>
            <xsl:template match="tablo//link">
                <a href="{@url}"><xsl:apply-templates/></a>
            </xsl:template>
            <xsl:template match="text()"/>
            <xsl:template match="tablo//text()">
                <xsl:copy-of select="."/>
            </xsl:template>
        <xsl:template match="carte">
            <p class="sous-titre">5. <xsl:value-of select="intro"/></p>
            <xsl:apply-templates select="fichiers"/>
        </xsl:template>
            <xsl:template match="fichiers">
                <xsl:for-each select="fichier">
                    <li><xsl:apply-templates/></li>
                </xsl:for-each>
            </xsl:template>
    <xsl:template match="analyse">
        <h2><xsl:value-of select="intro"/></h2>
        <xsl:for-each select="*">
            <xsl:choose>
                <xsl:when test="name()='img'">
                    <img id="{@id}" src="{@url}"/>
                </xsl:when>
                <xsl:otherwise>
                    <p><xsl:value-of select="."/></p>
                </xsl:otherwise>
            </xsl:choose>
        </xsl:for-each>
    </xsl:template>
</xsl:stylesheet>