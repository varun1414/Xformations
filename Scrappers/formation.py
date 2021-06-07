import bs4
import requests
URL = "https://www.footballcritic.com/fc-barcelona/formations/721/45794"
r = requests.get(URL)
print(r.content)
