from flask import Flask
from markupsafe import escape
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/test/<name>')
def test(name):
    return f'Hello,{name}'

@app.route('/about')
def about():
    return '<h1>About us</h1>'

@app.route('/news')
def news():
    return """<html> 
        <h1>News</h1> 
        <p>SWU News daily topics:</p>
        <ul>
            <li>Technology</li>
            <li>Sport</li>
            <li>Education</li>
        </ul>
    </html>"""

@app.route('/news/tech')
def tech_news():
    return '<b>technology news</b>'

@app.route('/product/<name>')
def get_product(name):
  return "The product is " + str(name)

@app.route('/name/<int:num>')
def favorite_number(num):
    return f"Your favorite number is {num}, which is half of {num * 2}"

@app.route('/create/<first_name>/<last_name>')
def create(first_name=None, last_name=None): #ค่า default
  return 'Hello ' + first_name + ',' + last_name

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id
    
@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)

app.env="development"
app.run(debug=True)
