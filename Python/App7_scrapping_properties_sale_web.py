import requests
from bs4 import BeautifulSoup

r = requests.get('https://pythonizing.github.io/data/real-estate/rock-springs-wy/LCWYROCKSPRINGS/')
c = r.content
print(r.status_code)
#print(c)

soup = BeautifulSoup(c, "html.parser")
#print(soup.prettify())

all = soup.find_all('div',{"class":"propertyRow"}) #get all div tags whose class value is propertyrow
print(len(all))

#this is capturing only first element
print(all[0].find('h4',{"class":"propPrice"}).text.replace("\n","").replace(" ","")) #using replace to clean all unwanted spaces and escape chars

#iterate through all elements and extract price
for item in all:
    print(item.find('h4',{"class":"propPrice"}).text.replace("\n","").replace(" ",""))

    #next capturing address
    item.find_all('span',{"class":"propAddressCollapse"})
    print(item.find_all('span',{"class":"propAddressCollapse"})[0].text)

    #find tag inside tag
    try:
        print(item.find('span',{'class':'infoBed'}).find('b').text)
    except:
        pass