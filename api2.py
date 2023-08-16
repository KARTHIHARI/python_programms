import requests
import re
import json
from flask import Flask,request
import math
app=Flask(__name__)

@app.route("/data",methods=["GET","POST"])
def fun():
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
    f=open("temp2.json","w")
    s=json.dumps(l,indent=4)
    f.write(s)
    return s

app.run(debug=True,host="0.0.0.0")