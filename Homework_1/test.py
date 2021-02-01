from flask import Flask,render_template,request
from urllib.parse import quote
from urllib.request import urlopen
import json
import requests
import requests
import json
url = "http://newsapi.org/v2/everything?q=tesla&from=2020-12-31&sortBy=publishedAt&apiKey=524f6394cc7744d4bba39ecbd765c268"
data = urlopen(url).read()
parsed = json.loads(data)
news = []
    
for i in range(1,5): #แก้ให้เริ่มที่ 1
        title = parsed['articles'][i]['title']
        description = parsed['articles'][i]['description']
        img = parsed['articles'][i]['urlToImage']
        link = parsed['articles'][i]['url']
        news.append({"title":title,"description":description,"Link":link,"img":img})

print(news)