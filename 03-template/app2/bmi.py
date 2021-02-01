from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def bmi_calc():
    bmi = ''
    bmi_cal = ''
    if request.method == 'POST':
        weight = float(request.form.get('weight'))
        height = float(request.form.get('height'))
        bmi = calc_bmi(weight, height) 
        if bmi < 15:
            bmi_cal = "Very severely underweight"
        elif bmi >= 15 and bmi < 16:
            bmi_cal = "Severely underweight"
        elif bmi >= 16 and bmi < 18.5:
            bmi_cal = "Underweight"
        elif bmi >= 18.5 and bmi < 25:
            bmi_cal = "Normal (healthy weight)"
        elif bmi >= 25 and bmi < 30:
            bmi_cal = "Overweight"
        elif bmi >= 30 and bmi < 35:
            bmi_cal = "Moderately obese"
        elif bmi >= 35 and bmi < 40:
            bmi_cal = "Severely obese"
        else:
            bmi_cal = "Very severely obese"
            
    return render_template("bmi.html",
	                        bmi=bmi,bmi_cal=bmi_cal)

def calc_bmi(weight, height):
    return round((weight / ((height / 100) ** 2)), 2)

