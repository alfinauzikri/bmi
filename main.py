from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/api/v1/bmi', methods=['POST'])
def bmi():

    req = request.json

    height = float(request.form.get('height'))
    weight = float(request.form.get('weight'))

    BMI = weight / (height/100)**2

    msg = "You BMI is " + str(BMI)

    if BMI <= 18.4:
        ket = "You are underweight."
    elif BMI <= 24.9:
        ket = "You are healthy."
    elif BMI <= 29.9:
        ket = "You are over weight."
    elif BMI <= 34.9:
        ket = "You are severely over weight."
    elif BMI <= 39.9:
        ket = "You are obese."
    else:
        ket = "You are severely obese."

    data = {'result': 'true', 'msg': msg, 'ket': ket}
    return data


if __name__ == '__main__':
    app.run(debug=True, port=8080)
