import requests
from bs4 import BeautifulSoup
req=requests.get("https://opennews.org/blog/opennews-hiring-co-director/")
soup=BeautifulSoup(req.content,"html.parser")
res=soup.title
# sapiens=res.get_text()
sapiens=soup.get_text()