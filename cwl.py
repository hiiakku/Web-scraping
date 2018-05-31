import re
import requests
from bs4 import BeautifulSoup
 
URL = 'https://www.hindustantimes.com'
location_url=[]

r = requests.get(URL)
soup = BeautifulSoup(r.text,'lxml')

h=soup.find("div", {"class" : "sub-menu-dt sub-menu-open"})
x=h.find('ul')
x=x.findAll('li')
for j in range(min(len(x),13)):
    location_url.append(URL+x[j].find('a').attrs['href'])

print location_url


for k in range(len(location_url)):
                   
    r1 = requests.get(location_url[k])
    soup1 = BeautifulSoup(r1.text,'lxml')
    urls = []

    regex1 = re.compile('.*heading.*')
    regex = re.compile('.*cb-section.*')


    c =0
    for h in soup1.find_all("div", {"class" : regex1}):
        #print h
        if h.parent.name == 'div':
            a = h.find('a')
            if a is not None:
                c=c+1
                urls.append(a.attrs['href'])

    fl = "data"+str(k)+".txt"
    f= open(fl,"w+")
    ##
    for j in range(c):
        r = requests.get(urls[j])
        soup = BeautifulSoup(r.text,'html.parser')
         
        l = soup.find_all("ul")
    
    
        for i in soup.find_all("a", {"class" : regex}):
                f.write("Place => " + i.text+'\n')
    
        string = "Heading => "+soup.h1.string
        str1=string.encode('utf8', 'replace')
        #print(str1)
        f.write(str1+'\n')
        
    
        mydivs = soup.findAll("span", {"class": "text-dt"})
        for i in mydivs:
                f.write("Date and Time => "+i.text.split("d:")[1]+'\n')
    
    
        article = soup.find("div",{"class":"story-details"})
        if article:
            srttt=article.findAll("p")
            for i in srttt:
                    s=i.text
                    str1=s.encode('utf8', 'replace')
                    f.write(str1+'\n')
        article = soup.find("div",{"class":"storyContent"})
        if article:
            srttt=article.findAll("p")
            for i in srttt:
                    s=i.text
                    str1=s.encode('utf8', 'replace')
                    f.write(str1+'\n')
                #print s
    
        f.write("------------------------------------------------------------------------------------------------------------------------"+'\n\n')
        
    f.close()
    print "done"
    
