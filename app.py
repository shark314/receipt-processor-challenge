from flask import Flask, request, jsonify
import uuid
from datetime import datetime
import math

app = Flask(__name__)

# In-memory storage for receipts
receipts = {}

def count_alphanumeric(s):
    return sum(1 for char in s if char.isalnum())

def calculate_points(receipt):
    points = 0
    
    # Points for retailer name
    retailer_name = receipt['retailer']
    points += count_alphanumeric(retailer_name)

    # Points for total amount
    total = float(receipt['total'])
    if total.is_integer():
        points += 50
    if total % 0.25 == 0:
        points += 25

    # Points for items
    items = receipt['items']
    points += (len(items) // 2) * 5

    # Points for item descriptions
    for item in items:
        description_length = len(item['shortDescription'].strip())
        if description_length % 3 == 0:
            price = float(item['price'])
            points += math.ceil(price * 0.2)

    # Points for purchase date
    purchase_date = datetime.strptime(receipt['purchaseDate'], '%Y-%m-%d')
    if purchase_date.day % 2 == 1:
        points += 6

    # Points for purchase time
    purchase_time = datetime.strptime(receipt['purchaseTime'], '%H:%M')
    if purchase_time.hour == 14 and 0 <= purchase_time.minute < 60:
        points += 10
    elif purchase_time.hour == 15 and 0 <= purchase_time.minute < 60:
        points += 10

    return points

@app.route('/receipts/process', methods=['POST'])
def process_receipt():
    receipt = request.json
    receipt_id = str(uuid.uuid4())
    points = calculate_points(receipt)
    
    # Store receipt with points in memory
    receipts[receipt_id] = {**receipt, 'points': points}
    
    return jsonify({'id': receipt_id}), 201

@app.route('/receipts/<id>/points', methods=['GET'])
def get_points(id):
    if id not in receipts:
        return jsonify({'error': 'Receipt not found'}), 404

    return jsonify({'points': receipts[id]['points']}), 200

if __name__ == '__main__':
    app.run(debug=True)
