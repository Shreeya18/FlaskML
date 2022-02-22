print("I Love Python!")
import gunicorn
from flask import Flask,request,jsonify
import util

app = Flask(__name__)

"""@app.route('/')
def hello():
    return "Hello World!"""


@app.route('/locations')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/',methods =['POST'])
def predict():
    total_sqft = float(request.form.get('total_sqft'))
    bath = int(request.form.get('bath'))
    bhk = int(request.form.get('bhk'))
    location = request.form.get('location')

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__=='__main__':
    util.loadSaved()
    app.run(debug=True)
