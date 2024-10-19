from bs4 import BeautifulSoup
import requests
import pandas as pd

rez = {'img':[]}
count=0
url = "https://www.bing.com/images/search?q=Повышение+уровня+моря&form=HDRSC2&first=1&cw=1177&ch=941"
response = requests.get(url)
bs = BeautifulSoup(response.text,"lxml")

temp = bs.find_all("main", "content")
for i in temp:
    rez['img'].append(i.find('p'),)
    count+=1
    if count == 600:
        rez = pd.DataFrame(rez, columns=['img'])
        rez.to_csv("./saved_data.csv")

    