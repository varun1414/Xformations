from bs4 import BeautifulSoup
import requests
import re
def clean(text):
    """Remove html tags from a string"""
    import re
    # cleans = re.compile()
    s= re.sub(r'<.*?>','', text)
    return s.replace("\n","")
URL = "https://www.footballcritic.com/fc-barcelona/formations/721/13478"
r = requests.get(URL)
soup = BeautifulSoup(r.content,features="html.parser")
matches=[]
# print(soup.prettify()
count=0

for i in soup.find_all('tr')[2:]:
    match={}

    match["comp"]=str(i.find('span',attrs={'class':'txt'}))
    match["date"]=str(i.find('td',attrs={'class':'date'}))
    match["result"]=str(i.find('td',attrs={'class':'form'}))
    match["teams"]=str(i.find_all('span',attrs={'class':'hidden-xs'}))
    match["score"]=str(i.find('span',attrs={'class':'score-text'}))
    match["formation"]=str(i.find('span',attrs={'class':'formationLabel'}))
    
    matches.append(match)

for match in matches:
    match["comp"]=clean(match["comp"])
    match["date"]=clean(match["date"])
    match["result"]=clean(match["result"])
    match["teams"]=clean(match["teams"])
    match["score"]=clean(match["score"])
    match["formation"]=clean(match["formation"])

print(matches)

