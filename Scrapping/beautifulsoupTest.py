from bs4 import BeautifulSoup

html_doc = """
<html>
    <head>
    <title>Titre de votre site</title>
    </head>
    <body>
        <p class="c1 c2">Texte a lire 1</p>
        <p class="c3">Texte a lire 1</p>
    </body>
</html>
"""
soup = BeautifulSoup(html_doc, "html5lib")
print(soup)

for p in soup.find_all('p'):
    # la balise <p>
    print(p)
    # valeur de l'attribut "class" de la balise <p>
    print(p.get("class"))
    # contenu de la balise <p>
    print(p.string)
    # exemple de modification de contenu <p>
    p.string = "BigData"

print(soup)

print(type(soup.prettify()))