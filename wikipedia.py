from bs4 import BeautifulSoup
import requests
import csv

def getdata(url):
    r = requests.get(url)
    return r.text

dt = []
d1 = []
para = []
infobox = []
title = []
link = getdata("https://en.wikipedia.org/wiki/J._K._Rowling")

soup = BeautifulSoup(link, 'html.parser')

headTitle = soup.find('h1').get_text()
infoTable = soup.find('table')
paragraph = soup.find_all('p')[1].get_text()

print(headTitle,'heading')
print(infoTable,'infoTable')
print(paragraph,'paragraph')

title.append(headTitle)
para.append(paragraph)

if infoTable is None:
    infobox.append('No InfoBox')
else:
    infobox.append(infoTable.get_text())


all_links = soup.find_all("a", href = True, text = True)

count = 0
link_text = ""
for d in all_links:
    if d['href'].find("/wiki/") == -1:
        continue
    count += 1
    link_text = d['href']
    print(link_text,'==============', count)
    x = "https://en.wikipedia.org" + link_text
    
    link_info = getdata(x)
    soup = BeautifulSoup(link_info, 'html.parser')
    k = soup.find('table')
    p = soup.find('h1').get_text()
    paragraph = soup.find_all('p')[1].get_text()
    
    title.append(p)
    para.append(paragraph)

    if k is None:
        infobox.append('No InfoBox')
    else:
        infobox.append(k.get_text())

    if count == 10:
        break
   
datarow = []
count2 = 0
while count2 != 11:
    d = [title[count2], infobox[count2], para[count2]]
    datarow.append(d)
    count2 += 1
    
with open('wikipedia_scraper.csv', 'w', encoding ='UTF8') as f:
   writer = csv.writer(f)
   
   for row in datarow:
        writer.writerow(row)

