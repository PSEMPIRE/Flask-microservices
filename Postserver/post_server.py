from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
import sys
import os
import requests  # Import requests to send HTTP requests
sys.path.append(os.path.abspath('..'))
# from database import Session, Item  # Remove this import

app = Flask(__name__)
CORS(app)  

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/', methods=['POST'])
def add_item():
    data = request.json
    if not data or 'name' not in data:
        return jsonify({"error": "Name is required"}), 400
    
    response = requests.post('http://dataserver:5002/items', json=data)  # Update the URL to point to data.py
    return jsonify(response.json()), response.status_code  # Return the response from data.py

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    logger.info("Starting POST server on port 5001")
    app.run(host='0.0.0.0', port=5001)