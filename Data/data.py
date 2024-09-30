from flask import Flask, jsonify, request
import logging
import sys
import os
sys.path.append(os.path.abspath('..'))
from database import Session, Item  
from sqlalchemy.exc import IntegrityError, OperationalError

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/data', methods=['GET'])
def relay_data():
    session = Session()
    items = session.query(Item).all()
    session.close()
    return jsonify([{"id": item.id, "name": item.name} for item in items])

@app.route('/items', methods=['POST'])
def add_item():
    data = request.json
    if 'name' not in data:
        return jsonify({"error": "Name is required"}), 400
    
    session = Session()
    try:
        session.add(Item(name=data['name']))
        session.commit()
        return jsonify({"id": session.query(Item.id).order_by(Item.id.desc()).first()[0], "name": data['name']}), 201
    except (IntegrityError, OperationalError) as e:
        session.rollback()
        error_message = "Integrity Error: Possibly a duplicate entry." if isinstance(e, IntegrityError) else "Database connection error."
        return jsonify({"error": error_message}), 400 if isinstance(e, IntegrityError) else 500
    finally:
        session.close()

if __name__ == '__main__':
    logger.info("Starting data relay server on port 5002")
    app.run(host='0.0.0.0', port=5002)
    
    
    
#git ignore file 
