from bs4 import BeautifulSoup
import requests
import urllib.request
import os
import time

def getSearchTerm():
    topic = input("enter topic: >> ")
    return topic

def downloadOne(l,name):
    urllib.request.urlretrieve(l, os.path.join(os.path.join(os.getcwd(), name), os.path.basename(l)))
    print("download complete\n")

def main():
    topic = getSearchTerm()
    url="https://imgur.com/search?q="+topic
    page=requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    ims = soup.find_all("img")
    if len(ims) >0:
        print(len(ims), " results found")
        if not os.path.exists(os.path.join(os.getcwd(),topic)):
            os.mkdir(os.path.join(os.getcwd(),topic))
        imgs=[]
        for i in ims:
            if "i.imgur.com" in i['src']:
                l= str(i['src']).replace(r"//","")
                imgs.append("https://"+l)
        for l in imgs:
            print("downloading: ",os.path.basename(l))
            time.sleep(1)
            downloadOne(l,topic)

if __name__ == '__main__':
    main()




