from bs4 import BeautifulSoup
import urllib.parse
from urllib.request import urlopen


url ="http://www.pythonscraping.com/exercises/exercise1.html"
url1= "http://www.pythonscraping.com/pages/warandpeace.html"

url = url1
html = urlopen(url)
# print(html.read)  #html.read return memory address
bsObj = BeautifulSoup(html,'html.parser', from_encoding = 'utf-8')
# print(bsObj.h1) #打印 <h1>team</h1>
# obj= bsObj.findAll("div")
# print(obj)
# [4].findAll("tr")[2].find("td").findAll("div")[1].find("a")
# print(bsObj.tagName)]
# print(bsObj.find("span"))
nameList = bsObj.findAll("span", {"class":"red"})  #.findAll(tagName,tagAttributes)
for name in nameList:
    # print(name.get_text())
    print(name)


# urllib.request, urllib.parse, and urllib.error
