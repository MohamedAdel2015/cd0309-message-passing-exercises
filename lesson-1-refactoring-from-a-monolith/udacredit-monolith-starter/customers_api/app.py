from flask import Flask, jsonify, make_response
from services.customers import get_customers

app = Flask(__name__)

@app.route('/api/customers', methods=['GET'])
def customers():
    sample_response = {
        "customers": get_customers()
    }
    response = make_response(jsonify(sample_response))
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'
    return response