from flask import Flask, jsonify
from flask_cors import CORS
import subprocess
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)  

@app.route('/run-script', methods=['GET'])
def run_script():
   
    result = subprocess.run(['C:/Python312/python.exe', './scrapper.py'], capture_output=True, text=True)

    
    client = MongoClient('mongodb://localhost:27017/')
    db = client['twitter_trends']
    collection = db['trends']
    
   
    latest_entry = collection.find().sort([('_id', -1)]).limit(1)
    
    
    latest_entry_list = list(latest_entry)
    if latest_entry_list:
        return jsonify(latest_entry_list[0])  
    else:
        return jsonify({"error": "No entries found in the database"}), 404


if __name__ == '__main__':
    app.run(port=5000)
