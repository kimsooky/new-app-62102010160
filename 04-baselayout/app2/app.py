from flask import Flask,render_template
from data import Articles

app = Flask(__name__)
articles_data = Articles()

@app.route('/')
def index():
   return render_template('home.html')

@app.route('/news')
def news():
   return render_template('news.html')

@app.route('/articles')
def articles():
   return render_template('articles.html',articles = articles_data) #ส่ง data 

@app.route('/article/<string:id>')
def article(id,title):
   return render_template('article.html',id=id,title=title)

@app.route('/about')
def about():
   return render_template('about.html')

