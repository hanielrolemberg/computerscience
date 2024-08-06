from flask import Blueprint, request, jsonify
from app import create_app

bp = Blueprint('routes', __name__)

@bp.route('/set', methods=['POST', 'GET'])
def set_value():
    if request.method == 'POST':
        key = request.json.get('key')
        value = request.json.get('value')
        if not key or not value:
            return jsonify({'error': 'Missing key or value'}), 400
        
        app = create_app()
        app.redis.set(key, value)
        return jsonify({'message': 'Value set successfully'}), 200
    else:
        return jsonify({'message': 'Please use POST to set values'}), 200

@bp.route('/get/<key>', methods=['GET'])
def get_value(key):
    app = create_app()
    value = app.redis.get(key)
    if value is None:
        return jsonify({'error': 'Key not found'}), 404
    
    return jsonify({'key': key, 'value': value.decode('utf-8')}), 200
