from bs4 import BeautifulSoup as bs
import requests 
import pandas as pd
brightstarsurl="https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page=requests.get(brightstarsurl)
print(page)
soup=bs(page.text,"html.parser")
startable=soup.find("table")
templist=[]
tablerows=startable.find_all("tr")
for tr in tablerows:
    td=tr.find_all("td")
    row=[i.text.rstrip() for i in td]
    templist.append(row)
Star_names = [] 
Distance =[] 
Mass = [] 
Radius =[] 
Lum = []
for i in range(1,len(templist)):
    Star_names.append(templist[i][1])
    Distance.append(templist[i][1])
    Mass.append(templist[i][1])
    Radius.append(templist[i][1])
    Lum.append(templist[i][1])
df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,Lum)),columns=['Star_name','Distance','Mass','Radius','Luminosity']) 
print(df2) 
df2.to_csv('bright_stars.csv')