import requests
from bs4 import BeautifulSoup

# if __name__ == "__main__":

url = "https://gov.uk/search/news-and-communications"
reponse = requests.get(url)
page = reponse.content

soup = BeautifulSoup(page, "html.parser")
soup.title
class_name = "gem-c-document-list__item-title"
soup.find_all("a", class_=class_name)
class_description = "gem-c-document-list__item-description"
soup.find_all("p", class_=class_description)
print(soup.find_all("a"))
