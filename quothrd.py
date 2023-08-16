import requests
import re
import json
import threading
import time
import multiprocessing
def fun1():
    res=requests.get("http://quotes.toscrape.com/random")
    # print(res.status_code)
    # print(res.text)
    # f=open("rest.txt","+r",encoding="utf-8")
    # f.write(res.text)
    # f.close()

    # f=open("rest.txt","r",encoding="utf-8")
    # result=f.read()
    # print(result)
    # f.close()
    tags=re.findall(r'<a class="tag" .+>(.+)</a',res.text)
    # print("tags:",tags)
    quotes=re.findall(r'<span class="text" itemprop="text">“(.+)”</span>',res.text)
    quotes=quotes[0]
    # print("quotes:",quotes)
    author=re.findall(r'<span>by <small class="author" itemprop="author">(.+)</small>',res.text)
    author=author[0]
    # print("Author:",author)
    about=re.findall(r'<a href="(.+)">[(]about[)]</a>',res.text)
    about="http://quotes.toscrape.com"+about[0]
    # print("about url",about)
    d={}
    d["tags"]=tags
    d["quotes"]=quotes
    d["author"]=author
    d["about"]=about
    print(d)
if __name__=="__main__":
    for i in range(5):
        t1=threading.Thread(target=fun1)

        t1.start()