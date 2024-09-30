# import sys
# import os
# sys.path.append(os.path.abspath('..'))
import requests
from flask import Flask, jsonify

# from Data.data import relay_data

app = Flask(__name__)

# @app.route('/', methods=['GET'])
# def get_items():
#     session = Session()
#     items = session.query(Item).all()
#     session.close()
#     return jsonify([{"id": item.id, "name": item.name} for item in items])

@app.route('/', methods=['GET'])
def get_items():
    response = requests.get('http://dataserver:5002/data')  
    return jsonify(response.json())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

