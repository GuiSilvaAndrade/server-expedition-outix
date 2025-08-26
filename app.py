from flask import Flask, jsonify, request
from flask_cors import CORS
from services.nf_data import *


app = Flask(__name__)
CORS(app)

@app.route("/", methods=['POST'])
def home():
    barcode = request.get_json().get('value')

    response = nf_data(barcode)
    
    return response


if __name__ == "__main__":
    app.run(debug=True)
