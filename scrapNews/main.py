import requests

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

# print(titre_textes, description_textes, date_textes)

article = dict(zip(titre_textes, description_textes))
print(article)

# for i in range(len(titres)):
#     print(f"{titres[i].string}\n{descriptions[i].string}\n{dates[i].time.string}\n")
