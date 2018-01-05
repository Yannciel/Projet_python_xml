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
                <meta name="viewport" content="width=device-width, initial-scale=1"/>
                <link href='http://fonts.googleapis.com/css?family=PT+Sans:400,700|Merriweather:400italic,400' rel='stylesheet' type='text/css'/>
                <link rel="stylesheet" href="../css/reset.css"/> <!-- CSS reset -->
                <link rel="stylesheet" href="../css/style.css"/> <!-- Resource style -->
                <script src="../js/modernizr.js"></script> <!-- Modernizr -->
                <link href="https://fonts.googleapis.com/css?family=Nunito:700" rel="stylesheet"/>
            </head>
            <body>
                <a class="cd-nav-trigger cd-text-replace" href="#primary-nav">Menu<span aria-hidden="true" class="cd-icon"></span></a>
                
                <div class="cd-projects-container">
                    <ul class="cd-projects-previews">
                        <li>
                            <a href="#0">
                                <div class="cd-project-title">
                                    <h2>Présentation du projet</h2>
                                </div>
                            </a>
                        </li>
                        
                        <li>
                            <a href="#0">
                                <div class="cd-project-title">
                                    <h2>Méthodes &amp; Étapes</h2>
                                </div>
                            </a>
                        </li>
                        
                        <li>
                            <a href="#0">
                                <div class="cd-project-title">
                                    <h2>Analyse &amp; Difficultés</h2>
                                </div>
                            </a>
                        </li>
                        
                        <li>
                            <a href="#0">
                                <div class="cd-project-title">
                                    <h2>Auto-complétion Python</h2>
                                </div>
                            </a>
                        </li>
                    </ul> <!-- .cd-projects-previews -->
                    
                    <ul class="cd-projects">
                        <li>
                            <div class="preview-image">
                                <div class="cd-project-title">
                                    <h2>Présentation du projet</h2>
                                </div> 
                            </div>
                            
                            <div class="cd-project-info">
                                <xsl:apply-templates select="PROJET/presentation"/>
                            </div> <!-- .cd-project-info -->
                        </li>
                        
                        <li>
                            <div class="preview-image">
                                <div class="cd-project-title">
                                    <h2>Méthodes &amp; Étapes</h2>
                                </div> 
                            </div>
                            
                            <div class="cd-project-info">
                                <xsl:apply-templates select="PROJET/etapes"/>
                            </div> <!-- .cd-project-info -->
                        </li>
                        
                        <li>
                            <div class="preview-image">
                                <div class="cd-project-title">
                                    <h2>Project 3</h2>
                                    <p>Brief description of the project here</p>
                                </div> 
                            </div>
                            
                            <div class="cd-project-info">
                                <p>
                                    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minima, quod dicta aliquid nemo repellendus distinctio minus dolor aperiam suscipit, ea enim accusantium, deleniti qui sequi sint nihil modi amet eligendi, quidem animi error labore voluptatibus sed. Qui magnam labore, iusto nostrum. Praesentium non, impedit accusantium consequatur officia architecto, mollitia placeat aperiam tenetur pariatur voluptatibus corrupti vitae deserunt! Nostrum non mollitia deserunt ipsam. Sunt quaerat natus cupiditate iure ipsa voluptatibus recusandae ratione vitae amet distinctio, voluptas, minus vero expedita ea fugit similique sit cumque ad id facere? Ab quas, odio neque quis ratione. Natus labore sit esse, porro placeat eum hic.
                                    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minima, quod dicta aliquid nemo repellendus distinctio minus dolor aperiam suscipit, ea enim accusantium, deleniti qui sequi sint nihil modi amet eligendi, quidem animi error labore voluptatibus sed. Qui magnam labore, iusto nostrum. Praesentium non, impedit accusantium consequatur officia architecto, mollitia placeat aperiam tenetur pariatur voluptatibus corrupti vitae deserunt! Nostrum non mollitia deserunt ipsam. Sunt quaerat natus cupiditate iure ipsa voluptatibus recusandae ratione vitae amet distinctio, voluptas, minus vero expedita ea fugit similique sit cumque ad id facere? Ab quas, odio neque quis ratione. Natus labore sit esse, porro placeat eum hic.
                                    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minima, quod dicta aliquid nemo repellendus distinctio minus dolor aperiam suscipit, ea enim accusantium, deleniti qui sequi sint nihil modi amet eligendi, quidem animi error labore voluptatibus sed. Qui magnam labore, iusto nostrum. Praesentium non, impedit accusantium consequatur officia architecto, mollitia placeat aperiam tenetur pariatur voluptatibus corrupti vitae deserunt! Nostrum non mollitia deserunt ipsam. Sunt quaerat natus cupiditate iure ipsa voluptatibus recusandae ratione vitae amet distinctio, voluptas, minus vero expedita ea fugit similique sit cumque ad id facere? Ab quas, odio neque quis ratione. Natus labore sit esse, porro placeat eum hic.
                                    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minima, quod dicta aliquid nemo repellendus distinctio minus dolor aperiam suscipit, ea enim accusantium, deleniti qui sequi sint nihil modi amet eligendi, quidem animi error labore voluptatibus sed. Qui magnam labore, iusto nostrum. Praesentium non, impedit accusantium consequatur officia architecto, mollitia placeat aperiam tenetur pariatur voluptatibus corrupti vitae deserunt! Nostrum non mollitia deserunt ipsam. Sunt quaerat natus cupiditate iure ipsa voluptatibus recusandae ratione vitae amet distinctio, voluptas, minus vero expedita ea fugit similique sit cumque ad id facere? Ab quas, odio neque quis ratione. Natus labore sit esse, porro placeat eum hic.
                                </p>
                            </div> <!-- .cd-project-info -->
                        </li>
                        
                        <li>
                            <div class="preview-image">
                                <div class="cd-project-title">
                                    <h2>Project 4</h2>
                                    <p>Brief description of the project here</p>
                                </div> 
                            </div>
                            
                            <div class="cd-project-info">
                                <p>
                                    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minima, quod dicta aliquid nemo repellendus distinctio minus dolor aperiam suscipit, ea enim accusantium, deleniti qui sequi sint nihil modi amet eligendi, quidem animi error labore voluptatibus sed. Qui magnam labore, iusto nostrum. Praesentium non, impedit accusantium consequatur officia architecto, mollitia placeat aperiam tenetur pariatur voluptatibus corrupti vitae deserunt! Nostrum non mollitia deserunt ipsam. Sunt quaerat natus cupiditate iure ipsa voluptatibus recusandae ratione vitae amet distinctio, voluptas, minus vero expedita ea fugit similique sit cumque ad id facere? Ab quas, odio neque quis ratione. Natus labore sit esse, porro placeat eum hic.
                                    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minima, quod dicta aliquid nemo repellendus distinctio minus dolor aperiam suscipit, ea enim accusantium, deleniti qui sequi sint nihil modi amet eligendi, quidem animi error labore voluptatibus sed. Qui magnam labore, iusto nostrum. Praesentium non, impedit accusantium consequatur officia architecto, mollitia placeat aperiam tenetur pariatur voluptatibus corrupti vitae deserunt! Nostrum non mollitia deserunt ipsam. Sunt quaerat natus cupiditate iure ipsa voluptatibus recusandae ratione vitae amet distinctio, voluptas, minus vero expedita ea fugit similique sit cumque ad id facere? Ab quas, odio neque quis ratione. Natus labore sit esse, porro placeat eum hic.
                                    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minima, quod dicta aliquid nemo repellendus distinctio minus dolor aperiam suscipit, ea enim accusantium, deleniti qui sequi sint nihil modi amet eligendi, quidem animi error labore voluptatibus sed. Qui magnam labore, iusto nostrum. Praesentium non, impedit accusantium consequatur officia architecto, mollitia placeat aperiam tenetur pariatur voluptatibus corrupti vitae deserunt! Nostrum non mollitia deserunt ipsam. Sunt quaerat natus cupiditate iure ipsa voluptatibus recusandae ratione vitae amet distinctio, voluptas, minus vero expedita ea fugit similique sit cumque ad id facere? Ab quas, odio neque quis ratione. Natus labore sit esse, porro placeat eum hic.
                                    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minima, quod dicta aliquid nemo repellendus distinctio minus dolor aperiam suscipit, ea enim accusantium, deleniti qui sequi sint nihil modi amet eligendi, quidem animi error labore voluptatibus sed. Qui magnam labore, iusto nostrum. Praesentium non, impedit accusantium consequatur officia architecto, mollitia placeat aperiam tenetur pariatur voluptatibus corrupti vitae deserunt! Nostrum non mollitia deserunt ipsam. Sunt quaerat natus cupiditate iure ipsa voluptatibus recusandae ratione vitae amet distinctio, voluptas, minus vero expedita ea fugit similique sit cumque ad id facere? Ab quas, odio neque quis ratione. Natus labore sit esse, porro placeat eum hic.
                                </p>
                            </div> <!-- .cd-project-info -->
                        </li>
                    </ul> <!-- .cd-projects -->
                    
                    <button class="scroll cd-text-replace">Scroll</button>
                </div> <!-- .cd-project-container -->
                
                <nav class="cd-primary-nav" id="primary-nav">
                    <ul>
                        <li class="cd-label">Navigation</li>
                        <li><a href="#0">The team</a></li>
                        <li><a href="#0">Our services</a></li>
                        <li><a href="#0">Our projects</a></li>
                        <li><a href="#0">Contact us</a></li>
                    </ul>
                </nav> <!-- .cd-primary-nav -->
                <script src="../js/jquery-2.1.1.js"></script>
                <script src="../js/main.js"></script> <!-- Resource jQuery -->
            </body>
        </html>
    </xsl:template>
    <xsl:template match="PROJET/presentation">
        <h3>
            <xsl:value-of select="titre"/>
        </h3><br/><br/><br/>
        <xsl:for-each select="introduction">
            <p>
                <xsl:value-of select="."/>
            </p><br/><br/>
        </xsl:for-each>
    </xsl:template>
    <xsl:template match="PROJET/etapes">
        <h3><xsl:value-of select="titre"/></h3><br></br><br></br><br></br>
        <p><xsl:value-of select="intro"/></p><br></br><br></br>
        <xsl:apply-templates select="structuration"/><br></br><br></br>
        <xsl:apply-templates select="modelisation"/><br></br><br></br>
        <xsl:apply-templates select="grammaires"/><br></br><br></br>
        <xsl:apply-templates select="trans_tablo"/><br></br><br></br>
        <xsl:apply-templates select="carte"/>
    </xsl:template>
        <xsl:template match="structuration">
            <p class="sous-titre">1. <xsl:value-of select="intro"/></p><br></br>
            <p><xsl:value-of select="creation_env"/></p><br></br>
            <xsl:apply-templates select="recuperation"/><br></br>
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
                        <ul>
                            <xsl:for-each select="info">
                                <p><li><xsl:value-of select="."/></li></p>
                            </xsl:for-each>
                        </ul>
                    </xsl:template>
        <xsl:template match="modelisation">
            <p class="sous-titre">2. <xsl:value-of select="intro"/></p><br></br>
            <p><xsl:value-of select="csv2xml"/></p><br></br>
            <xsl:apply-templates select="fichiers"/>
        </xsl:template>
            <xsl:template match="fichiers">
                <ul>
                    <xsl:for-each select="fichier/link">
                        <p><li><a href="{@url}"><xsl:value-of select="."/></a></li></p>
                    </xsl:for-each>
                </ul>
            </xsl:template>
        <xsl:template match="grammaires">
            <p class="sous-titre">3. <xsl:value-of select="liste"/></p><br></br>
            <ul>
                <xsl:for-each select="fichier">
                    <p><li><xsl:apply-templates/></li></p>
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
            <p class="sous-titre">4. <xsl:value-of select="liste"/></p><br></br>
            <xsl:apply-templates select="xml2html"/><br></br>
            <xsl:apply-templates select="tableaux"/>
        </xsl:template>
    
    <xsl:template match="link">
        <a href="{@url}"><xsl:apply-templates/></a>
    </xsl:template>
</xsl:stylesheet>