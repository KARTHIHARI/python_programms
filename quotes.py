import requests
import re
import json
import threading
import time
import multiprocessing

l=[]
for i in range(5):
    i={}
    res=requests.get("http://quotes.toscrape.com/random")
    tags=re.findall(r'<a class="tag" .+>(.+)</a',res.text)
    quotes=re.findall(r'<span class="text" itemprop="text">“(.+)”</span>',res.text)
    quotes=quotes[0]
    author=re.findall(r'<span>by <small class="author" itemprop="author">(.+)</small>',res.text)
    author=author[0]
    about=re.findall(r'<a href="(.+)">[(]about[)]</a>',res.text)
    about="http://quotes.toscrape.com"+about[0]
    i["tags"]=tags
    i["quotes"]=quotes
    i["author"]=author
    i["about"]=about
    l.append(i)
    
# print(l)
f=open("temp.json","w")
s=json.dumps(l,indent=4)
f.write(s)
print(s)



#ANOTHER METHOD

# import requests
# import re


# def fun2():
#     res=requests.get("http://quotes.toscrape.com/random")
#     # print(res.status_code)
#     # print(res.text)
#     # f=open("rest.txt","+r",encoding="utf-8")
#     # f.write(res.text)
#     # f.close()

#     # f=open("rest.txt","r",encoding="utf-8")
#     # result=f.read()
#     # print(result)
#     # f.close()
#     tags=re.findall(r'<a class="tag" .+>(.+)</a',res.text)
#     # print("tags:",tags)
#     quotes=re.findall(r'<span class="text" itemprop="text">“(.+)”</span>',res.text)
#     quotes=quotes[0]
#     # print("quotes:",quotes)
#     author=re.findall(r'<span>by <small class="author" itemprop="author">(.+)</small>',res.text)
#     author=author[0]
#     # print("Author:",author)
#     about=re.findall(r'<a href="(.+)">[(]about[)]</a>',res.text)
#     about="http://quotes.toscrape.com"+about[0]
#     # print("about url",about)
#     d={}
#     d["tags"]=tags
#     d["quotes"]=quotes
#     d["author"]=author
#     d["about"]=about
#     print(d)

# def fun3():
#     res=requests.get("http://quotes.toscrape.com/random")
#     # print(res.status_code)
#     # print(res.text)
#     # f=open("rest.txt","+r",encoding="utf-8")
#     # f.write(res.text)
#     # f.close()

#     # f=open("rest.txt","r",encoding="utf-8")
#     # result=f.read()
#     # print(result)
#     # f.close()
#     tags=re.findall(r'<a class="tag" .+>(.+)</a',res.text)
#     # print("tags:",tags)
#     quotes=re.findall(r'<span class="text" itemprop="text">“(.+)”</span>',res.text)
#     quotes=quotes[0]
#     # print("quotes:",quotes)
#     author=re.findall(r'<span>by <small class="author" itemprop="author">(.+)</small>',res.text)
#     author=author[0]
#     # print("Author:",author)
#     about=re.findall(r'<a href="(.+)">[(]about[)]</a>',res.text)
#     about="http://quotes.toscrape.com"+about[0]
#     # print("about url",about)
#     d={}
#     d["tags"]=tags
#     d["quotes"]=quotes
#     d["author"]=author
#     d["about"]=about
#     print(d)

# def fun4():
#     res=requests.get("http://quotes.toscrape.com/random")
#     # print(res.status_code)
#     # print(res.text)
#     # f=open("rest.txt","+r",encoding="utf-8")
#     # f.write(res.text)
#     # f.close()

#     # f=open("rest.txt","r",encoding="utf-8")
#     # result=f.read()
#     # print(result)
#     # f.close()
#     tags=re.findall(r'<a class="tag" .+>(.+)</a',res.text)
#     # print("tags:",tags)
#     quotes=re.findall(r'<span class="text" itemprop="text">“(.+)”</span>',res.text)
#     quotes=quotes[0]
#     # print("quotes:",quotes)
#     author=re.findall(r'<span>by <small class="author" itemprop="author">(.+)</small>',res.text)
#     author=author[0]
#     # print("Author:",author)
#     about=re.findall(r'<a href="(.+)">[(]about[)]</a>',res.text)
#     about="http://quotes.toscrape.com"+about[0]
#     # print("about url",about)
#     d={}
#     d["tags"]=tags
#     d["quotes"]=quotes
#     d["author"]=author
#     d["about"]=about
#     print(d)

# def fun5():
#     res=requests.get("http://quotes.toscrape.com/random")
#     # print(res.status_code)
#     # print(res.text)
#     # f=open("rest.txt","+r",encoding="utf-8")
#     # f.write(res.text)
#     # f.close()

#     # f=open("rest.txt","r",encoding="utf-8")
#     # result=f.read()
#     # print(result)
#     # f.close()
#     tags=re.findall(r'<a class="tag" .+>(.+)</a',res.text)
#     # print("tags:",tags)
#     quotes=re.findall(r'<span class="text" itemprop="text">“(.+)”</span>',res.text)
#     quotes=quotes[0]
#     # print("quotes:",quotes)
#     author=re.findall(r'<span>by <small class="author" itemprop="author">(.+)</small>',res.text)
#     author=author[0]
#     # print("Author:",author)
#     about=re.findall(r'<a href="(.+)">[(]about[)]</a>',res.text)
#     about="http://quotes.toscrape.com"+about[0]
#     # print("about url",about)
#     d={}
#     d["tags"]=tags
#     d["quotes"]=quotes
#     d["author"]=author
#     d["about"]=about
#     print(d)

# t1=threading.Thread(target=fun1)
# t2=threading.Thread(target=fun2)
# t3=threading.Thread(target=fun3)
# t4=threading.Thread(target=fun4)
# t5=threading.Thread(target=fun5)



# t2.start()
# t3.start()
# t4.start()
# t5.start()

# print("\n\n")


# fun1()
# fun2()
# fun3()
# fun4()
# fun5()