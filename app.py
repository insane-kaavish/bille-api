from flask import Flask, request, jsonify
from pymongo import MongoClient
import random
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

MONGO_PASS = os.environ.get('MONGO_PASS')
client = MongoClient(MONGO_PASS)
db = client.bille
myCollection = db.bille

@app.route('/', methods=['GET'])
def home():
    return {'message': 'Hello World!'}

@app.route('/predict', methods=['POST'])
def predictData():
    try:
        # Parse the JSON data
        data = request.json
        x = myCollection.insert_one(data)
        print(x)

        oct_bill = float(data.get('octBill', 0))
        sep_bill = float(data.get('sepBill', 0))
        aug_bill = float(data.get('augBill', 0))
        
        return {'predictedUnits': random.randint(min([oct_bill, sep_bill, aug_bill]), max([oct_bill, sep_bill, aug_bill]))}
    except Exception as e:
        print(e)
        return {'error': 'Something went wrong'}

if __name__ == "__main__":
    app.run()
