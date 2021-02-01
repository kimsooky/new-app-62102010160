from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/bmi', methods=['GET'])
def score():
    weight = request.args.get('weight',type = float)
    height = request.args.get('height',type = float)
    
    bmi = round((weight / ((height/100) ** 2)),2)
    
    return f"bmi is {bmi}"

@app.route('/bmijson', methods=['POST']) 
def user():
    data = request.json
    weight = data['weight']
    height = data['height']
    bmi = round((weight / ((height/100) ** 2)),2)

    rdata = {"weight" : weight, "height" : height, "bmi" : bmi }
    return jsonify(rdata)


