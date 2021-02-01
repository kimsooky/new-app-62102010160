from flask import Flask, render_template

app = Flask(__name__)

@app.route('/name/<user>')
def hello(user):
    return render_template('hello.html', name = user)

@app.route('/grade/<int:score>')
def grade(score):
    return render_template('grade.html', marks = score)
    
@app.route('/detail')
def detail():
    my_dict = {"brand": "Ford", "model": "Mustang", "year": 1964}
    return render_template('detail.html', data = my_dict)
app.env="development"
app.run(debug=True)