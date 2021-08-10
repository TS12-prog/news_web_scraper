import urllib.request
from bs4 import BeautifulSoup
import validators

url=input("Enter news article url ")
valid=validators.url(url)
if valid==True:
	html=urllib.request.urlopen(url)
	soup=BeautifulSoup(html, 'html.parser')
	t=soup.title.get_text()
	print(t)
	for para in soup.find_all("p"):
		print(para.get_text())
else:
	print("invalid url")


