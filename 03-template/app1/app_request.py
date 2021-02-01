from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/score', methods=['GET'])
def score():
    val1 = request.args.get('val1', default = 1, type = int)
    val2 = request.args.get('val2', default = 0.5, type = float)
     
    return f"val1 is {val1} , val2 is {val2}"

@app.route('/user', methods=['POST']) 
def user():
    data = request.json
    return jsonify(data)

