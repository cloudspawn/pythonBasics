import requests, csv

from bs4 import BeautifulSoup

url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

print(soup.title.string + "\n")

titres = soup.find_all("a", class_="gem-c-document-list__item-title")
descriptions = soup.find_all("p", class_="gem-c-document-list__item-description")
dates = soup.find_all("li", class_="gem-c-document-list__attribute")

# for titre in titres:
#     print(titre.string)

# print("\nDescription >>> \n")
# for description in descriptions:
#     print(description.string)

# print("\nDates >>> \n")
# for date in dates:
#     print(date.time.string)


titre_textes = []
for titre in titres:
    titre_textes.append(titre.string)

description_textes = []
for description in descriptions:
    description_textes.append(description.string)

date_textes = []
for date in dates:
    date_textes.append(date.time.string)

list_articles = [titre_textes, description_textes, date_textes]

# for i in range(len(list_articles[0])):
#     print(list_articles[0][i], list_articles[1][i], list_articles[2][i])

# print(list_articles)
# print(titre_textes, description_textes, date_textes)

# combinaison titre et description dans un dictionnaire titre:description
# article = dict(zip(titre_textes, description_textes))
# print(article)

# for i in range(len(titres)):
#     print(f"{titres[i].string}\n{descriptions[i].string}\n{dates[i].time.string}\n")

en_tete = ["titre", "description", "date"]

# creer un nouveau fichier poru ecrire dans le fichier appelé data.csv
with open("data.csv", "w") as fichier_csv:
    # creer un objet writer avec ce fichier
    writer = csv.writer(fichier_csv, delimiter=",")
    writer.writerow(en_tete)
    # parcourir les titre et description  - zip permet d'iterer sur deux liste ou plus a la fois
    for titre, description, date in zip(titre_textes, description_textes, date_textes):
        # creer une nouvelle ligne avec titre description et date  a chaque iteration
        ligne = [titre, description, date]
        writer.writerow(ligne)
